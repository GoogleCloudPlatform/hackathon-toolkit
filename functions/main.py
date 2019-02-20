from google.cloud import vision
from google.cloud.vision import types
from google.cloud import firestore

def process_image(data, context):
	file = data

	# Call Vision API and get response
	vision_client = vision.ImageAnnotatorClient()
	image = types.Image()
	image.source.image_uri = 'gs://' + file['bucket'] + '/' + file['name']
	response = vision_client.label_detection(image=image)
    
    # Process labels from Vision API
	labels = response.label_annotations
	labels_array = []
	for label in labels:
		labels_array.append(label.description)
    
    # Add data to Cloud Firestore database
	db = firestore.Client()
	doc_ref = db.collection(u'photos').document(file['name'])
	doc_ref.set({
		u'labelsDetected': labels_array
	})
