from pyrogram import Client, filters

import os

BOT_TOKEN = os.environ.get("7660290146:AAEfz-YAUOcG3q7Kkck1GCfSBD-srpv9ltE")

app = Client("anime_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start_handler(client, message):
    user = "@" + message.from_user.username if message.from_user.username else message.from_user.first_name
    message.reply_text(f"سلام {user} 🌿\nکدام انیمه را می‌خواهی؟")

@app.on_message(filters.command("help"))
def help_handler(client, message):
    message.reply_text(
        "📖 راهنمای روبات:\n\n"
        "/start - شروع کار با روبات\n"
        "/help - دیدن راهنما\n"
        "هر متن دیگری بفرستی، روبات همان را برایت تکرار می‌کند\n"
        "عکس یا استیکر بفرستی، روبات جواب مخصوص می‌دهد"
    )

@app.on_message(filters.text & ~filters.command)
def echo_handler(client, message):
    message.reply_text(f"تو نوشتی: {message.text}")

@app.on_message(filters.photo)
def photo_handler(client, message):
    message.reply_text("📷 عکس قشنگی فرستادی!")

@app.on_message(filters.sticker)
def sticker_handler(client, message):
    message.reply_text("🙂 استیکر باحال بود!")

app.run()
