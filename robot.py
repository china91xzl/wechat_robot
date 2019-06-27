from wxpy import *
bot = Bot()
tuling = Tuling(api_key='71c1ae31512544a99e49e86013971be1')
# my_friend = ensure_one(bot.friends().search(""))


@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)


bot.join()



