# Madness Service

## Current State - UPDATE 12/15/21
1. **Dockerize It** (Medium Effort) 
   - [x] Implement MySQL
   - [x] Implement Docker-Compose
2. **Implement Flask W/ Basic Endpoints** 
   - [x] Create Endpoints for basic user, game, school CRUD


## TO-DO:
1. **Game Builder** (Medium) - In Progress
  * Generate/Build board json
	- [ ] Generate JSON representation of game to send to UI
	- [ ] Set Pick Owner as User ID when stored, and replace ID with name when sent to front end
   - [ ] Given Regions and Seeds, autofill game board

2. **Database Functionality** (Medium Effort) 
   - [ ] Implement SQLAlchemy
     - Make use of it returning IDs for Inserts. Use IDs to create user/game link
   - [x] Create Models for Users, Gameboards, and schools

3. **SuperAdmin and Admin Functionality Logic** (Small effort)
   - [ ] Manage users (add, edit, remove users)
   - [ ] Manage picks (add, edit, remove picks)
   - [ ] SuperAdmin inherits Admin functionality plus:
   *  - [ ] Access all users (CRUD)
   *  - [ ] Access all games (CRUD)

4. **Test Suite** (Heavy Effort)
   [ ] Load mock data into MySQL
   [ ] API Endpoints
   [ ] DB Functionality
   [ ] Lamdbas


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

## Next Steps
* **Clean Up Code**
 - [ ] [Make Flask App More Production Ready](https://mark.douthwaite.io/getting-production-ready-a-minimal-flask-app/)
 - [ ] [Update Dockerfile to wait for MySQL](https://www.datanovia.com/en/lessons/docker-compose-wait-for-container-using-wait-tool/docker-compose-wait-for-mysql-container-to-be-ready/)
 - [ ] Generalize utility functions to connect to docker and query db on start up

* **AWS Integration** (Heavy Effort)
- [ ] Implement localstack (dynamodb, s3 [to store db data])
- [ ] Implement serverless
- [ ] Create api-spec.yaml
- [ ] Create Models for User/Game requests/responses

* **Score Service** (Medium Effort) 
 - [ ] Create scraper to pulls scores and odds from KenPom (or some other college baskeball website) and update the scores and odds stored in a cache using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - [ ] Create scraper to get the info of teams that are in the tournament 
 - [ ] Create Lambda running on cron to trigger score scraper during tournament times and 
    
* **Score Cache** (Small Effort)
 - [ ] Simple DyanmoDB or Redis Cache
 - [ ] Stores latest results from games being played

* Probability to Win % per player on board

* Integrate Leagues (to make yearly sign ups easier)
  

Start Date - 11/15/2021