from flask import Flask, render_template, request, jsonify
from vercel import Vercel

app = Flask(__name__)

@app.route('/')
def home():
    artworks = [
        {"name": "Alariko", "artist": "Grand Basin", "year": 2025, "image": "IMG_3515.JPG"},
        {"name": "Christ on the mount of Olives", "artist": "Matthias Stom", "year": 1630, "image": "IMG_3517.JPG"},
        {"name": "A Calm at Mediterranean Port", "artist": "Claude-Joseph Vernet", "year": 1770, "image": "IMG_3521.JPG"},
        {"name": "The Flower Seller", "artist": "Diego Rivera", "year": 1886, "image": "IMG_3523.JPG"},
        {"name": "Potrait of Rita de Acosta Lydig", "artist": "Giovanni Boldini", "year": 2025, "image": "IMG_3525.JPG"},
        {"name": "A Celestial Sorceress illuminated by Moonlight", "artist": "Ricardo Falero", "year": 2024, "image": "IMG_3528.JPG"},
        {"name": "Silence", "artist": "Lucien Levy Dhurmer", "year": 1895, "image": "IMG_3532.JPG"},
        {"name": "An Experiment on a Bird in the Air Pump", "artist": "Joseph Wright of Derby", "year": 1768, "image": "IMG_3534.JPG"},
        {"name": "Anubis with Yuji", "artist": "Joanna Karpowicz", "year": 2023, "image": "IMG_3536.JPG"},
        {"name": "Saint Matthew and the Angel", "artist": "Caravaggio", "year": 1602, "image": "IMG_3538.JPG"},
        # Add more artworks here
    ]
    return render_template('Ody.html', artworks=artworks)

@app.route('/admire', methods=['POST'])
def admire():
    data = request.json
    artwork_name = data.get('artwork_name')
    return jsonify({"status": "success", "message": f"You admired {artwork_name}!"})

@app.route('/dislike', methods=['POST'])
def dislike():
    data = request.json
    artwork_name = data.get('artwork_name')
    return jsonify({"status": "success", "message": f"You disliked {artwork_name}!"})

# Vercel serverless handler
vercel_handler = Vercel(app)

if __name__ == '__main__':
    app.run(debug=True)