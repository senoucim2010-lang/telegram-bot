from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎭 مرحبًا بك في «آخر ليلة في القصر» 👑\n\n"
        "قصرٌ غامض، 4 إلى 8 أشخاص، "
        "وقضية قتل واحدة فقط...\n\n"
        "اكتشفوا القاتل قبل انتهاء الوقت. 🔎"
    )

def main():
    print("البوت جاهز 👑")

if __name__ == "__main__":
    main()
