# DevHacks2020

## Problem
As a user of some slack channel in some community forum, most of the time we ask our questions without checking whether similar questions have already been asked. Objective is to remove that extra conversation and reduce the effort of both questioner and responsder.

## Solution 
A slack bot
Normally a user asks questions like `Which is best book to learn Javascript?`. If admin installs this slack bot, user can use slash command /question before asking question example: `/question Which is best book to learn Javascript?`. 
By doing this he will get a list of similar questions already asked in that slack channel. He can follow any thread if any of them matches his question, in case none matches, he may proceed with Submit to post his question.

## Exmaple Images
![alt text](https://github.com/prash471/DevHacks2020/blob/master/images/slackChat.png?raw=true)


![alt text](https://github.com/prash471/DevHacks2020/blob/master/images/slackDialog.png?raw=true)

## Future
For now I am using slack search API based on keywords, this can be improved with AI for better search result. 

## WIP
Project still has some bugs to fix. 
