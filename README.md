# PythonServer

### Build and start the servers

```
docker-compose up -d
```

### Test the server

Open the following links:

API: [http://localhost:90/query](http://localhost:90/query)

DB: [http://localhost:8083](http://localhost:8083)

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
