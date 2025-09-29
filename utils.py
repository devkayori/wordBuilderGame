import random
import json
import requests
from basicword import BasicWord

WORDS_URL = 'https://www.jsonkeeper.com/b/JNSGY'


def load_words_from_file():
    """
    Загрузка данных из JSON с сайта jsonkeeper
    возвращает json строку
    """
    response = requests.get(WORDS_URL)
    return response.text


def serialize_json(url_text):
    """
    Сериализация json в python-объекты
    возвращает словарь из json-строки
    """
    url_json = json.loads(url_text)
    return url_json


def load_random_word():
    """
    Генерация рандомного слова на основе сериализованных данных
    возвращает объект класса BasicWord
    """
    random_list_words = random.choice(serialize_json(load_words_from_file()))
    random_word = random_list_words['word']
    random_subword = random_list_words['subwords']

    random_original_word = BasicWord(random_word, random_subword)

    return random_original_word
