import logging

from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, \
    CallbackQueryHandler
from telegram import Update, MessageEntity
from settings import TELEGRAM_TOKEN


from default import send_contact, send_location, main_menyu, \
    comment_button, menu_button, settings_button, \
    backet_button, placing_button

from inline import language_inline

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# states
PHONE_STATE, MENU_STATE, COMMENT_STATE, SETTINGS_STATE, BACKET_STATE = range(5)


# commands
def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Salom", reply_markup=send_contact())
    return PHONE_STATE


def send_phone_number_handler(update: Update, context: CallbackContext):
    user_phone = update.message.contact.phone_number
    update.message.reply_text(
        "Menudan maxsulot tanlashingiz mumkin!", reply_markup=main_menyu())
    context.chat_data["phone_number"] = user_phone
    return ConversationHandler.END


def menu_handler(update: Update, context: CallbackContext):
    text = """Qaysi manzilga yetkazilsin?
    Manzilni kiriting yoki "📍 Manzilini yuborish" tugmachasini bosing 👇🏻"""
    update.message.reply_text(text=text, reply_markup=send_location())
    return MENU_STATE


def location_handler(update: Update, context: CallbackContext):
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    chat_id = update.message.chat.id
    context.chat_data['latitude'] = latitude
    context.chat_data['longitude'] = longitude
    context.bot.send_message(chat_id=chat_id, text="asd", reply_markup=menu_button())


def order_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = """Savatingiz:\n\n1. 🛍 Пакет\n1 x 1 000 so'm = 1 000 so'm\n\nJami: 1 000 so'm"""
    context.bot.send_message(
        chat_id=chat_id, text=text, reply_markup=backet_button())
    print(context.chat_data)
    return BACKET_STATE


def backet_pakect(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    text = f"""«CIAO!»  {first_name}! Kichik Italiyaga xush kelibsiz 🇮🇹 \n\nNima buyurtma qilamiz?"""
    context.bot.send_message(chat_id, text)
    return back_to_home_handler(update, context)


def contact_handler(update: Update, context: CallbackContext):
    text = """Buyurtma va boshqa savollar bo'yicha javob olish uchun \
    "@pastarobot ga murojaat qiling, barchasiga javob beramiz :)"""
    context.bot.send_message(chat_id=update.message.chat_id, text=text)


def cafe_location_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_location(chat_id, latitude=41.368091, longitude=69.273425)


def order_about_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = """🇮🇹 Italiyani yetkazib berish!
    🍝 Italiyancha pasta korobochkalarda!
    ⏰ С 11:00 до 01:00
    🛵 Hoziroq buyurtma bering!

    *Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin"""
    context.bot.send_message(chat_id, text)


def comment_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = """✅ PASTA-PASTA ni tanlaganingiz uchun rahmat.
    Agar Siz bizning xizmatlarimiz sifatini yaxhshilashga yordam bersangiz benihoyat hursand bo’lamiz.
    Buning uchun 5 ballik tizim asosida bizni baholang"""
    context.bot.send_message(chat_id=chat_id, text=text,
                             reply_markup=comment_button())
    return COMMENT_STATE


def comment_good_result_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = """Yoqganidan hursandmiz 😊. Nima deb o'ylaysiz, xizmatimizni yanada qulay va
    yaxshiroq qilishimiz uchun yana nima qilishimiz kerak?"""
    context.bot.send_message(chat_id=chat_id, text=text)
    return back_to_home_handler(update, context)


def comment_bad_result_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = """Xizmatimiz sizni mamnun qoldirmaganidan afsusdamiz 😔.
    Iltimos, o'z izohlaringizni yozib qoldiring va biz albatta ularni inobatga olib, to'g'irlanishga harakat qilamiz 🙏🏻"""
    context.bot.send_message(chat_id=chat_id, text=text)
    return back_to_home_handler(update, context)


def back_to_home_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    first_name = update.message.from_user.first_name
    text = f"""«CIAO!»  {first_name}! Kichik Italiyaga xush kelibsiz 🇮🇹
    Nima buyurtma qilamiz?"""
    context.bot.send_message(chat_id=chat_id, text=text,
                             reply_markup=main_menyu())
    return ConversationHandler.END


def settings_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="⚙️ Sozlamalar",
                             reply_markup=settings_button())
    return SETTINGS_STATE


def language_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = """Iltimos, tilni tanlang
    Пожалуйста, выберите язык ⬇️"""
    context.bot.send_message(
        chat_id=chat_id, text=text, reply_markup=language_inline())


def lang_uz_handler(update: Update, context: CallbackContext):
    chat_id = update.callback_query.message.chat_id
    first_name = update.callback_query.from_user.first_name
    text = f"""«CIAO!»  {first_name}! Kichik Italiyaga xush kelibsiz 🇮🇹
    Nima buyurtma qilamiz?"""
    context.bot.send_message(chat_id=chat_id, text=text,
                             reply_markup=main_menyu())
    return ConversationHandler.END


