import os
from datetime import date

import pandas as pd

from config import MIN_ANNOTATION_ID

# Read the exported CSV files.
annotations_df = pd.read_csv("annotations.csv") # Has columns ean, highlighttext, pagenumber, timestamp
ean_df = pd.read_csv("ean_codes.csv") # Has columns ean, max(_id)

# Merge the two dataframes together.
ean_df.columns = ["ean", "id"]
df = annotations_df.merge(ean_df, on=["ean"])

# Export the highlights for every book separatly.
extract_folder = f"extract_{date.today().strftime('%Y%m%d')}"
os.mkdir(extract_folder)
for book_id in list(df["id"]):
    if book_id > MIN_ANNOTATION_ID:
        df[df.id == book_id].to_csv(os.path.join(extract_folder, f"annotations_{book_id}.csv"))
