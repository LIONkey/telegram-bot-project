from telegram import InlineKeyboardButton, InlineKeyboardMarkup


from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🤰 Embarazo", callback_data="embarazo"), InlineKeyboardButton("🦠 ETS", callback_data="ets")],
        [InlineKeyboardButton("🛡️ Anticonceptivos", callback_data="anticonceptivos"), InlineKeyboardButton("❤️ Consentimiento", callback_data="consentimiento")],
        [InlineKeyboardButton("🌐 Redes Sociales", callback_data="redes_sociales")],
        [InlineKeyboardButton("🔙 Volver", callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def embarazo_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 Definición", callback_data="embarazo_definicion")],
        [InlineKeyboardButton("📋 Causas", callback_data="embarazo_causas")],
        [InlineKeyboardButton("⚠️ Consecuencias", callback_data="embarazo_consecuencias")],
        [InlineKeyboardButton("✅ Prevención", callback_data="embarazo_prevencion")],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="back_to_menu")]
    ])

def volver_a_embarazo_menu():
    """Crea un botón para regresar al submenú de embarazo."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Volver", callback_data="embarazo")]
    ])

def ets_menu():
    return InlineKeyboardMarkup([
       [InlineKeyboardButton("📖 Definición", callback_data="ets_definicion")],
        [InlineKeyboardButton("🤒 Síntomas", callback_data="ets_sintomas")],
        [InlineKeyboardButton("🛡️ Prevención", callback_data="ets_prevencion")],
        [InlineKeyboardButton("💊 Tratamiento", callback_data="ets_tratamiento")],
        [InlineKeyboardButton("🔙 Volver", callback_data="back_to_menu")]
    ])

def volver_a_ets_menu():
    """Crea un botón para regresar al submenú de ets."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Volver", callback_data="ets")]
    ])

def anticonceptivos_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛡️ Métodos de Barrera", callback_data="anticonceptivos_barrera")],
        [InlineKeyboardButton("💊 Métodos Hormonales", callback_data="anticonceptivos_hormonales")],
        [InlineKeyboardButton("🌀 Métodos Intrauterinos", callback_data="anticonceptivos_intrauterinos")],
        [InlineKeyboardButton("🔬 Métodos Quirúrgicos", callback_data="anticonceptivos_quirurgicos")],  # Nuevo botón
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="back_to_menu")]
    ])

def consentimiento_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📖 Definición", callback_data="consentimiento_definicion")],
        [InlineKeyboardButton("🔑 Claves de Consentimiento", callback_data="consentimiento_claves")],
        [InlineKeyboardButton("⚖️ Importancia Legal", callback_data="consentimiento_importancia_legal")],
        [InlineKeyboardButton("🔙 Volver", callback_data="back_to_menu")]
    ])

def social_media_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/edusex_001/")],
        [InlineKeyboardButton("🎥 TikTok", url="https://www.tiktok.com/@edusex01")],
        [InlineKeyboardButton("📱 WhatsApp", url="https://whatsapp.com/channel/0029Vb6J3uAEwEk3BF8FcO2d")],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="back_to_menu")]
    ])

def back_to_menu():
    """Crea un botón para volver al menú principal."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="back_to_menu")]
    ])

def sintomas_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⚠️ Síntomas", callback_data="sintomas_contenido")],
        [InlineKeyboardButton("🔙 Volver al Menú Principal", callback_data="back_to_menu")]
    ])

def volver_a_sintomas_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Volver", callback_data="sintomas")]
    ])
