from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('Ody.html')
@app.route('/')
def home():
    artworks = [
        {"name": "Starry Night", "artist": "Vincent Van Gogh", "year": 1889, "image": "starry_night.jpg"},
        {"name": "Mona Lisa", "artist": "Leonardo da Vinci", "year": 1503, "image": "mona_lisa.jpg"},
        # Add more artworks here
    ]
    return render_template('index.html', artworks=artworks)