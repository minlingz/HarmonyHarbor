"""
import unittest
from unittest.mock import patch, MagicMock

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

import app  # Import the module where your actual code resides


class TestGetCompletion(unittest.TestCase):
    #     @patch("app.DefaultAzureCredential")
    #     @patch("app.SecretClient")
    #     @patch("openai.OpenAI")
    #     def test_get_completion_success(
    #         self, mock_openai, mock_secret_client, mock_credential
    #     ):
    #         # Mock Azure Key Vault
    #         mock_credential.return_value = "mocked_credential"
    #         mock_secret_client.return_value.get_secret.return_value.value = (
    #             "mocked_openai_secret_value"
    #         )

    #         # Mock the OpenAI class and its methods
    #         mock_response = MagicMock()
    #         mock_response.content = "Mocked completion content"
    #         mock_openai.return_value.Completion.create.return_value = mock_response

    #         # Call the function with mocked dependencies
    #         result = app.get_completion("User's preference")

    #         # Assertions based on the expected response
    #         self.assertEqual(result, "Mocked completion content")

    @patch("app.DefaultAzureCredential")
    @patch("app.SecretClient")
    @patch("openai.OpenAI")
    def test_get_completion_failure(
        self, mock_openai, mock_secret_client, mock_credential
    ):
        # Mock Azure Key Vault
        mock_credential.return_value = "mocked_credential"
        mock_secret_client.return_value.get_secret.return_value.value = (
            "mocked_openai_secret_value"
        )

        # Mock the OpenAI class to simulate an exception
        mock_openai.return_value.Completion.create.side_effect = Exception(
            "Mocked error"
        )

        # Call the function with mocked dependencies
        result = app.get_completion("User's preference")

        # Assertions based on the expected error response
        self.assertEqual(result, "Sorry, I don't know how to respond to that.")


if __name__ == "__main__":
    unittest.main()
"""
