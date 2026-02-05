import tkinter as tk

class TopScreen(tk.Frame):
    def __init__(self, master, show_screen_callback, new_screen, list_screen, search_screen):
        super().__init__(master)
        self.place(relwidth=1, relheight=1)
        self.show_screen = show_screen_callback
        self.new_screen = new_screen
        self.list_screen = list_screen
        self.search_screen = search_screen

        # タイトル
        tk.Label(self, text="引継ぎ・日報 管理アプリ", font=("Arial", 14)).pack(pady=20)

        # 新規登録ボタン
        new_Button = tk.Button(self, text="新規登録", width=50, height=5, command=lambda: self.show_screen(new_screen))
        new_Button.pack(pady=10)
        # 一覧表示ボタン
        list_Button = tk.Button(self, text="一覧表示", width=50, height=5, command=lambda: self.show_screen(list_screen))
        list_Button.pack(pady=10)
        # 検索ボタン
        serch_Button = tk.Button(self, text="検索", width=50, height=5, command=lambda: self.show_screen(search_screen))
        serch_Button.pack(pady=10)
