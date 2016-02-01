"""
Name: Anirudh K M
Indiana Univeristy
Date: 30th Jan, 2016
Objective: To build a rule based classifier, to classify
           if a given tweet sentiment is positive or negative.
"""
import re
from string import punctuation


def generate_number():
    """
    This generator helps to 
    generate numbers
    """
    
    num = 1
    while 1:
        yield num
        num += 1
        
def get_dict_words(file_name):
    """
    This function loads the file given and
    cleans by removing special character and
    returns a list of words from each line.
    """

    with open(file_name) as f:
        data = f.read()
        # read data from the file
        data = data.replace('_', ' ')
        # replace the underscore with spaces
        return data.split('\n')
        
def get_tweet_list(input_file):
    """
    This function helps to get the tweets in the
    input file as a list and returns them
    """
    
    with open(input_file) as f:
        return re.findall('@[^@]*', f.read())
        # get all the tweets in a list and return 
        
def clean_tweet(tweet):
    """
    This function helps to clean
    the input tweet by removing \n and
    special characters to facilitate comparison
    and returns it
    """
    
    tweet = tweet.replace('\n', ' ')
    # replace the new line characters
    tweet = tweet[tweet.index(' ') + 1:]
    # remove the name from the tweet
    for char in punctuation:
        # iterate over each punctuation
        tweet = tweet.replace(char, ' ')
        # replace special characters with space
    return tweet 
    
def classify_tweets_two(cleaned_tweet_str, pos_key_list, neg_key_list,
                        num_generator):
    """
    This function takes the cleaned tweet 
    as an input and allocates points to it, 
    inorder for classification
    """
    
    if not cleaned_tweet_str:
        return 0
    points_int = 0
    # initial points
    word_list = cleaned_tweet_str.split()
    # split the tweet based on white spaces
    for word in word_list:
        if word.lower() in pos_key_list:
            points_int += 1
        elif word.lower() in neg_key_list:
            points_int -= 1
        else:
            pass
    if points_int > 0: 
        sentiment = 'Positive'
    elif points_int < 0:
        sentiment = 'Negative'
    elif points_int == 0:
        sentiment = 'Neutral'
    
    f.write('{},{},{},{}\n'.format(num_generator.next(), cleaned_tweet_str,
                                    points_int, sentiment))
    # write the output to a file

def classify_tweets_one(input_file, pos_key_list, neg_key_list, num_generator):
    """
    Classify the given tweets as positive and negative
    """
    
    tweets_list = get_tweet_list(input_file)
    # function call
    for tweet in tweets_list:
        tweet = clean_tweet(tweet)
        # function call
        classify_tweets_two(tweet, pos_key_list, neg_key_list, num_generator)
        # function call
        
def main():
    """
    This is the main function of the program starts.
    """

    pos_key_list = get_dict_words('pos.wn')
    # get the positive key word lists
    neg_key_list = get_dict_words('neg.wn')
    # get the negative key word lists
    num_generator = generate_number()
    # generator call
    classify_tweets_one('negTweets.txt', pos_key_list, neg_key_list, num_generator)
    # function call    
    classify_tweets_one('posTweets.txt', pos_key_list, neg_key_list, num_generator)
    # function call

if __name__ == "__main__":
    # start of the program
    f = open('tweets_emotions.csv', 'a')
    # open new file
    f.write('S.No,Tweet,Points,Sentiment\n')
    main()
    # main function call
    f.close()
    # close the opened file