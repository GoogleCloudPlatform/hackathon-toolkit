# Google Cloud Video Intelligence API Sample

This sample demonstrates how to use the [Google Cloud Video Intelligence API](https://cloud.google.com/video-intelligence/) and [Google Cloud Storage](https://cloud.google.com/storage/) on the [App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python3/).

The frontend of the application displays information retrieved from the Video Intelligence API including the labels detected. It also displays the uploaded video served via Google Cloud Storage.

## Setup

1. Create a project with the [Google Cloud Platform Console Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager).
  1. Make note of your project ID, which may be different than your project name.
  1. Make sure to [Enable Billing](https://console.cloud.google.com/billing?debugUI=DEVELOPERS) for your project.

### Enable the Video Intelligence API

1. Go to the [Google Cloud Platform console](https://console.cloud.google.com).
1. Click the button in the top left, select `APIs & services`.
1. Click `Enable APIs and Services` at the top.
1. Search for `Video Intelligence`, click the first result, then click the `Enable` button.
1. Enable the Google Cloud Storage JSON API as well. (If it says 'Manage' when you visit its page, it's already enabled)

### Create a Cloud Storage bucket

1. Go to the [Google Cloud Platform console](https://console.cloud.google.com).
1. Click the button in the top left, scroll down and select `Storage`.
1. Click `Create Bucket` at the top.
1. Name your bucket the same as your project ID.

Set the `CLOUD_STORAGE_BUCKET` environment variable to your Cloud Storage bucket using command line:

    export CLOUD_STORAGE_BUCKET=INSERT_NAME_OF_YOUR_BUCKET

### Set up the Cloud SDK

Download the [Google Cloud SDK command line tool](https://cloud.google.com/sdk/downloads#interactive), also known as `gcloud`.

Initialize gcloud, selecting your Google account and project ID:

    gcloud init

## Getting the sample code

Run the following command to clone the Github repository:

    git clone https://github.com/GoogleCloudPlatform/hackathon-toolkit.git

Change directory to the sample code location:

    cd hackathon-toolkit/video

## Authentication

Set up a service account.

1. Visit the [Google Cloud Platform console](https://console.cloud.google.com).
1. Search `Service Accounts` on the top search bar, click on `Service accounts`.
1. Click the `Create Service Account` button at the top.
1. Give your service account a name and click `CREATE`.
    1. For service account permissions, click `Select a role` and choose `Project > Owner`.
    1. Click `CONTINUE`.
    1. Click `CREATE KEY`, and click `CREATE` to download a JSON service account key to your computer.
    1. Click `DONE` to finish creating your service account.
    1. Save the generated service account key JSON file to somewhere on your computer and rename it to `key.json`.

Set the `GOOGLE_APPLICATION_CREDENTIALS` variable to point to the service account key location:

    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service/account/key.json

## Running Locally

Set up your virtual environment:

    virtualenv env

> Note: If you do not already have `virtualenv` installed, run 'sudo easy_install pip' and then 'pip install virtualenv'.

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

Deploy your application to App Engine (should take <1 minute). When prompted to choose a region, choose the one that is closest to you geographically.

    gcloud app deploy

## Further Reference

- [Google Cloud Video Intelligence API](https://cloud.google.com/video-intelligence/docs/)
- [Google Cloud Storage](https://cloud.google.com/storage/docs/)
- [App Engine Standard Python 3.7 Quickstart Tutorial](https://cloud.google.com/appengine/docs/standard/-python3/quickstart)
- [Documentation for Google Cloud Client Libraries for Python](https://googlecloudplatform.github.io/-google-cloud-python/latest/index.html)
- [Flask Web Framework](http://flask.pocoo.org/docs/1.0/)
- [Generating Templates in Flask with Jinja2](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates)
