import pyshorteners

shortners = pyshorteners.Shortener()
long_link=input("Your Link: ")
short_link= shortners.tinyurl.short(long_link)
print(short_link)