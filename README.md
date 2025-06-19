🛠 Tabula 導入ガイド（2025年版）

✅ Step 1：Javaがインストールされているか確認

● macOS/Linux:
```
java -version
```
→ Java version "1.8..." などと出ればOK。出なければJava公式サイトからダウンロードしてください。

✅ Step 2：Tabulaをダウンロード

[公式サイト](https://tabula.technology/)

ページ中段の「Download」ボタンから、以下を選択：

● Linux: tabula.jar.zip

✅ Step 3：Tabulaを起動

● macOS/Linux:

ZIPを展開

```
cd tabula
java -jar tabula.jar
```

→ ブラウザが開いて、http://127.0.0.1:8080 にアクセスされるはず。

✅ Step 4：PDFを読み込んでCSVに変換

[ファイルをアップロード] → sangiin21_3_13.pdf を選択

表があるページを選ぶ（たぶん1ページ目か2ページ目）

表の範囲をマウスでドラッグ選択

抽出形式は「CSV」を選んで「Export」ボタンでダウンロード

💡Tabulaは表の行・列が明確な場合の精度が抜群に高いです。

✅ Step 5：整形と保存

抽出されたCSVはExcelやPythonでそのまま使えます

列ズレや文字化けがあればUTF-8で再保存すればOK

