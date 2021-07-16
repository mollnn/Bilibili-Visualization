source /etc/profile

echo "EXPORTING 0%"

mysql -uroot -p123456 -e "drop table if exists biliview.oviewdistrib; create table biliview.oviewdistrib(val bigint, cnt bigint, PRIMARY KEY (val) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table oviewdistrib \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/oviewdistrib \
 --m 8


echo "EXPORTING 10%"

mysql -uroot -p123456 -e "drop table if exists biliview.odurationdistrib; create table biliview.odurationdistrib(val bigint, cnt bigint, PRIMARY KEY (val) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table odurationdistrib \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/odurationdistrib \
 --m 8


echo "EXPORTING 20%"

mysql -uroot -p123456 -e "drop table if exists biliview.oreplydistrib; create table biliview.oreplydistrib(val bigint, cnt bigint, PRIMARY KEY (val) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table oreplydistrib \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/oreplydistrib \
 --m 8


echo "EXPORTING 30%"

mysql -uroot -p123456 -e "drop table if exists biliview.ofavoritedistrib; create table biliview.ofavoritedistrib(val bigint, cnt bigint, PRIMARY KEY (val) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table ofavoritedistrib \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/ofavoritedistrib \
 --m 8


echo "EXPORTING 40%"

mysql -uroot -p123456 -e "drop table if exists biliview.olikesdistrib; create table biliview.olikesdistrib(val bigint, cnt bigint, PRIMARY KEY (val) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table olikesdistrib \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/olikesdistrib \
 --m 8


echo "EXPORTING 50%"

mysql -uroot -p123456 -e "drop table if exists biliview.ocoindistrib; create table biliview.ocoindistrib(val bigint, cnt bigint, PRIMARY KEY (val) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table ocoindistrib \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/ocoindistrib \
 --m 8


echo "EXPORTING 60%"

mysql -uroot -p123456 -e "drop table if exists biliview.otype; create table biliview.otype(tname varchar(255), cnt bigint, PRIMARY KEY (tname) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table otype \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/otype \
 --m 8


echo "EXPORTING 70%"

mysql -uroot -p123456 -e "drop table if exists biliview.ovinfo; create table biliview.ovinfo(bvid varchar(20), aid varchar(1024), cid varchar(1024), iscopy int, tid int, tname varchar(1024), \
 pic varchar(1024), title varchar(1024),descs varchar(1024), duration int, dimension varchar(1024), videos int, pubdate varchar(1024), ctime varchar(1024), view int, \
 danmaku int, reply int, likes int, dislikes int, coin int, favorite int, share int, now_rank int, his_rank int, \
 mid varchar(1024), PRIMARY KEY (bvid) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table ovinfo \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/ovinfo \
 --m 8


echo "EXPORTING 80%"

mysql -uroot -p123456 -e "drop table if exists biliview.odmdistrib; create table biliview.odmdistrib(bvid varchar(255), t bigint, cnt bigint, PRIMARY KEY (bvid, t) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table odmdistrib \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/odmdistrib \
 --m 8


echo "EXPORTING 90%"

mysql -uroot -p123456 -e "drop table if exists biliview.odmwfreq; create table biliview.odmwfreq(bvid varchar(255), word varchar(255), cnt bigint, PRIMARY KEY (bvid, word) )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sqoop export "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \
 --connect "jdbc:mysql://localhost:3306/biliview?useUnicode=true&characterEncoding=utf-8" \
 --driver com.mysql.jdbc.Driver \
 --table odmwfreq \
 --username root \
 --password 123456 \
 --input-fields-terminated-by '\t' \
 --export-dir /user/hive/warehouse/hmain.db/odmwfreq \
 --m 8

echo
echo
echo EXPORT OK! 
echo
echo
