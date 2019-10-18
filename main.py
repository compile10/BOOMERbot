
import praw
import time

print("For Boomerbot to work it needs a client id and client secret.\nGo to https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps\nand follow the \"First Steps\" to get these. ")

client_id = input("Enter client ID: " )
client_secret = input("Enter client secret: " )
username = input("Enter username: " )
password = input("Enter password: " )
boomerName = input("Enter the username of the boomer: ")

zoomer = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='python.boomerbot',
                     username=username,
                     password=password)


boomer = zoomer.redditor(boomerName)

print("Replying to the boomer. Wait time is 8 minutes between comments.")

for comment in boomer.comments.new():
    comment.reply('ok boomer')
    print("Replied to comment with id: ", comment)
    time.sleep(480)