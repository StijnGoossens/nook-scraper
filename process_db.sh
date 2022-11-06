#!/bin/bash

# The main script, to be run with './process_db.sh'.

# Stop the bash script when an error occurs
set -e

export PATH=$PATH:~/.android-sdk/platform-tools/
# The IP address migh change over time. Adapt it as needed.
adb connect 192.168.0.176:5555
adb shell <<EOF
mount -o remount,rw /dev/block/mmcblk0p5 /system
exit
EOF
adb pull /data/data/com.bn.nook.reader.activities/databases/

# Export the annotations to CSV with sqlite
sqlite3 databases/annotations.db <<EOF
.mode csv
.headers on
.once annotations.csv
select ean, highlighttext, pagenumber, timestamp from annotations order by ean;
#.system open annotations.csv
EOF

# Export notes to CSV.
sqlite3 databases/annotations.db <<EOF
.mode csv
.headers on
.once notes.csv
select ean, highlighttext, note, pagenumber, timestamp from annotations where note is not null order by ean;
#.system open notes.csv
EOF

# Export the latest id for every ean code to CSV with sqlite
sqlite3 databases/annotations.db <<EOF
.mode csv
.headers on
.once ean_codes.csv
select ean, max(_id) from annotations group by ean;
#.system open ean_codes.csv
EOF

# Process the exported data into CSV's with the annotations per book
python process_annotations.py
