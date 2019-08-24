import os

from bll import GameCoreControllerl


class GameConsoleView:
    def __init__(self):
        self.__consoleview=GameCoreControllerl()
    def start(self):
        self.__consoleview.generate_new_number()
        self.__consoleview.generate_new_number()
        self.__draw_map()
    def main(self):

        pass
    def __draw_map(self):
        os.system('clear')
        for line in self.__consoleview.map:
            for item in line:
                print(item)
            print()
    def __updata(self):







