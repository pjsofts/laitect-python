```docker run --name my-postgres1 --rm --publish 5432:5432   -e POSTGRES_PASSWORD=secret  postgres:14-alpine```



```
 docker run -d \
    --restart always \
	--name some-postgres \
	-e POSTGRES_PASSWORD=mysecretpassword \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /custom/mount:/var/lib/postgresql/data \
	postgres
```