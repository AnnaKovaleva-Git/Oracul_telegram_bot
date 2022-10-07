#библиотеки, которые загружаем из вне
import telebot
from telebot import types
from random import randint

TOKEN = '5728427224:AAHTPvwL_TrBoa0W5XqAQk3zN7-53YiI3m4'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("❤️ Дела сердечные")
	item2 = types.KeyboardButton("Что ждет меня в будущем?")
	item3 = types.KeyboardButton("Фото создателя 😍")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Привет тебе от доброго волшебника (или не очень 😈), {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	predictions1 = ['Счастье придет, когда ты будешь готов его встретить', 'Тебя ожидает приятное известие от дорогого твоему сердцу человека','Твое сердце готово к новой любви – только открой его','Не исключено, что рядом с тем, кто тебе дорог, появится интригант','Кто-то, находящийся совсем рядом с тобой, хотел бы, чтобы ваши отношения стали прочнее','В сердечных делах тебе поможет твоя знакомая','Тебя ждет легкий, ни к чему не обязывающий и очень приятный флирт','Счастье в том, чтобы сосредоточиться на семье','Неужели ты не видишь, что счастье – прямо у тебя перед глазами?', 'Наступило время экспериментов, новизны и остроты ощущений', 'Даже если вам что-то не нравится, любовь и время все исправят']
	predictions2 = ['Уже вскоре ты получишь важное известие', 'В ситуации замешан хорошо известный тебе мужчина','Осторожнее относись к людям, поскольку не исключен обман','Кто-то из близких способен подставить тебе подножку в ответственный момент','Твои ожидания не напрасны','Ты движешься в верном направлении','Похоже, твоя жизнь наполнится тревогами и беспокойствами','То, что выйдет в результате, принесет тебе разочарование','Двигайся лишь вперед, поскольку ты поступаешь верно', 'Цель, к которой ты стремишься, вполне реальна']
	photo = open('photo_2022.webp', 'rb')

	if message.chat.type == 'private':
		if message.text == '❤️ Дела сердечные':
			bot.send_message(message.chat.id, predictions1[randint(0, len(predictions1)-1)])
		elif message.text == 'Что ждет меня в будущем?':
			bot.send_message(message.chat.id, predictions2[randint(0, len(predictions2)-1)])
		elif message.text == 'Фото создателя 😍':
			sti = open('photo_2022.webp', 'rb')
			bot.send_photo(message.chat.id, sti)
		else:
			bot.send_message(message.chat.id, 'Я не понимаю твой язык!')


bot.polling(none_stop=True)