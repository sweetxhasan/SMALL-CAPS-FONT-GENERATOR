import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# স্মল ক্যাপস কনভার্সন ডিকশনারি
SMALL_CAPS_MAP = {
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ', 'g': 'ɢ', 'h': 'ʜ', 
    'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 
    'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 
    'y': 'ʏ', 'z': 'ᴢ',
    'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ꜰ', 'G': 'ɢ', 'H': 'ʜ', 
    'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ', 'O': 'ᴏ', 'P': 'ᴘ', 
    'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 
    'Y': 'ʏ', 'Z': 'ᴢ',
    ' ': ' ', '!': '!', '?': '?', '.': '.', ',': ',', ':': ':', ';': ';', 
    '-': '-', '_': '_', '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', 
    '7': '7', '8': '8', '9': '9'
}

def convert_to_small_caps(text: str) -> str:
    """টেক্সটকে স্মল ক্যাপসে কনভার্ট করে"""
    converted_text = []
    for char in text:
        converted_text.append(SMALL_CAPS_MAP.get(char, char))
    return ''.join(converted_text)

# কমান্ড হ্যান্ডলার
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """স্টার্ট কমান্ড হ্যান্ডলার"""
    welcome_text = """
✨ **Welcome to Small Caps Font Generator Bot!** ✨

যেকোনো ইংরেজি টেক্সট পাঠান, আমি সেটাকে Small Caps Font-এ কনভার্ট করে দিব! 🎯

**উদাহরণ:**
Input: hello world
Output: ʜᴇʟʟᴏ ᴡᴏʀʟᴅ

📝 **ঠিক যেমন:**  
`hello` → `ʜᴇʟʟᴏ`
`telegram` → `ᴛᴇʟᴇɢʀᴀᴍ`
`small caps` → `sᴍᴀʟʟ ᴄᴀᴘs`

এবার আপনার টেক্সট পাঠান! 🚀
    """
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """হেল্প কমান্ড হ্যান্ডলার"""
    help_text = """
🆘 **Help Guide**

🤖 **How to use:**
1. যেকোনো ইংরেজি টেক্সট বটে পাঠান
2. বট অটোমেটিকally সেটাকে Small Caps Font-এ কনভার্ট করে দিবে

📝 **Supported Characters:**
- সকল ইংরেজি অক্ষর (A-Z, a-z)
- সংখ্যা (0-9)
- সাধারণ সিম্বল (! ? . , : ; - _ )

🛠 **Commands:**
/start - বট শুরু করুন
/help - এই হেল্প মেসেজ দেখুন
/about - বট সম্পর্কে তথ্য

**উদাহরণ ট্রাই করুন:**
`hello world` লিখে পাঠান!
    """
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """এবাউট কমান্ড হ্যান্ডলার"""
    about_text = """
ℹ️ **About Small Caps Bot**

📱 **Version:** 1.0
🐍 **Language:** Python
🛠 **Framework:** python-telegram-bot
☁️ **Host:** Render

🚀 **Features:**
• Fast text conversion
• Real-time processing
• Support for all English characters
• Clean and modern font style

📞 **Developer:** @YourName
🔗 **Source Code:** GitHub
    """
    await update.message.reply_text(about_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ইউজারের মেসেজ হ্যান্ডলার"""
    user_message = update.message.text
    user_id = update.message.from_user.id
    
    logger.info(f"User {user_id} sent: {user_message}")
    
    # টেক্সট কনভার্ট করুন
    converted_text = convert_to_small_caps(user_message)
    
    # রেসপন্স তৈরি করুন
    response = f"""
📥 **Input:** `{user_message}`
📤 **Output:** `{converted_text}`

✨ **Copy this:** 
`{converted_text}`
    """
    
    await update.message.reply_text(response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """এরর হ্যান্ডলার"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """মেইন অ্যাপ্লিকেশন"""
    # বট টোকেন
    TOKEN = "8011981998:AAGrdUuUyMSPU_Jpa02rnuQzUkqwxDZ79rM"
    
    # অ্যাপ্লিকেশন তৈরি করুন
    application = Application.builder().token(TOKEN).build()
    
    # কমান্ড হ্যান্ডলার
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    
    # মেসেজ হ্যান্ডলার
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # এরর হ্যান্ডলার
    application.add_error_handler(error_handler)
    
    # Render-এ ডেপ্লয়মেন্টের জন্য পোর্ট সেটআপ
    PORT = int(os.environ.get('PORT', 10000))
    
    # ওয়েবহুক সেটআপ (Production)
    if 'RENDER' in os.environ:
        WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=WEBHOOK_URL
        )
    else:
        # লোকাল ডেভেলপমেন্ট (Polling)
        application.run_polling()

if __name__ == '__main__':
    main()
