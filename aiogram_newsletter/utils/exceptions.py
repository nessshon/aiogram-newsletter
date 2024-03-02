class AiogramNewsletterException(Exception):
    ...


# List of error messages related to editing messages
MESSAGE_EDIT_ERRORS = [
    "no text in the message",
    "message can't be edited",
    "message is not modified",
    "message to edit not found",
]

# List of error messages related to deleting messages
MESSAGE_DELETE_ERRORS = [
    "message can't be deleted",
    "message to delete not found",
]
