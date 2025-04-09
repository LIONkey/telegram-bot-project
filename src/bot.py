import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
from pyngrok import ngrok
from utils.keyboards import main_menu, ets_menu, anticonceptivos_menu, consentimiento_menu, social_media_menu, embarazo_menu, volver_a_embarazo_menu, sintomas_menu, volver_a_sintomas_menu
from src.handlers.commands import start, help_command, menu
from src.data.content import ANTICONCEPTIVOS_CONTENT, CONSENTIMIENTO_CONTENT, ETS_CONTENT, EMBARAZO_CONTENT
from telegram.ext import CallbackQueryHandler
# Cargar las variables de entorno
load_dotenv()

# Configurar el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Obtener las variables de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")

# Verificar que las variables de entorno estén configuradas
if not TELEGRAM_TOKEN or not NGROK_AUTH_TOKEN:
    logger.error("Las variables de entorno no están configuradas correctamente.")
    exit(1)

# Configurar ngrok
ngrok.set_auth_token(NGROK_AUTH_TOKEN)
public_url = ngrok.connect(5000).public_url  # Exponer el puerto 5000
logger.info(f"ngrok URL: {public_url}")

def escape_markdown_v2(text):
    """Escapa caracteres especiales para MarkdownV2."""
    escape_chars = r"_*[]()~`>#+-=|{}.!"
    return "".join(f"\\{char}" if char in escape_chars else char for char in text)

# Manejador para los botones del menú
async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "back_to_menu":
        await query.edit_message_text(
            "🏠 Menú Principal",  # Escapa los asteriscos para MarkdownV2
            reply_markup=main_menu(),
            parse_mode="MarkdownV2"
        )
    elif query.data == "embarazo_causas":
        await query.edit_message_text(
            escape_markdown_v2(EMBARAZO_CONTENT["causas"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="embarazo")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "embarazo_consecuencias":
        await query.edit_message_text(
            escape_markdown_v2(EMBARAZO_CONTENT["consecuencias"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="embarazo")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "embarazo_prevencion":
        await query.edit_message_text(
            escape_markdown_v2(EMBARAZO_CONTENT["prevencion"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="embarazo")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "embarazo_definicion":
        await query.edit_message_text(
            escape_markdown_v2(EMBARAZO_CONTENT["definicion"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="embarazo")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "embarazo":
        await query.edit_message_text(
            "🤰 *Embarazo Adolescente*",  # Escapa los asteriscos
            reply_markup=embarazo_menu(),
            parse_mode="MarkdownV2"
        )
    elif query.data == "ets":
        await query.edit_message_text(
            "🦠 Enfermedades de Transmisión Sexual \\(ETS\\)",  # Escapa los caracteres especiales
            reply_markup=ets_menu(),
            parse_mode="MarkdownV2"
        )
    elif query.data == "ets_definicion":
        await query.edit_message_text(
            escape_markdown_v2(ETS_CONTENT["definicion"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="ets")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "ets_sintomas":
        await query.edit_message_text(
            escape_markdown_v2(ETS_CONTENT["sintomas"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="ets")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "ets_prevencion":
        await query.edit_message_text(
            escape_markdown_v2(ETS_CONTENT["prevencion"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="ets")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "ets_tratamiento":
        await query.edit_message_text(
            escape_markdown_v2(ETS_CONTENT["tratamiento"]),  # Escapa el contenido para MarkdownV2
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="ets")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "anticonceptivos":
        await query.edit_message_text(
            "🛡️ *Métodos Anticonceptivos*",  # Escapa los asteriscos
            reply_markup=anticonceptivos_menu(),
            parse_mode="MarkdownV2"
        )
    elif query.data == "anticonceptivos_barrera":
        await query.edit_message_text(
            escape_markdown_v2(ANTICONCEPTIVOS_CONTENT["barrera"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="anticonceptivos")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "anticonceptivos_hormonales":
        await query.edit_message_text(
            escape_markdown_v2(ANTICONCEPTIVOS_CONTENT["hormonales"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="anticonceptivos")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "anticonceptivos_intrauterinos":
        await query.edit_message_text(
            escape_markdown_v2(ANTICONCEPTIVOS_CONTENT["intrauterinos"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="anticonceptivos")]
            ]),
            parse_mode="MarkdownV2"
       )
    elif query.data == "anticonceptivos_quirurgicos":
        await query.edit_message_text(
            escape_markdown_v2(ANTICONCEPTIVOS_CONTENT["quirurgicos"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="anticonceptivos")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "consentimiento":
        await query.edit_message_text(
            "❤️ *Consentimiento*",  # Escapa los asteriscos
            reply_markup=consentimiento_menu(),
            parse_mode="MarkdownV2"
        )
    elif query.data == "consentimiento_definicion":
        await query.edit_message_text(
            escape_markdown_v2(CONSENTIMIENTO_CONTENT["definicion"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="consentimiento")]
            ]),
            parse_mode="MarkdownV2"
        )
    elif query.data == "consentimiento_claves":
        await query.edit_message_text(
            escape_markdown_v2(CONSENTIMIENTO_CONTENT["claves"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="consentimiento")]
            ]),
            parse_mode="MarkdownV2"
        )

    elif query.data == "consentimiento_importancia_legal":
        await query.edit_message_text(
            escape_markdown_v2(CONSENTIMIENTO_CONTENT["importancia_legal"]),  # Escapa el contenido
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Volver", callback_data="consentimiento")]
            ]),
            parse_mode="MarkdownV2"
        )

    elif query.data == "redes_sociales":
        await query.edit_message_text(
            "🌐 *Nuestras Redes Sociales*"
            "📌 \\*Haz clic en los botones para visitarnos\\.\\*",
            reply_markup=social_media_menu(),
            parse_mode="MarkdownV2"
        )
    else:
        await query.edit_message_text(
            "⚠️ \\*\\*Opción no reconocida\\. Usa el menú principal\\.\\*\\*",
            reply_markup=main_menu(),
            parse_mode="MarkdownV2"
        )

# Función principal
def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("menu", menu))

    # Manejador de botones
    application.add_handler(CallbackQueryHandler(button_handler))

    # Configurar el webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=5000,
        url_path="webhook",
        webhook_url=f"{public_url}/webhook"
    )

    logger.info("Bot iniciado con webhook...")

if __name__ == "__main__":
    main()