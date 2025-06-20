🛠 Tabula Installation Guide (2025 Edition)

---

✅ Step 1: Check if Java is Installed

● macOS/Linux:

```
java -version
```

→ If you see something like `Java version "1.8..."`, you're good to go. If not, download it from the official Java website.

---

✅ Step 2: Download Tabula

[Official Website](https://tabula.technology/)

Scroll to the middle of the page and click the "Download" button. Then choose:

● Linux: tabula.jar.zip

---

✅ Step 3: Launch Tabula

● macOS/Linux:

Unzip the downloaded file:

```
cd tabula
java -jar tabula.jar
```

→ This should open your browser and navigate to [http://127.0.0.1:8080](http://127.0.0.1:8080) automatically.

---

✅ Step 4: Import a PDF and Convert to CSV

Click \[Upload a File] and select `sangiin21_3_13.pdf`

Choose the page with the table (most likely page 1 or 2)

Drag and select the table area with your mouse

Choose "CSV" as the output format and click the "Export" button to download

💡Tabula works extremely well when the table rows and columns are clearly defined.

---

✅ Step 5: Clean Up and Save

The extracted CSV can be used directly in Excel or Python

If you encounter misaligned columns or garbled text, just re-save the file in UTF-8 format
