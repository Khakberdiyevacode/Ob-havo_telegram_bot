from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
obshi = ReplyKeyboardMarkup()
btn = KeyboardButton(text='Toshkent',callback_data='ташкент')
btn2 = KeyboardButton(text='Samarqand',callback_data='самарканд')
btn3 = KeyboardButton(text='Buxoro',callback_data='бухара')
btn4 = KeyboardButton(text='Navoiy',callback_data='навои')
btn5 = KeyboardButton(text='Andijon',callback_data='андижан')
btn6 = KeyboardButton(text='Surxondaryo',callback_data='термез')
btn7 = KeyboardButton(text='Qashqadaryo',callback_data='карши')
btn8 = KeyboardButton(text='Jizzax',callback_data='джизак')
btn9 = KeyboardButton(text="Farg'ona",callback_data="фергана")
btn10 = KeyboardButton(text='Sirdaryo',callback_data='сырдарья')
btn11 = KeyboardButton(text="Qoraqaolpog'iston(Nukus)",callback_data="нукус")

obshi.add(btn,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11)


