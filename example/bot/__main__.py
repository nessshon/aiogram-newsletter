import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram_newsletter.handlers import AiogramNewsletterHandlers
from aiogram_newsletter.middleware import AiogramNewsletterMiddleware

from .handlers import router
from .throttling import ThrottlingMiddleware

BOT_TOKEN = os.getenv("BOT_TOKEN", "1234567890:QWERTY")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = os.getenv("REDIS_DB", 0)


async def main():
    job_store = RedisJobStore(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
    )
    apscheduler = AsyncIOScheduler(
        jobstores={'default': job_store},
    )
    storage = RedisStorage.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}")
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(storage=storage)

    dp.update.middleware.register(ThrottlingMiddleware())
    dp.update.middleware.register(AiogramNewsletterMiddleware(apscheduler))

    dp.include_router(router)
    AiogramNewsletterHandlers().register(dp)

    apscheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
