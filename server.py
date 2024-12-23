"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, predict_emotion

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the user-provided text for emotions and return the result.
    Returns the formatted response with emotion scores and dominant emotion.
    If the input is invalid, returns an error message.
    """
    # Retrieve the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    formatted_response = predict_emotion(response)

    if formatted_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given text, the system response is "
        f"'anger': {formatted_response['anger']}, "
        f"'disgust': {formatted_response['disgust']}, "
        f"'fear': {formatted_response['fear']}, "
        f"'joy': {formatted_response['joy']} and "
        f"'sadness': {formatted_response['sadness']}. "
        f"The dominant emotion is {formatted_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main application page.
    Returns HTML template for the main page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
