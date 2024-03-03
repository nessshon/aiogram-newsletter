import asyncio
import pickle
import re
from datetime import datetime
from typing import Union, Any, List, Tuple

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, User
from aiogram.exceptions import TelegramRetryAfter, TelegramBadRequest

from aiogram_newsletter.utils.texts import TextMessage


async def send_message(bot: Bot, chat_id: int, message_data: dict) -> bool:
    message_obj = Message(**message_data).as_(bot)

    try:
        await message_obj.send_copy(
            chat_id=chat_id,
            reply_markup=message_obj.reply_markup,
        )

    except TelegramRetryAfter as e:
        await asyncio.sleep(e.retry_after)
        await send_message(bot, chat_id, message_data)

    except (TelegramBadRequest, Exception):
        return False

    return True


async def run_newsletter(bot: Bot, users_ids: List[int], message_data: dict) -> Tuple[int, int]:
    successful, unsuccessful = 0, 0

    for user_id in users_ids:
        is_success = await send_message(bot, user_id, message_data)

        if is_success:
            successful += 1
        else:
            unsuccessful += 1

    return successful, unsuccessful


async def run_newsletter_task(users_ids: list[int], user_data: dict, message_data: dict) -> None:
    loop = asyncio.get_running_loop()
    bot: Bot = loop.__getattribute__("bot")

    user: User = User(**user_data)
    text_message = TextMessage(user.language_code)

    text = text_message.get("newsletter_started")
    await bot.send_message(user.id, text=text)

    text = text_message.get("newsletter_ended")
    successful, unsuccessful = await run_newsletter(bot, users_ids, message_data)
    text = text.format(total=len(users_ids), successful=successful, unsuccessful=unsuccessful)
    await bot.send_message(user.id, text=text)


def validate_url(url: str) -> Union[str, None]:
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    matches = re.findall(url_pattern, url)

    return matches[0] if matches else None


def validate_datetime(datetime_string: str) -> Union[datetime, None]:
    try:
        datetime_obj = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
    except ValueError:
        return None

    return datetime_obj


class DataStorage:
    def __init__(self, state: FSMContext) -> None:
        self.state = state

    @classmethod
    def data_to_hex(cls, data: Any) -> str:
        return pickle.dumps(data).hex()

    @classmethod
    def hext_to_data(cls, hext: str) -> Any:
        return pickle.loads(bytes.fromhex(hext))

    async def set_data(self, data: Any, key: str) -> None:
        data = {key: self.data_to_hex(data)}
        await self.state.update_data(**data)

    async def get_data(self, key: str) -> Any:
        state_data = await self.state.get_data()
        return self.hext_to_data(state_data.get(key))
