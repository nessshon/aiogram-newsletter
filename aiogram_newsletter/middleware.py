import asyncio
from typing import Callable, Dict, Any, Awaitable, Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from .manager import ANManager
from .utils.keyboards import InlineKeyboard
from .utils.texts import TextMessage


class AiogramNewsletterMiddleware(BaseMiddleware):

    def __init__(
            self,
            apscheduler: AsyncIOScheduler,
            text_message: Optional[TextMessage] = None,
            inline_keyboard: Optional[InlineKeyboard] = None,
    ) -> None:
        self.apscheduler = apscheduler
        self.text_message = text_message
        self.inline_keyboard = inline_keyboard

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user: User = data.get("event_from_user")

        text_message = self.text_message or TextMessage(user.language_code)
        inline_keyboard = self.inline_keyboard or InlineKeyboard(user.language_code)

        an_manager = ANManager(
            apscheduler=self.apscheduler,
            text_message=text_message,
            inline_keyboard=inline_keyboard,
            data=data,
        )

        data["an_manager"] = an_manager
        loop = asyncio.get_running_loop()
        loop.__setattr__("bot", event.bot)

        return await handler(event, data)
