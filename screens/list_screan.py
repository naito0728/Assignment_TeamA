import tkinter as tk
from tkinter import messagebox,scrolledtext
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.getrecord import get_connection, fetch_by_id
import json

def listscreandetail(root,record,change):
	# GUI作成
	for widget in root.winfo_children():
		widget.destroy()

	root.title("詳細画面")

	#スクロールバーによる画面崩れを起こさないため
	canvas = tk.Canvas(root)
	frame = tk.Frame(canvas)
	scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
	canvas.configure(yscrollcommand=scrollbar.set)
	scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
	canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
	# FrameをCanvasに埋め込む
	win = canvas.create_window((0, 0), window=frame, anchor="nw")
	# 動的なサイズ調整
	def on_frame_configure(event):
		canvas.configure(scrollregion=canvas.bbox("all"))

	def on_canvas_configure(event):
		canvas.itemconfigure(win, width=event.width)

	frame.bind("<Configure>", on_frame_configure)
	canvas.bind("<Configure>", on_canvas_configure)


	frame_top = tk.Frame(frame, pady=5)
	var = tk.StringVar(value="1")  # 初期値を設定
	tk.Label(frame_top, text=f"詳細:{record['title']}", font=("", 16,"bold")).pack(pady=20)

	backbutton = tk.Button(frame_top,text="一覧に戻る",command=lambda: list_screan(root,change))

	backbutton.pack()
	frame_top.pack(fill=tk.X,anchor=tk.CENTER)

	frame_main = tk.Frame(frame, width=200 , height=300,pady=5,bg="lightblue")

	meta = json.loads(record['meta_json'])

	
	if record:
    	# 種類ラベルの隣にDBから取った値を表示するイメージ
		for key,value in meta.items():
			tk.Label(frame_main, text=f"{key}: {value}",font=("", 12),anchor="w").pack(fill='x',pady=3)

	frame_main.pack(anchor=tk.CENTER)

	root.mainloop()


#テスト用　後ほど一覧画面と共有
def list_screan(root,change):
	for widget in root.winfo_children():
		widget.destroy()

	change(root)