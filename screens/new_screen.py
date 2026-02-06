import tkinter as tk
from tkinter import messagebox,scrolledtext

def selType(event=None):
	print("hoge")

# TOP画面から呼び出せる用フレーム化　澁谷 2026/02/05 Start
class NewScreen(tk.Frame):
	def __init__(self, master, show_screen_callback, top_frame):
		super().__init__(master)
		self.show_screen = show_screen_callback
		self.top_frame = top_frame
		
		tk.Label(self, text="新規登録画面", font=("Arial", 14)).pack(pady=20)
		tk.Button(self, text="TOPへ戻る", command=lambda: self.show_screen(self.top_frame)).pack(pady=10)
# TOP画面から呼び出せる用フレーム化　澁谷 2026/02/05 End

		# GUI作成
		#root = tk.Tk()
		#root.title("新規登録")
		#root.geometry("600x400")
		#root.configure(bg="lightblue")
		canvas = tk.Canvas(self)
		frame = tk.Frame(canvas)
		scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
		canvas.configure(yscrollcommand=scrollbar.set)
		scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		# FrameをCanvasに埋め込む
		win = canvas.create_window((0, 0), window=frame, anchor="nw")
		
		# マウスホイールでスクロール 澁谷 2026/02/06 Start
		def _on_mousewheel(event):
			canvas.yview_scroll(-1 * int(event.delta / 120), "units")
		canvas.bind_all("<MouseWheel>", _on_mousewheel)
		# マウスホイールでスクロール 澁谷 2026/02/06 End
	
		# 動的なサイズ調整
		def on_frame_configure(event):
			canvas.configure(scrollregion=canvas.bbox("all"))

		def on_canvas_configure(event):
			canvas.itemconfigure(win, width=event.width)

		frame.bind("<Configure>", on_frame_configure)
		canvas.bind("<Configure>", on_canvas_configure)

		#####共通#####
		#選択
		frame_top = tk.Frame(frame, pady=5)
		var = tk.StringVar(value="1")  # 初期値を設定
		tk.Label(frame_top, text="種類:").pack(pady=5)
		radiobutton1 = tk.Radiobutton(frame_top,text="日報", variable=var, value="1")
		radiobutton2 = tk.Radiobutton(frame_top,text="引継ぎ", variable=var, value="2")
		radiobutton3 = tk.Radiobutton(frame_top,text="障害/問合せ", variable=var, value="3")

		# ラジオボタンをウィンドウに配置
		radiobutton1.pack(side=tk.LEFT)
		radiobutton2.pack(side=tk.LEFT)
		radiobutton3.pack(side=tk.LEFT)
		frame_top.pack(fill=tk.X,anchor=tk.CENTER)

		#####日報#####
		frame_standup = tk.Frame(frame, pady=5)
		tk.Label(frame_standup, text="日付:").pack(pady=5)
		date_entry = tk.Entry(frame_standup, width=50)
		date_entry.pack(pady=5)
		tk.Label(frame_standup, text="昨日やったこと:").pack(pady=5)
		done_entry = scrolledtext.ScrolledText(frame_standup, width=50, height=5)
		done_entry.pack(pady=5)
		tk.Label(frame_standup, text="今日やったこと:").pack(pady=5)
		today_entry = scrolledtext.ScrolledText(frame_standup, width=50, height=5)
		today_entry.pack(pady=5)
		tk.Label(frame_standup, text="困っていること:").pack(pady=5)
		blocker_entry = scrolledtext.ScrolledText(frame_standup, width=50, height=5)
		blocker_entry.pack(pady=5)
		tk.Label(frame_standup, text="チケット番号:").pack(pady=5)
		ticket_entry = scrolledtext.ScrolledText(frame_standup, width=50, height=5)
		ticket_entry.pack(pady=5)
		frame_standup.pack(fill=tk.X,anchor=tk.CENTER)

		#####引継ぎ#####
		frame_handover = tk.Frame(frame, pady=5)
		tk.Label(frame_handover, text="タイトル:").pack(pady=5)
		title_entry = tk.Entry(frame_handover, width=50)
		title_entry.pack(pady=5)
		tk.Label(frame_handover, text="背景:").pack(pady=5)
		context_entry = scrolledtext.ScrolledText(frame_handover, width=50, height=5)
		context_entry.pack(pady=5)
		tk.Label(frame_handover, text="現状:").pack(pady=5)
		current_entry = scrolledtext.ScrolledText(frame_handover, width=50, height=5)
		current_entry.pack(pady=5)
		tk.Label(frame_handover, text="次アクション:").pack(pady=5)
		next_entry = scrolledtext.ScrolledText(frame_handover, width=50, height=5)
		next_entry.pack(pady=5)
		tk.Label(frame_handover, text="注意点:").pack(pady=5)
		notes_entry = scrolledtext.ScrolledText(frame_handover, width=50, height=5)
		notes_entry.pack(pady=5)
		tk.Label(frame_handover, text="参考リンク:").pack(pady=5)
		link_entry = scrolledtext.ScrolledText(frame_handover, width=50, height=5)
		link_entry.pack(pady=5)
		frame_handover.pack(fill=tk.X,anchor=tk.CENTER)



		#####障害/問合せ#####
		frame_incident = tk.Frame(frame, pady=5)
		tk.Label(frame_incident, text="現象:").pack(pady=5)
		summary_entry = tk.Entry(frame_incident, width=50)
		summary_entry.pack(pady=5)
		tk.Label(frame_incident, text="影響範囲:").pack(pady=5)
		impact_entry = scrolledtext.ScrolledText(frame_incident, width=50, height=5)
		impact_entry.pack(pady=5)
		tk.Label(frame_incident, text="環境:").pack(pady=5)
		env_entry = scrolledtext.ScrolledText(frame_incident, width=50, height=5)
		env_entry.pack(pady=5)
		tk.Label(frame_incident, text="再現手順:").pack(pady=5)
		repro_entry = scrolledtext.ScrolledText(frame_incident, width=50, height=5)
		repro_entry.pack(pady=5)
		tk.Label(frame_incident, text="確認済みログ:").pack(pady=5)
		chkedlog_entry = scrolledtext.ScrolledText(frame_incident, width=50, height=5)
		chkedlog_entry.pack(pady=5)
		tk.Label(frame_incident, text="仮設:").pack(pady=5)
		hypo_entry = scrolledtext.ScrolledText(frame_incident, width=50, height=5)
		hypo_entry.pack(pady=5)
		frame_incident.pack(fill=tk.X,anchor=tk.CENTER)


#root.mainloop()