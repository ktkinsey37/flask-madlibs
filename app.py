from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hi'
debug = DebugToolbarExtension(app)

@app.route('/hello')
def get_words():
    return render_template('hello.html', prompts=story.prompts, template=story.template)

@app.route('/story')
def create_story():
    prompt_and_word_dict = {}
    for prompt in story.prompts:
        word = request.args.get(f"{prompt}")
        prompt_and_word_dict[f"{prompt}"] = f"{word}"
    return render_template('story.html', output_story=story.generate(prompt_and_word_dict))