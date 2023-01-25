from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate

from loader import dp
from aiogram.dispatcher import FSMContext
import requests
from bs4 import BeautifulSoup as BS
from keyboards.default.default_key import glavni,tur,Viloyat,Samarkand,Andijon,Fargona,Namangan,Toshkent,Jizzax,Xorazim,Navoiy,Qashqadaryo,Sirdaryo,Surxandaryo,Qoraqalpogiston
from utils.db_api.postgres import send_ex
from loader import bot
from states.command import ObshiStates


@dp.message_handler(commands='start')
async def download(message: types.Message):
    user = send_ex("""SELECT telegram_id FROM demo""")
    if str(message.from_user.id) in [i[0] for i in user]:
        print("foydalanuvchi  datanaseda")
    else:
        send_ex(f"""INSERT INTO demo(name,username,telegram_id) VALUES ('{message.from_user.first_name}','{message.from_user.username}','{message.from_user.id}') returning *""")
    await message.answer(f"Asslomu Aleykum {message.from_user.first_name},men Ob-havo🌦🌦🌦 botman",reply_markup=glavni)

@dp.message_handler(text='/user')
async def obunachi(message:types.Message):
    foydalanuchi = ''
    if message.from_user.id == 5253015820 or 1737841515:
        a = len(send_ex(f"""SELECT telegram_id FROM demo"""))
        b = send_ex(f"""SELECT username FROM demo""")
        for x in b:
            foydalanuchi+=f"@{x[0]}\n"


        await message.answer(f"Foydalanuvchilar soni : {a} \n {foydalanuchi}")
    else:
        print('xato')



@dp.message_handler(text='Viloyatni tanlash')
async def viloyat(message:types.Message):
    await message.answer(f"Marhamat tanlang:",reply_markup=Viloyat)


@dp.message_handler(text=['Samarqand'])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Samarkand)


@dp.message_handler(text=['Andijon'] )
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Andijon)


