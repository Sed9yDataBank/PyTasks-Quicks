"""
Get Profile Statistics About Player To Check If He Is A Smurf In CSGO
"""
import re
import requests
import json
import time
import colorama
import tabulate

APIKEY = ""
colorama.init()


class User:
    def __init__ (self, steamID64, personaName, isProfilePublic, profileUrl, timeCreated = None):
        self.steamID64 = steamID64
        self.isProfilePublic = isProfilePublic
        self.personaName = personaName
        self.timeCreated = timeCreated
        self.profileUrl = profileUrl


    def get_playtime_stats(self):
        """
        For Public Profiles Only, This Gets The Following Statistics And Adds Them As Variables To Self
        Number Of Games Owned, Playtime In Csgo All Time, Playtime In Csgo Past 2 Weeks, It Also Creates
        The Variable Accountage To Self Which Contains The Age Of The Account In Years
        """


        assert self.isProfilePublic == True, "Can Not Get Playtime Stats For Private Profile"

        reqUrl = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + APIKEY + "&steamid=" + self.steamID64

        resp = api_call(reqUrl)

        jsonResp = json.loads(resp)

        gameCount = jsonResp["response"]["game_count"]
        csgoForever = None
        csgo2Week = None
        for game in jsonResp["response"]["games"]:
            if game['appid'] == 730:
                csgoForever = game["playtime_forever"]
                csgo2Week = game["playtime_2weeks"]

        self.gameCount = gameCount
        self.csgoForever = round(csgoForever / 60)
        self.csgo2Week = csgo2Week
        self.accountAge = (round((time.time() - self.timeCreated)/(60*60*24*365), 1))

    def get_friends(self):
        """
        Gets A List Of Tuples Containing All The Friends That A User Has And The Unix Timestamp That Is The Date
        That The Two Users Became Friends. Returns Nothing, Just Adds It To Self
        """

        url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + APIKEY + "&steamid=" + self.steamID64 + "&relationship=friend"
        resp = api_call(url)

        jsonResp = json.loads(resp)

        friendList = []

        for friend in jsonResp['friendslist']['friends']:
            friendList.append((friend['steamid'], friend['friend_since']))

        self.friendsList = friendList



def get_player_summaries(steamID64List):
    """
    Takes A List Of Steamid64S And Returns A List Of User Objects Containing The Following Information
    Username, Steamid64, profileurl, isprofileprivate, And If The Profile Is Not Private It Also Adds The
    Date The Account Was Created In Unix Timestamp
    """
    fullSteamIDsString = ",".join(steamID64List)

    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + APIKEY + "&steamIDS=" + fullSteamIDsString

    response = api_call(url)
    jsonResp = json.loads(response)

    returnUserList = []

    for player in jsonResp['response']['players']:
        name = player['personaname']
        steamID64 = player['steamid']
        profileUrl = player['profileurl']

        if player['communityvisibilitystate'] == 3: #Public Profile
            timeCreated = player['timecreated']
            returnUserList.append(User(steamID64, name, True, profileUrl, timeCreated))
        else: #Private Profile
            returnUserList.append(User(steamID64, name, False, profileUrl))
    return returnUserList


def steamid_to_64bit(steamid):
  
    steam64id = 76561197960265728
    id_split = steamid.split(":")
    steam64id += int(id_split[2]) * 2
    if id_split[1] == "1":
        steam64id += 1
    return steam64id

def get_steam_users_from_status(status):
  
    steamID64List = []

    for currentUser in re.findall(r'#\s+\d+\s\d+\s"(.+?)"\s(.+?) ', status):
        steamID64List.append(str(steamid_to_64bit(currentUser[1])))

    return get_player_summaries(steamID64List)

def check_friends(listOfUsers):
    """
    Checks For Users Inside Listofusers That Are Friends With Each Other, It Loops Through Every User, Then For Every
    User Loops Through Every Friend, Then For Every Friend It Loops Through Every User Again, It Checks If The
    Friend Has The Same Steamid64 As The User

    Returns A List Of Tuples That Contain (Username1, Username2, Howlongindaysbeenfriends)
    """
    currentFriends = []
    for user in listOfUsers:
        if user.isProfilePublic == False:
            continue
        for friend in user.friendsList:
            for checkUser in listOfUsers:
                if checkUser.steamID64 == friend[0]:

                    timeFriends = round((time.time() - friend[1])/(60*60*24), 1)

                    #Make Sure They Haven't Already Been Logged As Friends, The Reversal Is Extremely Important                    if (checkUser.personaName, user.personaName, timeFriends) not in currentFriends:
                    currentFriends.append((user.personaName, checkUser.personaName, timeFriends))

    return currentFriends

def hours_played_key(itemToCheck):
    
    if itemToCheck[1] == "":
        return 0
    return itemToCheck[1]


def api_call(url):
    """
    All Api Calls Get Passed Through Here So The Program Can Have A Single Way To Keep Track Of How Long Api Calls
    Are Taking
    """

    startTime = time.time()
    respText = requests.get(url).text
    totalTime = round(time.time() - startTime, 2)

    with open("apiCalls.txt", "a") as f:
        f.write(str(totalTime) + "s" + " -- " +  url + "\n")

    print(str(totalTime) + "s", "--", url)

    return respText

open("apiCalls.txt", "w").close()

with open("status.txt", "r") as f:
    status = f.read()

usersList = get_steam_users_from_status(status)

for user in usersList:
    if user.isProfilePublic:
        user.get_playtime_stats()
        user.get_friends()


printTupleList = []
for user in usersList:
    if user.isProfilePublic:
        printTupleList.append((user.personaName, user.csgoForever, user.accountAge))
    else:
        printTupleList.append((colorama.Fore.RED + user.personaName + colorama.Fore.RESET, "", ""))

printTupleList.sort(key=hours_played_key)

print("\n")
print(tabulate.tabulate(printTupleList, headers=["Name", "HRS", "YR"], tablefmt="orgtbl"))

print("\n")
for friend in check_friends(usersList):
    print(colorama.Fore.CYAN + friend[0], "And", friend[1], "Have Been Friends For", friend[2], "Days" + colorama.Fore.RESET)