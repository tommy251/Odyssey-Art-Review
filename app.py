from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    artworks = [
        {"name": "Starry Night", "artist": "Vincent Van Gogh", "year": 1889, "image": "starry_night.jpg"},
        {"name": "Mona Lisa", "artist": "Leonardo da Vinci", "year": 1503, "image": "mona_lisa.jpg"},
        # Add more artworks here
    ]
    return render_template('Ody.html', artworks=artworks)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)