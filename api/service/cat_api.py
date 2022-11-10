import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)


def fetch_breeds():
    url = "https://api.thecatapi.com/v1/breeds"
    headers = {
        "x-api-key": "live_X3z9DesKKCqSdk6nKCIt0pjNT5ScwJlAXZwC9Tpr4VOBODxLutVa4RKWy0XfbYZC"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return response.status_code
    except Exception as e:
        logger.error(e)
