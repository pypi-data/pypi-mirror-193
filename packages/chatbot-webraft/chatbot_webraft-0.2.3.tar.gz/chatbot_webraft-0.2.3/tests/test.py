import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# input sentence
input_sentence = input("Enter a sentence: ")

# sample sentences in lists
list1 = ["I am feeling happy today", "The weather is sunny", "I like to play tennis"]
list2 = ["Great to hear that you are feeling happy!", "Yes, it's a lovely day outside.", "That's great, tennis is a fun sport."]

# function to find the matching sentence in list2 and generate a new sentence with the same structure
def match_sentence(input_sentence, list1, list2):
    # tokenize input sentence
    tokens = word_tokenize(input_sentence)

    # check each sentence in list1 for a match
    for i, sentence in enumerate(list1):
        # tokenize sentence in list1
        sentence_tokens = word_tokenize(sentence)

        # find matching words between input sentence and sentence in list1
        matches = set(tokens).intersection(sentence_tokens)

        # if there is a match, generate a new sentence with the same structure as the corresponding sentence in list2
        if len(matches) > 0:
            # tokenize corresponding sentence in list2
            output_tokens = word_tokenize(list2[i])

            # create a dictionary to store the word mappings between the input sentence and corresponding sentence in list2
            word_map = {}
            for j in range(len(sentence_tokens)):
                if sentence_tokens[j] in matches:
                    # if word is a match, map it to corresponding word in output sentence
                    word_map[sentence_tokens[j]] = output_tokens[j]

            # generate new sentence with same structure as corresponding sentence in list2
            new_sentence = []
            for token in sentence_tokens:
                if token in word_map:
                    new_sentence.append(word_map[token])
                else:
                    new_sentence.append(token)

            return " ".join(new_sentence)

    # if no match is found, return None
    return None

# find matching sentence and generate new sentence with same structure
new_sentence = match_sentence(input_sentence, list1, list2)

# print output
if new_sentence is not None:
    print("Match found! Generated sentence: ", new_sentence)
else:
    print("No match found.")
