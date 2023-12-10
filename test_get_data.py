import unittest
from unittest.mock import patch, MagicMock

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

import app  # Import the module where your actual code resides


class TestGetDataFromDeltaTable(unittest.TestCase):
    @patch("app.DefaultAzureCredential")
    @patch("app.SecretClient")
    @patch("app.requests.post")
    def test_get_data_from_delta_table_success(
        self, mock_post, mock_secret_client, mock_credential
    ):
        # Mock Azure Key Vault
        mock_credential.return_value = "mocked_credential"
        mock_secret_client.return_value.get_secret.return_value.value = (
            "mocked_secret_value"
        )

        # Mock Databricks REST API response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "result": {
                "data_array": [
                    {"column1": "value1", "column2": "value2"},
                    {"column1": "value3", "column2": "value4"},
                    # Add more sample data as needed
                ]
            }
        }

        # Call the function with mocked dependencies
        result = app.get_data_from_delta_table()

        # Assertions based on the expected response
        self.assertEqual(
            result,
            [
                {"column1": "value1", "column2": "value2"},
                {"column1": "value3", "column2": "value4"},
                # Add expected data based on the mocked Databricks response
            ],
        )

    @patch("app.DefaultAzureCredential")
    @patch("app.SecretClient")
    @patch("app.requests.post")
    def test_get_data_from_delta_table_failure(
        self, mock_post, mock_secret_client, mock_credential
    ):
        # Mock Azure Key Vault
        mock_credential.return_value = "mocked_credential"
        mock_secret_client.return_value.get_secret.return_value.value = (
            "mocked_secret_value"
        )

        # Mock Databricks REST API response with an error status code
        mock_post.return_value.status_code = 500
        mock_post.return_value.json.return_value = {"error": "Some error message"}

        # Call the function with mocked dependencies
        result = app.get_data_from_delta_table()

        # Assertions based on the expected error response
        self.assertEqual(
            result,
            {
                "error": "Failed to retrieve data from Delta table, check status code: 500 and response: {'error': 'Some error message'}"
            },
        )


if __name__ == "__main__":
    unittest.main()
