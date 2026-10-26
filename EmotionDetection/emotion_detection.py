
import requests


def emotion_detector(text_to_analyze):
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not text_to_analyze or not text_to_analyze.strip():
        return empty_result

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json={"raw_document": {"text": text_to_analyze}},
            timeout=30
        )

        if response.status_code == 400:
            return empty_result

        if response.status_code != 200:
            return empty_result

        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        scores = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }

        scores["dominant_emotion"] = max(
            scores, key=scores.get
        )

        return scores

    except (requests.RequestException, ValueError, KeyError, IndexError):
        return empty_result
