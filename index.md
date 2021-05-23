# Preface
My favorite baseball team is the San Francisco Giants. Having grown up in the Bay Area, it was impossible to escape them because they dominated baseball from 2010-2014. I am a huge fan of the team, so I decided to create a twitter bot that tweets out the daily articles from different sites that cover the SF Giants. You can check it out [@GiantsArticles](https://twitter.com/GiantsArticles) on Twitter!

The bot is currently not tweeting anymore because it became a burden. Ideally, I would have server space that could run the python script automatically, but that costs money and there are too many potential errors. So, I was running the python script manually everyday to tweet out the articles. I stopped doing this because it became too much to maintain. However, the code is still available for you to check out!

# Project
## Coding 
This twitter bot uses [Selenium](https://www.selenium.dev/) for web scraping and uses a python library called [Tweepy](https://www.tweepy.org/) for making the API calls to Twitter. I made this bot quite early in my computer science career, so there are definitely some shortcomings that I will discuss. But for now, lets look at how I made the bot.

The first step was to get the articles from the internet. I have a list of the websites that I scraped, chosen by popularity and credibility. There are like 4 or 5 websites on there and they all post articles daily, some more than others. So I navigate to those websites using Selenium and then I collect information about the first two articles displayed. I first get the title of the article by using the full XPath of the article. Then I click on the title using Selenium, to navigate to the actual article. I then copy the link of the article using Selenium. I write the title and article to a text file and then repeat this process to get the next article's information.

Once I have the information, I use the Twitter API and Tweepy to tweet out the contents of the text file. If that is the first tweet I make, I grab the tweet ID so that I can set subsequent tweets to be replies to the first tweet. I then go on to the next website and do this process over again. It is really quite simple. 

I added some error handling and some security to the code a little later on. I had to catch errors and swallow them because if one website returned an error, then all the websites that came after that would be ignored because the program exited. There were quite a bit of errors, so this really helped. When I uploaded the code to Github, I needed to make sure that the API keys weren't visible to the public. So, I put these in a text file that was not uploaded to Github and just read them from that file.

Another thing I had to worry about was exceeding the Twitter APIs tweeting rate. I initially ran this script twice a day, so I was sending about 10 tweets a day. Apparently, that exceeds the limit for tweeting from an API, and I got a temporary ban. So, I only ran the script once a day after that.

**The code can be found [here](https://github.com/ayelrod/GiantsArticles/blob/main/giantsArticles.py)**

## Shortcomings
One of the main reasons I stopped running this script was because of the amount of errors I got
