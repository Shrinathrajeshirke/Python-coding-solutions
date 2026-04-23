# Create a functional pipeline:

# Take a list of text reviews
# Clean reviews (remove extra spaces, lowercase)
# Filter reviews with more than 3 words
# Map to find sentiment:

# Positive if contains: "good","great","excellent","amazing"
# Negative if contains: "bad","terrible","awful","poor"
# Neutral otherwise


# Count each sentiment using reduce
# # Print summary

reviews = [
    "Great product highly recommended",
    "Bad quality terrible experience",
    "Ok",
    "Amazing value for money excellent",
    "Poor quality bad packaging",
    "Good",
    "Excellent service great experience"
]

positives = ["good","great","excellent","amazing"]
negatives = ["bad","terrible","awful","poor"]

from functools import reduce

def review_analyzer(reviews):
    reviews = list(map(lambda sent:  sent.strip().lower(), reviews))
    reviews = list(filter(lambda sent: len(sent.split())>3, reviews))
    reviews = list(map(lambda sent: (sent, "Positive" if any(word in sent.split() for word in positives)
                                     else "Negative" if any(word in sent.split() for word in negatives) 
                                     else "Neutral"), reviews ))
    
    positive_sentiment_count = reduce(lambda x,y: x+ (1 if y[1]=='Positive' else 0), reviews,0)
    negative_sentiment_count = reduce(lambda x,y: x+ (1 if y[1]=='Negative' else 0), reviews,0)
    neutral_sentiment_count = reduce(lambda x,y: x+ (1 if y[1]=='Neutral' else 0), reviews,0)

    print("Output: ")
    print(f"Valid reviews: {len(reviews)}")
    print("Sentiments: ")
    for sent, sentiment in reviews:
        print(f"{sent} -> {sentiment}")
    print("Summary: ")
    print(f"Positive: {positive_sentiment_count}")
    print(f"Negative: {negative_sentiment_count}")
    print(f"Neutral: {neutral_sentiment_count}")

review_analyzer(reviews)
