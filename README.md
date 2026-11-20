# Student Performance Classifier

A small Flask web application that demonstrates how a machine learning classification model can use marks, attendance and daily task scores to predict an example student performance category.

## Features
- Input marks, attendance and daily task score (0–100)
- Predicts one of four example categories
- Simple web interface built with Flask
- Decision Tree classifier using scikit-learn

## Requirements
- Python 3.10 or newer
- pip

## Run locally
1. Create and activate a virtual environment (recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000` in your browser.

## Model and dataset note
The project currently trains on a small illustrative dataset embedded in `app.py` so it can run immediately. It is only a learning demo and is not suitable for real student evaluation. For a real project, use an authorised, representative dataset, document the labels, evaluate the model with a held-out test set, and check for bias before use.

## Technologies
Python, Flask, NumPy, scikit-learn, HTML, CSS
