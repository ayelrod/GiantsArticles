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
One of the main reasons I stopped running this script was because of the amount of errors I kept getting. This is because these websites that I was scraping changed their layout very often (~once a week), so my XPaths became invalid. This was a huge downfall. What I should've done is spent more time learning about web scraping and done this in a way that searched for the articles, instead of hard coding them in. This would've also allowed me to scale the project much easier.

Another reason I stopped running this script was because I had to run it manually. I wanted to put the code on to a server and have it run automatically, but that wasn't possible with the way I wrote the code. The version of Selenium I was used needed access to the browser on my computer to work. It would pull up the actual browser and do everything as if it were a real user doing it, right in front of my eyes. This wouldn't work if I wanted to do this remotely (from a server using SSH). I would have to do more research to see if I could fix this using Selenium, if not, I'm sure there's another library out there that can do this.

## Scaling
I have discussed the possibility of scaling this python script in a job interview I had and I think it was a very interesting conversation. So, let's discuss how this could be scaled in the future. This is a script that scrapes web articles about my favorite team. So naturally, there is a lot more information that can be extracted from these articles about the games. The score, the location, the players, etc. can be taken from the articles and this can be some useful information. This information is obviously available elsewhere with an easier way to aquire it, but the data from the articles can be useful. If we scale this to all the teams in the MLB, we would have a large amount of information (in the form of articles) to parse. Combining this with NLP could give us some insight into how the teams doing and their future potential matchups. I see this as a possibility for potientially predicting the outcomes of future games.

## Conclusion
Although this was a very simple project, I learned a lot about how to start individual projects and do them correctly. If I had done some more research and put some more time into coding, I would've saved a lot of time not having to run this manually and it would've allowed me to scale it. It also allowed me to get closer with the Giants community, as the account has ~90 followers for a reason. One day, I will fix this code and do it correctly so that the project can live without having to be maintained as often.
