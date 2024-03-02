from aiogram import Router, F, Bot
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, User
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_newsletter.manager import ANManager

router = Router()
router.message.filter(F.chat.type == ChatType.PRIVATE)
router.callback_query.filter(F.message.chat.type == ChatType.PRIVATE)


async def main_menu(bot: Bot, event_from_user: User, **_) -> None:
    text = "This bot is an example of how to use aiogram-newsletter."
    builder = InlineKeyboardBuilder()
    builder.button(text="Try the newsletter menu", callback_data="newsletter_menu")
    await bot.send_message(event_from_user.id, text, reply_markup=builder.as_markup())


@router.message(Command("start"))
async def start_command(message: Message) -> None:
    await main_menu(message.bot, message.from_user)


@router.callback_query(F.data == "newsletter_menu")
async def open_newsletter_menu(call: CallbackQuery, an_manager: ANManager) -> None:
    users_ids = [call.from_user.id, 123456789, 987654321]
    await an_manager.newsletter_menu(users_ids, return_callback=main_menu)
    await call.message.delete()
