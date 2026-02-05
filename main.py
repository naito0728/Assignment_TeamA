import tkinter as tk
from screens.top_screen import TopScreen

def show_screen(frame):
    frame.tkraise()

# メニュー画面
root = tk.Tk()
root.title("TOP画面")
root.geometry("800x600")

#top_frame = tk.Frame(root)
new_screen = tk.Frame(root)
list_screen = tk.Frame(root)
search_screen = tk.Frame(root)

# TopScreenクラスのインスタンスを作成してtop_frameに代入
top_frame = TopScreen(root, show_screen, new_screen, list_screen, search_screen)

for frame in (top_frame, new_screen, list_screen, search_screen):
    frame.place(relwidth=1, relheight=1)

# 新規画面表示
tk.Label(new_screen, text="新規登録画面", font=("Arial", 14)).pack(pady=20)
tk.Button(new_screen, text="TOPへ戻る", command=lambda: show_screen(top_frame)).pack()

# 一覧画面表示
tk.Label(list_screen, text="一覧表示画面", font=("Arial", 14)).pack(pady=20)
tk.Button(list_screen, text="TOPへ戻る", command=lambda: show_screen(top_frame)).pack()

# 検索画面表示
tk.Label(search_screen, text="検索画面", font=("Arial", 14)).pack(pady=20)
tk.Button(search_screen, text="TOPへ戻る", command=lambda: show_screen(top_frame)).pack()

# 初期画面表示
show_screen(top_frame)

root.mainloop()