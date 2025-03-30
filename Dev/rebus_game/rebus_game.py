import random


class RebusGame:
    def __init__(self):
        self.subjects = {
            "Информатика": {
                "Ребус 1": {
                    "image": "ПА3.ОТ",
                    "hint": "Это устройство компьютера",
                    "answer": "пазот"
                },
                "Ребус 2": {
                    "image": "100ЛИТКА",
                    "hint": "Единица измерения информации",
                    "answer": "столитка"
                }
            },
            "Математика": {
                "Ребус 1": {
                    "image": "ВИ3НА",
                    "hint": "Геометрическая фигура",
                    "answer": "витрина"
                },
                "Ребус 2": {
                    "image": "КО100ЧКА",
                    "hint": "Математический знак",
                    "answer": "косточка"
                }
            },
            "Русский язык": {
                "Ребус 1": {
                    "image": "ФИ1Л",
                    "hint": "Часть слова",
                    "answer": "финал"
                },
                "Ребус 2": {
                    "image": "РО1КА",
                    "hint": "Часть речи",
                    "answer": "родика"
                }
            }
        }
        self.score = 0
        self.attempts = 3

    def show_subjects(self):
        print("Доступные предметы:")
        for i, subject in enumerate(self.subjects.keys(), 1):
            print(f"{i}. {subject}")
        print("0. Выход")

    def show_rebuses(self, subject):
        print(f"\nРебусы по предмету '{subject}':")
        rebuses = self.subjects[subject]
        for i, (name, data) in enumerate(rebuses.items(), 1):
            print(f"{i}. {name}: {data['image']} ({data['hint']})")
        print("0. Назад")

    def play_rebus(self, subject, rebus_name):
        rebus = self.subjects[subject][rebus_name]
        print(f"\nРебус: {rebus['image']}")
        print(f"Подсказка: {rebus['hint']}")

        attempts_left = self.attempts
        while attempts_left > 0:
            answer = input("Ваш ответ: ").strip().lower()
            if answer == rebus['answer']:
                print("Правильно! 🎉")
                self.score += attempts_left
                return True
            else:
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"Неверно. Осталось попыток: {attempts_left}")
                else:
                    print(f"Правильный ответ: {rebus['answer']}")
                    return False

    def run(self):
        print("Добро пожаловать в игру 'Школьные ребусы'!")

        while True:
            self.show_subjects()
            choice = input("\nВыберите предмет (номер): ")

            if choice == "0":
                break

            try:
                subject = list(self.subjects.keys())[int(choice)-1]
            except (ValueError, IndexError):
                print("Некорректный выбор. Попробуйте снова.")
                continue

            while True:
                self.show_rebuses(subject)
                rebus_choice = input("\nВыберите ребус (номер) или введите 's' для случайного выбора: ")

                if rebus_choice == "0":
                    break
                elif rebus_choice.lower() == 's':
                    rebus_name = random.choice(list(self.subjects[subject].keys()))
                    self.play_rebus(subject, rebus_name)
                else:
                    try:
                        rebus_name = list(self.subjects[subject].keys())[int(rebus_choice)-1]
                        self.play_rebus(subject, rebus_name)
                    except (ValueError, IndexError):
                        print("Некорректный выбор. Попробуйте снова.")
                        continue

        print(f"\nИгра завершена. Ваш итоговый счет: {self.score}")


if __name__ == "__main__":
    game = RebusGame()
    game.run()
