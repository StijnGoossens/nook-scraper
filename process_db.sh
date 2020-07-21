#!/bin/bash

# The main script, to be run with './process_db.sh'.

# Stop the bash script when an error occurs
set -e

export PATH=$PATH:~/.android-sdk/platform-tools/
# The IP address migh change over time. Adapt it as needed.
adb connect 192.168.0.120:5555
adb shell <<EOF
mount -o remount,rw /dev/block/mmcblk0p5 /system
exit
EOF
adb pull /data/data/com.bn.nook.reader.activities/databases/

sqlite3 databases/annotations.db <<EOF
.mode csv
.headers on
.once annotations.csv
select ean, highlighttext, pagenumber, timestamp from annotations order by ean;
#.system open annotations.csv
EOF

sqlite3 databases/annotations.db <<EOF
.mode csv
.headers on
.once ean_codes.csv
select ean, max(_id) from annotations group by ean;
#.system open ean_codes.csv
EOF

python process_annotations.py
