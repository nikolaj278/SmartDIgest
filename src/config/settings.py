import os
from dotenv import load_dotenv


load_dotenv()  # reads .env file

# to initialize telegram client
TG_API_ID = int(os.getenv("TG_API_ID"))
TG_API_HASH = os.getenv("TG_API_HASH")
TG_SESSION = os.getenv("TG_SESSION")

# telegram bot sender
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = int(os.getenv("TG_CHAT_ID"))

# deepseek api
DS_API_KEY = os.getenv("DS_API_KEY")

#prompt for llm model 
COMMAND_EN = """Summarise the following Telegram content. The messages are ordered chronologically. The text consists of usernames followed by their messages. Choose the format (paragraph, bullet points, or numbered points) that best fits the content. Output only the summary text, with no explanations, labels, system prompts, or additional comments. Keep the summary concise and minimalistic but informative.\nThe text:\n
"""

COMMAND_RU = """Суммируй следующий контент из Telegram. Сообщения упорядочены в хронологическом порядке. Текст состоит из имён пользователей, за которыми следуют их сообщения. Выбери формат (абзац, маркированный список или нумерованный список), который лучше всего подходит содержанию. Выведи только текст резюме без объяснений, меток, системных подсказок или дополнительных комментариев. Сделай резюме лаконичным, минималистичным, но информативным.\nТекст:\n
"""


#channels which not to include in a summary
EXCLUDE = [int(val.strip()) for val in os.getenv("EXCLUDE").split(",")]
