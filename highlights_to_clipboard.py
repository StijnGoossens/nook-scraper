"""Read annotations CSV file and copy it's content to the clipboard."""

import sys
import pandas as pd

try:
    filename = sys.argv[1]
except IndexError:
    print("You should pass the relative path of an annotations or notes CSV as a parameter, e.g. annotations_20221027/annotations_4698.csv")
    exit()

df = pd.read_csv(filename)
cols = ["highlighttext", "pagenumber", "timestamp"]
if "note" in df.columns:
    cols.append("note")
df[cols].to_clipboard(index=False)

print("Book name:", df["ean"].iloc[0].split("/")[-1].replace(".epub", ""))
print(f"{len(df)} highlights were copied to clipboard.")
