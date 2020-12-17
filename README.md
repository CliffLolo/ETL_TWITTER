# ETL_TWITTER
## Project Overview 
This project is on basic ETL using twitter data. It is in 2 parts- Part 1 and Part 2.<br>
Part 1 has to do with scrapping the tweets and storing the results in a CV
Part 2 deals with saving the tweets extracted to MongoDB

## SetUp
* Apply for a Twitter developer account
* Clone this repo
* Create an environment using :
  ```
  conda creat -n "env name" python=3.7
  
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
```

## Activities done 
Part 1 contains two functions:
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
