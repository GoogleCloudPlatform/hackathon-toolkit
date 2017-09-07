import base64
import os

from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route('/')
def homepage():
    # Return a Jinja2 HTML template and pass in image_entities as a parameter.
    return render_template('homepage.html')

@app.route('/run_language', methods=['GET', 'POST'])
def run_language():
    from google.cloud import language

    # Create a Cloud Translate client.
    client = language.LanguageServiceClient()

    # Retrieve inputs and create document object
    doc = request.form['doc']
    docType = request.form['doc-type']
    print(docType)
    document = language.types.Document(content=doc, type=docType)

    # Retrieve response from Natural Language's analyze_entities() method
    response = client.analyze_entities(
        document=document,
        encoding_type='UTF32')
    entities = response.entities

    # Retrieve response from Natural Language's analyze_sentiment() method
    response = client.analyze_sentiment(
        document=document,
        encoding_type='UTF32')
    sentiment = response.document_sentiment

    return render_template('homepage.html', entities=entities, sentiment=sentiment)

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
