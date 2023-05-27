import telebot
import mysql.connector

bot = telebot.TeleBot("5869928689:AAE7mj2ndceNda_O_eWWfxX0rX0xUpdM0Xo")

db = mysql.connector.connect(
   host="172.18.0.2",
   user="root",
   passwd="p@ssw0rd1",
   database="finance", 
   port="3306"
)
print("fdfdf FFFKDK")

cursor=db.cursor()

user_data = {}

class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ''
        self.age=''

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Введите имя")
    bot.register_next_step_handler(msg, process_firstname_step)

def process_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, process_firstage_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка')
def process_firstage_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = bot.send_message(message.chat.id, "Введите количество лет")
        
        bot.register_next_step_handler(msg, process_lastname_step)
    except Exception as e:
        
        bot.reply_to(message, 'Ошибка')

def process_lastname_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text
        user.age=message.text
        sql = "INSERT INTO users (age, first_name, last_name, user_id) VALUES (%s,%s, %s, %s)"
        val = (user.age, user.first_name, user.last_name, user_id)
        cursor.execute(sql, val)
        db.commit()

        bot.send_message(message.chat.id, "Вы успешно зарегистрированны!")
    except Exception as e:
        bot.reply_to(message, 'Ошибка, или Вы уже зарегистрированы!')

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
