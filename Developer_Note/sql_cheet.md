## SQL sheets





```sql
from table a table b
join 
on a.key = b.key
```

```sql
select ifnull('column', value)
```

```sql
round() # 반올림
ceil() # 올림
floor() # 내림
```

```sql
date_format(column, '%Y-%m-%d') # 2022-01-01
# %i 분 %k 시간(24) %l 시간(12)  %M(full eng) %p(am,pm) %s(Second) 
```

```sql
group by
특정 컬럼을 그룹화
having 그룹화된 것에서 조건걸기
where 그룹화 되기 전에 조건걸기
```

