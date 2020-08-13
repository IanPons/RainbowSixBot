# RainbowSixBot
Web scraping bot that show stats of Rainbow Six Siege players.


# How to use:
!StatsPc *nickname* for PC player
!StatsXbox *nickname* for Xbox player
!StatsPs4 *nickname* for PS4 player

Returns MMR, player rank, player KD (kill/death) ratio.

![alt text](https://github.com/IanPons/RainbowSixBot/blob/master/res/printscreen.png?raw=true)

#How it works:
A HTTP Request is made to the website *https://r6.tracker.network* wich has a database of all Rainbow Six players.
Using the *BeautifulSoup4* library. The data is extracted and sent in the discord server.

BeautifulSoup4 library: *https://pypi.org/project/beautifulsoup4/*


