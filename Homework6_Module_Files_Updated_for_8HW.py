import os
import random
import re

import requests
import datetime
import json
import Homework7_CSV


def main():
    # Ask user option to receive 1, 2 or 3
    askuseroption = AskUserOption()
    askuseroption.return_user_option()

    # Autogenerating News or Adv file to parse data from
    create_news_file = CreateNewsFile()
    create_adv_file = CreateAdvFile()
    create_news_json_file = CreateNewsJSONFile()
    create_adv_json_file = CreateAdvJSONFile()

    # Ask user the path to the file with data to parse
    askuserfile = AskUserFile()

    # Process lines from user file to create a LIST with necessary data (.txt and .csv formats)
    filedata = FileData()

    # Autoremoving the file with test data to parse
    remove_processed_file = RemoveFile()

    # Test data file paths
    # auto_news_file = "Text.csv"
    # auto_news_file = "Text.txt"
    # auto_news_file = "Text.json"
    # auto_adv_file = "Text_adv.csv"
    # auto_adv_file = "Text_adv.txt"
    # auto_adv_file = "Text_adv.json"
    file_with_output = "HW8_output.txt"

    if askuseroption.answer_option == 1:
        # Autogenerate a test file with random data in order not to create unique data for test purposes
        # create_news_file.create_news_file(auto_news_file)
        # create_news_json_file.create_news_json_file(auto_news_file)

        # Ask user file - it can also be a real file with a real path
        askuserfile.ask_user_file()

        # Process lines from user file to create a LIST with necessary data (.txt, .csv or .json formats)
        filedata.news_data(askuserfile.answer_user_file, askuseroption.answer_option)

        # Create News with parsed data from the file
        news = News(askuseroption.news, filedata.user_list[0], filedata.user_list[1])

        # Print all rows for News
        with open(file_with_output, "a") as file:
            file.write(f"{news.print_1_row()}\n")
            file.write(f"{news.print_2_row()}\n")
            file.write(f"{news.print_3_row()}\n")
            file.write(f"{news.print_4_row()}\n")

        # Remove autogenerated file if it was autogenerated
        # if askuserfile.answer_user_file == auto_news_file:
        #     remove_processed_file.remove_processed_file(auto_news_file)

        # Write a count of words from output file to a new CSV file
        Homework7_CSV.write_word_to_csv(Homework7_CSV.word_count()[0])

        # Write a count of letters from output file to a new CSV file
        Homework7_CSV.write_letter_to_csv(Homework7_CSV.word_count()[1], Homework7_CSV.word_count()[2],
                                          Homework7_CSV.word_count()[3])
        exit()
    elif askuseroption.answer_option == 2:
        # Autogenerate a test file with random data in order not to create unique data for test purposes
        # create_adv_file.create_adv_file(auto_adv_file)
        # create_adv_json_file.create_adv_json_file(auto_adv_file)

        # Ask user file - it can also be a real file with a real path
        askuserfile.ask_user_file()

        # Process lines from user file to create a LIST with necessary data (.txt, .csv or .json formats)
        filedata.news_data(askuserfile.answer_user_file, askuseroption.answer_option)

        # Create Adv with parsed data from the file
        adv = Adv(askuseroption.adv, filedata.user_list[0], filedata.user_list[1])

        # Print all rows for Adv
        with open(file_with_output, "a") as file:
            file.write(f"{adv.print_1_row()}\n")
            file.write(f"{adv.print_2_row()}\n")
            file.write(f"{adv.print_3_row()}\n")
            file.write(f"{adv.print_4_row()}\n")

        # Remove autogenerated file if it was autogenerated
        # if askuserfile.answer_user_file == auto_adv_file:
        #     remove_processed_file.remove_processed_file(auto_adv_file)

        # Write a count of words from output file to a new CSV file
        Homework7_CSV.write_word_to_csv(Homework7_CSV.word_count()[0])

        # Write a count of letters from output file to a new CSV file
        Homework7_CSV.write_letter_to_csv(Homework7_CSV.word_count()[1], Homework7_CSV.word_count()[2],
                                          Homework7_CSV.word_count()[3])
        exit()
    elif askuseroption.answer_option == 3:
        print("Wait for a joke...")

        # Create Joke with parsed data from the file
        joke = Joke(askuseroption.joke)

        # Print all rows for Joke
        with open(file_with_output, "a") as file:
            file.write(f"{joke.print_1_row()}\n")
            file.write(f"{joke.print_joke_setup()}\n")
            file.write(f"{joke.print_joke_punchline()}\n")
            file.write(f"{joke.print_4_row()}\n")

        # Write a count of words from output file to a new CSV file
        Homework7_CSV.write_word_to_csv(Homework7_CSV.word_count()[0])

        # Write a count of letters from output file to a new CSV file
        Homework7_CSV.write_letter_to_csv(Homework7_CSV.word_count()[1], Homework7_CSV.word_count()[2],
                                          Homework7_CSV.word_count()[3])
    else:
        print("else")


