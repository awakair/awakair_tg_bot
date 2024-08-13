from os import getenv
from datetime import timedelta

bot_username='awakair_bot'
log_file='awakair_bot.log'
file_url = 'https://disk.yandex.ru/i/v80oVS14VcY8YA'
update_interval = timedelta(minutes=10)

bot_token = getenv('BOT_TOKEN')
