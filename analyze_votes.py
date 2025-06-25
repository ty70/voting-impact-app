import pandas as pd
import re

columns = ['当落',	'候補者氏名',	'党派', 
           '新前元別', '性別', '年齢', '職業',
            '投票数',	'有権者数の1%の人数（四捨五入）']

# ステップ1: CSV読み込み
df = pd.read_csv("./input/tabula-sangiin2016_07_10.csv", encoding="utf-8", skip_blank_lines=False, names=columns)
# df = pd.read_csv("./input/tabula-sangiin2013_07_21.csv", encoding="utf-8", skip_blank_lines=False)
# df = pd.read_csv("./input/tabula-sangiin2010_07_11.csv", encoding="utf-8", skip_blank_lines=False)
# df = pd.read_csv("./input/tabula-sangiin2007_07_29.csv", encoding="utf-8", skip_blank_lines=False)
# ステップ2: 都道府県ごとに候補者をマーク
pref = None
rows = []

todouhuken = []
one_percent = []
# rows = []

for _, row in df.iterrows():
    if isinstance(row[0], str) and "（定数" in row[0]:
        pref = row[0].split("（")[0].strip()
        # 行全体を文字列に連結して末尾の数字を抽出
        row_text = ",".join(row.astype(str).tolist())
        match = re.search(r"(\d{4,})$", row_text)
        percent1 = int(match.group(1)) if match else None
        print(f"pref: {pref}, 1%: {percent1}")
        todouhuken.append(pref)
        one_percent.append(percent1)
        continue
    if pd.notna(row[0]) and row[0] in ["当", "落"]:
        row_data = row.copy()
        row_data["都道府県"] = pref
        rows.append(row_data)

df_cleaned = pd.DataFrame(rows)

to2per = dict(zip(todouhuken, one_percent))

# ステップ3: 数値整形（有効なら）
df_cleaned["投票数"] = df_cleaned["投票数"].astype(str).str.replace(",", "").astype(float)
# )

# ステップ4: 逆転可能な都道府県の抽出
results = []

for key, group in df_cleaned.groupby("都道府県"):
    winners = group[group["当落"] == "当"].sort_values("投票数")
    losers = group[group["当落"] == "落"].sort_values("投票数", ascending=False)

    if len(winners) == 0 or len(losers) == 0:
        continue

    bottom_winner = winners.iloc[0]
    top_loser = losers.iloc[0]

    try:
        vote_gap = bottom_winner["投票数"] - top_loser["投票数"]
        threshold = to2per.get(key)

        if pd.notna(threshold) and vote_gap > 0 and vote_gap < threshold:
            results.append({
                "都道府県": key,
                "最下位当選者": bottom_winner["候補者氏名"],
                "得票（当選）": int(bottom_winner["投票数"]),
                "最高位落選者": top_loser["候補者氏名"],
                "得票（落選）": int(top_loser["投票数"]),
                "票差": int(vote_gap),
                "1%基準": int(threshold)
            })
    except Exception as e:
        print(f"{key}でエラー: {e}")

# ステップ5: 結果出力
df_result = pd.DataFrame(results)
print(df_result)
# df_result.to_csv("逆転可能な都道府県一覧.csv", index=False, encoding="utf-8-sig")
