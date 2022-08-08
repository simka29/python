from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import telebot

token = '5462091681:AAGuBryakGTbju9ykouXuVtmPB2JoQYhTPA'
bot = telebot.TeleBot(token)
chat_id = '543612371'
path='test_bot'

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        text = 'В папке появился новый файл:\n' + event.src_path
        bot.send_message(chat_id, text) 

observer = Observer()
observer.schedule(Handler(), path, recursive=True)
observer.start()

bot.polling(non_stop=True)
