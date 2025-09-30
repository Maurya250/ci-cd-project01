import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my name is Aniket. I am passionate about technology and currently focusing on DevOps and Cybersecurity. I enjoy working on real-world projects, learning step by step, and applying my knowledge to practical solutions. I believe in continuous learning and growth"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)

