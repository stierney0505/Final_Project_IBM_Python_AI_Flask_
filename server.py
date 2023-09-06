from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_analyzer
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = json.loads(emotion_analyzer(text_to_analyze))
    returnStr = statement = "For the given statement, the system response is 'anger': {:.6f}, 'disgust': {:.6f}, 'fear': {:.6f}, 'joy': {:.6f} and 'sadness': {:.6f}. The dominant emotion is {}."
    formatted_returnStr = returnStr.format(
    response['anger'],
    response['disgust'],
    response['fear'],
    response['joy'],
    response['sadness'],
    response['dominant_emotion'])
    return(formatted_returnStr)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

