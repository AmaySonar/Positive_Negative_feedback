from textblob import TextBlob

feedbacks = ['I think this is amazing','This is awful',
             'hey i really think this helped me so much',
             'Damn this is really tough','Everyone is trying to help me quit it ','i just want to get over it ',
             'ohhh i am bored now i dont want to work','this is bad and i dont like it','I love the app is amazing ',
             "The experience was bad as hell",
             "This app is really helpful",
             "Damn the app tastes like shit ",
             'Well hello darling',
             'isnt it wonderful that we meet tonight',
             'sarima and arima are time series algorithm',
             'maybe you and i meant to be together']




positive_feedbacks =[]
negative_feedbacks =[]



for feedback in feedbacks:
    feedback_polarity = TextBlob(feedback).sentiment.polarity
    if feedback_polarity >0:
        positive_feedbacks.append(feedback)
        continue
    negative_feedbacks.append(feedback)
    
    
    
    
    
print('Positive_feedbacks Count : {}'.format(len(positive_feedbacks)))
print(positive_feedbacks)

print('Negative_feedback Count : {}'.format(len(negative_feedbacks)))
print(negative_feedbacks)
    
    
    
    
    
# one observation i recorded that neutral or genral responses are recorded as the negative feedback in the application there's something can be done to 
# rectify that problem