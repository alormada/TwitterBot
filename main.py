from InternetSpeedTwitterBot import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.speed_too_low():
    bot.tweet_at_provider()