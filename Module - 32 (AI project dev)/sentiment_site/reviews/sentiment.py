from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text:str) -> tuple[str,float]:
    score = analyzer.polarity_scores(text)
    compound_score = score['compound']
    
    if compound_score >= 0.05:
        sentiment_level = 'positive'
    elif compound_score <= -0.05:
        sentiment_level = 'negative'
    else:
        sentiment_level = 'neutral'
        
    return sentiment_level, compound_score
    