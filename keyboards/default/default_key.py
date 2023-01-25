from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
glavni = ReplyKeyboardMarkup(resize_keyboard=True)
a = KeyboardButton(text='Viloyatni tanlash')
glavni.add(a)

Viloyat = ReplyKeyboardMarkup(resize_keyboard=True)
a1 = KeyboardButton(text="Farg'ona")
a2 = KeyboardButton(text="Namangan")
a3 = KeyboardButton(text="Andijon")
a4 = KeyboardButton(text="Toshkent")
a5 = KeyboardButton(text="Jizzax")
a6 = KeyboardButton(text="Xorazim")
a7 = KeyboardButton(text="Navoiy")
a8 = KeyboardButton(text="Qashqadaryo")
a9 = KeyboardButton(text="Samarqand")
a10 = KeyboardButton(text="Sirdaryo")
a11 = KeyboardButton(text="Surxandaryo")
a12 = KeyboardButton(text="Qoraqalpog'iston(Nukus)")
Viloyat.add(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12)


tur = ReplyKeyboardMarkup(resize_keyboard=True)
a = KeyboardButton(text='Hozirgi ob-havo🌦')
b = KeyboardButton(text='Bir haftalik ob-havo📆')
c= KeyboardButton(text='Izoh qoldirish✍🏻')
d = KeyboardButton(text="Hududni o'zgartirish📍")
tur.add(a,b,c,d)


Samarkand = ReplyKeyboardMarkup(resize_keyboard=True)
c1 = KeyboardButton('Ishtixon')
c2 = KeyboardButton('Oqtosh')
c3 = KeyboardButton('Jomboy')
c4 = KeyboardButton("Bulung'ur")
c5 = KeyboardButton('Urgut')
c6 = KeyboardButton("Kattako'rg'on")
c7 = KeyboardButton("Samarqand shahri")
Samarkand.add(c1,c2,c3,c4,c5,c6,c7)


Andijon = ReplyKeyboardMarkup(resize_keyboard=True)
n1 = KeyboardButton('Andijon shahri')
n2 = KeyboardButton('Marhamat')
n3 = KeyboardButton('Asaka')
n4 = KeyboardButton("Xo'jaobod")

Andijon.add(n1,n2,n3,n4)

Fargona = ReplyKeyboardMarkup(resize_keyboard=True)
f1 = KeyboardButton('Quva')
f2 = KeyboardButton('Beshariq')
f3 = KeyboardButton("Farg'ona shahri")
f4 = KeyboardButton("Oltiariq")
f5 = KeyboardButton("Yangi marg'ilon")

Fargona.add(f1,f2,f3,f4)


Namangan = ReplyKeyboardMarkup(resize_keyboard=True)
nam1 = KeyboardButton('Uychi')
nam2 = KeyboardButton('Chust')
nam3 = KeyboardButton("Namangan shahri")
nam4 = KeyboardButton("Kosonsoy")
nam5 = KeyboardButton("To'raqorg'on")
nam6 = KeyboardButton("Yangiqorg'on")
nam7 = KeyboardButton("Uch ko'rg'on")

Namangan.add(nam1,nam2,nam3,nam4,nam5,nam6,nam7)

Toshkent = ReplyKeyboardMarkup(resize_keyboard=True)
tosh1 = KeyboardButton('Olmaliq')
tosh2 = KeyboardButton('Bektemir')
tosh3 = KeyboardButton("Toshkent shahri")

Toshkent.add(tosh1,tosh2,tosh3,)



Jizzax = ReplyKeyboardMarkup(resize_keyboard=True)
jiz = KeyboardButton("Do'stlik")
jiz2 = KeyboardButton('Jizzax shahri')

Jizzax.add(jiz,jiz2)


Xorazim = ReplyKeyboardMarkup(resize_keyboard=True)
xor = KeyboardButton('Gurlan')
xor2 = KeyboardButton('Shovot')
xor3 = KeyboardButton("Urganch")

Xorazim.add(xor,xor2,xor3)


Navoiy = ReplyKeyboardMarkup(resize_keyboard=True)
nav = KeyboardButton('Nurota')
nav2 = KeyboardButton('Navoiy shahri')

Navoiy.add(nav,nav2)


Qashqadaryo = ReplyKeyboardMarkup(resize_keyboard=True)
qash = KeyboardButton('Qarshi')
qash2 = KeyboardButton('Muborak')
qash3 = KeyboardButton("Koson")
qash4 = KeyboardButton("Chiroqchi")
qash5 = KeyboardButton("Shahrisabz")

Qashqadaryo.add(qash,qash2,qash3,qash4,qash5)

Sirdaryo = ReplyKeyboardMarkup(resize_keyboard=True)
sir = KeyboardButton('Guliston')
sir2 = KeyboardButton('Sirdaryo shahri')

Sirdaryo.add(sir,sir2)


Surxandaryo = ReplyKeyboardMarkup(resize_keyboard=True)
sur = KeyboardButton('Denov')
sur2 = KeyboardButton("Sho'rchi")
sur3 = KeyboardButton("Termiz")
sur4 = KeyboardButton("Boysun")

Surxandaryo.add(sur,sur2,sur3,sur4)


Qoraqalpogiston = ReplyKeyboardMarkup(resize_keyboard=True)
qor = KeyboardButton('Beruniy')
qor2 = KeyboardButton('Chimboy')
qor3 = KeyboardButton('Kegeyli')
qor4 = KeyboardButton('Nukus')
qor5 = KeyboardButton("To'rtko'l")

Qoraqalpogiston.add(qor,qor2,qor3,qor4,qor5)