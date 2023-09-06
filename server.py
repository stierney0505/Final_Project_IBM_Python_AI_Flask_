"""
This module creates a server that hosts a basic web page
that takes text input and analyzes the emotions of the 
statement and returns the values of the emotions analyzed
"""
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_analyzer



app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """
    This function sends a request to the api to analyze a string.

    :return: A formatted string with the emotions and scores
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = json.loads(emotion_analyzer(text_to_analyze))
    if response['anger'] is None:
        return "Invalid text! Please try again!"
    return_str = "For the given statement, the system response is 'anger': {:.6f}, " \
                "'disgust': {:.6f}, 'fear': {:.6f}, 'joy': {:.6f} and 'sadness': {:.6f}." \
                "The dominant emotion is {}."
    formatted_return_str = return_str.format(
    response['anger'],
    response['disgust'],
    response['fear'],
    response['joy'],
    response['sadness'],
    response['dominant_emotion'])
    return formatted_return_str

@app.route("/")
def render_index_page():
    """
    route for default page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
