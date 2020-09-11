import pandas as pd
import numpy as np


class Investor:
    def __init__(self, name, open_rub=pd.DataFrame(), closed_rub=pd.DataFrame(), open_dollars=pd.DataFrame(), closed_dollars=pd.DataFrame()):
        self.name = name
        self.open_rub= open_rub
        self.closed_rub = closed_rub
        self.open_dollars = open_dollars
        self.closed_dollars = closed_dollars
        self.current_feature = dict()
        self.df_dict = {"open_rub": self.open_rub, "closed_rub": self.closed_rub,
                        "open_dollars": self.open_dollars, "closed_dollars": self.closed_dollars}

    def match_market(self, market_name):
        if market_name == "open_rub":
            return self.open_rub
        elif market_name == "closed_rub":
            return self.closed_rub
        elif market_name == "open_dollars":
            return self.open_dollars
        elif market_name == "closed_dollars":
            return self.closed_dollars

    def input_stock(self):
        print("Введите Тикер")
        self.current_feature["Тикер"] = input()
        print("Введите название акции")
        self.current_feature["Название акции"] = input()
        print("Введите цену покупки")
        self.current_feature["Цена покупки"] = float(input())
        print("Введите дату покупки")
        self.current_feature["Дата покупки"] = input() # обернуть в datetime
        print("Введите количество купленных акций")
        self.current_feature["Количество"] = float(input())


    def add_stock(self, market_name):
        market = self.df_dict[market_name]
        self.input_stock()
        self.current_feature["Стоимость"] = self.current_feature["Количество"] * self.current_feature["Цена покупки"]
        self.current_feature["Цена закрытия"] = self.current_feature["Цена покупки"]
        self.current_feature["Результат, %"] = 100*(self.current_feature["Цена закрытия"]-self.current_feature["Цена покупки"])\
                                               /self.current_feature["Цена покупки"]
        self.current_feature["Результат, руб"] = self.current_feature["Результат, %"]*self.current_feature["Цена покупки"]*self.current_feature["Количество"]
        if market.empty:
            self.current_feature["Доля от позиции,  %"] = 100
            market = pd.DataFrame(self.current_feature, index=[0])
        else:
            self.current_feature["Доля от позиции,  %"] = np.nan
            market = pd.concat((market, pd.DataFrame(self.current_feature, index=[0])), axis=0)
        self.df_dict[market_name] = market

    def display_dataset(self, market_name):
        print(self.df_dict[market_name])

    def display_name(self):
        print(self.name)



person = Investor("Lipatov")
person.add_stock("open_rub")
person.display_dataset("open_rub")
person.display_name()

#[inv1, inv2, ...]











