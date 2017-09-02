# gcp-hackathon-demos
Demos for GCP hackathon tech talks

Instructions

(1) Create a project at console.cloud.google.com.
(2) Enable the Vision API. Go to console.cloud.google.com, click the button in the top left, select 'APIs & services', click 'Enable APIs and Services' at the top, search for 'Vision', click the first result, then click the 'Enable' button.
(3) Create a Cloud Storage bucket. Go to console.cloud.google.com, click the button in the top left, scroll down and select 'Storage', click 'Create Bucket' at the top, and name your bucket the same as your project ID.
(4) Set the CLOUD_STORAGE_BUCKET environment variable to your Cloud Storage bucket using command line. Run `export GOOGLE_STORAGE_BUCKET=INSERT_NAME_OF_YOUR_BUCKET`.
(5) Download the Google Cloud SDK command line tool, also known as `gcloud`. See https://cloud.google.com/sdk/downloads#interactive.
(6) Initialize gcloud by running `gcloud init`.
(6) Authenticate by running `gcloud auth application-default login`.
(7) Set up your virtual environment by running `virtualenv env`. If you do not already have `virtualenv` installed, run 'sudo easy_install pip' and then 'pip install virtualenv'.
(8) Enter your virtual environment by running `source env/bin/activate`.
(9) Install dependencies by running `pip install -r requirements.txt`.
(10) Run `python main.py` to test your application locally.
(11) Deploy by running `gcloud app deploy`. This should take several minutes.
