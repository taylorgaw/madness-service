# Madness Service

## Current State - UPDATE 01/11/22
1. **Dockerize It**
   - [x] Implement MySQL
   - [x] Implement Docker-Compose
2. **Implement Flask W/ Basic Endpoints** 
   - [x] Create Endpoints for basic user, game, school CRUD
3. **Database Functionality**
   - [x] Implement SQLAlchemy
   - [x] Create Models for Users, Gameboards, and schools


## MVP TO-DO:
1. **Clean Up Code**
    - [ ] [Make Flask App More Production Ready](https://mark.douthwaite.io/getting-production-ready-a-minimal-flask-app/)
    - [ ] [Update Dockerfile to wait for MySQL](https://www.datanovia.com/en/lessons/docker-compose-wait-for-container-using-wait-tool/docker-compose-wait-for-mysql-container-to-be-ready/)
    - [ ] Generalize utility functions to connect to docker and query db on start up
    - [ ] Refactor endpoints and methods to work with SQLAlchemy
    - [ ] Create api-spec.yaml
    - [ ] Create Models for User/Game requests/responses

2. **Test Suite** (Heavy Effort)
   - [ ] Load mock data into MySQL
   - [ ] API Endpoints
   - [ ] DB Functionality

# Under the Hood
##  Database Models
```
* GameBoard
  * Board Name
  * Owner
  * Users
  * Picks (JSON)
  * Active
* User
  * Name
  * Email
  * Password
  * Admin
* User Game Match
   * User ID
   * Game ID
* School
  * Name
  * Mascot
  * Initials
```


# Next Steps
* **AWS Integration** (Heavy Effort)
- [ ] Implement localstack (redis, s3 [to store db data])
- [ ] Implement serverless
- [ ] Lamdbas

* **Score Service** (Medium Effort) 
 - [ ] Create scraper to pulls scores and odds from KenPom (or some other college baskeball website) and update the scores and odds stored in a cache using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - [ ] Create scraper to get the info of teams that are in the tournament 
 - [ ] Create Lambda running on cron to trigger score scraper during tournament times
    
* **Score Cache** (Small Effort)
 - [ ] Simple Redis Cache
 - [ ] Stores latest results scraped from Score Service


* Integrate Leagues (to make yearly sign ups easier)
  

Start Date - 11/15/2021