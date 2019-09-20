# Google Cloud Functions Sample

This sample demonstrates how to use the following Google Cloud products together:

- [Google Cloud Functions](https://cloud.google.com/functions/) – Core logic
- [Google Cloud Storage](https://cloud.google.com/storage/) – Image storage
- [Google Cloud Vision API](https://cloud.google.com/vision/) – Image machine learning
- [Google Cloud Firestore](https://cloud.google.com/firestore/) – Results database

## Setup

### Create a Project

1. Create a project with the [Google Cloud Platform Console Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager).
  1. Make note of your project ID, which may be different than your project name.
  1. Make sure to [Enable Billing](https://console.cloud.google.com/billing?debugUI=DEVELOPERS) for your project.

### Create a Firestore Database

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com)
1. Click the button in the top left and select `Firestore`.
    1. Click `Select Native Mode`.
    1. Select a region close to you geographically.
    1. Click `Create Database`.
    1. Wait for your database to be created.

### Enable the Vision API

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com)
1. Click the button in the top left.
1. Select `APIs & services`.
1. Click `Enable APIs and Services` at the top.
1. Search for `Vision`.
1. Click the first result.
1. Click the `Enable` button.

## Download the Sample Code

Run the following command to clone the Github repository:

    git clone https://github.com/GoogleCloudPlatform/hackathon-toolkit.git

Change directory to the sample code location:

    cd hackathon-toolkit/functions

## Deploying to Google Cloud Functions

Deploy the code to Google Cloud Functions:

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com)
1. Click the button in the top left and select `Cloud Functions`.
1. Click `Enable API` then click `Create Function`.

## Create a Google Cloud Function

Create a Google Cloud Function with a `Cloud Storage` trigger in Python:

1. Give your new Cloud Function the name `process_image`.
1. Change the `Trigger` from `HTTP` to `Cloud Storage`.
1. For the `Bucket` field, click `Browse` and then click the basket icon (New bucket) to create a new Cloud Storage bucket.
1. Name the bucket the same as your Google Cloud project.
1. Leave all fields the same and click `Create` to create a Cloud Storage bucket.
1. Click `Select` to select this bucket as the trigger for your Cloud Function.
1. Change the `Runtime` to `Python 3.7`.
1. Copy and paste the `main.py` code from this code sample into the `main.py` file in the inline editor.
1. Copy and paste the `requirements.txt` code from this code sample into the `requirements.txt` file in the inline editor.
1. Change `Function to execute` to `process_image`.
1. Click the `Create` button at the bottom to start the deployment process. Your Cloud Function should take <2 minutes to deploy.

## Testing the Cloud Function

Test the Google Cloud Function by first going to `Storage` to upload a file:

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com).
    1. Click the button in the top left, scroll down and select `Storage`
    1. Select the Cloud Storage bucket you created in the previous section.
    1. Click the `Upload Files` button and select an image from your computer to upload.
1. After the image uploads, click the navigation menu in the top left of your [Google Cloud Platform Console](https://console.cloud.google.com) and select `Firestore`.
    1. Make sure you have a `photos` collection and a document within it named the same as your uploaded image.
    1. Within that document, make sure that there is a `labelsDetected` field with an array of labels detected using the Vision API.

> Note: If you have any issues, visit the dashboard for your Cloud Function in the Cloud Functions section of the [Google Cloud Platform Console](https://console.cloud.google.com). See if there are any errors in the `Errors in the last 7 days` section at the bottom. You can also click the `View Logs` button at the top of your Cloud Function's dashboard.

## Further Reading

- [Google Cloud Functions](https://cloud.google.com/functions/docs/)
- [Google Cloud Functions - Background Functions](https://cloud.google.com/functions/docs/writing/background)
- [Google Cloud Storage](https://cloud.google.com/storage/docs/)
- [Google Cloud Vision API](https://cloud.google.com/vision/docs/)
- [Google Cloud Firestore](https://cloud.google.com/firestore/docs/)
- [Documentation for Google Cloud Client Libraries for Python](https://googlecloudplatform.github.io/google-cloud-python/latest/index.html)
- [Flask Web Framework](http://flask.pocoo.org/docs/1.0/)
