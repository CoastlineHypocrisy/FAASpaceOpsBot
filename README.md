# FAA Space Operations Bot
<h3>Follow the bot on: <a href="https://twitter.com/FAASpaceOpsBot">Twitter</a></h3>

This is a bot to automatically retrieve the list of expected space operations listed in the FAA's Operation Plan. This project currently runs on GitLab, which automatically runs the code for the bot and posts to Twitter automatically. The bot will be capable of posting on other platforms in the near future.

<b>.gitlab-ci.yml</b> pulls the configuration file as well as the Twitter API keys that are stored as variables for GitLab's runners. It also gets the ball rolling once the variables have been loaded.

<b>requirements.txt</b> contains the Python modules I've used in developing this bot.

<b>beepboop.py</b> is the main section of code that retrieves the FAA's <a href="https://www.fly.faa.gov/adv/adv_spt.jsp">Current Operation Plan Advisory</a> and extracts the section under 'Space Operations.' It also cleans up the code and stores it in a text file temporarily. Ideally, I wouldn't want to store it in a text file, but after some tinkering, I haven't found a better solution.

<b>post_to_twitter.py</b> does what it says on the tin. It decides whether the bot requires more than one tweet. If it doesn't, it simply pushes out the entire text with a header that includes the date (timezone UTC). If it does, it identifies where each section begins and ends, and tweets each section individually (as if it is the sole section). I'm not especially proud of the code here, but like above, I haven't found a better solution. 

At the end of everything, the temporary text files are deleted.

<i>I know some will skewer me for my messy code, but I write data analysis code in my day job, so I think I get a pass.</i>

Disclaimer: I'm not affiliated with the FAA in any way.

Last Updated: 6 May 2023
