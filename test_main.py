import sys
import os
import tkinter as tk

# modelsフォルダ「そのもの」を検索パスに追加する
current_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(current_dir, 'models')
sys.path.append(models_dir)

from models.formatters import copy_to_slack, copy_to_jira, copy_to_notion

def main():
    root = tk.Tk()
    root.title("コピーテスト")
    root.geometry("400x420")

    tk.Label(root, text="コピーしたいレコードIDを入力:", pady=10).pack()
    
    entry_id = tk.Entry(root)
    entry_id.insert(0, "1")
    entry_id.pack(pady=5)

    # Slackボタン
    tk.Button(
        root, text="Slack形式でコピー", bg="#4A154B", fg="white", width=25,
        command=lambda: copy_to_slack(root, entry_id.get())
    ).pack(pady=10)

    # Jiraボタン
    tk.Button(
        root, text="Jira形式でコピー", bg="#0052CC", fg="white", width=25,
        command=lambda: copy_to_jira(root, entry_id.get())
    ).pack(pady=10)

    # Notionボタン
    tk.Button(
        root, text="Notion形式でコピー", bg="#000000", fg="white", width=25,
        command=lambda: copy_to_notion(root, entry_id.get())
    ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()