def lang_ru_handler(update: Update, context: CallbackContext):
    chat_id = update.callback_query.message.chat_id
    first_name = update.callback_query.from_user.first_name
    update.callback_query.message.delete()
    text = f"""«CIAO!»  {first_name}! Добро пожаловать в маленькую Италию🇮🇹
    Что будете заказывать?"""
    context.bot.send_message(chat_id=chat_id, text=text,
                             reply_markup=main_menyu())
    return ConversationHandler.END


def placing_order_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = """Buyurtmani o'zingiz olib keting yoki Yetkazib berishni tanlang 👇🏻"""
    context.bot.send_message(chat_id=chat_id, text=text,
                             reply_markup=placing_button())


def delivery_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = """Yetkazish xizmatimiz 10:00'dan 23:00'gacha ishlaydi, hozir esa
    Yandex.Еда va Express24'dan buyurtma bersangiz bo'ladi. Mana havolalar 👇
    Yandex.Еда - https://eda.yandex.ru/restaurant/pastapasta_evfxw

    Express24 - https://express24.uz/store/11698"""
    context.bot.send_message(chat_id=chat_id, text=text)
    return ConversationHandler.END


def take_away_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = """Hozir faqat yetkazib berish xizmati mavjud, ushbu xizmatimiz soat 23:00 gacha ishlaydi.\n
    Kuryerlarimiz buyurtmangizni yetkazishga oshiqmoqdalar :)\n
    /start"""
    context.bot.send_message(chat_id=chat_id, text=text)
    print(context.chat_data)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start_handler),
            MessageHandler(Filters.regex(
                "^(📥 Savat)$"), order_handler),
            MessageHandler(Filters.regex(
                "^(☎️ Kontaktlar)$"), contact_handler),
            MessageHandler(Filters.regex(
                "^(KAFE LOKATSIYASI)$"), cafe_location_handler),
            MessageHandler(Filters.regex(
                "^(🚀 Buyurtma haqida)$"), order_about_handler),
            MessageHandler(Filters.regex(
                "^(✍️ Fikr bildirish)$"), comment_handler),
            MessageHandler(Filters.regex(
                "^(🍴 Menyu)$"), menu_handler),
            MessageHandler(Filters.regex(
                "⚙️ Sozlamalar"), settings_handler),
            MessageHandler(Filters.all, back_to_home_handler)
        ],
        states={
            PHONE_STATE: [
                MessageHandler(Filters.contact, send_phone_number_handler),
            ],
            MENU_STATE: [
                MessageHandler(Filters.regex("^(🍴 Menyu)$"), menu_handler),
                MessageHandler(Filters.location, location_handler),
                MessageHandler(Filters.regex("^(🏘 Bosh menu)$"),
                               back_to_home_handler),
            ],
            COMMENT_STATE: [
                MessageHandler(Filters.regex(
                    "^(😊Hammasi yoqdi ❤️|☺️Yaxshi ⭐️⭐️⭐️⭐️)$"), comment_good_result_handler),
                MessageHandler(Filters.regex(
                    "^(😐Yoqmadi ⭐️⭐️⭐️|🙁Yomon ⭐️⭐️|😤Juda yomon 👎)$"), comment_bad_result_handler),
                MessageHandler(Filters.regex("^(🏘 Bosh menu)$"),
                               back_to_home_handler),
                MessageHandler(Filters.all, back_to_home_handler)
            ],
            SETTINGS_STATE: [
                MessageHandler(Filters.regex(
                    "^🌐 Tilni tanlash$"), language_handler),
                CallbackQueryHandler(lang_uz_handler, pattern="^uz$"),
                CallbackQueryHandler(lang_ru_handler, pattern="^ru$"),

                MessageHandler(Filters.regex(
                    "^(📱 Raqamni o'zgartirish)$"), send_phone_number_handler),

                MessageHandler(Filters.regex("^(🏘 Bosh menu)$"),
                               back_to_home_handler),
            ],
            BACKET_STATE: [
                MessageHandler(Filters.regex(
                    "^(🚖 Buyurtma berish)$"), placing_order_handler),
                MessageHandler(Filters.regex(
                    "^(🚖 Yetkazib berish)$"), delivery_handler),
                MessageHandler(Filters.regex(
                    "^(🏃 Olib ketish)$"), take_away_handler),
                MessageHandler(Filters.regex("^🛍 Пакет$"), backet_pakect),
                MessageHandler(Filters.regex("^(🏘 Bosh menu)$"),
                               back_to_home_handler),
            ]
        },
        fallbacks=[
            # MessageHandler(Filters.contact, send_phone_number_handler),
            MessageHandler(Filters.regex("^(📥 Savat)$"), order_handler),
            MessageHandler(Filters.regex(
                "^(☎️ Kontaktlar)$"), contact_handler),
            MessageHandler(Filters.regex(
                "^(KAFE LOKATSIYASI)$"), cafe_location_handler),
            MessageHandler(Filters.regex(
                "^(🚀 Buyurtma haqida)$"), order_about_handler),
            MessageHandler(Filters.regex(
                "^(✍️ Fikr bildirish)$"), comment_handler),
            MessageHandler(Filters.regex("^(🍴 Menyu)$"), menu_handler),
            MessageHandler(Filters.regex(
                "⚙️ Sozlamalar"), settings_handler),
            MessageHandler(Filters.all, back_to_home_handler)
        ]
    )
    dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
