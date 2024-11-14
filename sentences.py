import random

# 1. Function to get determiner
def get_determiner(number):
    singular_determiners = ['the', 'a', 'one']
    plural_determiners = ['the', 'some', 'many']
    
    if number == 'singular':
        return random.choice(singular_determiners)
    else:
        return random.choice(plural_determiners)

# 2. Function to get noun
def get_noun(number):
    singular_nouns = ['cat', 'dog', 'bird']
    plural_nouns = ['cats', 'dogs', 'birds']
    
    if number == 'singular':
        return random.choice(singular_nouns)
    else:
        return random.choice(plural_nouns)

# 3. Function to get verb
def get_verb(tense, number):
    past_verbs = {'singular': ['ran', 'slept', 'ate'], 'plural': ['ran', 'slept', 'ate']}
    present_verbs = {'singular': ['runs', 'sleeps', 'eats'], 'plural': ['run', 'sleep', 'eat']}
    future_verbs = {'singular': ['will run', 'will sleep', 'will eat'], 'plural': ['will run', 'will sleep', 'will eat']}
    
    if tense == 'past':
        return random.choice(past_verbs[number])
    elif tense == 'present':
        return random.choice(present_verbs[number])
    else:
        return random.choice(future_verbs[number])

# 4. Function to get preposition
def get_preposition():
    prepositions = ['in', 'on', 'under', 'beside', 'between']
    return random.choice(prepositions)

# 5. Function to get prepositional phrase
def get_prepositional_phrase(number):
    determiner = get_determiner(number)
    noun = get_noun(number)
    preposition = get_preposition()
    return f"{preposition} {determiner} {noun}"

# 6. Function to make a sentence
def make_sentence(tense, number):
    determiner = get_determiner(number)
    noun = get_noun(number)
    verb = get_verb(tense, number)
    prepositional_phrase = get_prepositional_phrase(number)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence

# 7. Main function that prints six sentences
def main():
    # Create six sentences for different combinations
    print(make_sentence('past', 'singular'))    # Single past
    print(make_sentence('present', 'singular')) # Single present
    print(make_sentence('future', 'singular'))  # Single future
    print(make_sentence('past', 'plural'))     # Plural past
    print(make_sentence('present', 'plural'))  # Plural present
    print(make_sentence('future', 'plural'))   # Plural future

# 8. Call the main function to execute the program
main()
