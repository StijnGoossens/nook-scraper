"""Read annotations CSV file and copy it's content to the clipboard."""

import sys
import pandas as pd

try:
    filename = sys.argv[1]
except IndexError:
    print("You should pass the relative path of an annotations CSV as a parameter, e.g. extract_20221027/annotations_4698.csv")
    exit()

df = pd.read_csv(filename)
df[["highlighttext", "pagenumber", "timestamp"]].to_clipboard(index=False)

print("Book name:", df["ean"].iloc[0].split("/")[-1].replace(".epub", ""))
print(f"{len(df)-1} highlights were copied to clipboard.")
