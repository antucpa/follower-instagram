from flask import Flask
import requests
import re
import os

app = Flask(__name__)

@app.route('/')
def get_followers():
    username = "the_drunk_deer"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://www.instagram.com/{username}/"

    try:
        response = requests.get(url, headers=headers)
        html = response.text

        # Cerca il numero follower usando una regex
        match = re.search(r'"edge_followed_by":{"count":(\d+)}', html)
        if match:
            return match.group(1)
        else:
            return "-1"
    except:
        return "-1"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
