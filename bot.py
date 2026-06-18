from aiogram import Bot, Dispatcher, executor, types
import requests

bot = Bot(token='8779493234:AAGBv1c0_uT8exSlHg4jk5fM-0N63LKHdIY')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'data'])
async def send_data(message: types.Message):
    url = 'https://script.google.com/macros/s/AKfycbzJLxISsWEyBfyhglvh08xGN3emkZrUVA5mcldnVs_C_kSzc1DdQUQ7n47jeCWoCj4CoQ/exec'
    data = requests.get(url).json()
    latest_data = data[-5:] # နောက်ဆုံး ၅ ခု
    msg = "📊 ၂D ရလဒ်များ:\n\n"
    for item in latest_data:
        msg += f"🗓 {item['date']} | ⏰ {item['time']}\n🔢 2D: *{item['2d']}*\n\n"
    await message.answer(msg, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp)
