README: Reversible Prefecture Analysis Script

This script is a Python tool that extracts electoral districts where a seat could have been reversed within a 1% vote margin, using CSV data from Japan's House of Councillors elections.

🧩 Overview

The script loads election data in CSV format (e.g., extracted from PDF using Tabula), and performs the following steps:

Extracts candidate election results for each prefecture

Extracts the "1% threshold" vote count per prefecture

Calculates vote margin between winners and losers

Outputs prefectures where the vote gap is under the 1% threshold

📁 File Structure

```
project_root/
├── input/
│   └── tabula-sangiin2010_07_11.csv  # Input data (CSV)
├── analyze_votes.py                  # Main script
└── README.md                         # This file
```

🔧 Requirements

Python 3.x

pandas

pip install pandas

🚀 How to Run

python analyze_votes.py

📝 Script Logic

Step 1: Read CSV File

df = pd.read_csv("./input/tabula-sangiin2010_07_11.csv", encoding="utf-8", skip_blank_lines=False)

Step 2: Extract Prefecture and 1% Threshold Votes

If a row contains "（定数...）", it marks a new prefecture. The last number in the row is extracted as the 1% threshold.

Step 3: Candidate Data Processing

Rows labeled with "当" (elected) or "落" (not elected) are extracted and linked to their corresponding prefecture.

Vote counts are converted to numeric.

Step 4: Identify Reversible Prefectures

For each prefecture:

Compare the lowest vote-getting winner and highest vote-getting loser

If the vote gap is less than the 1% threshold, consider it potentially reversible and record it

Step 5: Output Results

Results are printed to standard output

Optionally, save to CSV (commented out by default)

# df_result.to_csv("reversible_prefectures.csv", index=False, encoding="utf-8-sig")

📊 Sample Output

   Prefecture  Bottom Winner  Votes (Winner)  Top Loser  Votes (Loser)  Vote Gap  1% Threshold
0     Example        Yamada Taro        12458     Suzuki Hanako      12310      148       200

📌 Notes

You may need to adapt the script depending on the CSV file format.

The 1% threshold must be explicitly present in the data.

©️ Disclaimer

Use this script at your own risk and in accordance with the terms of the original data source.

Feel free to submit questions or suggestions!

