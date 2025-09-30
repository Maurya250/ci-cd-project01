import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "I see you every day—your smile, your laugh, the way you move—it all stays in my eyes, in my mind. Yet, I never find the courage to speak. Every time I see you close by, my heart races, but my lips remain silent. It feels like just watching you is enough for me, even if I can’t say a word. In front of you, I become a quiet shadow, but inside, my thoughts are full of you. Maybe one day I’ll find the courage to tell you what’s in my heart, but for now, just seeing you, just being near you in silence, is the loudest way my feelings speak."
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)

