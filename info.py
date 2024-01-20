import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6401144686:AAE-KxQ4yURExdb00gK2haQuRJYs1ClAhwY')

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я могу провести небольшой опрос. Для начала, напиши /test.")

@bot.message_handler(commands=['test'])
def handle_start(message):
    global user_data
    user_id = message.from_user.id

    user_data[user_id] = {"total_score": 0, "current_question": 0}

    ask_question(message.chat.id, user_id)

def ask_question(chat_id, user_id):
    global user_data
    current_question = user_data[user_id]["current_question"]
    question_data = survey[current_question]

    bot.send_message(chat_id, question_data["question"])

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for answer, score in question_data["answers"].items():
        markup.add(KeyboardButton(answer))

    bot.send_message(chat_id, "Выбери вариант ответа:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    global user_data
    user_id = message.from_user.id

    if user_data[user_id]["current_question"] >= len(survey):
        bot.send_message(message.chat.id, "Опрос завершен. Результат: " + get_result(user_data[user_id]["total_score"]))
        return

    current_question = survey[user_data[user_id]["current_question"]]
    answers = current_question["answers"]

    if message.text in answers:
        user_data[user_id]["total_score"] += answers[message.text]
        user_data[user_id]["current_question"] += 1
        ask_question(message.chat.id, user_id)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выбери вариант ответа из предложенных.")

def get_result(total_score):
    if 7 <= total_score <= 9:
        return "Рудольф"
    elif 5 <= total_score <= 6:
        return "Оленёнок"
    elif 3 <= total_score <= 4:
        return "Лентяй"
    else:
        return "Недействительный счет"

survey = [
    {
        "question": "У тебя есть рога?",
        "answers": {
            "Да! Конечно!": 3,
            "Нет, но скоро вырастут!": 2,
            "Я не смотрел": 1
        }
    },
    {
        "question": "Ты много бегаешь?",
        "answers": {
            "Да! Конечно!": 3,
            "Бегаю, пока не устану": 2,
            "Неет": 1
        }
    },
    {
        "question": "Ты знаком с Санта Клаусом?",
        "answers": {
            "Знаком лично": 3,
            "Наслышан о нем": 2,
            "А кто это?": 1
        }
    }
]

bot.polling()
