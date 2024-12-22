import requests
import json

def emotion_detector(text_to_analyze):
    # URL of Emotion Predict Service 
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Custom header specifying the model ID for the Emotion Predict Service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the Emotion Predict Service API
    response = requests.post(URL, json=myobj, headers=header)
    # Format the response
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        return formatted_response
    elif response.status_code == 400:
        # Default response for bad input
        formatted_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return formatted_response

def predict_emotion(response_detected):
    if all(value is None for value in response_detected.values()):
        return response_detected
    if response_detected.get('emotionPredictions'):
        emotions = response_detected['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        max_emotion = max(emotions, key=emotions.get)
        formatted_emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': max_emotion
        }
        return formatted_emotions
