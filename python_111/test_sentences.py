'''
Full Name: Francesco Lezano
Teacher: Bro. Codling
Title: 06 Prove Assignment / Troubleshooting Functions
'''

from sentences import get_determiner, get_noun, get_verb, get_adverb, get_preposition, get_adjective, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
   # 1. Test the function get_determiner(single).

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test the function get_noun.
    single_determiners = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)
        assert word in single_determiners
    
    plural_determiners = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):

        quantity =  random.randint(2, 11)

        word = get_noun(quantity)

        assert word in plural_determiners

def test_get_verb():
    # Test the function get_verb.
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(1, 'past')
        assert word in past_verbs



    present_verb_singular = ["drinks", "eats", "grows", "laughs", "thinks",
                    "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        word = get_verb(1, 'present')
        assert word in present_verb_singular

    

    present_verb_plural = ["drink", "eat", "grow", "laugh", "think",
                    "run", "sleep", "talk", "walk", "write"]
    
    for _ in range(4):
        word = get_verb(2, 'present')
        assert word in present_verb_plural

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        word = get_verb(1, 'future')
        assert word in future_verbs

def test_get_adverb():
    # Test the function get_adverb.
    adverb = ["slowly", "rapidly", "clumsily", "badly", "diligently",
        "sweetly", "warmly", "sadly", "ruthlessly", "urgently", 
        "worriedly", "beautifully"]
    
    for _ in range (4):
        word = get_adverb()
        assert word in adverb

def test_get_preposition():
    # Test the function get_preposition.
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in preposition

def test_get_adjective():
    # Test the function get_adjective.
    adjective = ["charming", "cruel", "fantastic", "gentle", "huge",
        "perfect", "rough", "sharp", "adventurous", "alive", "arrogant",
        "awful", "adorable", "bored", "cheerful"]
    
    for _ in range(4):
        word = get_adjective()
        assert word in adjective

def test_get_prepositional_phrase():
    # Test the function get_preposition_phrase.
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    determiner_singular = ["a", "one", "the"]
    
    determiner_plural = ["two", "some", "many", "the"]

    noun_singular = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]
    
    noun_plural = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        sentence = get_prepositional_phrase(1)
        # 'about the dog' simple sentence.
        sentence = sentence.split(' ')
        # ['about', 'the', 'dog'] example of a split sentence.
        
        assert sentence[0] in preposition
        assert sentence[1] in determiner_singular
        assert sentence[2] in noun_singular

    for _ in range(4):
        sentence = get_prepositional_phrase(2)
        sentence = sentence.split(' ')
        
        assert sentence[0] in preposition
        assert sentence[1] in determiner_plural
        assert sentence[2] in noun_plural

pytest.main(["-v", "--tb=line", "-rN", __file__])

