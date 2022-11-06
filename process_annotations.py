import os
from datetime import date

import pandas as pd

from config import MIN_ANNOTATION_ID

def process_db_export(filename: str):
    # Read the exported CSV files.
    annotations_df = pd.read_csv(f"{filename}.csv") # Has columns ean, highlighttext, pagenumber, timestamp
    ean_df = pd.read_csv("ean_codes.csv") # Has columns ean, max(_id)

    # Merge the two dataframes together.
    ean_df.columns = ["ean", "id"]
    df = annotations_df.merge(ean_df, on=["ean"])

    # Export the highlights for every book separatly.
    extract_folder = f"{filename}_{date.today().strftime('%Y%m%d')}"
    os.mkdir(extract_folder)
    for book_id in list(df["id"]):
        if book_id > MIN_ANNOTATION_ID:
            df[df.id == book_id].to_csv(os.path.join(extract_folder, f"{filename}_{book_id}.csv"))

process_db_export("annotations")
process_db_export("notes")