# Google Cloud Translate API Python sample for App Engine Standard Environment

This sample demonstrates how to use the [Google Cloud Translate API](https://cloud.google.com/translate/) on the [App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python3/). This app allows users to input text, which is sent to the Google Cloud Translate API. The frontend of the application displays information retrieved from the Translate API including the French and Chinese translations of the text and the detected language for the input text.

## Setup

Create a project with the [Google Cloud Platform Console Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager). Make note of your project ID, which may be different than your project name. Make sure to [Enable Billing](https://console.cloud.google.com/billing?debugUI=DEVELOPERS) for your project.

Enable the Translate API. Go to the [Google Cloud Platform console](https://console.cloud.google.com), click the button in the top left, select 'APIs & services', click 'Enable APIs and Services' at the top, search for 'Translate', click the first result, then click the 'Enable' button.

Download the [Google Cloud SDK command line tool](https://cloud.google.com/sdk/downloads#interactive), also known as `gcloud`.

Initialize gcloud, selecting your Google account and project ID:

    gcloud init

## Getting the sample code

Run the following command to clone the Github repository:

    git clone https://github.com/ryanmats/gcp-hackathon-demos.git

Change directory to the sample code location:

    cd gcp-hackathon-demos/translate

## Authentication

Set up a service account. Visit the [Google Cloud Platform console](https://console.cloud.google.com), search 'Service Accounts' on the top search bar, click on 'Service accounts', and click the 'Create Service Account' button at the top. Give your service account a name and click 'CREATE'. For service account permissions, click 'Select a role' and choose Project > Owner. Click 'CONTINUE', click 'CREATE KEY', and click 'CREATE' to download a JSON service account key to your computer. Click 'DONE' to finish creating your service account. Save the generated service account key JSON file to somewhere on your computer and rename it to key.json.

Set the `GOOGLE_APPLICATION_CREDENTIALS` variable to point to the service account key location:

    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service/account/key.json

## Running Locally

Set up your virtual environment:

    virtualenv env

Note: If you do not already have `virtualenv` installed, run 'sudo easy_install pip' and then 'pip install virtualenv'.

Enter your virtual environment:

    source env/bin/activate

Install dependencies:

    pip install -r requirements.txt

Test your application locally:

    python main.py

Visit `localhost:8080` to view your application running locally. Press `Control-C` from command line when you are finished.

When you are ready to leave your virtual environment:

    deactivate

## Deploying to App Engine

Deploy your application to App Engine (should take <1 minute). When prompted to choose a region, choose the one that is closest to you geographically.

    gcloud app deploy

## Further Reference

[Google Cloud Translate API](https://cloud.google.com/translate/docs/)

[App Engine Standard Python 3.7 Quickstart Tutorial](https://cloud.google.com/appengine/docs/standard/python3/quickstart)

[Documentation for Google Cloud Client Libraries for Python](https://googlecloudplatform.github.io/google-cloud-python/latest/index.html)

[Flask Web Framework](http://flask.pocoo.org/docs/1.0/)

[Generating Templates in Flask with Jinja2](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates)
