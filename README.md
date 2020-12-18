# ETL With Twitter Data
## Project Overview 
This script scrapes data from [Twitter](https://twitter.com/en). Results are saved into a csv file for further analysis.

*Tools used:*
- **jupyter noteboook**
- **Python 3.7**
- **tweepy**
- **pandas**
- **pymongo**

*The script does the following:*
- a function to scrape data from the twitter site
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
  ### Store env variables

To store your API credentials:  

* Duplicate  ``` .env.example ``` file and create a new file name *.env*



## Resources used

- [Twitter Search API](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets)
- [Tweepy Documentation](http://docs.tweepy.org/en/latest/index.html)
- [Pymongo Documentation](https://pymongo.readthedocs.io/en/stable/)
- [Scraping Tweets with Tweepy Python - Python in Plain English](https://medium.com/python-in-plain-english/scraping-tweets-with-tweepy-python-59413046e788)
- [How to Scrape More Information From Tweets on Twitter - Towards Data Science](https://towardsdatascience.com/how-to-scrape-more-information-from-tweets-on-twitter-44fd540b8a1f)

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
