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

        # DEBUG: mostra i primi 500 caratteri della pagina HTML
        return html[:500]

    except Exception as e:
        return f"Errore: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
