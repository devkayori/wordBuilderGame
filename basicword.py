class BasicWord:

    def __init__(self, original_word, set_subwords):
        self.original_word = original_word
        self.set_subwords = set_subwords

    def __repr__(self):
        return (f"Исходное слово: {self.original_word}\n"
                f"Набор допустимых подслов {self.set_subwords}")

    def check_entered_word_in_set_subwords(self, player_answers):
        """
        Проверка вхождения пользователем слова в изначальный список подслов
        возвращает bool
        """
        if player_answers.lower() in self.set_subwords:
            return True
        return False

    def count_of_set_subwords(self):
        """
        Вывод количество слов в списке подслов
        возвращает int
        """
        return len(self.set_subwords)
