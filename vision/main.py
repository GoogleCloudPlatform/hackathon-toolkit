import os
import sys

from flask import Flask, redirect, render_template, request

from google.cloud import firestore
from google.cloud import storage
from google.cloud import vision


app = Flask(__name__)


@app.route('/')
def homepage():
    # Create a Cloud Firestore client.
    firestore_client = firestore.Client()

    # Use the Cloud Firestore client to fetch information from Cloud Firestore about
    # each photo.
    photo_documents = list(firestore_client.collection(u'photos').get())

    # Return a Jinja2 HTML template.
    return render_template('homepage.html', photo_documents=photo_documents)

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
    vision_client = vision.ImageAnnotatorClient()

    # Retrieve a Vision API response for the photo stored in Cloud Storage
    image = vision.types.Image()
    image.source.image_uri = 'gs://{}/{}'.format(os.environ.get('CLOUD_STORAGE_BUCKET'), blob.name)
    
    response = vision_client.annotate_image({'image': image})
    labels = response.label_annotations
    faces = response.face_annotations
    web_entities = response.web_detection.web_entities

    # Create a Cloud Firestore client
    firestore_client = firestore.Client()

    # Get a reference to the document we will upload to
    doc_ref = firestore_client.collection(u'photos').document(blob.name)

    # Note: If we are using Python version 2, we need to convert
    # our image URL to unicode to save it to Cloud Firestore properly.
    if sys.version_info < (3, 0):
        image_public_url = unicode(image_public_url, "utf-8")

    # Construct key/value pairs with data
    data = {
        u'image_public_url': image_public_url,
        u'top_label': labels[0].description
    }

    # Set the document with the data
    doc_ref.set(data)

    # Redirect to the home page.
    return render_template('homepage.html', labels=labels, faces=faces, web_entities=web_entities, image_public_url=image_public_url)


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