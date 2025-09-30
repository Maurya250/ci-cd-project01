import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "From the moment I met you, my world has never been the same. Every thought, every heartbeat, every silent wish seems to revolve around you. Your smile has a magic that can light up the darkest corners of my soul, and your voice lingers in my ears like a melody I never want to end. I find myself lost in your eyes, in the depth of emotions they hold, and in the warmth that your presence brings to my life. Even in your absence, I feel you around me—in the breeze that brushes my face, in the quiet whispers of the night, and in the small moments that remind me of you. Loving you is not just a feeling; it has become my way of living, the rhythm that keeps me moving forward, and the reason I believe in dreams and hope. Every memory of us feels like a treasure, every smile you give me is a universe in itself, and every promise between us is a bridge that connects my heart to yours, no matter the distance. Life without you feels incomplete, and yet every second apart makes me realize that my heart has found its home in you. You are not just someone I love—you are my story, my forever, my solace, and the most beautiful part of every day I wake up to. And I promise, in ways words can barely capture, that my heart will keep cherishing you, every moment, in every possible way, for all the lifetimes that might exist."
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)

