# Python Google Cloud Translate sample for Google App Engine Flexible Environment

This sample demonstrates how to use the [Google Cloud Translate API](https://cloud.google.com/translate/) and [Google Cloud Storage](https://cloud.google.com/storage/) on [Google App Engine Flexible Environment](https://cloud.google.com/appengine).

## Setup

Create a project with the [Google Cloud Platform Console Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager). Make note of your project ID, which may be different than your project name. Make sure to [Enable Billing](https://console.cloud.google.com/billing?debugUI=DEVELOPERS) for your project.

Enable the Translate API. Go to the [Google Cloud Platform console](https://console.cloud.google.com), click the button in the top left, select 'APIs & services', click 'Enable APIs and Services' at the top, search for 'Translate', click the first result, then click the 'Enable' button.

Enable the Google Cloud Storage JSON API as well. (If it says 'Manage' when you visit its page, it's already enabled)

Create a Cloud Storage bucket. Go to the [Google Cloud Platform console](https://console.cloud.google.com), click the button in the top left, scroll down and select 'Storage', click 'Create Bucket' at the top, and name your bucket the same as your project ID.

Set the `CLOUD_STORAGE_BUCKET` environment variable to your Cloud Storage bucket using command line:

    export CLOUD_STORAGE_BUCKET=INSERT_NAME_OF_YOUR_BUCKET

Download the [Google Cloud SDK command line tool](https://cloud.google.com/sdk/downloads#interactive), also known as `gcloud`.

Initialize gcloud:

    gcloud init

Create an App Engine project:

    gcloud app create

## Getting the sample code

Run the following command to clone the Github repository:

    git clone https://github.com/ryanmats/gcp-hackathon-demos.git

Change directory to the sample code location:

    cd gcp-hackathon-demos/translate

## Authentication

Set up application default credentials:

    gcloud auth application-default login

Set up a service account. Visit the [Google Cloud Platform console](https://console.cloud.google.com), search 'Service Accounts' on the top search bar, click on the first result, and click the 'Create a Service Account button' towards the top. Give your service account a name and set the 'Role' to Project > Owner. Check the 'Furnish a new private key' box and click 'Create'. Save the generated service account key json file to somewhere on your computer.

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

Before deploying, open the `app.yaml` file and replace `YOUR_CLOUD_STORAGE_BUCKET` with the name of your cloud storage bucket. This allows your code to access the appropriate environment variable when it is deployed.

Deploy your application to App Engine (takes several minutes):

    gcloud app deploy

## Further Reference

[Documentation for Google Cloud Client Libraries for Python](https://googlecloudplatform.github.io/google-cloud-python/latest/index.html)
