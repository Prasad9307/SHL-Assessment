from flask import Flask, request, jsonify
from utils import transcribe_audio, check_grammar, calculate_score

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    audio = request.files['audio']
    audio.save("temp.wav")

    transcript = transcribe_audio("temp.wav")
    issues = check_grammar(transcript)
    score = calculate_score(transcript, issues)

    return jsonify({
        "transcript": transcript,
        "score": round(score, 2),
        "suggestions": [m.message for m in issues]
    })

if __name__ == '__main__':
    app.run(debug=True)
