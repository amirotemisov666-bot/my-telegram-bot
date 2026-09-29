import os
import asyncio
import urllib.parse
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TELEGRAM_TOKEN = "8820153046:AAFcnSf1m6s..."  # Замените на твой полный токен

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Напиши мне текстовый запрос, и я сгенерирую картинку.")

@dp.message()
async def generate_image(message: types.Message):
    await message.answer("🎨 Генерирую изображение, подождите...")
    try:
        prompt_encoded = urllib.parse.quote(message.text)
        image_url = f"https://pollinations.ai/p/{prompt_encoded}"
        await message.answer_photo(photo=image_url)
    except Exception as e:
        await message.answer(f"Ошибка при генерации: {e}")

async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_website():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    # Запускаем сайт и бота в одном цикле событий
    await start_website()
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
        
