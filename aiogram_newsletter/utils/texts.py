from dataclasses import dataclass


@dataclass
class TextMessage:
    text_messages = {
        "en": {
            "outdated_text": (
                "..."
            ),
            "newsletters": (
                "Newsletter menu\n\n"
                "<b>Add</b> - add/launch a scheduled newsletter\n\n"
                "List of scheduled newsletters:"
            ),
            "newsletter": (
                "The message above is an example of a scheduled message.\n\n"
                "<b>Delete</b> - delete the scheduled message\n\n"
                "Choose an action:"
            ),
            "newsletter_delete": (
                "Confirm the deletion of the scheduled message?"
            ),
            "send_message": (
                "Please send or forward your message:"
            ),
            "send_buttons": (
                "Please provide buttons for pinning the message.\n"
                "If you do not wish to pin, press skip.\n\n"
                "Send button text and link(s) in the format:\n"
                "<code>Button text | link</code>\n"
                "Example:\n"
                "<code>Text | https://example.com</code>\n\n"
                "To add multiple buttons in a row, separate links with commas.\n"
                "Example:\n"
                "<code>First Text | https://example.com, Second Text | https://example.com</code>\n\n"
                "To add multiple buttons in a column, write new links on new lines.\n"
                "Example:\n"
                "<code>First Text | https://example.com\nSecond Text | https://example.com</code>"
            ),
            "send_buttons_error": (
                "There was an error processing the provided button information. "
                "Please ensure that each button is formatted correctly:\n"
                "<code>Button text | link</code>\n"
                "Example:\n"
                "<code>Text | https://example.com</code>\n\n"
                "If you encounter issues, check for typos, missing links, or incorrect formatting."
            ),
            "message_preview": (
                "The message above is an example of a scheduled message.\n\n"
                "<b>Next</b> - continue customization\n\n"
                "Choose an action:"
            ),
            "choose_options": (
                "Choose an action:\n\n"
                "<b>Now</b> - launch the newsletter\n"
                "<b>Later</b> - postpone the newsletter\n"
            ),
            "confirmation_now": (
                "Are you sure you want to confirm and run the newsletter?"
            ),
            "send_datetime": (
                "Send the date and time for the newsletter launch in the format:\n"
                "<code>YYYY-MM-DD HH:MM</code>\n"
                "Example:\n"
                "<code>2031-11-01 12:00</code>"
            ),
            "send_datetime_error": (
                "There was an error processing the provided date and time. "
                "Please ensure that the format is correct:\n"
                "<code>YYYY-MM-DD HH:MM</code>\n"
                "Example:\n"
                "<code>2031-11-01 12:00</code>"
            ),
            "confirmation_later": (
                "Are you sure you want to confirm and postpone the newsletter?"
            ),
            "newsletter_started": (
                "The newsletter has been started. Please wait for the completion notification."
            ),
            "newsletter_ended": (
                "The newsletter has been successfully completed for a total of {total} users.\n\n"
                "Successful: {successful} | Unsuccessful: {unsuccessful}"
            ),
        },
        "ru": {
            "outdated_text": (
                "..."
            ),
            "newsletters": (
                "Меню рассылки\n\n"
                "<b>Добавить</b> - добавить/запустить отложенную рассылку\n\n"
                "Список отложенных рассылок:"
            ),
            "newsletter": (
                "Сообщение выше - пример отложенного сообщения.\n\n"
                "<b>Удалить</b> - удалить отложенное сообщение\n\n"
                "Выберите действие:"
            ),
            "newsletter_delete": (
                "Подтвердить удаление отложенного сообщения?"
            ),
            "send_message": (
                "Пожалуйста, отправьте или перешлите ваше сообщение:"
            ),
            "send_buttons": (
                "Пожалуйста, предоставьте кнопки для закрепления к сообщению.\n"
                "Если вы не хотите закреплять, нажмите пропустить.\n\n"
                "Отправьте текст кнопок и ссылок в формате:\n"
                "<code>Текст кнопки | ссылка</code>\n"
                "Пример:\n"
                "<code>Текст | https://example.com</code>\n\n"
                "Чтобы добавить несколько кнопок в один ряд, разделите ссылки запятыми.\n"
                "Пример:\n"
                "<code>Первый текст | https://example.com, Второй текст | https://example.com</code>\n\n"
                "Чтобы добавить несколько кнопок в колонку, напишите новые ссылки на новых строках.\n"
                "Пример:\n"
                "<code>Первый текст | https://example.com\nВторой текст | https://example.com</code>"
            ),
            "send_buttons_error": (
                "Произошла ошибка при обработке предоставленной информации о кнопках. "
                "Пожалуйста, убедитесь, что каждая кнопка отформатирована правильно:\n"
                "<code>Текст кнопки | ссылка</code>\n"
                "Пример:\n"
                "<code>Текст | https://example.com</code>\n\n"
                "Если возникли проблемы, проверьте наличие опечаток, отсутствие ссылок или неверное форматирование."
            ),
            "message_preview": (
                "Сообщение выше - пример отложенного сообщения.\n\n"
                "<b>Далее</b> - продолжить настройку\n\n"
                "Выберите действие:"
            ),
            "choose_options": (
                "Выберите действие:\n\n"
                "<b>Сейчас</b> - запустить рассылку\n"
                "<b>Позже</b> - отложить рассылку\n"
            ),
            "confirmation_now": (
                "Вы уверены, что хотите подтвердить и запустить рассылку?"
            ),
            "send_datetime": (
                "Отправьте дату и время для запуска рассылки в формате:\n"
                "<code>YYYY-MM-DD HH:MM</code>\n"
                "Пример:\n"
                "<code>2031-11-01 12:00</code>"
            ),
            "send_datetime_error": (
                "Произошла ошибка при обработке предоставленной даты и времени. "
                "Пожалуйста, убедитесь, что формат правильный:\n"
                "<code>YYYY-MM-DD HH:MM</code>\n"
                "Пример:\n"
                "<code>2031-11-01 12:00</code>"
            ),
            "confirmation_later": (
                "Вы уверены, что хотите подтвердить и отложить рассылку?"
            ),
            "newsletter_started": (
                "Рассылка запущена. Пожалуйста, дождитесь уведомления о завершении."
            ),
            "newsletter_ended": (
                "Рассылка успешно завершена для общего числа пользователей: {total}.\n\n"
                "Успешные: {successful} | Неуспешные: {unsuccessful}"
            ),
        }
    }

    def __init__(self, language_code: str) -> None:
        self.language_code = language_code if language_code in self.text_messages else "en"

    def get(self, code: str) -> str:
        return self.text_messages[self.language_code][code]
