import asyncio
import urllib.parse
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TELEGRAM_TOKEN = "8820153046:AAFcnSflm6sIjG-yxPJ0YFdHU3Eldz1AmJE"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Напиши мне слово на английском (например: 'elephant' или 'car'), и я пришлю картинку!")

@dp.message()
async def generate_image(message: types.Message):
    await message.answer("🎨 Генерирую картинку...")
    try:
        prompt_encoded = urllib.parse.quote(message.text)
        image_url = f"https://image.pollinations.ai/prompt/{prompt_encoded}?width=1024&height=1024&nologo=true"
        await message.answer_photo(photo=image_url)
    except Exception as e:
        await message.answer("Произошла ошибка при генерации картинки.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
