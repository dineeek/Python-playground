# 1. Login to your Facebook
# 2. Download your friends names and save them local as file
# 3. Use previosly stored file to compare with facebook friends after some time
# not possible anymore with v2 Facebook API :(


# import facebook as face

# myToken = ""
# myName = ""

# graph = face.GraphAPI(access_token=myToken, version="2.12")
# graph = face.GraphAPI(myToken)
# profile = graph.get_object("me")
# friends = graph.get_connections("me", "friends")

# friend_list = [friend['name'] for friend in friends['data']]


# basic reading file and comparing it with another
import codecs
import re

fileBefore = codecs.open("friendsBefore.html", "r", "utf-8") #need to download friends.html from Facebook - older better version
friendsBefore = fileBefore.read().split("/")

friendsBeforeArray = []
for friend in friendsBefore:
    result = re.search('_2lel">(.*)<', friend)
    if result is not None:
        friendsBeforeArray.append(result.group(1))

friendsBeforeArray = sorted(set(friendsBeforeArray))
fileNow = codecs.open("friendsNow.html", "r", "utf-8") #download new friends.html after you notice someone deleted you
friendsNow = fileNow.read().split("/")

friendsNowArray = []
for friend in friendsNow:
    result = re.search('_2lel">(.*)<', friend)
    if result is not None:
        friendsNowArray.append(result.group(1))

friendsNowArray = sorted(set(friendsNowArray))

noLongerFriends = []

for friend in friendsBeforeArray:
    if friend not in friendsNowArray:
        noLongerFriends.append(friend)

file = open("enemies.txt", "w")

for enemy in noLongerFriends:
    newLine = "".join(enemy)+"\n"
    file.write(newLine)




