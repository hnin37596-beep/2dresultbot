import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import requests

# သင်၏ Token နှင့် URL
API_TOKEN = '8779493234:AAGBv1c0_uT8exSlHg4jk5fM-0N63LKHdIY'
GOOGLE_SHEET_URL = 'https://script.google.com/macros/s/AKfycbzJLxISsWEyBfyhglvh08xGN3emkZrUVA5mcldnVs_C_kSzc1DdQUQ7n47jeCWoCj4CoQ/exec'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("data"))
async def send_data(message: Message):
    try:
        response = requests.get(GOOGLE_SHEET_URL)
        data = response.json()
        latest_data = data[-5:]
        msg = "📊 နောက်ဆုံးရ ၂D ရလဒ်များ:\n\n"
        for item in latest_data:
            msg += f"🗓 {item['date']} | ⏰ {item['time']}\n🔢 2D: *{item['2d']}*\n\n"
        await message.answer(msg, parse_mode="Markdown")
    except Exception as e:
        await message.answer(f"Error: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
