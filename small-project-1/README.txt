This script is a simple rule based classifier wriiten using python. 

1. The input tweets come from the files negTweets.txt and posTweets.txt.

2. The dictionary of positive and negative emotions come neg.wn and pos.wn.

3. Each tweet is taken and cleaned by removed new lines and punctuations.

4. Then the words in the tweet are compared with the dictionary of positive and negative words.

5. A point is added when there is a match in positive dictionary and reduced if in negative dictionary.

6. Finally if the points is less than zero means it is assigned as a negative tweet and if more than one means positive tweet and neutral if zero.

7. Finally, the output are written to a file called tweets_emotions.csv.


Note: 

The same classifier will be built with more complex algorithms like SVM and neural networks in the coming weeks.

