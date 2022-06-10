




from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton


tel = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Telefon raqam yuborish",callback_data='uz'), 
        ],
    ],

)


joy = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Joylashuvingizni  yuboring",request_location=True), #request_contact=True,location=True
        ],
    ],
    resize_keyboard=True
)

