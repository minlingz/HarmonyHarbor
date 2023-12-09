# Harmony Harbor (HL)

[![Python package](https://github.com/minlingz/HarmonyHarbor/actions/workflows/python-app.yml/badge.svg)](https://github.com/minlingz/HarmonyHarbor/actions/workflows/python-app.yml)
[![Build and deploy container app to Azure Web App - HarmonyHarbor](https://github.com/minlingz/HarmonyHarbor/actions/workflows/main_HarmonyHarbor.yml/badge.svg)](https://github.com/minlingz/HarmonyHarbor/actions/workflows/main_HarmonyHarbor.yml)

:musical_note: Welcome to the Harmony Harbor service! We offer a microservice-based web application capable of analyzing and adapting to the latest music trends to suit your taste. 

:heart_on_fire: Discover a new way of exploring music with Harmony Harbor, where we transform the experience of finding your next favorite song. Dive into our vast collection of over 100,000 tracks and tailor your listening to fit exactly how you're feeling or what you're doing.

- Fine-tune your search with filters like tempo, song duration, or time signature to find music that resonates with your current activity or mood, from a morning jog to a relaxed evening or those quiet moments lost in a book.

- Interact with our intuitive chatbox that understands your emotions and preferences. Simply express how you feel, like "I'm feeling upbeat," and get three song recommendations with explanations on why they're the perfect fit for you.

:bar_chart: Our analytical tools go beyond basic playlists; we provide insightful analyses into music trends. Discover how song duration and tempo have evolved through the years, reflecting shifts in musical styles. Explore our unique radar charts that profile top artists, contrasting aspects such as average song duration, tempo, and time signature, to reveal the distinctive musical imprint of each artist in their creations.

:hammer_and_pick: Built with Python and Databricks, our service features a containerized approach with Container Registry for security, efficient data handling with top-notch libraries like Spark and Pandas, and robust infrastructure management via IaC tools. Dive into our high-performance service, and enjoy seamless updates through our CI/CD pipeline.

## Contributors

:sparkles: Thanks goes to these wonderful people 

- [Meixiang Du](link): the idea juggler and project wrangler
- [Lin Hui](https://github.com/linhui7): the data whisperer and design Picasso
- [Lisa Wang](link): the API ninja and our ever-ready helper
- [Minling Zhou](https://github.com/minlingz): our very own CTO, Sherlock Holmes with a debugger

## Description (ML)
Harmony Harbor is a microservice-based web application capable of analyzing and adapting to the latest music trends to suit your taste. It offers a unique way of exploring music, with a vast collection of over 100,000 tracks and a chatbox that understands your emotions and preferences. It also provides insightful analyses into music trends, with radar charts that profile top artists and line charts that trace the evolution of song duration and tempo through the years.

## Architecture Diagram (HL & ML)
![Alt text](<images/DE final Fall 2023.png>)

## Technologies Used (ML)
- Python, Flask
- Pandas, NumPy, Matplotlib, Seaborn
- Docker, Azure Container Registry, Azure App Service
- Azure Databricks, Spark SQL, delta tables
- Azure Key Vault, Azure Active Directory
- Azure Resource Manager (ARM) templates
- GitHub Actions, GitHub Secrets, GitHub Codespaces
- OpenAI API
- Locust

## Microservices (ML)
### Harmony Harbor (https://harmonyharbor.azurewebsites.net/)
* `app.py`: This file contains the code for the Harmony Harbor service. It uses the Flask framework to handle the HTTP requests and responses.
    ```python
    from flask import Flask, request, jsonify
    app = Flask(__name__)
    ```
* `requirements.txt`: This file contains the Python dependencies for the Harmony Harbor service. It uses the `requests` library to make HTTP requests to the OpenAI API.
    ```text
    flask==3.0.0
    black==23.3.0
    ruff==0.0.285
    requests==2.31.0
    azure-identity
    azure-keyvault-secrets
    openai
    ```

### Harmony Harbor Chatbot (https://harmonyharbor.azurewebsites.net/chatbot)

### Use of logging
* `app.py`: This file contains the code for logging in the Harmony Harbor service. It uses the Python logging module to log the requests and responses.
    ```python
    logging.basicConfig(filename="app.log", level=logging.ERROR)
    ```
* Azure web app: We use Azure web app to host our service. It provides a centralized location for all our logs, with support for log streaming and log analysis.

### Containerization
* `Dockerfile`: This file is used to build the Docker image for the Harmony Harbor service. It uses the Python base image, installs the Python dependencies, and copies the source code into the image.
    ```dockerfile
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt /app
    RUN pip install -r requirements.txt
    COPY . /app
    EXPOSE 9000
    ENV LANG C.UTF-8
    CMD ["python", "app.py"]
    ```

## Data Engineering (HL)
Our dataset is a subset of the Million Song Dataset, a collection of features and metadata for contemporary music tracks. It is available in the sample datasets included in the Databricks workspace. 

Below is a list of fields we included with each track in the database:
- Artist Name
- Duration
- Release
- Tempo
- Time Signature
- Title
- Year

The ETL pipeline leverages Databricks features to explore and process a raw dataset, utilizing Databricks notebooks to ingest, transform, and load the data into target tables. Additionally, it incorporates error handling, data validation, and automation through a Databricks job for streamlined data processing and visualization.

The transformed data is stored as Delta Lake file, as it's a reliable form with high performance.

Spark SQL offers high-performance, scalable data processing across diverse sources, with seamless integration in the Apache Spark ecosystem. 

AI tools, such as Copilot and ChatGPT, played a crucial role in streamlining the ETL pipeline by providing valuable insights and recommendations on data cleaning techniques, effective error handling strategies, and the selection of appropriate graph types for data analysis. These tools significantly enhanced the efficiency and quality of the data processing workflow, ultimately leading to more informed and accurate decision-making

## Data Science (HL)
We have two intriguing findings that stand out from a data science perspective.

![Artist Comparison](./images/Artists_Comparison.png)

The first finding, depicted in a radar chart, encapsulates the distinctive musical signatures of various top artists by comparing average song duration, tempo, and time signature. This visual distillation demonstrates how data can unravel the unique stylistic elements that define an artist's body of work.

![Trend Analysis](./images/Trend_Analysis.png)

The second revelation comes from a line chart that traces the ebb and flow of song characteristics through the ages. It charts the average duration and tempo of songs, offering a historical lens on how music has adapted to cultural currents and technological advancements from 1925 to 2010. This trend analysis is a testament to data science's capacity to chronicle and interpret the shifting tides of artistic expression.

## Load Testing (Lisa)

## LLM (Lisa)

## Infrastructure as Code (IaC) (MX)
Utilize an Infrastructure as Code (IaC) solution for infrastructure setup and management in Azure with Resource Manager (ARM) templates.

IaC standardizes infrastructure deployment, fostering rapid, error-free scaling and collaboration through version control. This approach streamlines operations, optimizes costs, and ensures robust security and disaster recovery measures.

Azure provides several tools and services for IaC, with Azure Resource Manager (ARM) templates being the primary choice. ARM templates are JSON files that define the resources you want to deploy, their configurations, and the relationships between them.

Using Infrastructure as Code (IaC) in Azure allows us to automate the provisioning and management of our infrastructure.

* Create a template`template.json` that includes App Service, App Service Plan, Application Insights, and deployments for HarmonyHarbor under the Harmony Harbor resource group.
* Set parameters `parameters.json`for the above resources as needed.
* Deploy using Azure Custom deployment, using JSON templates and parameters.

![ARM resource](<images/ARM resource.png>)


## Continuous Integration and Continuous Delivery (CI/CD) (ML)
We use GitHub Actions to implement Continuous Integration and Continuous Delivery (CI/CD) for our service. It provides a workflow to automate the build, test, and deployment of our application.
* Python package: `python-app.yml` - This workflow will run every time a new commit is pushed to main branch. It will install the dependencies, format and lint the code, run the tests, and upload the test results to GitHub.
* Build and deploy container app to Azure Web App: `main_HarmonyHarbor.yml` - This workflow will run every time a new commit is pushed to main branch. It will build the container image, push it to Azure Container Registry, and deploy it to Azure App Service.

## GitHub Configurations (ML)
### Github Actions
We implemented two workflows in GitHub Actions:
* `python-app.yml`: This workflow will run every time a new commit is pushed to main branch. It will install the dependencies, format and lint the code, run the tests, and upload the test results to GitHub.
* `main_HarmonyHarbor.yml`: This workflow will run every time a new commit is pushed to main branch. It will build the container image, push it to Azure Container Registry, and deploy it to Azure App Service.

### Guthub Secrets
* `AzureAppService_ContainerUsername_9be46abaa20344908e13ba6bbe4d7065`: The username for the Azure App Service container registry.
* `AzureAppService_ContainerPassword_aac379ebce6247ab9f1ca5883053939f`: The password for the Azure App Service container registry.

### Github Codespaces
* `devcontainer.json`: This file is used to configure the Codespace. It specifies the Dockerfile to use, the extensions to install, and the commands to run when the Codespace is created.

## Security (ML)
The security of our service is ensured by the following measures:
* `Container Registry`: We use Azure Container Registry to store and manage our container images. It provides a private registry for our Docker container images, with support for all types of container deployments. It integrates with Azure Container Instances, it also supports Azure Active Directory for authentication, so we can control who has access to our images.
* `Azure Key Vault`: We use Azure Key Vault to store and manage our application API tokens integrated with Azure Databricks and OpenAI. It provides centralized key management, with access control, auditing, and logging features. It also integrates with Azure Active Directory for authentication, so we can control who has access to our secrets.

    Python code example in `app.py` to access Azure Key Vault:
    ```python
        key_vault_url = "https://dek.vault.azure.net/"
        credential = DefaultAzureCredential()
        secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
        secret_value = secret_client.get_secret("HLDB").value
    ```
* `Azure Active Directory`: We use Azure Active Directory to manage our users and applications. It provides centralized identity management, with support for multi-factor authentication, single sign-on, and more. It also integrates with Azure Key Vault for authentication, so we can control who has access to our secrets.
* `Github Secrets`: We use Github Secrets to store and manage our application secrets required by CI/CD pipeline with Azure Deployment Center. It provides centralized key management, with access control, auditing, and logging features. It also integrates with Azure Active Directory for authentication, so we can control who has access to our secrets.

    Github workflow example in `main_HarmonyHarbor.yml` in our code access Github Secrets:
    ```yaml
        - name: Log in to registry
        uses: docker/login-action@v2
        with:
            registry: https://706registry.azurecr.io/
            username: ${{ secrets.AzureAppService_ContainerUsername_9be46abaa20344908e13ba6bbe4d7065 }}
            password: ${{ secrets.AzureAppService_ContainerPassword_aac379ebce6247ab9f1ca5883053939f }}
    ```
