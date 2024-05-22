# Nook annotations scraper

## Prerequisites
* The Nook Simple Touch should have been rooted, e.g. by following the following [Lifehacker tutorial](https://lifehacker.com/turn-a-99-nook-into-a-fully-fledged-android-tablet-in-5889158). It should have an app called `adbWireless` installed (this is included when you root with `TouchNooter`).
* On the computer you should have the following installed:
	* `adb` For MacOS, you can install this with brew: `brew install android-platform-tools` ([source](https://stackoverflow.com/questions/17901692/set-up-adb-on-mac-os-x)).
	* `sqlite3`
	* `python` and `pandas`

## Extracting the highlights
1) Start on the Nook the app `adbWireless` and make sure the Nook and computer are both on the same WiFi network.
2) If needed change the IP adress in the `process_db.sh` script to match the address shown on the Nook.
3) Run the `process_db.sh` script.

## Output
The script will extract the databases from the Nook and use `annotations.db` to extract the highlights per book. It will create an `extract_yyyymmdd` folder with a CSV file per book. In `min_annotation_id.py` you can set the lowest id to consider. This filter is applied on a book level and not on an individual annotation level. The id of a book is the id of the latest annotation of that book.

## Copy highlights to OneNote
1) Run the `highlights_to_clipboard.py` script. This will copy the highlights to the clipboard. E.g. `/Users/stijngoossens/.pyenv/versions/3.9.7/bin/python /Users/stijngoossens/Documents/personal/nook-scraper/highlights_to_clipboard.py annotations_20240302/annotations_5007.csv`
2) Paste the highlights from the clipboard into an empty Excel sheet.
3) Copy the resulting table from Excel and paste it into a new page in OneNote.
