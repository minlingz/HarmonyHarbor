# Hamony Harbor (HL)
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
- [Minling Zhou](link): our very own CTO, Sherlock Holmes with a debugger

## Description (ML)
A publicly accessible auto-scaling container using Azure App Services and Flask ...

## Architecture Diagram (HL & ML)
![Alt text](<images/DE final Fall 2023.png>)
## Microservices (ML)

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

The transformed data is stored as Delta Lake file, as it's a reliable form with high performance.

Spark SQL offers high-performance, scalable data processing across diverse sources, with seamless integration in the Apache Spark ecosystem. It's used for data processing in this project. 

Try-except is used in the program to make sure file is read without error, and data quality is good to proceed with.

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

## GitHub Configurations (ML)

## Security (ML)

