import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use.


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

"""
Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own?
--------------------------------------------------------------------------------------------------------------------------------
I find it interesting the fact that cats, monkeys, and bananas are different in terms of their physical characteristics, behavior, and 
biology, they can still be compared and have similarities from a linguistic perspective using tools such as Spacy. Spacy, a natural 
language processing library, can analyze and understand the relationships between words and identify similarities in their usage and meaning. For example, 
it could determine that all three of these words are nouns and have a relation to the concepts of animals and food, 
respectively. It's fascinating to see how technology can uncover patterns and connections in 
language that can bring together seemingly disparate objects.
"""

nlp = spacy.load('en_core_web_sm') # specifying the model we want to use.

tokens = nlp('man women mortality pencil ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""
Difference between "en_core_web_sm" and "en_core_web_md"?
-----------------------------------------------------------
The "en_core_web_sm" has no word vectors loaded, so the result of the Token.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 
"en_core_web_sm", which don't ship with word vectors and only use context-sensitive tensors. 
"en_core_web_md" is a medium model with more information and capabilities, while "en_core_web_sm" is a smaller, lighter-weight model.
"""