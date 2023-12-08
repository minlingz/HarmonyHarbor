# Hamony Harbor (HL)
:musical_note: Welcome to the Music Trend Analysis service! We offer a microservice-based web application capable of analyzing and adapting to the latest music trends to suit your taste. 

:heart_on_fire: Gone are the days of simple searches for songs and artists. Our Music Trend Analysis service revolutionizes the way you find music by offering advanced search options based on the tempo, duration, or time signature of tracks. Select the perfect soundtrack from our extensive library of over 100,000 songs to match the rhythm of your day, whether you’re energizing for a run, unwinding in the evening, or seeking the serene accompaniment for your reading time.

:bar_chart: Our analytical tools go beyond basic playlists; we provide insightful analyses into music trends. Discover how song duration and tempo have evolved through the years, reflecting shifts in musical styles. Explore our unique radar charts that profile top artists, contrasting aspects such as average song duration, tempo, and time signature, to reveal the distinctive musical imprint of each artist in their creations.

:hammer_and_pick: Built with Python and Databricks, our service features a containerized approach with Container Registry for security, efficient data handling with top-notch libraries like Spark and Pandas, and robust infrastructure management via IaC tools. Dive into our high-performance service, and enjoy seamless updates through our CI/CD pipeline.

## Description (ML)
A publicly accessible auto-scaling container using Azure App Services and Flask ...

## Architecture Diagram (HL & ML)

## Microservices (ML)

## Data Engineering (HL)
data set, analysis

## Data Science (HL)
plots , explain, why this analysis

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
![ARM resource](https://github.com/minlingz/HarmonyHarbor/blob/main/ARM%20resource.png)


## Continuous Integration and Continuous Delivery (CI/CD) (ML)

## GitHub Configurations (ML)

## Security (ML)

