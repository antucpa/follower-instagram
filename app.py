from flask import Flask, Response
import requests
import os

app = Flask(__name__)

@app.route('/')
def debug_instagram_html():
    username = "the_drunk_deer"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url, headers=headers)
        html = response.text
        return Response(html, mimetype='text/plain')
    except Exception as e:
        return f"Errore: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
