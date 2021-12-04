# Madness Service

## Current State - 11/30/21
1. **Game Builder** (Medium) - In Progress
  * Generate/Build board json
	- [x] Enter 16 player names
	- [x] Generate JSON representation of game to send to UI
	- [ ] Validate Gameboard sent from UI


## TO-DO:
1. **Dockerize It** (Heavy Effort) 
   [ ] Implement MySQL
   [ ] Create utility functions to connect to docker and query db
   [ ] Add API endpoints Flask app.py
   [ ] Implement Docker-Compose

2. **Database Models** (Small Effort) 
   [x] Create Models for Users, Gameboards, and schools
 
3. **SuperAdmin and Admin Functionality Logic** (Small effort)
   [ ] Manage users (add, edit, remove users)
   [ ] Manage picks (add, edit, remove picks)
   [ ] SuperAdmin inherits Admin functionality
   *  [ ] Access all users (CRUD)
   *  [ ] Access all games (CRUD)

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
  * Losers
* User
  * Name
  * Email
  * Password
  * Linked Games 
* School
  * Name
  * Mascot
  * Initials
```

## Next Steps
* **AWS Integration** (Heavy Effort)
  [ ] Implement localstack (dynamodb, s3 [to store db data])
  [ ] Implement serverless
  [ ] Create api-spec.yaml
  [ ] Create Models for User/Game requests/responses

* **Score Service** (Medium Effort) 
   * Create scraper to pulls scores and odds from KenPom (or some other college baskeball website) and update the scores and odds stored in a cache using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
   * Create scraper to get the info of teams that are in the tournament 
   * Create Lambda running on cron to trigger score scraper during tournament times and 
    
* **Score Cache** (Small Effort)
   * Simple DyanmoDB or Redis Cache
   * Stores latest results from games being played

* Probability to Win % per player on board
  

