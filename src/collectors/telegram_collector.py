from telethon.sync import TelegramClient

from config.settings import SESSION_NAME, TG_API_ID, TG_API_HASH, EXCLUDE
from storage.models import MessageItem

class TelegramCollector:

    """
    Define an object which initializes a client to connect to telegram, 
    fetches mesasges and sorts for channel posts only.
    """
    
    def __init__(self, ):
        self.client = TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH)
        

    def fetch_new(self, nr_posts=None):
        with self.client:
            dialogs = self.client.get_dialogs()
            channels = [d for d in dialogs if (type(d.entity).__name__ == "Channel") 
                                          and (d.id not in EXCLUDE)]
            fetched_msgs = {}
            for ch in channels:
                # take explicitely defined nr of posts per channel or all unread posts
                unread = nr_posts if nr_posts else ch.unread_count 
                if unread == 0:
                    continue
                msgs = self.client.get_messages(ch, limit=unread)
                # write messeges to a dictionary with channel names as keys
                fetched_msgs[(ch.name, ch.id)] = [
                     MessageItem(
                        msg_id=m.id,
                        channel_name=ch.name,
                        channel_id=ch.id,
                        # use name if author has a name else "user nr. {sender_id}"
                        author_name=getattr(m, "author_name", "User nr." + str(m.sender_id)),
                        author_id=m.sender_id,
                        text=m.text,
                        date=m.date,
                        raw=m
                    )
                    for m in msgs
                    if m.text is not None
                ]
                # Mark that message (and everything before it) as read
                self.client.send_read_acknowledge(ch, msgs[0])

                
            return fetched_msgs
        





