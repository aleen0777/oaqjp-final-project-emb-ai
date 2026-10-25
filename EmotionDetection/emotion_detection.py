
import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze the emotions expressed in the input text.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(
        url,
        headers=headers,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30
    )

    if response.status_code == 200:
        return response.json()

    return None