@dp.message_handler(text=["Farg'ona"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Fargona)

@dp.message_handler(text=["Namangan"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Namangan)



@dp.message_handler(text=["Toshkent"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Toshkent)


@dp.message_handler(text=["Jizzax"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Jizzax)



@dp.message_handler(text=["Xorazim"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Xorazim)



@dp.message_handler(text=["Navoiy"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Navoiy)



@dp.message_handler(text=["Qashqadaryo"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Qashqadaryo)


@dp.message_handler(text=["Sirdaryo"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Sirdaryo)


@dp.message_handler(text=["Surxandaryo"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Surxandaryo)


@dp.message_handler(text=["Qoraqalpog'iston(Nukus)"])
async def Haftaobhavo(message:types.Message):
    await message.answer('Marhamat kerakli viloyatni tanlang',reply_markup=Qoraqalpogiston)


@dp.message_handler(text=['Ishtixon','Oqtosh','Jomboy',"Bulung'ur",'Urgut',"Kattako'rg'on","Samarqand shahri",'Andijon shahri','Marhamat','Asaka',"Xo'jaobod","Quva","Farg'ona shahri",'Oltiariq','Beshariq',"Yangi marg'ilon",
                          'Uychi','Chust','Namangan shahri','Kosonsoy',"To'raqorg'on","Yangiqorg'on",'Olmaliq','Bektemir','Toshkent shahri',"Do'stlik","Jizzax shahri",'Gurlan','Shovot','Urganch',"Uch ko'rg'on","Nurota","Navoiy shahri",
                          'Qarshi','Muborak','Koson','Chiroqchi','Shahrisabz',"Guliston","Sirdaryo shahri","Denov","Sho'rchi","Termiz","Boysun",'Beruniy',"Chimboy","Kegeyli","Nukus","To'rtko'l"])
async def viloyat(message:types.Message):
    await message.answer(f"Marhamat tanlang:",reply_markup=tur)
    global sin
    sin = message.text



@dp.message_handler(text="Hududni o'zgartirish📍")
async def Hudud(message:types.Message):
    await message.answer('Kerakli buyruqni tanlang',reply_markup=Viloyat)


@dp.message_handler(text=['Hozirgi ob-havo🌦',"Bir haftalik ob-havo📆"])
async def NowObHavo(message:types.Message):
    global sin
    global vil
    if sin == 'Ishtixon':
        vil = 'иштыхан'
    elif sin == 'Oqtosh':
        vil = 'акташ-101217926'
    elif sin == 'Jomboy':
        vil = 'джамбай'
    elif sin == "Bulung'ur":
        vil = 'булунгур'
    elif sin == "Urgut":
        vil = 'ургут'
    elif sin == "Kattako'rg'on":
        vil = 'каттакурган'
    elif sin == "Samarqand shahri":
        vil = 'самарканд'
    elif sin == "Andijon shahri":
        vil = 'андижан'
    elif sin == "Marhamat":
        vil = 'мархамат'
    elif sin == "Asaka":
        vil = 'асака'
    elif sin == "Xo'jaobod":
        vil = 'ходжаабад'
    elif sin == "Farg'ona shahri":
        vil = 'фергана'
    elif sin == "Quva":
        vil = 'кува'
    elif sin == "Oltiariq":
        vil = 'алтыарык'
    elif sin == "Beshariq":
        vil = 'бешарык'
    elif sin == "Yangi marg'ilon":
        vil = 'янги-маргилан'
    elif sin == "Uychi":
        vil = 'уйчи'
    elif sin == "Chust":
        vil = 'чуст'
    elif sin == "Namangan shahri":
        vil = 'наманган'
    elif sin == "Kosonsoy":
        vil = 'касансай'
    elif sin == "To'raqorg'on":
        vil = 'туракурган'
    elif sin == "Yangiqorg'on":
        vil = 'янгикурган'
    elif sin == "Olmaliq":
        vil = 'алмалык'
    elif sin == "Bektemir":
        vil = 'бектемир'
    elif sin == "Toshkent shahri":
        vil = 'ташкент'
    elif sin == "Do'stlik":
        vil = 'дустлик'
    elif sin == "Jizzax shahri":
        vil = 'джизак'
    elif sin == "Gurlan":
        vil = 'гурлен'
    elif sin == "Shovot":
        vil = 'шават'
    elif sin == "Urganch":
        vil = 'ургенч'
    elif sin == "Uch ko'rg'on":
        vil = 'учкурган'
    elif sin == "Nurota":
        vil = 'нурата'
    elif sin == "Navoiy":
        vil = 'навои'
    elif sin == "Navoiy shahri":
        vil = 'навои'
    elif sin == "Qarshi":
        vil = 'карши'
    elif sin == "Muborak":
        vil = 'мубарек'
    elif sin == "Koson":
        vil = 'касан'
    elif sin == "Chiroqchi":
        vil = 'чиракчи'
    elif sin == "Shahrisabz":
        vil = 'шахрисабз'
    elif sin == "Guliston":
        vil = 'гулистан'
    elif sin == "Sirdaryo shahri":
        vil = 'сырдарья'
    elif sin == "Denov":
        vil = 'денау'
    elif sin == "Sho'rchi":
        vil = 'шурчи'
    elif sin == "Termiz":
        vil = 'термез'
    elif sin == "Boysun":
        vil = 'байсун'
    elif sin == "Beruniy":
        vil = 'беруни'
    elif sin == "Chimboy":
        vil = 'чимбай'
    elif sin == "Kegeyli":
        vil = 'кегейли'
    elif sin == "Nukus":
        vil = 'нукус'
    elif sin == "To'rtko'l":
        vil = 'турткуль'

    if message.text == 'Hozirgi ob-havo🌦':
        t = requests.get(f'https://sinoptik.ua/погода-{vil}')
        html_t = BS(t.content, 'html.parser')
        for el in html_t.select('#content'):
            min = el.select('.temperature .min')[0].text
            max = el.select('.temperature .max')[0].text
            t_min = min[4:]
            t_max = max[5:]
            img = str(el.select('.weatherImg')).split('"')[5]
            month = str(str(el.select('.month')[0]).split('>')[1]).split('<')[0]
            day = str(str(el.select('.day-link')[0]).split('"')[3]).split('/')[-1]

            print(t_min, t_max, month, day)

            await bot.send_animation(message.from_user.id, animation=f'https:{img}',
                                     caption=f"<b>{sin}</b>\nKunduzi:<b>{t_max}</b>\nKechasi:<b>{t_min}</b>\n{month} \nBugun: <b>{day}</b>",reply_markup=tur)



    if message.text == 'Bir haftalik ob-havo📆':
        print(vil)
        t = requests.get(f'https://sinoptik.ua/погода-{vil}')
        html_t = BS(t.content, 'html.parser')
        h= []
        s2 = ''
        s = ''
        ruz = []

        for el in html_t.select('#content'):
            a1 = str(el.select('.min')).split('>')[2::4]
            b =str(el.select('.max')).split('>')[2::4]
            hafta = str(el.select('.day-link')).split('>')[1::2]
            day = str(el.select('.day-link')).split('"')[3::4]
            for y in day:
                y = y.split("/")[-1]
                if y.startswith("2"):
                    ruz.append(y)
            print(ruz)

            for x in a1:
                s+=x
            s = s.split('</span')
            for x in b:
                s2 += x
            s2 = s2.split('</span')


            for m in hafta:
                if m.startswith('Воскресенье'):
                     h.append('Yakshanba')
                if m.startswith('Понедельник'):
                    h.append('Dushanba')
                if m.startswith('Вторник'):
                    h.append('Seshanba')
                if m.startswith('Среда'):
                    h.append('Chorshanba')
                if m.startswith('Четверг'):
                    h.append('Payshanba')
                if m.startswith('Пятница'):
                    h.append('Jumma')
                if m.startswith('Суббота'):
                    h.append('Shanba')

        gradus = list(zip(s, s2))

        d = f"""  
    <b>{sin.upper()}</b> 
{h[0].upper()} 📆 \n Kechasi : <b>{gradus[0][0]}</b>\n Kunduzi <b>{gradus[0][-1]}</b> \n Sana : <b>{ruz[0]}</b> \n
{h[1].upper()} 📆 \n Kechasi : <b>{gradus[1][0]}</b>\n Kunduzi <b>{gradus[1][-1]}</b> \n Sana : <b>{ruz[1]}</b> \n
{h[2].upper()} 📆 \n Kechasi : <b>{gradus[2][0]}</b>\n Kunduzi <b>{gradus[2][-1]}</b> \n Sana : <b>{ruz[2]}</b> \n
{h[3].upper()} 📆 \n Kechasi : <b>{gradus[3][0]}</b>\n Kunduzi <b>{gradus[3][-1]}</b> \n Sana : <b>{ruz[3]}</b> \n
{h[4].upper()} 📆 \n Kechasi : <b>{gradus[4][0]}</b>\n Kunduzi <b>{gradus[4][-1]}</b> \n Sana : <b>{ruz[4]}</b> \n
{h[5].upper()} 📆 \n Kechasi : <b>{gradus[5][0]}</b>\n Kunduzi <b>{gradus[5][-1]}</b> \n Sana : <b>{ruz[5]}</b> \n
{h[6].upper()} 📆 \n Kechasi : <b>{gradus[6][0]}</b>\n Kunduzi <b>{gradus[6][-1]}</b> \n Sana : <b>{ruz[6]}</b> \n"""
        await message.answer(f"""{d}""" )







@dp.message_handler(text='Izoh qoldirish✍🏻',state=None)
async def Comment(msg:types.Message):
    await msg.answer("Marhamat izoh qoldirishingiz mumkin")
    await ObshiStates.xabar.set()
@dp.message_handler(state=ObshiStates.xabar )
async def CommentAnswer(msg: types.Message,state:FSMContext):
    message = msg.text
    await state.update_data(
        {
            "xabar" : message
        }
    )
    data = await state.get_data()
    b = data['xabar']
    await msg.answer(f"""Juda yaxshi xabar adminga \n Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing
    Doimiy ob-havo ma'lumotlari👉https://t.me/obhavo_weather_pagodabot """)
    a = f"xabar : {b}\n username : {msg.from_user.username}\n Firstname : {msg.from_user.first_name}\n id : {msg.from_user.id}"
    await bot.send_message(chat_id='5253015820',text=a)
    await state.finish()






