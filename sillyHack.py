import random

articles = ['the', 'a', 'an']
nouns = ['cat', 'dog', 'banana', 'robot']
verbs = ['eats', 'runs', 'sleeps', 'jumps']
adverbs = ['quickly', 'slowly', 'eagerly', 'carefully']

sentence = random.choice(articles) + ' ' + random.choice(nouns) + ' ' + random.choice(verbs) + ' ' + random.choice(adverbs) + '.'
print(sentence)