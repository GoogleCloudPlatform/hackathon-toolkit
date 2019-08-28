# Google Cloud Firestore Code Sample

This sample demonstrates how to use [Google Cloud Firestore](https://firebase.google.com/docs/firestore/)
on [Google App Engine standard environment](https://cloud.google.com/appengine).

<img width="551" alt="Screen Shot 2019-08-28 at 17 18 53" src="https://user-images.githubusercontent.com/744973/63893374-fea5fd00-c9b7-11e9-8436-af97c51e7262.png">

## Download the Sample Code

Run the following command to clone the Github repository:

    git clone https://github.com/GoogleCloudPlatform/hackathon-toolkit.git

Change directory to the sample code location:

    cd hackathon-toolkit/firestore

## Set Up Firebase

1. Open the [Firebase Console](https://console.firebase.google.com/) and create a new project.
1. On the left navigation bar, click `Develop`, then click `Database`, then click `Create Database`.
1. Click the button for `Start in test mode`, then click `Enable`.
1. On the left navigation bar at the top, click `Project Overview`.
    1. Under `Get started by adding Firebase to your app`, click the `</>` button. This will help you add Firebase to your web app.
    1. Set an `App nickname` and press `Next`.
    1. Copy everything from the `var firebaseConfig = {` line down to the `};` line.
1. In the `templates/homepage.html` code file, find the `// Firebase Configuration - REPLACE WITH YOUR OWN VALUES` comment and replace the existing config values with your own config values that you just copied from the Firebase console. Make sure to fix the spacing.
1. In the `templates/dashboard.html` code file, find the `// Firebase Configuration - REPLACE WITH YOUR OWN VALUES` comment and replace the existing config values with your own config values that you just copied from the Firebase console. Make sure to fix the spacing.

## Set Up the Cloud Firestore Database

In the [Firebase Console](https://console.firebase.google.com/), click `Database` on the left navigation bar.

### Create an `answers` Collection

1. Click `Start Collection`.
    1. Set `Collection ID` to `answers` and press `Next`.
1. Next you will create your first document for this collection.
    1. Set the `Document ID` to be `sunsetPhoto`.
    1. Name your field `answers` and change the type to `array`.
    1. Add a few array `string` values like `sunset`, `beach`, `ocean`, and `tree`.
        1. (These will be your sample correct answers for the app.)
    1. Click `Save` to create your new collection.

### Create a `scores` Collection

1. Click `Start Collection` again.
    1. Set `Collection ID` to `scores` and press `Next`.
1. Next you will create your first document for this collection.
    1. Set the `Document ID` to be `groupScore`.
        1. Name your field `correct`, change its type to `number`, and set its value to be `0`.
        1. Click the `Add field` button to create another field named `incorrect`, with type of `number`, and a value of `0`.
    1. Click `Save` to create your new collection.

Congrats! Your Cloud Firestore database is all set up for this sample app.

## Running Locally

Set up your virtual environment:

    virtualenv env

Note: If you do not already have `virtualenv` installed, run `sudo easy_install pip` and then `pip install virtualenv`.

Enter your virtual environment:

    source env/bin/activate

Install dependencies:

    pip install -r requirements.txt

Test your application locally:

    python main.py

Visit `localhost:8080` to view your application running locally. The root URL is where users play the game and guess which labels the Cloud Vision API detected for the photo. Visit `localhost:8080/dashboard` to view the dashboard for a summary of scores and guesses and a demonstration of the realtime aspect of the app.

Press `Control-C` from command line when you are finished.

When you are ready to leave your virtual environment:

    deactivate

## Deploying to App Engine

Download the [Google Cloud SDK command line tool](https://cloud.google.com/sdk/downloads#interactive), also known as `gcloud`.

Initialize gcloud, selecting your Google account and project ID (the same one you created in the Firebase console):

    gcloud init

Deploy your application to App Engine (takes 10-20 seconds).

    gcloud app deploy

Once it finishes deploying, visit your app at `YOUR_PROJECT_ID.appspot.com` and `YOUR_PROJECT_ID.appspot.com/dashboard`.

## Further Reference

- [Documentation and Tutorials for Google Cloud Firestore](https://firebase.google.com/docs/firestore/)
- [App Engine Standard for Python Flask Quickstart](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
- [App Engine Flexible for Node.js Tutorial](https://cloud.google.com/nodejs/getting-started/hello-world)
- [Google Cloud Vision API](https://cloud.google.com/vision/)
- [Google Cloud Natural Language API](https://cloud.google.com/natural-language/)
- [Google Cloud Speech API](https://cloud.google.com/speech/)
- [Google Cloud Translation API](https://cloud.google.com/translate/)
- [Google Cloud Video Intelligence API](https://cloud.google.com/video-intelligence/)
