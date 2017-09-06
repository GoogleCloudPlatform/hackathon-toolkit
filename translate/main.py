import base64
import os

from flask import Flask, redirect, render_template, request

from google.cloud import translate

app = Flask(__name__)


@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('homepage.html')

@app.route('/run_translate', methods=['GET', 'POST'])
def run_translate():
    # Create a Cloud Translate client.
    client = translate.Client()

    # Retrieve Translate API's responses for the input text
    input_text = request.form['text']
    lang_response = client.detect_language(input_text)
    translate_response = client.translate(input_text)

    confidence = lang_response.get('confidence')
    inputt = lang_response.get('input')
    language = lang_response.get('language')
    translated_text = translate_response.get('translatedText')

    return render_template('homepage.html', confidence=confidence, inputt=inputt, language=language, 
                                            translated_text=translated_text)

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