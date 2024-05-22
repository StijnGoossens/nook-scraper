"""Read annotations CSV file and copy it's content to the clipboard."""

import sys

import pandas as pd

try:
    filename = sys.argv[1]
except IndexError:
    print("You should pass the relative path of an annotations or notes CSV as a parameter, e.g. annotations_20240302/annotations_5007.csv")
    exit()

def csv_to_df(filename):
    return pd.read_csv(filename)


df_annotations = csv_to_df(filename)
try:
    df_notes = csv_to_df(filename.replace("annotations", "notes"))
except FileNotFoundError:
    df_notes = pd.DataFrame(columns=["highlighttext", "pagenumber", "timestamp", "note"])
    print("Notes file not found. Only annotations will be copied.")
df = pd.concat([df_annotations, df_notes], ignore_index=True)
df = df.sort_values(by=["pagenumber", "timestamp"])
# Drop duplicates and keep the row with the note
df = df.drop_duplicates(subset=["highlighttext", "pagenumber", "timestamp"], keep="last")
df = df.reset_index(drop=True)
cols = ["highlighttext", "pagenumber", "timestamp"]
if "note" in df.columns:
    cols.append("note")
df[cols].to_clipboard(index=False, excel=True, sep="\t")
df[cols].to_csv("highlights.csv", index=False, sep=";")
print("Book name:", df["ean"].iloc[0].split("/")[-1].replace(".epub", ""))
print(f"{len(df)} highlights were copied to clipboard.")
