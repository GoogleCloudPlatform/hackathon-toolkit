import os

from flask import Flask, redirect, render_template, request

from google.cloud import storage
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


app = Flask(__name__)


@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('homepage.html')

# Transcribes the audio file specified by the source_uri.
# Adapted from: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/speech/cloud-client/transcribe.py
def transcribe_audio(source_uri):

    # Create a Speech Client object to interact with the Speech Client Library.
    client = speech.SpeechClient()

    # Create audio and config objects that you'll need to call the API.
    audio = types.RecognitionAudio(uri=source_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Call the Speech API using the Speech Client's recognize function.
    response = client.recognize(config, audio)
    return response

@app.route('/upload_audio', methods=['GET', 'POST'])
def upload_audio():
    # Create a Cloud Storage client.
    storage_client = storage.Client()

    # Get the Cloud Storage bucket that the file will be uploaded to.
    bucket = storage_client.get_bucket(os.environ.get('CLOUD_STORAGE_BUCKET'))

    # Create a new blob and upload the file's content to Cloud Storage.
    audio = request.files['file']
    blob = bucket.blob(audio.filename)
    blob.upload_from_string(
            audio.read(), content_type=audio.content_type)

    # Retrieve a Speech API response for the audio file stored in Cloud Storage
    source_uri = 'gs://{}/{}'.format(os.environ.get('CLOUD_STORAGE_BUCKET'), blob.name)
    response = transcribe_audio(source_uri)
    results = response.results
    
    # Redirect to the home page.
    return render_template('homepage.html', results=results)


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