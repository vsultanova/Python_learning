"""
homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

test_string1 = """homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


print("The initial test text:\n" + test_string1)


def capitalization(test_string):
    test_string_split = test_string.split(".")
    capitalized_list = []
    for elem in range(len(test_string_split)):
        capitalized_list.append(test_string_split[elem].strip().capitalize())
    capitalized_sentence = ".\n".join(capitalized_list)
    return capitalized_sentence


capitalized_text = capitalization(test_string1)
print("\nThe capitalized text:\n" + capitalized_text)


def last_words_from_text(test_string):
    test_string_split = test_string.split(".")
    combined_last_words = []
    for elem in range(len(test_string_split)):
        separate_sentence = test_string_split[elem].split(" ")  # string
        last_word = separate_sentence[-1:]  # string
        combined_last_words = combined_last_words + last_word  # list
    combined_last_words_capitalized = " ".join(combined_last_words).capitalize()
    return combined_last_words_capitalized


sentence_with_last_words = last_words_from_text(test_string1)
print("\nThe sentence made of last words:\n" + sentence_with_last_words)


def initial_and_last_words_sentences():
    two_sentences_together = capitalized_text + sentence_with_last_words
    return two_sentences_together


whole_text = initial_and_last_words_sentences()
print("\nTwo together (initial and combined sentences):\n", whole_text)


def correct_misspelling():
    return whole_text.replace(" iz ", ' is ')


corrected_test = correct_misspelling()
print("\nCorrected whole text:\n", corrected_test)


def whitespaces_counter():
    whitespaces_count = 0
    for x in corrected_test:
        whitespaces_count = corrected_test.count(" ")
    return whitespaces_count


general_count_whitespaces = whitespaces_counter()
print("\nWhite spaces count for the whole text:", general_count_whitespaces)














