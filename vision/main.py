import base64
import os

from flask import Flask, redirect, render_template, request
from google.cloud import storage
from google.cloud import vision
from google.cloud.vision import types


app = Flask(__name__)


@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('homepage.html')

@app.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo():
    # Create a Cloud Storage client.
    storage_client = storage.Client()

    # Get the Cloud Storage bucket that the file will be uploaded to.
    bucket = storage_client.get_bucket(os.environ.get('CLOUD_STORAGE_BUCKET'))

    # Create a new blob and upload the file's content to Cloud Storage.
    photo = request.files['file']
    blob = bucket.blob(photo.filename)
    blob.upload_from_string(
            photo.read(), content_type=photo.content_type)

    # Make the blob publicly viewable.
    blob.make_public()
    image_public_url = blob.public_url
    
    # Create a Cloud Vision client.
    client = vision.ImageAnnotatorClient()

    # Retrieve a Vision API response for the photo stored in Cloud Storage
    source_uri = 'gs://{}/{}'.format(os.environ.get('CLOUD_STORAGE_BUCKET'), blob.name)
    response = client.annotate_image({
        'image': {'source': {'image_uri': source_uri}},
    })
    labels = response.label_annotations
    faces = response.face_annotations
    web_entities = response.web_detection.web_entities

    # Redirect to the home page.
    return render_template('homepage.html', labels=labels, faces=faces, web_entities=web_entities, public_url=image_public_url)


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