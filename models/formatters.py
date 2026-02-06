import json
from datetime import datetime
from tkinter import messagebox
from getrecord import fetch_by_id

# コピーしてSlack形式に整形してクリップボードに保存
def copy_to_slack(root, record_id):
    record = fetch_by_id(record_id)
    if not record:
        messagebox.showerror("エラー", "対象のデータが見つかりません")
        return

    try:
        meta = json.loads(record.get('meta_json', '{}'))
    except (json.JSONDecodeError, TypeError):
        meta = {}

    # typeカラムの値で判別
    rec_type = record.get('type')
    lines = []

    if rec_type == "standup":  # 日報
        raw_date = meta.get('date')
        if not raw_date:
            report_date = datetime.now().strftime('%Y-%m-%d')
        else:
            report_date = raw_date

        lines.extend([
            "*【日報】*",
            f"・日付: {report_date}",
            f"・昨日やったこと: {meta.get('done', 'なし')}",
            f"・今日やること: {meta.get('today', 'なし')}",
            f"・困りごと: {meta.get('blocker', 'なし')}",
            f"・チケット番号: {meta.get('ticket', 'なし')}"
        ])
    
    elif rec_type == "handover":  # 引継ぎ
        lines.extend([
            "*【引継ぎ】*",
            f"・タイトル: {record.get('title', 'なし')}",
            f"・背景: {meta.get('context', 'なし')}",
            f"・現状: {meta.get('current', 'なし')}",
            f"・次アクション: {meta.get('next', 'なし')}",
            f"・注意点: {meta.get('notes', 'なし')}",
            f"・参考リンク: {meta.get('links', 'なし')}"
        ])

    elif rec_type == "incident":  # 障害/問い合わせ
        lines.extend([
            "*【障害/問い合わせ報告】*",
            f"・現象: {meta.get('summary', 'なし')}",
            f"・影響範囲: {meta.get('impact', 'なし')}",
            f"・環境: {meta.get('env', 'なし')}",
            f"・再現手順: {meta.get('repro_steps', 'なし')}",
            f"・確認済みログ: {meta.get('logs_checked', 'なし')}",
            f"・仮説: {meta.get('hypothesis', 'なし')}"
        ])
    
    else:
        lines.append(f"*{rec_type}*\n{record.get('body', '内容なし')}")

    # 整形してコピー
    formatted_text = "\n".join(lines)
    root.clipboard_clear()
    root.clipboard_append(formatted_text)
    messagebox.showinfo("完了", f"Slack形式でコピーしました")

# コピーしてJira形式に整形してクリップボードに保存
def copy_to_jira(root, record_id):
    record = fetch_by_id(record_id)
    if not record:
        messagebox.showerror("エラー", "対象のデータが見つかりません")
        return

    try:
        meta = json.loads(record.get('meta_json', '{}'))
    except (json.JSONDecodeError, TypeError):
        meta = {}

    rec_type = record.get('type')
    lines = []

    if rec_type == "standup":
        raw_date = meta.get('date')
        report_date = raw_date if raw_date else datetime.now().strftime('%Y-%m-%d')
        lines.extend([
            "【日報】",
            f"・日付: {report_date}",
            f"・昨日やったこと: {meta.get('done', 'なし')}",
            f"・今日やること: {meta.get('today', 'なし')}",
            f"・困りごと: {meta.get('blocker', 'なし')}",
            f"・チケット番号: {meta.get('ticket', 'なし')}"
        ])

    elif rec_type == "handover":
        lines.extend([
            "【引継ぎ】",
            f"・タイトル: {record.get('title', 'なし')}",
            f"・背景: {meta.get('context', 'なし')}",
            f"・現状: {meta.get('current', 'なし')}",
            f"・次アクション: {meta.get('next', 'なし')}",
            f"・注意点: {meta.get('notes', 'なし')}",
            f"・参考リンク: {meta.get('links', 'なし')}"
        ])

    elif rec_type == "incident":
        lines.extend([
            "【障害/問い合わせ報告】",
            f"・現象: {meta.get('summary', 'なし')}",
            f"・影響範囲: {meta.get('impact', 'なし')}",
            f"・環境: {meta.get('env', 'なし')}",
            f"・再現手順: {meta.get('repro_steps', 'なし')}",
            f"・確認済みログ: {meta.get('logs_checked', 'なし')}",
            f"・仮説: {meta.get('hypothesis', 'なし')}"
        ])

    else:
        lines.append(f"{rec_type}")
        lines.append(record.get('body', '内容なし'))

    formatted_text = "\n".join(lines)
    root.clipboard_clear()
    root.clipboard_append(formatted_text)
    messagebox.showinfo("完了", "Jira形式（プレーンテキスト）でコピーしました")

# コピーしてNotion形式に整形してクリップボードに保存
def copy_to_notion(root, record_id):
    record = fetch_by_id(record_id)
    if not record:
        messagebox.showerror("エラー", "対象のデータが見つかりません")
        return

    try:
        meta = json.loads(record.get('meta_json', '{}'))
    except (json.JSONDecodeError, TypeError):
        meta = {}

    rec_type = record.get('type')
    lines = []

    if rec_type == "standup":
        raw_date = meta.get('date')
        report_date = raw_date if raw_date else datetime.now().strftime('%Y-%m-%d')
        lines.append("### 🗓️ 日報") #Notionは絵文字と親和性が高いので絵文字付与
        lines.extend([
            f"- **日付:** {report_date}",
            f"- **昨日やったこと:** {meta.get('done', 'なし')}",
            f"- **今日やること:** {meta.get('today', 'なし')}",
            f"- **困りごと:** {meta.get('blocker', 'なし')}",
            f"- **チケット番号:** {meta.get('ticket', 'なし')}"
        ])

    elif rec_type == "handover":
        lines.append("### 引継ぎ")
        lines.extend([
            f"- **タイトル:** {record.get('title', 'なし')}",
            f"- **背景:** {meta.get('context', 'なし')}",
            f"- **現状:** {meta.get('current', 'なし')}",
            f"- **次アクション:** {meta.get('next', 'なし')}",
            f"- **注意点:** {meta.get('notes', 'なし')}",
            f"- **参考リンク:** {meta.get('links', 'なし')}"
        ])

    elif rec_type == "incident":
        lines.append("### 障害/問い合わせ報告")
        lines.extend([
            f"- **現象:** {meta.get('summary', 'なし')}",
            f"- **影響範囲:** {meta.get('impact', 'なし')}",
            f"- **環境:** {meta.get('env', 'なし')}",
            f"- **再現手順:** {meta.get('repro_steps', 'なし')}",
            f"- **確認済みログ:** {meta.get('logs_checked', 'なし')}",
            f"- **仮説:** {meta.get('hypothesis', 'なし')}"
        ])

    else:
        lines.append(f"### {rec_type}")
        lines.append(record.get('body', '内容なし'))

    formatted_text = "\n".join(lines)
    root.clipboard_clear()
    root.clipboard_append(formatted_text)
    messagebox.showinfo("完了", "Notion形式でコピーしました")
