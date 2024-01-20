import telebot
from telebot import types, ReplyKeyboardMarkup, KeyboardButton, Message

# Замените 'YOUR_TOKEN' на реальный токен вашего бота
bot = telebot.TeleBot('токен')

@bot.message_handler()
def save_age(message):
    # Проверяем, что возраст - число
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, пришли свой возраст цифрами.")
    else:
        # Получаем `user_id` пользователя
        user_id = message.from_user.id

        # Запоминаем присланный возраст в локальную переменную `age`
        age = int(message.text)
        # Сохраняем возраст пользователя в словарь по `user_id`
        user_data[user_id] = age
        bot.send_message(message.chat.id, "Отлично, я запомнил! Теперь можешь использовать команду /test")



survey = [
    {
        ["question"]: "У тебя есть рога?",
        ["answers"] : {
            "Да! Конечно!": 3,
            "Нет, но скоро вырастут!": 2,
            "Я не смотрел": 1
        }
    },
    {
        ["question"]: "Ты много бегаешь?",
        ["answers"]: {
            "Да! Конечно!": 3,
            "Бегаю, пока не устану": 2,
            "Неет": 1
        }
    },
    {
        ["question"]: "Ты знаком с Санта Клаусом?",
        ["answers"]: {
            "Знаком лично": 3,
            "Наслышан о нем": 2,
            "А кто это?": 1
        }
    }
]

# Заводим счётчик
total_score = 0

# Проходимся по вопросам по порядку
for question in survey:
    # Выводим текст вопроса
    @bot.message_handler(commands=['test'])
    def handle_start(message):
        bot.send_message(message.chat.id, (question["question"])

    # Выводим варианты ответов
        @bot.message_handler()
        def save_age(message):
        bot.send_message(message.chat.id,(f"- {answer}")

    # Получаем ответ пользователя
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(answers["answers"])))

        # Добавляем баллы за ответ пользователя
    total_score += question["answers"][user_answer]

# Выводим количество баллов в конце анкеты
print(f"Всего {total_score} баллов")

# Выводим категорию, в которую попал пользователь
if 7 <= total_score <= 9:
    print("Рудольф")
elif 5 <= total_score <= 6:
    print("Оленёнок")
elif 3 <= total_score <= 4:
    print("Лентяй")
else:
    print("Недействительный счет")

bot.polling()