
import logging
from db import Sql 
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
API_TOKEN = '5352746650:AAE_Yz63-nw3pnL7qm2rD5HcmwEqlLQRe-o'
Admin = 918664325
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Sql()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    db.baza_create()
    global user_id
    user_id = message.chat.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    data1 = db.id_user(user_id)
    print(data1)
    if data1 is None:
        db.user_add(user_id,username,first_name)
        await message.reply("Assalomu alaykum!\nTelefon raqamingizni yuboring..",reply_markup=tel)
    else:
        await message.answer("Siz ro'yxatdan o'tgansiz")




@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    raqam = message.contact['phone_number']
    db.contact_update(user_id,raqam)
    await message.reply("Joylashuvingizni yuboring...",reply_markup=joy)


@dp.message_handler(content_types=['location'])
async def contact(message: types.Message):
    kor1 = message.location.latitude
    print(kor1)
    kor2 = message.location.longitude
    print(kor2)
    db.location_update(user_id,kor1,kor2)
    z = db.admin_send(user_id)
    await message.reply("Siz ro'yxatdan o'tdingiz")
    await bot.send_message(Admin,f"✅ Ro'yxatga o'tgan foydalanuvchi\nid: {z[0]}\nusername: @{z[1]}")
    await bot.send_location(Admin,latitude={z[5]},longitude={z[4]})
    # await bot.send_location(user_id,latitude=float({z[4]}),longitude=float({z[5]}))
    # print(type(z[4]))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


