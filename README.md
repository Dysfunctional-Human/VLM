Myracle.io Assignment Submission
Greetings! I am Aarav Kumar and this is my submission for the Myracle.io assignment. This repository contains a Flask web application that utilizes a multimodal model to generate detailed test cases based on screenshots of web applications.

Overview
The application uses the microsoft/Phi-3-vision-128k-instruct model to process screenshots and generate comprehensive test cases. The Flask app provides a simple interface where users can upload a screenshot and receive a generated test case as a response.

Features
Homepage: A welcome page with a form to upload screenshots and provide optional context.
Test Case Generation: The model processes the uploaded image and generates a detailed test case based on the provided context and the content of the image.
Requirements
To run the application yourself, kindly clone the repository and install requirements using:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
pip install -r requirements.txt
Running the Application
Ensure you have Python installed.

Clone the repository and navigate to the project directory.

Install the required packages from requirements.txt:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000 to access the application.

Usage
Home Page: Access the home page to upload an image file (screenshot) and provide optional context.
Generate Instructions: Submit the form to generate test cases based on the uploaded image and provided context.
Folder Structure
app.py: The main Flask application file.
templates/index.html: The HTML template for the home page.
requirements.txt: List of required Python packages.
