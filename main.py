from utils import load_random_word
from player import Player

word_data = load_random_word()

player_name = input("Введите имя игрока: \n")
print(f"Привет, {player_name}\n"
      f"Составьте {word_data.count_of_set_subwords()} слов из слова "
      f"{word_data.original_word}\n"
      f"Слова должны быть не короче 3 букв\n"
      f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n")

player = Player(player_name, [])

max_subwords = word_data.count_of_set_subwords()

while len(player.player_answers) < max_subwords:
    answer = input("Введите слово: ")

    if answer.lower() in ["stop", "стоп"]:
        print(f"Игра завершена, вы угадали {player.count_player_answers()}")
        break
    elif len(answer) < 3:
        print("Слишком короткое слово")
    elif player.check_using_player_answers(answer):
        print("уже использовано")
    elif not word_data.check_entered_word_in_set_subwords(answer):
        print("неверно")
    else:
        player.append_player_answer(answer)
        print("верно")
print(f"Игра завершена, вы угадали {player.count_player_answers()}")
