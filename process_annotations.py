import pandas as pd
from datetime import date
import os

from min_annotation_id import min_annotation_id

today = date.today().strftime("%Y%m%d")
os.mkdir(f"extract_{today}")

annotations_df = pd.DataFrame.from_csv("annotations.csv")
ean_df = pd.DataFrame.from_csv("ean_codes.csv")
ean_df.columns = ["id"]

df = annotations_df.join(ean_df)

for book_id in list(df["id"]):
    if book_id > min_annotation_id:
        df[df.id == book_id].to_csv(f"extract_{today}/annotations_{book_id}.csv")
