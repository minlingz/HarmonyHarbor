# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template
import requests
import json
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR)

app = Flask(__name__)

delta_table_url = (
    "https://adb-1158426884895395.15.azuredatabricks.net/api/2.0/sql/statements/"
)


# @app.route("/get_data")
def get_data_from_delta_table():
    key_vault_url = "https://dek.vault.azure.net/"
    credential = DefaultAzureCredential()

    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

    secret_value = secret_client.get_secret("HLDB").value

    query = "SELECT * FROM prepared_song_data LIMIT 10"
    # query = "SELECT * FROM test"
    # Headers for Databricks REST API request
    headers = {
        "Authorization": "Bearer " + secret_value,
        "Content-Type": "application/json",
    }

    # sql query
    warehouse_id = "cfc6093cfe691c79"

    response = requests.post(
        delta_table_url,
        headers=headers,
        data=json.dumps(
            {
                "statement": query,
                "warehouse_id": warehouse_id,
                "wait_timeout": "30s",
                "on_wait_timeout": "CONTINUE",
            }
        ),
    )

    # response = requests.post(delta_table_url, headers=headers, json=params)
    if response.status_code == 200:
        data = response.json().get("result", {}).get("data_array", [])
        return data

    else:
        return {
            "error": "Failed to retrieve data from Delta table, check status code: "
            + str(response.status_code)
            + " and response: "
            + str(response.json())
        }


@app.route("/get_data", methods=["GET"])
def get_data():
    data = get_data_from_delta_table()
    print(data)
    return jsonify(data)


@app.route("/display_data", methods=["GET"])
def display_data():
    data = get_data_from_delta_table()
    return render_template("songs.html", songs=data)


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
