# Bravo_day19_csv_example.py
import csv

people = [{"name": "Asha", "phone": "0711000001"}, {"name": "Brian", "phone": "0711000002"}]

# write csv
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "phone"])
    writer.writeheader()
    for p in people:
        writer.writerow(p)

        # read csv
        with open("people.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row["name"], "-", row["phone"])
                