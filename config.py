import os
import json


class config():
    def __init__(self):

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #Добавлена базовая дериктория

        self.data = {} #массив для Json данных

        while True: #Цикл для открытия файла, если файла нет то он создастся и заново откроется
            try:
                with open('config.json', 'r') as json_file:
                    # Если есть файл открываем его, записываем в переменную и останавливаем цикл
                    self.data = json.load(json_file)
                    break
            except FileNotFoundError:
                # На случай если файла нет, то мы создаем снова и заново его открываем
                with open('config.json', 'w') as json_file:
                    json_file.write('''{"TOKEN": "TOKEN1223","ROOT_ADMIN_ID": 1234567890,"ADMINS_ID": [1234567890,1234567890]}''')


