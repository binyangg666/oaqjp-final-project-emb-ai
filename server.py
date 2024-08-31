"""
server.py

This module provides server functionalities. 
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")

def sent_detector():
    """
        Detects and returns the emotions according to the input text.

        Returns:
            A list of strings containing the emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response"
            f" is 'anger': {anger}, 'disgust': {disgust}, "
            f"'fear': {fear}, 'joy': {joy} and"
            f" 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
        Renders and returns the HTML content for the index page.

        Returns:
            str: The HTML content of the index page as a string.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
