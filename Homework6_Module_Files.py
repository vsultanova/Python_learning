import os
import random

import requests
import datetime
import json


def main():
    askuseroption = AskUserOption()
    askuseroption.return_user_option()
    create_news_file = CreateNewsFile()
    create_adv_file = CreateAdvFile()
    askuserfile = AskUserFile()
    filedata = FileData()
    remove_processed_file = RemoveFile()
    if askuseroption.answer_option == 1:
        create_news_file.create_news_file()
        askuserfile.ask_user_file()
        filedata.news_data(askuserfile.answer_user_file)
        news = News(askuseroption.news, filedata.user_list[0], filedata.user_list[1])
        with open("HW6_output.txt", "a") as file:
            file.write(f"{news.print_1_row()}\n")
            file.write(f"{news.print_2_row()}\n")
            file.write(f"{news.print_3_row()}\n")
            file.write(f"{news.print_4_row()}\n")
        remove_processed_file.remove_processed_file(askuserfile.answer_user_file)
        exit()
    elif askuseroption.answer_option == 2:
        create_adv_file.create_Adv_file()
        askuserfile.ask_user_file()
        filedata.news_data(askuserfile.answer_user_file)
        adv = Adv(askuseroption.adv, filedata.user_list[0], filedata.user_list[1])
        with open("HW6_output.txt", "a") as file:
            file.write(f"{adv.print_1_row()}\n")
            file.write(f"{adv.print_2_row()}\n")
            file.write(f"{adv.print_3_row()}\n")
            file.write(f"{adv.print_4_row()}\n")
        remove_processed_file.remove_processed_file(askuserfile.answer_user_file)
        exit()
    elif askuseroption.answer_option == 3:
        print("Wait for a joke...")
        joke = Joke(askuseroption.joke)
        with open("HW6_output.txt", "a") as file:
            file.write(f"{joke.print_1_row()}\n")
            file.write(f"{joke.print_joke_setup()}\n")
            file.write(f"{joke.print_joke_punchline()}\n")
            file.write(f"{joke.print_4_row()}\n")
    else:
        print("else")


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
                self.answer_option = int(input(f"\n{self.user_question_1}\n1. {self.news}, 2. {self.adv}, 3. {self.joke}\n{self.user_question_2}"))
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


class CreateNewsFile:
    def create_news_file(self):
        self.news_file = []
        with open("Text_csv.csv", "w") as file:
            self.news_file = file.write(f"tEXT{random.randrange(1,10)}, \ncITY{random.randrange(10,20)}")
        return self.news_file


class CreateAdvFile:
    def create_Adv_file(self):
        self.adv_file = []
        with open("Text_adv_csv.csv", "w") as file:
            self.adv_file = file.write(f"tEXT{random.randrange(1,10)}, \n{random.randrange(1,28)}/{random.randrange(1,12)}/{random.randrange(2024, 2028)}")
        return self.adv_file


class AskUserFile:
    def __init__(self):
        self.answer_user_file = ""

    def ask_user_file(self):
        self.answer_user_file = input("Please write a file name/path to get the data? ")
        return self.answer_user_file


class FileData:
    def news_data(self, file_name):
        self.user_list = []
        self.file_name = file_name
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.capitalize()
                self.user_list.append(line.rstrip())
        print(self.user_list)
        return self.user_list


class RemoveFile:
    def remove_processed_file(self, file_name):
        self.file_name = file_name
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            print("Removed")
        else:
            print("No file")


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


