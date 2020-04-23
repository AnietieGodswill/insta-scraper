#----------------modules--------------------#
import requests 
from bs4 import BeautifulSoup
#----------------end--------------------#

while(True):
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
    #----------------end--------------------#

    #----------------credit--------------------#
    print(f"""
    {re}
    ------------------------------------------
    Insta Scapper             
    Developed By: Nishant Tiwari          
    ------------------------------------------
    """)
    #----------------end--------------------#

    #--------------instagram request----------------#
    instaUsername = input(f"{cy}Enter Username:{nu} ")
    instaURL = 'https://www.instagram.com/'+ instaUsername
    instaURLReq = requests.get(instaURL).text
    #--------------end----------------#

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
    #for instaprofilepic
    instaSoup = BeautifulSoup(instaURLReq,"html.parser")
    instaPP = instaSoup.find("meta",attrs={"property":"og:image"})
    instaProfilePic = instaPP.get("content")
    #for externallink
    startsWithExternalLink = '"external_url":'
    endsWithExternalLink= ',"external_url'
    instaExternalLink = instaURLReq[instaURLReq.find(startsWithExternalLink)+len(startsWithExternalLink):instaURLReq.rfind(endsWithExternalLink)]
    #for biography
    startsWithBiography = '"biography":"'
    endsWithBiography ='","blocked_by_viewer"'
    instaBiography= instaURLReq[instaURLReq.find(startsWithBiography)+len(startsWithBiography):instaURLReq.rfind(endsWithBiography)]
    #--------------end----------------#

    #--------------instagram output----------------#
    print(f"{gr}[~]{gr} Name: {nu}{instaWithURL}")
    print(f"{gr}[~]{gr} ID: {nu}{instaWithID}")
    print(f"{gr}[~]{gr} Followers: {nu}{instaFollowers}")
    print(f"{gr}[~]{gr} Following: {nu}{instaFollowing}")
    print(f"{gr}[~]{gr} Profile Pic: {nu}{instaProfilePic}")
    if ('""' not in instaExternalLink):
        print(f"{gr}[~]{gr} External URL: {nu}{instaExternalLink}")
    if(instaBiography == ""):
        print(f"{gr}[~]{gr} Biography: {nu}null")
    else:
        print(f"{gr}[~]{gr} Biography: {nu}{instaBiography}")

    #--------------end----------------#
