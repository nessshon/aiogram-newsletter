## 🤖 aiogram Newsletter Bot

[![Telegram Bot](https://img.shields.io/badge/Bot-grey?logo=telegram)](https://core.telegram.org/bots)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License](https://img.shields.io/github/license/nessshon/aiogram-tonconnect)](https://github.com/nessshon/aiogram-tonconnect/blob/main/LICENSE)
[![Redis](https://img.shields.io/badge/Redis-Yes?logo=redis&color=white)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=docker&logoColor=white)](https://www.docker.com/)

Bot example: [@aiogramNewsletterBot](https://t.me/aiogramNewsletterBot)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nessshon/aiogram-newsletter.git
    ```

2. Change into the bot directory:

    ```bash
    cd aiogram-newsletter/example
    ```
3. Clone environment variables file:

   ```bash
   cp .env.example .env
   ```

4. Configure [environment variables](#environment-variables-reference) variables file:

   ```bash
   nano .env
   ```

5. Running a bot in a docker container:

   ```bash
   docker-compose up --build
   ```

## Environment Variables Reference

Here is a reference guide for the environment variables used in the project:

| Variable   | Description                                                   | Example           |
|------------|---------------------------------------------------------------|-------------------|
| BOT_TOKEN  | Bot token, obtained from [@BotFather](https://t.me/BotFather) | 1234567890:QWERTY | 
| REDIS_HOST | The hostname or IP address of the Redis server                | redis             |
| REDIS_PORT | The port number on which the Redis server is running          | 6379              |
| REDIS_DB   | The Redis database number                                     | 0                 |