# Ask user for option 1, 2 or 3 with validation of data type and count of attempts
# Max count of attempts is 3
class AskUserOption:
    def __init__(self):
        self.news = "News"
        self.adv = "Adv"
        self.joke = "Joke"
        self.user_question_1 = "What would you like to post?"
        self.user_question_2 = "Select a number: "
        self.not_integer = "You entered not integer value."
        self.out_of_range = "The value is out of the range."
        self.try_another_time = "Please try another time."
        self.user_option_text = "You selected: "
        self.i = 0
        self.limit = 3

    def __ask_user_option(self):
        while self.i < self.limit:
            self.i = self.i + 1
            try:
                self.answer_option = int(input(
                    f"\n{self.user_question_1}\n1. {self.news}, 2. {self.adv}, 3. {self.joke}\n{self.user_question_2}"))
            except ValueError:
                if self.i < self.limit:
                    print(f"\n{self.not_integer}")
                    print(f"You used {self.i} of {self.limit} attempts.")
                if self.i >= self.limit:
                    print(f"You used {self.i} of {self.limit} attempts.")
                    print(f"\n{self.try_another_time}")
                    exit()
            else:
                if (self.answer_option > 3 or self.answer_option <= 0) and self.i < self.limit:
                    print(f"\n{self.out_of_range}")
                    print(f"\nYou used {self.i} of {self.limit} attempts.")
                elif (self.answer_option > 3 or self.answer_option <= 0) and self.i >= self.limit:
                    print(f"\nYou used {self.i} of {self.limit} attempts.")
                    print(f"\n{self.try_another_time}")
                    exit()
                else:
                    print(self.user_option_text, self.answer_option)
                    return self.answer_option

    def return_user_option(self):
        return self.__ask_user_option()


# Autogenerate file with random data (News text and City) to parse News text for test purposes
class CreateNewsFile:
    def create_news_file(self, auto_news_file):
        self.news_file = []
        if os.path.exists(auto_news_file):
            os.remove(auto_news_file)
        else:
            with open(auto_news_file, "w") as file:
                self.news_file = file.write(f"tEXT{random.randrange(1, 10)}, \ncITY{random.randrange(10, 20)}")
                return self.news_file


# Autogenerate file with random data (Adv text and Exp date) to parse Adv text for test purposes
class CreateAdvFile:
    def create_adv_file(self, auto_adv_file):
        self.adv_file = []
        if os.path.exists(auto_adv_file):
            os.remove(auto_adv_file)
        else:
            with open(auto_adv_file, "w") as file:
                self.adv_file = file.write(
                    f"tEXT{random.randrange(1, 10)}, \n{random.randrange(1, 28)}/{random.randrange(1, 12)}/{random.randrange(2024, 2028)}")
                return self.adv_file


# Autogenerate file with random data for News text and News city
# to parse News data for test purposes
class CreateNewsJSONFile:
    def create_news_json_file(self, auto_news_json_file):
        self.news_json_file = {
            "News_text": f"My old news{random.randrange(1, 10)}",
            "News_city": f"My city{random.randrange(10, 20)}"
        }
        print("Test: json dict", self.news_json_file)
        json.dump(self.news_json_file, open(auto_news_json_file, "w"))
        return self.news_json_file


# Autogenerate file with random data for Adv text and Exp date
# to parse Adv data for test purposes
class CreateAdvJSONFile:
    def create_adv_json_file(self, auto_adv_json_file):
        self.adv_json_file = {
            "Adv_text": f"My adv text{random.randrange(30, 40)}",
            "Adv_date": f"{random.randrange(1, 28)}/{random.randrange(1, 12)}/{random.randrange(2024, 2028)}"
        }
        print("Test: json dict", self.adv_json_file)
        json.dump(self.adv_json_file, open(auto_adv_json_file, "w"))
        return self.adv_json_file


