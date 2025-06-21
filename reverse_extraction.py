import pandas as pd

# ステップ1: CSV読み込み
df = pd.read_csv("yourfile.csv", encoding="utf-8", skip_blank_lines=False)

# ステップ2: 都道府県ごとに候補者をマーク
pref = None
rows = []

for _, row in df.iterrows():
    if isinstance(row[0], str) and "（定数" in row[0]:
        pref = row[0].split("（")[0].strip()
        continue
    if pd.notna(row[0]) and row[0] in ["当", "落"]:
        row_data = row.copy()
        row_data["都道府県"] = pref
        rows.append(row_data)

df_cleaned = pd.DataFrame(rows)

# ステップ3: 数値整形
df_cleaned["投票数"] = df_cleaned["投票数"].astype(str).str.replace(",", "").astype(float)
df_cleaned["有権者数の1%の人数（四捨五入）"] = pd.to_numeric(
    df_cleaned["有権者数の1%の人数（四捨五入）"], errors="coerce"
)

# ステップ4: 逆転可能な都道府県の抽出
results = []

for pref, group in df_cleaned.groupby("都道府県"):
    winners = group[group["当落"] == "当"].sort_values("投票数")
    losers = group[group["当落"] == "落"].sort_values("投票数", ascending=False)

    if len(winners) == 0 or len(losers) == 0:
        continue  # データ不足

    bottom_winner = winners.iloc[0]
    top_loser = losers.iloc[0]

    try:
        vote_gap = bottom_winner["投票数"] - top_loser["投票数"]
        threshold = bottom_winner["有権者数の1%の人数（四捨五入）"]

        if pd.notna(threshold) and vote_gap < threshold:
            results.append({
                "都道府県": pref,
                "最下位当選者": bottom_winner["候補者氏名"],
                "得票": int(bottom_winner["投票数"]),
                "最高位落選者": top_loser["候補者氏名"],
                "得票": int(top_loser["投票数"]),
                "差": int(vote_gap),
                "1%基準": int(threshold)
            })
    except Exception as e:
        print(f"{pref}でエラー: {e}")

# ステップ5: 結果出力
df_result = pd.DataFrame(results)
print(df_result)
df_result.to_csv("逆転可能な都道府県一覧.csv", index=False, encoding="utf-8-sig")
