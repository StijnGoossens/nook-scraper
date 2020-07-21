# Nook annotations scraper

1) Start on the Nook the app 'adbWireless' and make sure the Nook and computer are both on the same network.
2) If needed change the IP adress in the 'process_db.sh' script to match the address shown on the Nook.
3) Run the 'process_db.sh' script.

The script will extract the databases from the Nook and use 'annotations.db' to extract the highlights per book. It will create an 'extract_yyyymmdd' folder with a CSV file per book. In 'min_annotation_id.py' you can set the lowest id to consider. This filter is applied on a book level and not on an individual annotation level. The id of a book is the id of the latest annotation of that book.