# Ask user for a real path to the real file to parse real data from
class AskUserFile:
    def __init__(self):
        self.answer_user_file = ""

    def ask_user_file(self):
        self.answer_user_file = input(
            "Please write a file name/path to get the data from? (in .txt, .csv or .json formats) ")
        return self.answer_user_file


# Process lines from user file to create a list with necessary data (.txt, .csv and .json formats)
class FileData:
    def news_data(self, file_name, user_option):
        self.user_list = []
        self.file_name = file_name
        try:
            if re.search("^.+\.txt$", self.file_name) or re.search("^.+\.csv$", self.file_name):
                # print("Test: Match txt/csv:", self.file_name)
                with open(self.file_name, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        line = line.capitalize()
                        self.user_list.append(line.rstrip())
                # print("Test: list processed from txt or csv:", self.user_list)
                return self.user_list
            elif re.search("^.+.json$", self.file_name) and user_option == 1:
                # print("Test: Match News json:", self.file_name)
                json_file = json.load(open(file_name))
                self.user_list.append(json_file["News_text"])
                self.user_list.append(json_file["News_city"])
                # print("Test: list processed from JSON:", self.user_list)
                return self.user_list
            elif re.search("^.+.json$", self.file_name) and user_option == 2:
                # print("Test: Match Adv json:", self.file_name)
                json_file = json.load(open(file_name))
                self.user_list.append(json_file["Adv_text"])
                self.user_list.append(json_file["Adv_date"])
                # print("Test: list processed from JSON:", self.user_list)
                return self.user_list
            else:
                print("File is in not allowed format")
                quit()
        except FileNotFoundError:
            print("File is not found, sorry")
            quit()


# Remove autogenerated file
class RemoveFile:
    def remove_processed_file(self, file_name):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            # print("Removed")
        else:
            print("No file")


# Print 1 and 4 rows for all types of publications
class Publication:
    def __init__(self, name):
        self.name = name

    def print_1_row(self):
        name_length = len(str(self.name))
        str_length = 30 - name_length
        self.row1 = f"\n{self.name} {str_length * '-'}"
        print(self.row1)
        return self.row1

    def print_4_row(self):
        self.dash = "-"
        self.row4 = f"{self.dash}" * 30
        print(self.row4)
        return self.row4


# Print 2 and 3 rows for News
# Calculation of the current date and time for the news (the 3d row)
class News(Publication):
    def __init__(self, name, text, city):
        super().__init__(name)
        self.text = text
        self.city = city

    def print_2_row(self):
        print(self.text)
        return self.text

    def print_3_row(self):
        self.row3 = f"{self.city}, {datetime.datetime.now().strftime('%d/%m/%Y %H.%M')}"
        print(f"{self.city}, {datetime.datetime.now().strftime('%d/%m/%Y %H.%M')}")
        return self.row3


# Print 2 and 3 rows for Adv
# Calculation of the left days for the adv (the 3d row)
class Adv(Publication):
    def __init__(self, name, text_ad, exp_date):
        super().__init__(name)
        self.text_ad = text_ad
        self.exp_date = exp_date

    def __days_left(self):
        new_list = list(self.exp_date.split("/"))
        new_list = datetime.datetime(int(new_list[2]), int(new_list[1]), int(new_list[0])).date()
        days_left = new_list - datetime.datetime.now().date()
        self.only_days = list(str(days_left).split(","))
        return self.only_days[0]

    def print_2_row(self):
        print(self.text_ad)
        return self.text_ad

    def print_3_row(self):
        self.row3 = f"Actual until: {self.exp_date}, {self.__days_left()} left"
        print(self.row3)
        return self.row3


# Calling to external API service to get random joke and print it
class Joke(Publication):
    def __init__(self, name):
        super().__init__(name)
        self.joke_json = self.__call_joke()

    def __call_joke(self):
        api_url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(api_url)
        self.joke_json = json.loads(response.text)
        return self.joke_json

    def print_joke_setup(self):
        self.setup = self.joke_json["setup"]
        print(self.setup)
        return self.setup

    def print_joke_punchline(self):
        self.punchline = self.joke_json["punchline"]
        print(self.punchline)
        return self.punchline


if __name__ == "__main__":
    main()
