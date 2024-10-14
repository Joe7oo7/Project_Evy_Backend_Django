# utils.py
from textblob import TextBlob
import nltk
from nltk.corpus import wordnet

# Ensure wordnet is available
nltk.download('wordnet', quiet=True)

def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        sentiment = blob.sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
        
        # Determine sentiment label based on polarity
        if polarity > 0.1:
            sentiment_label = "Positive"
        elif polarity < -0.1:
            sentiment_label = "Negative"
        else:
            # Further check for harmful content
            if "kill" in text.lower() or "murder" in text.lower():
                sentiment_label = "Harmful"
            else:
                sentiment_label = "Neutral"
        
        return polarity, subjectivity, sentiment_label, None
    except Exception as e:
        return None, None, None, str(e)
