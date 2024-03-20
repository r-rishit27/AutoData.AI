
# AutoData.AI

AutoData.AI is an automated data analytics and visualization tool built using OpenAI API and concepts of generative AI. The tool is deployed on Streamlit using the PandasAI LLM framework with the SmartDataframe framework.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
## Introduction

AutoData.AI is an innovative data analytics and visualization tool that leverages the power of OpenAI's language models to automate the process of data analysis and visualization. With AutoData.AI, users can easily upload their CSV files, interact with the data using natural language queries, and generate insightful visualizations without the need for complex coding or manual data manipulation.

## Features

- Upload multiple CSV files for analysis.
- Interact with the data using natural language queries powered by OpenAI's language models.
- Automatically generate descriptive statistics, insights, and visualizations.
- Customize visualizations and analysis based on user preferences.
- Deployed as a web application using Streamlit for easy accessibility.

## Usage

1. Upload your CSV files using the file uploader in the sidebar.
2. Select a CSV file from the uploaded files.
3. Interact with the data by entering natural language queries in the text area provided.
4. Click on the "Chat with csv" button to generate automated analysis and visualizations based on your queries.
5. Explore the generated insights and visualizations displayed on the web application.

## Contributing

Contributions to AutoData.AI are welcome! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

Please ensure that your contributions adhere to the project's coding standards and guidelines.

"""

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
