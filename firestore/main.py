from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route('/')
def play():
    # Return a Jinja2 HTML template
    return render_template('homepage.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally with 'python main.py'
    app.run(host='127.0.0.1', port=8080, debug=True)
