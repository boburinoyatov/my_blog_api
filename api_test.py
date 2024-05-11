import requests
from pprint import pprint as pp
import json

url = "http://127.0.0.1:8000/api/v1/posts/4/"

payload = json.dumps({
    "title": "new post",
    "content": "new content",
    "is_published": True
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YXNkZjoxMjM0'
}


# Ё
# def get_all_posts():
#     response = requests.request("GET", url, headers=headera, data=payloaЁЁЁd)
#     json_data = json.loads(response.text)
#     return json_data

def patch_all_posts():
    response = requests.request("PUT", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data


if __name__ == "__main__":
    data = patch_all_posts()
    pp(data)
