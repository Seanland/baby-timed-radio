from flask import Flask, render_template, send_from_directory, jsonify
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('/music', filename)

@app.route('/playlist/<int:minutes>')
def playlist(minutes):
    directory = '/music'
    files = os.listdir(directory)
    files = [f for f in files if f.endswith('.mp3') or f.endswith('.wav')]
    # Shuffle the list of files
    random.shuffle(files)
    # Assume each file is approximately 3 minutes long
    num_files = minutes // 3
    return jsonify(files[:num_files])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)