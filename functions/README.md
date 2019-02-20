# Google Cloud Functions, Cloud Storage, Vision API, and Cloud Firestore Python sample

This sample demonstrates how to use [Google Cloud Functions](https://cloud.google.com/functions/) with a [Google Cloud Storage](https://cloud.google.com/storage/) trigger to call the [Google Cloud Vision API](https://cloud.google.com/vision/) and store data in the [Google Cloud Firestore](https://cloud.google.com/firestore/) database.

## Setup

Create a project with the [Google Cloud Platform Console Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager). Make note of your project ID, which may be different than your project name. Make sure to [Enable Billing](https://console.cloud.google.com/billing?debugUI=DEVELOPERS) for your project.

Go to the [Google Cloud Platform Console](https://console.cloud.google.com), click the button in the top left and select 'Firestore'. Click 'Select Native Mode', select a region close to you geographically, then click 'Create Database'. Wait for your database to be created.

Enable the Vision API. Go to the [Google Cloud Platform Console](https://console.cloud.google.com), click the button in the top left, select 'APIs & services', click 'Enable APIs and Services' at the top, search for 'Vision', click the first result, then click the 'Enable' button.

## Getting the sample code

Run the following command to clone the Github repository:

    git clone https://github.com/ryanmats/gcp-hackathon-demos.git

Change directory to the sample code location:

    cd gcp-hackathon-demos/functions

## Deploying to Google Cloud Functions

Go to the [Google Cloud Platform Console](https://console.cloud.google.com), click the button in the top left and select 'Cloud Functions'. Click 'Enable API' then click 'Create Function'.

Give your new Cloud Function an appropriate name (such as process_image). Change the Trigger from HTTP to Cloud Storage.

For the 'Bucket' field, click 'Browse' and then click the basket icon (New bucket) to create a new Cloud Storage bucket. Name it the same as your Google Cloud project. Leave all fields the same and click 'Create' to create a Cloud Storage bucket. Click 'Select' to select this bucket as the trigger for your Cloud Function.

Change the Runtime from Node.js 6 to Python 3.7 (Beta).

Copy and paste the main.py code from this code sample into the main.py file in the inline editor.

Copy and paste the requirements.txt code from this code sample into the requirements.txt file in the inline editor.

Change 'Function to execute' to process_image.

Click the 'Create' button at the bottom to start the deployment process. Your Cloud Function should take <2 minutes to deploy.

## Testing the Cloud Function

Go to the [Google Cloud Platform Console](https://console.cloud.google.com), click the button in the top left, scroll down and select 'Storage', then select the Cloud Storage bucket you created in the previous section. Click the 'Upload Files' button and select an image from your computer to upload.

After the image uploads, click the navigation menu in the top left of your [Google Cloud Platform Console](https://console.cloud.google.com) and select 'Firestore'. Make sure you have a 'photos' collection and a document within it named the same as your uploaded image. Within that document, make sure that there is a 'labelsDetected' field with an array of labels detected using the Vision API.

If you have any issues, visit the dashboard for your Cloud Function in the Cloud Functions section of the [Google Cloud Platform Console](https://console.cloud.google.com). See if there are any errors in the 'Errors in the last 7 days' section at the bottom. You can also click the 'View Logs' button at the top of your Cloud Function's dashboard.

## Further Reference

[Google Cloud Functions](https://cloud.google.com/functions/docs/)

[Google Cloud Functions - Background Functions](https://cloud.google.com/functions/docs/writing/background)

[Google Cloud Storage](https://cloud.google.com/storage/docs/)

[Google Cloud Vision API](https://cloud.google.com/vision/docs/)

[Google Cloud Firestore](https://cloud.google.com/firestore/docs/)

[Documentation for Google Cloud Client Libraries for Python](https://googlecloudplatform.github.io/google-cloud-python/latest/index.html)

[Flask Web Framework](http://flask.pocoo.org/docs/1.0/)
