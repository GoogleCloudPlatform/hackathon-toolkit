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

    # Retrieve Translate API's detect_language response for the input text
    form_text = request.form['text']
    detect_language_response = client.detect_language(form_text)
    confidence = detect_language_response.get('confidence')
    input_text = detect_language_response.get('input')
    language = detect_language_response.get('language')

    # Retrieve Translate API's translate to french response for the input text
    # See https://cloud.google.com/translate/docs/languages for supported target_language values.
    translate_response_french = client.translate(form_text, target_language='fr')
    translated_text_french = translate_response_french.get('translatedText')

    # Retrieve Translate API's translate to traditional Chinese response for the input text
    translate_response_chinese = client.translate(form_text, target_language='zh-TW')
    translated_text_chinese = translate_response_chinese.get('translatedText')

    return render_template('homepage.html', confidence=confidence, input_text=input_text, language=language, 
                                            translated_text_french=translated_text_french, translated_text_chinese=translated_text_chinese)

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