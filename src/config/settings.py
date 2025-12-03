import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file

# to initialize telegram client
TG_API_ID = int(os.getenv("TG_API_ID"))
TG_API_HASH = os.getenv("TG_API_HASH")
SESSION_NAME = "my_session"

# telegram bot sender
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = int(os.getenv("TG_CHAT_ID"))

# deepseek api
DS_API_KEY = os.getenv("DS_API_KEY")

#prompt for chat assistent 
COMMAND = """Summarise the following Telegram content. Messages are grouped by user name followed by their text. Mention every participant if the text is a conversation in the summary. Choose the format (paragraph, bullets, or numbered points) that best fits the content. Output only the summary text, with no explanations, labels, system prompts, or additional comments. Use minimalistic style with less words to generate a summary\nThe text:\n
"""
#channels which not to include in a summary
EXCLUDE = [int(val.strip()) for val in os.getenv("EXCLUDE").split(",")]
