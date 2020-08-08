# PythonServer

### Build and start the servers

```
docker-compose up -d
```

### Test the server

Open the following links:

API: [http://localhost/query](http://localhost/query)

DB: [http://localhost:8080](http://localhost:8080)

In Adminer use `server=mysql`, `user=calitb`, `pass=12345`

### Enter container CLI

```
# Server Develop
docker exec -it python_server ash
# MySQL (password 12345)
docker exec -it mysql mysql -ucalitb -p
```

### Stop the servers

```
# Develop
docker-compose down
```
