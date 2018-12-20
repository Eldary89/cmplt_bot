from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

updater = Updater(token="743371278:AAGEctcfLtZQn8g_D__I4ka-32zF8716wH4")

dispatcher = updater.dispatcher

pr = [0 for i in range(31)]
num = 0


def echo(bot, update):
    if pr[int(update.message.text)] == "completed":
        update.message.reply_text("Already completed")
    elif pr[int(update.message.text)] > 0:
        update.message.reply_text("This one is not free")
    else:
        pr[int(update.message.text)] = update.message.chat['id']
        update.message.reply_text(update.message.text + " become in progress")


def check(bot, update):
    text = ""
    for i in range(1, 31):
        if pr[i] == 0:
            text = text + str(i) + ":is free\n"
        elif pr[i] == "complete":
            text = text + str(i) + ":is completed\n"
        else:
            text = text + str(i) + ":in progress\n"
    update.message.reply_text(text)


def cmplt(bot, update):
    pr[int(update.message.text[6:])] = "complete"
    update.message.reply_text("Ok," + update.message.text[6:] + " is completed")


dispatcher.add_handler(MessageHandler(Filters.text, echo))
dispatcher.add_handler(CommandHandler("view", check))
dispatcher.add_handler(CommandHandler("done", cmplt))
updater.start_polling()
updater.idle()