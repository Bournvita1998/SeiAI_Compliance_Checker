Compliance Checker API
======================

Overview
--------

This is a simple FastAPI-based API that checks a webpage's content for compliance with a predefined set of rules. The API takes a URL as input, fetches the content of the webpage, and checks it against the compliance rules. The results are returned as a JSON response indicating non-compliant terms and suggestions.

Setup Instructions
------------------

### 1\. Clone the Repository

`git clone https://github.com/Bournvita1998/SeiAI_Compliance_Checker
cd compliance_checker`

### 2\. Create a Virtual Environment

`source venv/bin/activate` 

### 3\. Install the Dependencies

`pip install -r requirements.txt`

### 4\. Run the FastAPI Application

`uvicorn app.__init__:app --reload`

The application will be accessible at `http://127.0.0.1:8000`.

### 5\. Use the API

Send a POST request to `/check_compliance` with a JSON body containing the `url` of the webpage to check:

`curl -X POST http://127.0.0.1:8000/check_compliance -H "Content-Type: application/json" -d '{"url": "https://mercury.com/"}'`

The API will return the compliance results in a JSON response.

Future Enhancements
-------------------

-   Add more complex compliance checks, including machine learning models for advanced content analysis.
-   Support additional input formats, such as PDFs or plain text files or images, etc.
-   Implement more detailed reporting with explanations and recommendations for compliance improvements.
-   Hard coding in compliance rules can be improved so that for a given text, we can automatically create the compliance rules
-   We can break different compliance as per the risk involved with each like: high, medium, low
