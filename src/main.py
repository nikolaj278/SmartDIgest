from collectors.telegram_collector import TelegramCollector
from summarizer.llm_summarizer import Summarizer
from storage.data_base import DB
from outputs.telegram_sender import send_summary

def main():
    # fetch new messages fro tg
    collected = TelegramCollector().fetch_new(nr_posts=1)
    DB().save_messages(collected)
    # send prompt+messages to DeepSeek 
    summaries = Summarizer().summarize(collected)
    DB().save_summaries(summaries)
    # send summaries of channel content with telegram bot
    for (ch_name, _), (_, summary) in summaries.items():
        send_summary(ch_name + ":\n" + summary)

if __name__ == "__main__":
    main()


    