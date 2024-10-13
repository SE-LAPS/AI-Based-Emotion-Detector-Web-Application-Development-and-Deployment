from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Endpoint for detecting emotions from a given text input.
    
    Returns:
        JSON response with the detected emotions or an error message for blank input.
    """
    text = request.json.get('text', '')

    if not text.strip():  # Check for blank input
        return jsonify({
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400

    result = emotion_detector(text)

    if result['dominant_emotion'] is None:  # Handle case when dominant emotion is None
        return jsonify({'message': 'Invalid text! Please try again!'}), 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
