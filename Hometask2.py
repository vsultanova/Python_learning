"""
Write a code, which will:

1. create a list of random number of dicts (from 2 to 10)
dict random numbers of keys should be a letter,
dict values should be a number (0-100),
example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
"""
import random
import string

random_dict_number = random.randrange(2, 10)
print("random_dict_number: ", random_dict_number)

original_list_with_dict = []

for i in range(random_dict_number):
    dict_with_key_value = {}
    random_dict_keys_number = random.randrange(1, 4)
    # print("for", i, "attempt random_dict_keys_number: ", random_dict_keys_number)
    for k in range(random_dict_keys_number):
        random_dict_key = random.choice(string.ascii_letters)
        random_dict_value = random.randint(0, 100)
        dict_with_key_value.update({random_dict_key: random_dict_value})
        # print(k, " : ", dict_with_key_value)
    original_list_with_dict.append(dict_with_key_value)
    # print("list with dict after", i, "attempt: ", original_list_with_dict)

print("final list with dict", original_list_with_dict)

"""
2. get previously generated list of dicts and create one common dict:

if dicts have the same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

Each line of code should be commented with description.

Commit script to git repository and provide link as home task result.
"""
combined_dict = {}
# combined_dict.update(original_list_with_dict[0])
# print("combined_dict: ", combined_dict)
#
# print("list_with_keys_for_combined: ", list_with_keys_for_combined)

for current_dict in original_list_with_dict:
    print("current dict:", current_dict)
    list_with_keys = current_dict.keys()
    print("list_with_keys from current dict: ", list_with_keys)

    list_with_keys_for_combined = combined_dict.keys()

    for current_key in list_with_keys:
        if current_key in list_with_keys_for_combined:
            print("not unique", current_key)
            if current_dict[current_key] > combined_dict[current_key]:
                combined_dict[current_key] = current_dict[current_key]
        else:
            print("unique", current_key)
            combined_dict.update({current_key: current_dict[current_key]})

print("combined dict: ", combined_dict)