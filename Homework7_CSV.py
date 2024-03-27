import csv
import os


def main():
    write_word_to_csv(word_count()[0])
    write_letter_to_csv((word_count()[1]), (word_count()[2]), word_count()[3])


def word_count():
    my_file = open("HW6_output.txt")
    # my_file = open("Test_data/Random_text.txt")
    my_dict_word = dict()
    my_dict_letter = dict()
    all_letter_count = 0
    upper_letter_count = 0

    for line in my_file:
        line = line.rstrip()
        words = line.split()
        for word in words:
            if word.isalnum():
                # word_count = word_count + 1
                my_dict_word[word.lower()] = my_dict_word.get(word.lower(), 0) + 1
                for letter in word:
                    if letter.isalpha():
                        all_letter_count = all_letter_count + 1
                        if letter.isupper():
                            upper_letter_count = upper_letter_count + 1
                        my_dict_letter[letter] = my_dict_letter.get(letter, 0) + 1
    all_count = [my_dict_word, my_dict_letter, all_letter_count, upper_letter_count]
    # print("my_dict_word", all_count[0])
    # print("my_dict_letter", all_count[1])
    # print("all_letter_count", all_count[2])
    # print("upper_letter_count", all_count[3])
    return all_count


def write_word_to_csv(text):
    file_name = "Word_count.csv"
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print(f"{file_name} does not exist, new file was created")
        pass
    csv_file = open(file_name, "w", newline='')
    headers = ["Word",  "Count"]
    writer = csv.DictWriter(csv_file, fieldnames=headers, delimiter="-")
    writer.writeheader()
    for k in text:
        writer.writerow({"Word": k, "Count": text[k]})


def write_letter_to_csv(letter, all, upper):
    file_name = "Letter_count.csv"
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print(f"{file_name} does not exist, new file was created")
        pass
    csv_file = open("Letter_count.csv", "w", newline='')
    headers = ["Letter", "All letter count", "Upper letter count", "Percentage"]
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for k in letter:
        writer.writerow({"Letter": k})
    writer.writerow({"All letter count": all, "Upper letter count": upper, "Percentage": round(upper*100/all, 2)})


if __name__ == "__main__":
    main()


