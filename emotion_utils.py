import nltk

nltk.download('punkt')
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()

def detect_emotion(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] >= 0.5:
        return "joy"
    elif scores['compound'] <= -0.5:
        return "sadness"
    elif scores['neu'] > 0.8:
        return "neutral"
    else:
        return "mixed"
