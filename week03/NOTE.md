学习笔记

1.安装了MySQL、 和老师一样调整了字符集；
2，对于外键，考虑性能多时，不用外键，在应用层解决；小系统，用外键保证数据一致性。

3,
SELECT DISTINCT player_id, player_name, count(*) as num  #5
FROM player JOIN team ON player.team_id = team.team_id   #1
WHERE height > 1.80                                      #2
GROUP BY player.team_id                                  #3
HAVING num > 2                                           #4
ORDER BY num DESC                                        #6
LIMIT 2                                                  #7

4,in 还是 exists
对于a 大 in （select  table  b where ???）


5， 自然连接，左连接，右连接 ，没有全连接 
