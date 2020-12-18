# Web Scaping With Tweepy
## Project Overview 
This script scrapes data from [Twitter](https://twitter.com/en). Results are saved into a csv file for further analysis.

*Tools used:*
- **jupyter noteboook**
- **tweepy**
- **pandas**

*The script does the following:*
- a function to scrape data from the tonaton site
- a function to save the data scrapped to a csv file.

## SetUp
* Apply for a Twitter developer account
* Clone this repo
* Create an environment using :
  ```
  conda create -n "env name" python=3.7
  
  ```
  
* Activate the environment using:

  ```
  conda activate "env name"
  ```
  
* Install Packages using:
  
  ```
  pip install -r requirements.txt 
  
  ```

## Resources used
```
* https://towardsdatascience.com/how-to-scrape-more-information-from-tweets-on-twitter-44fd540b8a1f
* https://medium.com/python-in-plain-english/scraping-tweets-with-tweepy-python-59413046e788
* https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
```

## Activities done 
The two functions:
  * scape_tweets() - This function returns a dataframe containng the tweets extracted and has the following parameters:<br>
      * Search topic
      * The number of tweets to download per request
      * The number of requests
  * Save_results_as_csv() - This function returns a csv file and has the following parameters:
      * the dataframe from the scrape_tweets function
The csv file returned has the following naming format:<br>
    * tweets_downloaded_yymmdd_hhmmss.csv (where ‘yymmdd_hhmmss’ is the current 	timestamp)<br>
    
The following attributes of the tweets would be extracted:<br>
   * Tweet text
   * Tweet id
   * Source
   * Coordinates
   * Retweet count
   * Likes count
   * User info
   * Username

Part 2 - A MongoDB database is created with the name Tweets_db and the extracted tweets are stored into a collection named: raw_tweets.
