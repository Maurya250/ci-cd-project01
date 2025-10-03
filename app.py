import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "I tried to eat healthy today, but my salad accidentally came with a side of pizza, fries, and a Coke. Then the gym called and asked if I was coming, and I told them, “Sorry, I’m in a committed relationship with my bed right now.” Honestly, if laziness was an Olympic sport, I’d still come in second—because I’d be too lazy to show up for the finals. "
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)

