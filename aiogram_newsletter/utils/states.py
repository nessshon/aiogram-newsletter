from aiogram.fsm.state import StatesGroup, State


class ANState(StatesGroup):
    newsletters = State()
    newsletter = State()
    newsletter_delete = State()
    send_message = State()
    send_buttons = State()
    message_preview = State()
    choose_options = State()
    confirmation_now = State()
    send_datetime = State()
    confirmation_later = State()
