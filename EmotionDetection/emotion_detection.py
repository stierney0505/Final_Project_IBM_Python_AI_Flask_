import requests
import json

def emotion_analyzer(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formattedResponse = json.loads(response.text)

    if response.status_code == 400:
        returnJSON = {'anger': None,
                      'disgust': None,
                      'fear': None,
                      'joy': None,
                      'sadness': None,
                      'dominant_emotion' : None
                     }
        return json.dumps(returnJSON)

    data = formattedResponse['emotionPredictions'][0]['emotion'];
    emotions = []
    dominant_emotion = ''
    dominant_value = -1
    for key in data:
        if(key == 'anger'):
            emotions.append(key)
            if(data[key] > dominant_value):
                dominant_emotion = key
                dominant_value = data[key]
        elif(key == 'disgust'):
            emotions.append(key)
            if(data[key] > dominant_value):
                dominant_emotion = key
                dominant_value = data[key]
        elif(key == 'fear'):
            emotions.append(key)
            if(data[key] > dominant_value):
                dominant_emotion = key
                dominant_value = data[key]
        elif(key == 'joy'):
            emotions.append(key)
            if(data[key] > dominant_value):
                dominant_emotion = key
                dominant_value = data[key]
        elif(key == 'sadness'):
            emotions.append(key)
            if(data[key] > dominant_value):
                dominant_emotion = key
                dominant_value = data[key]


    if response.status_code == 200:
        returnJSON = {emotions[0]: data[emotions[0]],
                      emotions[1]: data[emotions[1]],
                      emotions[2]: data[emotions[2]],
                      emotions[3]: data[emotions[3]],
                      emotions[4]: data[emotions[4]],
                      'dominant_emotion' : dominant_emotion
                     }

    return json.dumps(returnJSON)