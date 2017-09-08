import argparse
import base64
import os
import time

from flask import Flask, redirect, render_template, request
from google.cloud import storage
from google.cloud.gapic.videointelligence.v1beta1 import enums
from google.cloud.gapic.videointelligence.v1beta1 import video_intelligence_service_client


app = Flask(__name__)


@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('homepage.html')

# adapted from: 
# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/video/cloud-client/labels/labels.py
def get_label_annotations(gcs_uri):
    """ Detects labels given a Google Cloud Storage (GCS) URI. """
    # [START construct_request]
    video_client = video_intelligence_service_client.VideoIntelligenceServiceClient()
    features = [enums.Feature.LABEL_DETECTION]
    operation = video_client.annotate_video(gcs_uri, features)
    # [END construct_request]

    # [START check_operation]
    while not operation.done():
        time.sleep(20)
    # [END check_operation]

    # [START get_response]
    results = operation.result().annotation_results[0]
    return results.label_annotations
    # [END get_response]


@app.route('/upload_video', methods=['GET', 'POST'])
def upload_video():
    # Create a Cloud Storage client.
    storage_client = storage.Client()

    # Get the Cloud Storage bucket that the file will be uploaded to.
    bucket = storage_client.get_bucket(os.environ.get('CLOUD_STORAGE_BUCKET'))

    # Create a new blob and upload the file's content to Cloud Storage.
    video = request.files['file']
    blob = bucket.blob(video.filename)
    blob.upload_from_string(
            video.read(), content_type=video.content_type)

    # Make the blob publicly viewable.
    blob.make_public()
    video_public_url = blob.public_url

    # Retrieve a Video response for the video stored in Cloud Storage
    source_uri = 'gs://{}/{}'.format(os.environ.get('CLOUD_STORAGE_BUCKET'), blob.name)
    label_annotations = get_label_annotations(source_uri)
    
    # Redirect to the home page.
    return render_template('homepage.html', label_annotations=label_annotations)


@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)