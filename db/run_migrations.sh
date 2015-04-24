for sql in /docker-entrypoint-initdb.d/migrations/*.sql
do
  gosu postgres postgres --single -jE < $sql
done
