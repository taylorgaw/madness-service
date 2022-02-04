curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Mike Jones", "username": "mikejooooonez", "email": "mikejones@collapark.edu", "password": "purp"}' http://localhost:5000/users

curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Bob Gaws Group", "owner": 1, "picks": "{}"}' http://localhost:5000/games

curl -i -H "Content-Type: application/json" -X GET -d '{"id":3}' http://localhost:5000/user

curl -i -H "Content-Type: application/json" -X DELETE -d '{"id":4}' http://localhost:5000/users

curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/users