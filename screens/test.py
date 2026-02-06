import tkinter as tk
from tkinter import messagebox,scrolledtext
import sys
import os
from list_screan import listscreandetail

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.getrecord import get_connection, fetch_by_id


def test(root):
    

    record = fetch_by_id(3)

    a = tk.Button(text="aaa", command=lambda: listscreandetail(root,record,change))

    a.pack()

    root.mainloop()


def change(root):
    test(root)

root = tk.Tk()
test(root)