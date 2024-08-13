import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import filters
from aiogram import types
from aiogram.types.inline_query_result_article import InlineQueryResultArticle

import config
import predictions


dp = Dispatcher()


@dp.message(filters.CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer('hello ' + message.from_user.full_name)


@dp.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery) -> None:
    await inline_query.answer(results=[
        InlineQueryResultArticle(
            id='1',
            title='Получить предсказание',
            description='Узнай свой будущее здесь и сейчас!',
            input_message_content=types.InputTextMessageContent(
                message_text=inline_query.from_user.first_name + ', ' + predictions.fetch_random_prediction()
            ),
        )
    ], cache_time=0)

async def main() -> None:
    bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())