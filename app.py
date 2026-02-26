from flask import Flask, request, jsonify, send_file
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        topic = data.get("topic")
        style = data.get("style")

        if not topic:
            return jsonify({"response": "Please enter a topic."})

        prompt = f"Explain {topic} in {style} style."

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return jsonify({
            "response": response.choices[0].message.content
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"response": "Server error occurred."})

if __name__ == "__main__":
    app.run(debug=True)