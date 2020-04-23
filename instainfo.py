#----------------modules--------------------#
import requests 
from bs4 import BeautifulSoup
#----------------modules--------------------#

nu = '\033[0m'
re = '\033[1;31m'
gr = '\033[1;32m'
cy = '\033[1;36m'
yl ='\033[1;33m'

#----------------session--------------------#
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE
#----------------session--------------------#

#----------------credit--------------------#
print(f"""
{re}
------------------------------------------
All In One Social Scapper             
Developed By: Nishant Tiwari          
------------------------------------------
""")

#----------------credit--------------------#

#--------------instagram request----------------#
instaUsername = input(f"{cy}Enter Username:{nu} ")
instaURL = 'https://www.instagram.com/'+ instaUsername
instaURLReq = requests.get(instaURL).text
#--------------instagram request----------------#

#--------------instagram scraping----------------#
#for name
startsWithURL = '"full_name":"'
endsWithURL = '","has_ar_effects"'
instaWithURL = instaURLReq[instaURLReq.find(startsWithURL)+len(startsWithURL):instaURLReq.rfind(endsWithURL)]
#for id
startsWithID = '"id":"'
endsWithID = '","is_business_account"'
instaWithID = instaURLReq[instaURLReq.find(startsWithID)+len(startsWithID):instaURLReq.rfind(endsWithID)]
#for followedby
startsWithFollowed = '"edge_followed_by":{"count":' 
endsWithFollowed = '},"followed_by_viewer"'
instaFollowers = instaURLReq[instaURLReq.find(startsWithFollowed)+len(startsWithFollowed):instaURLReq.rfind(endsWithFollowed)]
#for followers
startsWithFollowing = '"edge_follow":{"count":'
endsWithFollowing = '},"follows_viewer"'
instaFollowing = instaURLReq[instaURLReq.find(startsWithFollowing)+len(startsWithFollowing):instaURLReq.rfind(endsWithFollowing)]

instaSoup = BeautifulSoup(instaURLReq,"lxml")
instaPP = instaSoup.find("meta",attrs={"property":"og:image"})
instaProfilePic = instaPP.get("content")
#--------------instagram scraping----------------#

#--------------instagram output----------------#
print(f"{gr}[~]{gr} Name: {nu}{instaWithURL}")
print(f"{gr}[~]{gr} ID: {nu}{instaWithID}")
print(f"{gr}[~]{gr} Followers: {nu}{instaFollowers}")
print(f"{gr}[~]{gr} Following: {nu}{instaFollowing}")
print(f"{gr}[~]{gr} Profile Pic: {nu}{instaProfilePic}")
#--------------instagram output----------------#
