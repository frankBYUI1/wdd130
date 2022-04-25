'''
Full Name: Francesco Lezano
Teacher: Bro. Codling
Title: 06 Prove Assignment / Troubleshooting Functions

Problem Statement: The Turing test, named after Alan Turing, is a test of a computer's 
ability to make conversation that is indistinguishable from human conversation. 
A computer that could pass the Turing test would need to understand sentences typed 
by a human and respond with sentences that make sense.

In English, a preposition is a word used to express spatial or temporal relations, 
such as "in", "over", and "before". A prepositional phrase is group of words that 
begins with a preposition and includes a noun. For example:

- above the water
- in the kitchen
- after the meeting
'''

import random

def main():
    # Print six sentences 
    # {determiner} {noun} {verb}
    # single - past, present, future
    # plural - past, present, future
    get_verb(1, "past") 
    get_verb(2, "present")
    get_verb(3, "future")
    get_verb(4, "past")
    get_verb(5, "present")
    get_verb(6, "future")


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present':
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                    "runs", "sleeps", "talks", "walks", "writes"]
        elif quantity != 1:
            words = ["drink", "eat", "grow", "laugh", "think",
                    "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_adverb():
    """Return a randomly chosen preposition
    from this list of adjectives:
        "slowly", "rapidly", "clumsily", "badly", 
        "diligently", "sweetly", "warmly", "sadly", "ruthlessly", 
        "urgently", "worriedly", "beautifully"

    Return: a randomly chosen adverb    
    """
    words = ["slowly", "rapidly", "clumsily", "badly", "diligently",
        "sweetly", "warmly", "sadly", "ruthlessly", "urgently", 
        "worriedly", "beautifully"]

    # Randomly choose and return a adverb.
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_adjective():
    """Return a randomly chosen preposition
    from this list of adjectives:
        "charming", "cruel", "fantastic", "gentle", 
        "huge", "perfect", "rough", "sharp"

    Return: a randomly chosen adjectives.
    """
    words = ["charming", "cruel", "fantastic", "gentle", "huge",
        "perfect", "rough", "sharp", "adventurous", "alive", "arrogant",
        "awful", "adorable", "bored", "cheerful"]
    
    # Randomly choose and return a adjective.
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or plural.
    Return: a prepositional phrase.
    """
    return get_preposition() + ' ' + get_determiner(quantity) + ' ' + get_noun(quantity) 

# This will run the order of the sentences. 
sentence1 = ''
sentence1 += get_determiner(1)
sentence1 += ' '
sentence1 += get_adjective()
sentence1 += ' '
sentence1 += get_noun(1)
sentence1 += ' '
sentence1 += get_verb(1, 'past')
sentence1 += ' '
sentence1 += get_adverb()
sentence1 += ' '
sentence1 += get_prepositional_phrase(1)
print(sentence1)

# This will run the order of the sentences. 
sentence2 = ''
sentence2 += get_determiner(1)
sentence2 += ' '
sentence2 += get_adjective()
sentence2 += ' '
sentence2 += get_noun(1)
sentence2 += ' '
sentence2 += get_verb(1, 'present')
sentence2 += ' '
sentence2 += get_adverb()
sentence2 += ' '
sentence2 += get_prepositional_phrase(1)
print(sentence2)

# This will run the order of the sentences. 
sentence3 = ''
sentence3 += get_determiner(1)
sentence3 += ' '
sentence3 += get_adjective()
sentence3 += ' '
sentence3 += get_noun(1)
sentence3 += ' '
sentence3 += get_verb(1, 'future')
sentence3 += ' '
sentence3 += get_adverb()
sentence3 += ' '
sentence3 += get_prepositional_phrase(1)
print(sentence3)

# This will run the order of the sentences. 
sentence4 = ''
sentence4 += get_determiner(2)
sentence4 += ' '
sentence4 += get_adjective()
sentence4 += ' '
sentence4 += get_noun(2)
sentence4 += ' '
sentence4 += get_verb(2, 'past')
sentence4 += ' '
sentence4 += get_adverb()
sentence4 += ' '
sentence4 += get_prepositional_phrase(2)
print(sentence4)

# This will run the order of the sentences. 
sentence5 = ''
sentence5 += get_determiner(2)
sentence5 += ' '
sentence5 += get_adjective()
sentence5 += ' '
sentence5 += get_noun(2)
sentence5 += ' '
sentence5 += get_verb(2, 'present')
sentence5 += ' '
sentence5 += get_adverb()
sentence5 += ' '
sentence5 += get_prepositional_phrase(2)
print(sentence5)

# This will run the order of the sentences. 
sentence6 = ''
sentence6 += get_determiner(2)
sentence6 += ' '
sentence6 += get_adjective()
sentence6 += ' '
sentence6 += get_noun(2)
sentence6 += ' '
sentence6 += get_verb(2, 'future')
sentence6 += ' '
sentence6 += get_adverb()
sentence6 += ' '
sentence6 += get_prepositional_phrase(2)
print(sentence6)


