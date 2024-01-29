import pandas as pd
from flask import Flask, request, render_template, jsonify
import joblib
import os

app = Flask(__name__)

# Update the model file path
model_path = os.path.abspath('model.pkl')

# Load the model
model = joblib.load(model_path)

# Load the dataset
dataset_path = os.path.abspath('stats.csv')
df = pd.read_csv(dataset_path, delimiter=';', encoding='latin1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve the input data
        print("Received POST request to /predict")
        features = [float(request.form[col]) for col in df.columns if col != 'PTS']
        print("Input Features:", features)

        # Make a prediction
        predicted_points = model.predict([features])[0]
        print("Predicted Points:", predicted_points)

        # Add the prediction to the dataframe
        df_result = pd.DataFrame({'Player': ['Your Player'], 'PTS': [predicted_points]})
        print("Result DataFrame:", df_result)

        # Return the result as JSON
        response_json = df_result.to_json(orient='records')
        print("JSON Response:", response_json)

        return response_json
    except Exception as e:
        print("Error in /predict route:", str(e))
        return jsonify({'error': str(e)}), 500  # Return a JSON error response with status code 500

if __name__ == '__main__':
    app.run(debug=True)
