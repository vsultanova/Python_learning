import requests
import datetime
import json


def main():
    askuseroption = AskUserOption()
    askuser = AskUser()
    askuseroption.return_user_option()
    if askuseroption.answer_option == 1:
        askuser.ask_user_text()
        askuser.ask_user_city()
        news = News(askuseroption.news, askuser.answer_text_news, askuser.answer_city)
        with open("Output.txt", "a") as file:
            file.write(f"{news.print_1_row()}\n")
            file.write(f"{news.print_2_row()}\n")
            file.write(f"{news.print_3_row()}\n")
            file.write(f"{news.print_4_row()}\n")
        exit()
    elif askuseroption.answer_option == 2:
        askuser.ask_user_text_ad()
        askuser.ask_user_exp_date()
        adv = Adv(askuseroption.adv, askuser.answer_text_ad, askuser.answer_exp_date)
        with open("Output.txt", "a") as file:
            file.write(f"{adv.print_1_row()}\n")
            file.write(f"{adv.print_2_row()}\n")
            file.write(f"{adv.print_3_row()}\n")
            file.write(f"{adv.print_4_row()}\n")
        exit()
    elif askuseroption.answer_option == 3:
        print("Wait for a joke...")
        joke = Joke(askuseroption.joke)
        with open("Output.txt", "a") as file:
            file.write(f"{joke.print_1_row()}\n")
            file.write(f"{joke.print_joke()[0]}\n")
            file.write(f"{joke.print_joke()[1]}\n")
            file.write(f"{joke.print_4_row()}\n")
        exit()
    else:
        exit()


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


class AskUser:
    def ask_user_text(self):
        self.answer_text_news = input("What is the news text? ")
        return self.answer_text_news

    def ask_user_text_ad(self):
        self.answer_text_ad = input("What is the ad text? ")
        return self.answer_text_ad

    def ask_user_city(self):
        self.answer_city = input("What is the news city? ")
        return self.answer_city

    def ask_user_exp_date(self):
        self.answer_exp_date = input("What is the exp date of your ad?\nPlease in format: (DD/MM/YYYY) ")
        return self.answer_exp_date


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

    def print_joke(self):
        self.setup = self.joke_json["setup"]
        self.punchline = self.joke_json["punchline"]
        print(self.setup)
        print(self.punchline)
        return self.setup, self.punchline


if __name__ == "__main__":
    main()


