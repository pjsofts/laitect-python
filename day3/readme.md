```docker run --name my-postgres1 --rm --publish 5432:5432   -e POSTGRES_PASSWORD=secret  postgres:14-alpine```



```
 docker run -d --restart always --name flights-postgres --publish 5432:5432
  -e POSTGRES_PASSWORD=secret -e PGDATA=/var/lib/postgresql/data/pgdata 
  -v /home/pouria/pgdata:/var/lib/postgresql/data postgres
```