import asyncio
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from utils import edit_config, edit_price
from filters.is_admin import Is_Admin
import json
from utils import database, qiwi
from keyboards import admin_keyboard, back_button_keyboard, mailing_photo_keyboard, prices_keyboard, admin_ids_keyboard
from states.admin import Admin
import sqlite3
from loader import dp, bot
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard

link = 't.me/+LWy3wgZP8vQ2ZDUy'
link_Alice = 'https://t.me/+z2ITOlyiCJE1NTU6'
content = -1001554088951



@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    text = f'''👋 Привет, {update.from_user.full_name}\n\n<b>Этот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏\n\n</b>🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
    try:
        await update.approve()
    except:
        pass
    if not database.user_exists(update.from_user.id):
        database.create_user(update.from_user.id, update.from_user.username)

    await asyncio.sleep(20)


    try:
        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b>💣Парни, это просто находка! Девочка творит нереальные вещи в своей випке!</b>

<tg-spoiler>🔥Сочный анал, горловой минет, паки нереально горячих фоток!</tg-spoiler>

Эта <a href = '{link_Alice}'>сучка</a>  заставляет кончить мужиков за считанные минуты, не упусти возможность обкончаться с <a href = '{link_Alice}'>красоткой</a> 🥵

<b>{link_Alice}</b>""", message_id=20)  # Пост на Алису

        await asyncio.sleep(600)
        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b><a href = '{link}'>ПОКОЛЕНИЕ Z</a> - самый аморальный канал, куда постится контент про отбитых малолеток и пьяных долбоебов! 
    
- Треш со вписок
- Бухие бляди
- Проебанное поколение
    
{link}
    
❗️ВХОД 18+❗️</b>""", message_id=3)  # Пост на канал

        await asyncio.sleep(500)

        await bot.send_message(chat_id = update.from_user.id,text = f"""<b>👊🏻 Избиения закладчиков
{link}
🔞Треш со вписок
{link}</b>""",disable_web_page_preview=True) #Ответка на канал


        await asyncio.sleep(3600)


        await bot.send_message(chat_id=update.from_user.id, text=f"""<b>😧 Конченые отбросы общества.
<tg-spoiler>{link}</tg-spoiler>
😳 Неадекватные малолетки.
<tg-spoiler>{link}</tg-spoiler></b>""",disable_web_page_preview=True)  # Ответка на канал

        await asyncio.sleep(10800)

        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b>В Telegram появился новый канал <a href = '{link}'>🔞 Поколение Z❗️</a></b>
    
<i>😧 Конченые отбросы общества.
    
😳 Неадекватные малолетки.
    
😱 Треш нашего поколения.</i>
    
<b>📲Заглядывай, увидишь каких долбаебов носит этот мир! 
    {link}</b>""", message_id=16)  # Пост на канал
        await asyncio.sleep(20000)
        await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content, caption=f"""<b>💣Парни, это просто находка! Девочка творит нереальные вещи в своей випке!</b>

<tg-spoiler>🔥Сочный анал, горловой минет, паки нереально горячих фоток!</tg-spoiler>

Эта <a href = '{link_Alice}'>сучка</a>  заставляет кончить мужиков за считанные минуты, не упусти возможность обкончаться с <a href = '{link_Alice}'>красоткой</a> 🥵

<b>{link}</b>""", message_id=20)  # Пост на Алису



        await asyncio.sleep(50000)


        await bot.send_photo(
            photo='https://sun1-95.userapi.com/impg/X3WP4VJR6QgTVolvcfobfgYM5tPU0opNeP7M9A/bLPaeXcs89Y.jpg?size=1280x1280&quality=96&sign=bf858645ce1d4ee9bd6d838d00c23095&type=album',
            caption = text, reply_markup=menu_keyboard.keyboard, chat_id=update.from_user.id)
        await bot.send_message(text='🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard,chat_id = update.from_user.id)



    except:
        pass
