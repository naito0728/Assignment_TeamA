import tkinter as tk
from tkinter import messagebox,scrolledtext
import sys
import os
from models.getrecord import get_connection, fetch_by_id
import pymysql
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DetailScreen(tk.Frame):
    def __init__(self, master, show_screen_callback, top_frame):
        super().__init__(master, bg="#FFFDD0")
        self.show_screen = show_screen_callback
        self.top_frame = top_frame

        top_frame_label = tk.Frame(self, bg="#FFFDD0")
        top_frame_label.pack(pady=20)
        tk.Label(top_frame_label, text="詳細画面：", font=("Arial", 14), bg="#FFFDD0").pack(side="left")
        self.type_label = tk.Label(top_frame_label, text="", font=("Arial", 14, "bold"), bg="#FFFDD0")
        self.type_label.pack(side="left", padx=10)

        # ScrolledTextで枠付きテキスト表示
        self.detail_text = scrolledtext.ScrolledText(
            self,
            font=("Arial", 12),
            width=80,
            height=20,
            wrap="word",
            bg="white",
            relief="solid",
            borderwidth=1
        )
        self.detail_text.pack(padx=20, pady=10, fill="both", expand=True)
        self.detail_text.configure(state="disabled")  # 編集不可

        # 戻るボタン
        tk.Button(self, text="TOPへ戻る", command=lambda: self.show_screen(self.top_frame)).pack(pady=10)

    def load_record(self, record_id):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='0728',
            database='app_assiggnment',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM records WHERE id=%s", (record_id,))
            record = cursor.fetchone()

        if not record:
            self.type_label.config(text="")
            self.detail_text.configure(state="normal")
            self.detail_text.delete("1.0", tk.END)
            self.detail_text.insert(tk.END, "該当レコードが存在しません")
            self.detail_text.configure(state="disabled")
            return

        self.type_label.config(text=record['record_type'])

        meta_json_str = record.get('meta_json', "")
        display_text = ""
        if meta_json_str:
            try:
                meta_dict = json.loads(meta_json_str)  # JSON文字列 → Python辞書
                # 辞書の内容を改行で表示
                for key, value in meta_dict.items():
                    display_text += f"{key}: {value}\n"
            except json.JSONDecodeError:
                display_text = meta_json_str  # 辞書でなければ文字列そのまま表示

        # 表示
        self.detail_text.configure(state="normal")
        self.detail_text.delete("1.0", tk.END)
        self.detail_text.insert(tk.END, display_text)
        self.detail_text.configure(state="disabled")