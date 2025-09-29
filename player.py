class Player:
    def __init__(self, player_name, player_answers):
        self.player_name = player_name
        self.player_answers = player_answers

    def __repr__(self):
        return (f"Имя пользователя: {self.player_name}\n"
                f"Использованные слова пользователя {self.player_answers}")

    def count_player_answers(self):
        """
        Вывод количества слов в списке ответов игрока
        возвращает int
        """
        return len(self.player_answers)

    def append_player_answer(self, player_answer):
        """
        Добавление нового слова в список отвеченных слов игрока
        ничего не возвращает
        """
        self.player_answers.append(player_answer.lower())

    def check_using_player_answers(self, current_player_answers):
        """
        Проверка вхождения слова игрока в список уже отвеченных слов игроком
        возвращает bool
        """
        if current_player_answers.lower() in self.player_answers:
            return True
        else:
            return False
