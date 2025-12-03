import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("data/messages.db")


class DB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                msg_id INTEGER PRIMARY KEY,
                channel_name TEXT,
                channel_id INTEGER,
                author_name TEXT,
                author_id INTEGER,
                text TEXT,
                date TEXT,
                inserted_at TEXT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS summaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                channel_name TEXT,
                channel_id INTEGER,
                deepseek_req TEXT,
                deepseek_summary TEXT,
                created_at TEXT
            )
        """)

        self.conn.commit()

    
    def save_messages(self, data: dict[str, list]):
        """
        data structure: {
            "ChannelA": [MessageItem, MessageItem, ...],
            "ChannelB": [...]
        }
        """
        cur = self.conn.cursor()

        for channel, messages in data.items():
            for m in messages:
                cur.execute("""
                    INSERT OR IGNORE INTO messages (msg_id, channel_name,
                                                    channel_id, author_name, 
                                                    author_id, text, date, inserted_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    m.msg_id,
                    m.channel_name,
                    m.channel_id,
                    m.author_name,
                    m.author_id,
                    m.text,
                    m.date.isoformat() if m.date else None,
                    datetime.utcnow().isoformat()
                ))

        self.conn.commit()

    def save_summaries(self, summaries: dict[str, tuple]):
        """
        Save summary oper channel.
        deedpseek_req - a promt sent to deepseek
        """
        cur = self.conn.cursor()
        # dict keys are tuples (channel_name, channel_id)
        for (ch_name, ch_id), (req, summary) in summaries.items():
            cur.execute("""
                INSERT INTO summaries (channel_name, channel_id, deepseek_req,
                                       deepseek_summary, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (ch_name,
                  ch_id,
                  req,
                  summary, 
                  datetime.utcnow().isoformat()))
        self.conn.commit()
