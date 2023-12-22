import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()

# Get environment variables.
api_key = os.getenv("API_KEY")

# Start CORS and fix security issues.
app = Flask(__name__)
CORS(app, origins=["http://localhost:8080"])

def scrape_website(url):
    content = BeautifulSoup(requests.get(url).text, "html.parser")
    content = content.get_text()
    return content

def get_chatgpt_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
            "role": "system",
            "content": "You are a helpful assistant who is an expert in every field!"
            },{
            "role": "user",
            "content": f"Do ___, return information in this exact format: ____"
            },
        ],
        "max_tokens": 500,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    response = response.json()
    resp = response['choices'][0]['message']['content'].split('\n')
    return resp

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    randomNum = scrape_website("https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new")
    data = {"message": f"Here is a random number: {randomNum}"}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "Data received.", "content": data['msg']})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
