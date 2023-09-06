from EmotionDetection.emotion_detection import emotion_analyzer
import unittest
import json

class TestEmotionAnalzyer(unittest.TestCase):
    def test_emotion_analyzer(self):
        result_1 = json.loads(emotion_analyzer('I am glad this happened'))
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        result_2 = json.loads(emotion_analyzer('I am really mad about this'))
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        result_3 = json.loads(emotion_analyzer('I feel disgusted just hearing about this'))
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        result_4 = json.loads(emotion_analyzer('I am so sad about this'))
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        result_5 = json.loads(emotion_analyzer('I am really afraid that this will happen'))
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()