from flask import Flask, render_template, request, make_response, jsonify
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

ENDPOINT = "<your API endpoint>"
prediction_key = "<your prediction key>"
prediction_resource_id = "<your prediction resource id>"

CUSTOM_VISION_PROJECT_ID = "<custome vision project id>"
publish_iteration_name = "<published iteration name>"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/image_class", methods=['POST'])
def get_image_class():
    if request.method == 'POST':
        f = request.files['image']
        results = predictor.classify_image(CUSTOM_VISION_PROJECT_ID, 
            publish_iteration_name, f.read())

        best_score = {'name': '', 'score': -1}
        for prediction in results.predictions:
            if prediction.probability * 100 > best_score['score']:
                best_score['name'] = prediction.tag_name
                best_score['score'] = round(prediction.probability * 100, 2)
        return best_score
    return "Error", 404
