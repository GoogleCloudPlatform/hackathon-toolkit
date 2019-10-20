from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        client = language.LanguageServiceClient()
        text = request.args.get('message')
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document).document_sentiment
        score = sentiment.score
        magnitude = sentiment.magnitude
        return str(score*magnitude)
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'