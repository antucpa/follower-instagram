from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def get_followers():
    username = "the_drunk_deer"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        count = data['graphql']['user']['edge_followed_by']['count']
        return str(count)
    except:
        return "-1"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
