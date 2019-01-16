# Google Cloud Natural Language API Python sample for App Engine Standard Environment

This sample demonstrates how to use the [Google Cloud Natural Language API](https://cloud.google.com/natural-language/) on the [App Engine Standard Environment](https://cloud.google.com/appengine). This app allows users to input text, which is sent to the Google Cloud Natural Language API. The frontend of the application displays information retrieved from the Natural Language API including sentiment analysis, entity detection, and entity sentiment.

## Setup using Google Cloud Console

Distribute GCP credits to workshop attendees and have them [activate them](https://console.cloud.google.com/education) for a Google account of their choice.

Visit the [Google Cloud Console](https://console.cloud.google.com). In the top bar to the left of the search bar, you should see either an existing project ID or 'Select a project'. Click on this text and then click the 'NEW PROJECT' button in the top right corner of the popup box. Type in a new project name and click 'CREATE'.

Enable the Natural Language API. In the Google Cloud Console, click the button in the top left, click 'APIs & Services', click 'Enable APIs and Services' at the top, search for 'Natural Language API', click the first result, then click the 'ENABLE' button.

## Launch Cloud Shell

Next, you will launch Cloud Shell, which is basically a virtual machine that has useful Google Cloud Platform programs and tools pre-installed. It has the gcloud command line tool, git, Python, and pip, for example.

In the Google Cloud Console, there should be a small Cloud Shell launch button to the right of the top search bar (not the gift box). If you hover over it it should say 'Activate Google Cloud Shell'. Click on this button.

## Get sample code from GitHub

Run the following command to clone the Github repository:

    git clone https://github.com/ryanmats/gcp-hackathon-demos.git

Change directory to the sample code location:

    cd gcp-hackathon-demos/language

## Authentication

Set up a service account. Search 'Service Accounts' in the top search bar, click on 'Service accounts', and click the 'Create Service Account' button at the top. Give your service account a name and click 'CREATE'. For service account permissions, click 'Select a role' and choose Project > Owner. Click 'CONTINUE', click 'CREATE KEY', and click 'CREATE' to download a JSON service account key to your computer. Click 'DONE' to finish creating your service account.

This will download a JSON file to your computer. Open this file and copy its contents.

Next, direct your attention to the top bar of your Cloud Shell window. Look for an icon that looks like a pen on the right side (if you hover over it it should say 'Launch code editor BETA'). Click this button to launch Cloud Shell's code editor.

On the left bar, open the drop down menu for 'gcp-hackathon-demos'. Right click on the 'language' folder and select 'New File'. Give it the name 'service-account.json'. Paste in the JSON file you copied to your clipboard. The Code Editor will automatically save this file.

Back in Cloud Shell, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to the service account key location:

    export GOOGLE_APPLICATION_CREDENTIALS=service-account.json

## Running Locally

Set up your virtual environment:

    virtualenv env

Enter your virtual environment:

    source env/bin/activate

Install dependencies:

    pip install -r requirements.txt

Test your application locally:

    python main.py

At the top right corner of Cloud Shell there should be a button that looks like an eye (if you hover over it it says 'Web preview'). Click this button and select 'Preview on port 8080.'

Test out the application by entering some text and viewing information returned from the Natural Language API.

Back in Cloud Shell, type `Control-C` when you are finished.

When you are ready to leave your virtual environment:

    deactivate

## Deploying to App Engine

Deploy your application to App Engine (should take <1 minute). When prompted to choose a region, choose the one that is closest to you geographically.

    gcloud app deploy

## Further Reference

[Google Cloud Natural Language API](https://cloud.google.com/natural-language/docs/)

[App Engine Standard Python 3.7 Quickstart Tutorial](https://cloud.google.com/appengine/docs/standard/python3/quickstart)

[Documentation for Google Cloud Client Libraries for Python](https://googlecloudplatform.github.io/google-cloud-python/latest/index.html)

[Flask Web Framework](http://flask.pocoo.org/docs/1.0/)

[Generating Templates in Flask with Jinja2](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates)
