# Myracle.io Assignment Submission

Greetings! I am Aarav Kumar and this is my submission for the Myracle.io assignment. This repository contains a Flask web application that utilizes a multimodal model to generate detailed test cases based on screenshots of web applications.

## Overview

The application uses the `microsoft/Phi-3-vision-128k-instruct` model to process screenshots and generate comprehensive test cases. The Flask app provides a simple interface where users can upload a screenshot and receive a generated test case as a response.

## Features

- **Homepage**: A welcome page with a form to upload screenshots and provide optional context.
- **Test Case Generation**: The model processes the uploaded image and generates a detailed test case based on the provided context and the content of the image.

## Requirements

To run the application yourself, kindly clone the repository and install requirements using:

## Running the Application

1. Ensure you have [Python](https://www.python.org/) installed.

2. Clone the repository and navigate to the project directory:

    ```bash
    git clone <https://github.com/Dysfunctional-Human/VLM>
    cd <VLM>
    ```

3. Install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the application.
