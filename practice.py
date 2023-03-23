import spacy

# Using the spaCy library to load the English language model and then it is using the similarity
# function to calculate the similarity between the words.
# 
# Using the spaCy library to load the English language model and then it is using the similarity
# function to calculate the similarity between the words.
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Creating a list of tokens from the sentence.
tokens = nlp('cat apple monkey banana ')

# Comparing the similarity of each word in the sentence to every other word in the sentence.
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
        
        
print("\n\n")        
        

# Creating a sentence that we can compare other sentences to.
sentence_to_compare = "Why is my cat on the car"

# Creating a list of sentences that we can compare to the model sentence.
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# Creating a model sentence that we can compare other sentences to.
model_sentence = nlp(sentence_to_compare)
# Comparing the similarity of the sentence to the model sentence.
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
    
# answers from the task requirements 
'''
So, I was just thinking about how crazy it is that a cat, a monkey,
and a banana have anything in common. I mean, one is a furry little creature,
one swings around in trees, and one is a sweet, delicious fruit. But get this,
when we look at them through the eyes of a fancy machine learning tool like spaCy,
it turns out that cats and monkeys actually have more in common with each other than either of them does with a banana.
Maybe it's because they're both animals with fur, unlike a slippery banana.

Now, let's take a trip down the road and think about cars, trains, and bicycles.
They're all ways to get around, but they have different speeds, sizes, and efficiencies.
A car and a train might be more similar to each other than to a bicycle because they're both
big vehicles that run on tracks or roads. But a car and a bicycle might be more similar in terms of personal transportation and speed.
I wonder how spaCy would score the similarities between these words?

'''   

# example diffrences 
'''
The 'en_core_web_sm' model is a smaller language model in comparison to the 'en_core_web_md'.
As such, it possesses fewer features and capabilities than its larger counterpart.
A notable disparity between the two is that the 'en_core_web_sm' model proves less accurate in its predictions than
the 'en_core_web_md'. Consequently, it may not be as precise when detecting similarities or dissimilarities between 
complaints and recipes. Additionally, the 'en_core_web_sm' model's vocabulary is smaller, meaning it may not recognize all
words present in a text. Thus, the model may prove less effective in processing more intricate and lengthy texts. Lastly,
it's worth noting that the 'en_core_web_sm' model is faster than its larger counterpart, which may provide an advantage 
for applications that prioritize speed over accuracy.

'''