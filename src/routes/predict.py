from flask import Blueprint, jsonify, request
from utils import downloader
import numpy as np

predict_bp = Blueprint('predict', __name__)
model = downloader.s3_model_download()

@predict_bp.route('/api/v1/predict', methods=['POST'])
def predict_route():
    
    data = request.json
    input_data = np.array(list(data.values())).reshape(1, -1)
    
    if model:
        prediction = model.predict(input_data)
        return jsonify({"prediction": prediction.tolist()})
    else:
        return jsonify({"error": "Error loading s3 model"})

