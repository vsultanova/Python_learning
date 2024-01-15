"""
homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

test_string = """homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

print("The initial test text:\n", test_string)

test_string_split = test_string.split(".")

capitalized_list = []

for elem in range(len(test_string_split)):
    capitalized_list.append(test_string_split[elem].strip().capitalize())

capitalized_final_sentence = ".\n".join(capitalized_list)
print("\nFinal capitalized string:\n", capitalized_final_sentence)

separate_sentence = ''
part_sentence = ''
new_sentence = []
final_sentence = ''

for elem2 in range(len(capitalized_list)):
    separate_sentence = capitalized_list[elem2].split(" ")  # string
    part_sentence = separate_sentence[-1:]  # string
    new_sentence = new_sentence + part_sentence  # list

final_sentence = " ".join(new_sentence).capitalize()
print("\nFinal new string:\n", final_sentence)

two_sentences_together = capitalized_final_sentence + final_sentence
print("\nTwo together (final and new sentences):\n", two_sentences_together)

print("\nReplaced:\n", two_sentences_together.replace(" iz ", ' is '))

for x in test_string:
    whitespaces_count = test_string.count(" ")
print("\nWhite spaces count for initial text:", whitespaces_count)

for x in capitalized_final_sentence:
    whitespaces_count = capitalized_final_sentence.count(" ")
print("\nWhite spaces count for final capitalized text:", whitespaces_count)

for x in two_sentences_together:
    whitespaces_count = two_sentences_together.count(" ")
print("\nWhite spaces count for two together:", whitespaces_count)












