# Data_Stats
## A package to make easier the obtention of data from the database _"statsbombpy"_

[![STATSBOMB](https://miro.medium.com/max/2970/0*fIjnUoscUWWWR-nB.png)](https://statsbomb.com/es/)

Data_Stats is a library that makes your life easier when you want to get data from the open [source](https://github.com/statsbomb/statsbombpy), helping you to get organized data instead of pulling the data in a unique way from game to game so you can pull an entire season for example.

## Code
-> Data_Stats folder

> Data_Stats.py: Code of all the library that will  be explained in the Features section

> __ init__.py: Import of the library

-> LICENSE.txt: Copyright license

-> setup.cfg: Description file

-> setup .py: This file contains information about the package that PyPi needs

## Features

In this library, three different functions have been used within the created class:
- **selection**
- **matches**
- **events**

The function **_selection_** returns a df with needed information for the other two functions as competition_id or season_id. 

The function **_matches_** returns another df that contains every match from the season that you have specified before, this process is made possible by the innformation that selection has provided. 

The last funtion **_events_** returns a list with two different dictionaries inside.
In the first dictionary the keys are the ids of the match_id and the information inside each key is a dictionary with the information of all the existing tables of that match.
The keys of the second dictionary are the names of the tables and inside them are joined all the data from all the matches.
