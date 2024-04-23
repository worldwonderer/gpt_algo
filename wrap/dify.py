import logging
import os
import json

import requests

BASE_URL = 'https://api.dify.ai/v1'
API_KEY = os.getenv("DIFY_API_KEY")


def fuzzy_search(query):
    if API_KEY == '' or API_KEY is None:
        return
    url = BASE_URL + '/chat-messages'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    data = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "conversation_id": "",
        "user": "gpt_algo",
    }
    try:
        res = requests.post(url, headers=headers, json=data, timeout=10)
        return parse_title_slug(res.json())
    except requests.exceptions.RequestException as e:
        logging.warning(f'dify api request {data} err {e}')
        return
    except json.JSONDecodeError as e:
        logging.warning(f'dify api response decode err {e}')
        return


def parse_title_slug(message):
    answer = message['answer']
    answer = answer.replace('```json', '').replace('```', '')
    title_slug = None
    try:
        title_slug = json.loads(answer)['title_slug']
    except json.JSONDecodeError:
        logging.warning(f'dify api parse json err')
    except KeyError:
        logging.warning(f'dify api parse title slug err')
    return title_slug
