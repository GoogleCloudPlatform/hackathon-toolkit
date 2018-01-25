import os

from flask import Flask, redirect, render_template, request

from google.cloud import storage
from google.cloud import videointelligence


app = Flask(__name__)


@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('homepage.html')


# Detects labels given a Google Cloud Storage (GCS) URI.
# Adapted from: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/video/cloud-client/labels/labels.py
def get_label_annotations(gcs_uri):
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]
    operation = video_client.annotate_video(gcs_uri, features=features)

    # Wait until the  annotate_video function call has completed.
    results = operation.result(timeout=90).annotation_results[0]
    label_annotations = results.segment_label_annotations
    return label_annotations


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
    return render_template('homepage.html', video_public_url=video_public_url, video_content_type=video.content_type, label_annotations=label_annotations)

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