from flask import Flask, redirect, render_template, request

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

app = Flask(__name__)


@app.route('/')
def homepage():
    # Return a Jinja2 HTML template of the homepage.
    return render_template('homepage.html')

@app.route('/run_language', methods=['GET', 'POST'])
def run_language():
    # Create a Cloud Natural Language client
    client = language.LanguageServiceClient()

    # Retrieve inputted text from the form and create document object
    text = request.form['text']
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    # Retrieve response from Natural Language API's analyze_entities() method
    response = client.analyze_entities(document)
    entities = response.entities

    # Retrieve response from Natural Language API's analyze_sentiment() method
    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment

    # Return a Jinja2 HTML template of the homepage and pass the 'text', 'entities',
    # and 'sentiment' variables to the frontend. These contain information retrieved
    # from the Natural Language API.
    return render_template('homepage.html', text=text, entities=entities, sentiment=sentiment)

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
