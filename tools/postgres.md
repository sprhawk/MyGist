PostgreSql
==========

```shell
select * from pg_stat_activity;
select pg_terminate_backend(13514) from pg_stat_activity where datname='collab';
```
