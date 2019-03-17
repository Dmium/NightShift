from textblob import TextBlob

def nightify(daytime):
    senti = TextBlob(daytime).sentiment
    if senti.subjectivity < 0.5:
        return daytime
    if senti.polarity > 0.4:
        return "Yeah"
    if senti.polarity < -0.4:
        return "Nah"
    return daytime
