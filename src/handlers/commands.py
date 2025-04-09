import os
import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
from pyngrok import ngrok
from src.utils.keyboards import main_menu

# Agregar la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Cargar las variables de entorno
load_dotenv()

# Configurar el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

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

async def start(update: Update, context: CallbackContext):
    """Manejador del comando /start."""
    await update.message.reply_text(
        "👋 ¡Hola! Soy EduSex,canal educativo de sexualidad.\n\n"
        "Usa el comando /menu para explorar los temas disponibles."
    )

async def help_command(update: Update, context: CallbackContext):
    """Manejador del comando /help."""
    await update.message.reply_text(
        "ℹ️ **Ayuda del Bot**\n\n"
        "Usa los botones del menú principal para explorar temas educativos.\n"
        "Comandos disponibles:\n"
        "- /start: Inicia el bot.\n"
        "- /menu: Muestra el menú principal.\n"
        "- /help: Muestra esta ayuda."
    )

# Función para mostrar el menú principal
async def menu(update: Update, context: CallbackContext):
    """Muestra el menú principal."""
    await update.message.reply_text("🏠 Menú Principal", reply_markup=main_menu())

# Manejador para los botones del menú
async def button_handler(update: Update, context: CallbackContext):
    """Manejador para los botones del menú."""
    query = update.callback_query
    await query.answer()

    if query.data == "embarazo":
        await query.edit_message_text("🤰 *Embarazo Adolescente*", reply_markup=embarazo_menu())
    elif query.data == "ets":
        await query.edit_message_text("🦠 *Enfermedades de Transmisión Sexual (ETS)*", reply_markup=ets_menu())
    elif query.data == "anticonceptivos":
        await query.edit_message_text("🛡️ *Métodos Anticonceptivos*", reply_markup=anticonceptivos_menu())
    elif query.data == "consentimiento":
        await query.edit_message_text("❤️ *Consentimiento*", reply_markup=consentimiento_menu())
    elif query.data == "redes_sociales":
        await query.edit_message_text("🌐 *Redes Sociales*", reply_markup=social_media_menu())
    elif query.data == "back_to_menu":
        await query.edit_message_text("🏠 *Menú Principal*", reply_markup=main_menu())
    else:
        await query.edit_message_text("⚠️ Opción no reconocida. Usa el menú principal.", reply_markup=main_menu())

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