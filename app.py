from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['user_input']
    score = analyzer.polarity_scores(user_input)
    compound = score['compound']

    if compound >= 0.05:
        mood = 'positive'
    elif compound <= -0.05:
        mood = 'negative'
    else:
        mood = 'neutral'

    return render_template('result.html', mood=mood, text=user_input)

if __name__ == '__main__':
    app.run(debug=True)
