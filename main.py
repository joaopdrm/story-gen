from flask import Flask, request, jsonify, render_template
from app.model import StoryGenerator
from app.utils import validate_keywords
from huggingface_hub import login
login(token='your hugginface token')

app = Flask(__name__)
story_generator = StoryGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    keywords = request.json.get('keywords')
    if not keywords or not validate_keywords:
        return jsonify({'error': 'Invalid input. Please provide 10 keywords.'}), 400
    
    story = story_generator.generate_story(keywords)
    return jsonify({'story': story})

if __name__ == "__main__":
    app.run(debug=True)