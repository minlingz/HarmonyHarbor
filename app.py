# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import requests
import json
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import logging
from openai import OpenAI


logging.basicConfig(filename="app.log", level=logging.ERROR)

app = Flask(__name__)

delta_table_url = (
    "https://adb-1158426884895395.15.azuredatabricks.net/api/2.0/sql/statements/"
)


# @app.route("/get_data")
def get_data_from_delta_table(q="SELECT * FROM prepared_song_data LIMIT 10"):
    key_vault_url = "https://dek.vault.azure.net/"
    credential = DefaultAzureCredential()

    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

    secret_value = secret_client.get_secret("HLDB").value

    query = q
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


@app.route("/execute_query", methods=["POST"])
def execute_query():
    q = request.form.get("queryInput")
    data = get_data_from_delta_table(q)
    return render_template("songs.html", songs=data)


@app.route("/get_data", methods=["GET"])
def get_data():
    data = get_data_from_delta_table()
    print(data)
    return jsonify(data)


@app.route("/display_data", methods=["GET"])
def display_data():
    data = get_data_from_delta_table()
    return render_template("songs.html", songs=data)


def get_completion(prompt, model="gpt-3.5-turbo"):
    key_vault_url = "https://dek.vault.azure.net/"
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    openai_secret_value = secret_client.get_secret("OPENAIAPIKEY").value

    client = OpenAI(api_key=openai_secret_value)
    prompt_complete = f"""
        Based on my preference below. give me a list of song names randomly.

        The output should be a list of 3 song names. 
        And with each song, include the artist name and the song's genre.
        And song's release year, duration, tempo, mood, best lyrics. 
        And why I should listen to it. 
        The reason should be related to user's preference.

        The user's preference is: {prompt}
        The preference does not necessarily has a very explicit idea about music. 
        Think about user's sentiment and background to understand the preference.

        
        At the end, say some warm words to the user.

        At the very end. Say 
        "Thank you for using our service. 
        Keep interacting with me if you need more songs."

        Don't print of bulk of responses, make it easier to read with new lines.
    """
    messages = [{"role": "user", "content": prompt_complete}]
    try:
        response = client.chat.completions.create(
            model=model, messages=messages, temperature=0
        )
        # print(response.choices[0].message)

        content = response.choices[0].message.content
        return content
    except Exception as e:  # if the model fails to return a response
        print(f"Error: {e}")
        logging.error(e)
        return "Sorry, I don't know how to respond to that."


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    response = get_completion(userText)
    # return str(bot.get_response(userText))
    return response


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/stats")
def stats():
    return render_template("stats.html")


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
