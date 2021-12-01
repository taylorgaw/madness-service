# Madness Service

## Current State - 11/30/21
1. **Game Builder** (Medium) - In Progress
  * Generate/Build board json
	- [x] Enter 16 player names
	- [x] Generate JSON representation of game to send to UI


## Next Steps

1. Dockerize it (Small Effort)
   *  Will want to run service and UI in same container at some point
   *  Implement localstack and serverless
  
2. **Score Service** (Medium Effort) 
   * Create web scraper using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) that pulls scores from KenPom (or some other college baskeball website) and update the scores stored in a cache
   * Will also pull odds from page
   * Runs at intervals using AWS Lambda

3. **Score Cache** (Small Effort)
   * Simple DyanmoDB or Redis Cache
   * Stores latest results from games being played

4. **User Database** (Small Effort) 
   * Simple DynamoDB thing
   * Still working on a simple model to implement so that multiple boards can be played at once:
```
* Tournament
  * Regions
  * Teams
      * Name
      * Seed
  * Losers
* Game
  * Players
      * Name
      * Picks 
```


## Nice-to-Haves
* Probability to Win % per player on board

