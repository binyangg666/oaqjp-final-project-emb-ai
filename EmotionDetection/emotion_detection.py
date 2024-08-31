import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    
    anger = None
    disgust = None
    fear = None
    joy = None
    sadness = None
    dominant = None
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text) 
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotion_predictions['anger']
        max_value = anger
        dominant = 'anger'
        disgust = emotion_predictions['disgust']
        if (disgust > max_value):
            max_value = disgust
            dominant = 'disgust'
        fear = emotion_predictions['fear']
        if (fear > max_value):
            max_value = fear
            dominant = 'fear'
        joy = emotion_predictions['joy']
        if (joy > max_value):
            max_value = joy
            dominant = 'joy'
        sadness = emotion_predictions['sadness']
        if (sadness > max_value):
            max_value = sadness
            dominant = 'sadness'

    return {'anger': anger, 'disgust': disgust, 'fear' : fear, 
        'joy': joy, 'sadness' : sadness, 'dominant_emotion' : dominant}
