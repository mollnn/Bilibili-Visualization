source /etc/profile

hive -e "create database if not exists himp; create database if not exists hmain;"

hive -e "drop table if exists himp.Vinfo; \
        drop table if exists himp.VReply; \
        drop table if exists himp.Danmu; \
        drop table if exists himp.dmwfreq  "

sqoop import "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
    --connect jdbc:mysql://localhost:3306/bilibili \
    --driver com.mysql.jdbc.Driver \
    --table Vinfo \
    --username root \
    --password 123456 \
    --hive-import \
    --hive-overwrite \
    --hive-drop-import-delims \
    --fields-terminated-by '\001' \
    --create-hive-table \
    --hive-database himp \
    --hive-table Vinfo \
    --delete-target-dir \

echo
echo
echo IMPORTING... 1/4 FINISH
echo
echo

sqoop import "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
    --connect jdbc:mysql://localhost:3306/bilibili \
    --driver com.mysql.jdbc.Driver \
    --table VReply \
    --username root \
    --password 123456 \
    --hive-import \
    --hive-overwrite \
    --hive-drop-import-delims \
    --fields-terminated-by '\001' \
    --create-hive-table \
    --hive-database himp \
    --hive-table VReply \
    --delete-target-dir \


echo
echo
echo IMPORTING... 2/4 FINISH
echo
echo

sqoop import "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
    --connect jdbc:mysql://localhost:3306/bilibili \
    --driver com.mysql.jdbc.Driver \
    --table Danmu \
    --username root \
    --password 123456 \
    --hive-import \
    --hive-overwrite \
    --hive-drop-import-delims \
    --fields-terminated-by '\001' \
    --create-hive-table \
    --hive-database himp \
    --hive-table Danmu \
    --delete-target-dir \

echo
echo
echo IMPORTING... 3/4 FINISH
echo
echo

sqoop import "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
    --connect jdbc:mysql://localhost:3306/bilibili \
    --driver com.mysql.jdbc.Driver \
    --table dmwfreq \
    --username root \
    --password 123456 \
    --hive-import \
    --hive-overwrite \
    --hive-drop-import-delims \
    --fields-terminated-by '\001' \
    --create-hive-table \
    --hive-database himp \
    --hive-table dmwfreq \
    --delete-target-dir \

echo
echo
echo IMPORT FINISH, INSERTING...
echo
echo

hive -e "create table if not exists hmain.Vinfo row format delimited fields terminated by '\001' as select * from himp.Vinfo where bvid='';"
hive -e "insert into hmain.Vinfo select distinct * from himp.Vinfo;"


echo
echo
echo INSERTING... 1/4 FINISH
echo
echo

hive -e "create table if not exists hmain.VReply row format delimited fields terminated by '\001' as select * from himp.VReply where rpid='';"
hive -e "insert into hmain.VReply select distinct * from himp.VReply;"


echo
echo
echo INSERTING... 2/4 FINISH
echo
echo

hive -e "create table if not exists hmain.Danmu row format delimited fields terminated by '\001' as select * from himp.Danmu where cid='';"
hive -e "insert into hmain.Danmu select distinct * from himp.Danmu;"


echo
echo
echo INSERTING... 3/4 FINISH
echo
echo

hive -e "create table if not exists hmain.dmwfreq row format delimited fields terminated by '\001' as select * from himp.dmwfreq where bvid='';"
hive -e "insert into hmain.dmwfreq select distinct * from himp.dmwfreq;"


echo
echo
echo FINISH import.sh
echo
echo