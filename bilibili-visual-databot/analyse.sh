hive -e "create database if not exists hexp;"

hive -e "use hmain; drop table if exists oViewDistrib; create table oViewDistrib row format delimited fields terminated by '\t' as \
    select v*100000 as val,count(v) as cnt from (select floor(view/100000) as v from Vinfo) as T group by v order by v;"

echo
echo
echo CALCULATING... 10%
echo
echo

hive -e "use hmain; drop table if exists oDurationDistrib; create table oDurationDistrib row format delimited fields terminated by '\t' as \
    select v*20 as val,count(v) as cnt from (select floor(duration/20) as v from Vinfo) as T group by v order by v;"

echo
echo



echo CALCULATING... 20%
echo
echo

hive -e "use hmain; drop table if exists oReplyDistrib; create table oReplyDistrib row format delimited fields terminated by '\t' as \
    select v*20 as val,count(v) as cnt from (select floor(reply/20) as v from Vinfo) as T group by v order by v;"

echo
echo
echo CALCULATING... 30%
echo
echo

hive -e "use hmain; drop table if exists oFavoriteDistrib; create table oFavoriteDistrib row format delimited fields terminated by '\t' as \
    select v*500 as val,count(v) as cnt from (select floor(favorite/500) as v from Vinfo) as T group by v order by v;"

echo
echo
echo CALCULATING... 40%
echo
echo

hive -e "use hmain; drop table if exists oLikesDistrib; create table oLikesDistrib row format delimited fields terminated by '\t' as \
    select v*5000 as val,count(v) as cnt from (select floor(likes/5000) as v from Vinfo) as T group by v order by v;"

echo
echo
echo CALCULATING... 50%
echo
echo

hive -e "use hmain; drop table if exists oCoinDistrib; create table oCoinDistrib row format delimited fields terminated by '\t' as \
    select v*1000 as val,count(v) as cnt from (select floor(coin/1000) as v from Vinfo) as T group by v order by v;"

echo
echo
echo CALCULATING... 60%
echo
echo

hive -e "use hmain; drop table if exists oType; create table oType row format delimited fields terminated by '\t' as SELECT distinct tname,cnt FROM \
 (SELECT tname, count(*) AS cnt FROM Vinfo vv1 GROUP BY tname ORDER BY cnt DESC LIMIT 10 ) AS t1 UNION ALL SELECT '其它', sum( cnt ) FROM ( SELECT tname, \
  count(*) AS cnt FROM Vinfo vv2 GROUP BY tname ORDER BY cnt DESC LIMIT 10, 99 ) AS t2;"

echo
echo
echo CALCULATING... 70%
echo
echo

hive -e "use hmain; drop table if exists oDmDistrib; create table oDmDistrib row format delimited fields terminated by '\t' as \
    select bvid, floor(floattime) as t, count(*) as cnt from (select bvid, Danmu.cid, floattime from Vinfo \
     inner join Danmu on Vinfo.cid=Danmu.cid) as TT group by bvid, floor(floattime) order by bvid, floor(floattime);"

echo
echo
echo CALCULATING... 80%
echo
echo

hive -e "use hmain; drop table if exists oDmWFreq; create table oDmWFreq row format delimited fields terminated by '\t' as select distinct * from dmwfreq;"

echo
echo
echo CALCULATING... 90%
echo
echo

hive -e "use hmain; drop table if exists oVinfo; create table oVinfo row format delimited fields terminated by '\t' as select distinct * from Vinfo;"

echo
echo
echo CALCULATE OK! 
echo
echo
