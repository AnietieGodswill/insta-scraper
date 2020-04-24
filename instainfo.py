#----------------modules--------------------#
import requests 
from bs4 import BeautifulSoup
#----------------modules--------------------#
def instascrap():
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
    Insta Scapper             
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
    instaBiography= instaURLReq[instaURLReq.find(startsWithBiography)+len(startsWithBiography):instaURLReq.rfind(endsWithBiography)].replace("\\n"," ")
    #for private
    startWithPrivate = 'is_private":'
    endsWithPrivate = ',"is_verified"'
    instaIsPrivate = instaURLReq[instaURLReq.find(startWithPrivate)+len(startWithPrivate):instaURLReq.rfind(endsWithPrivate)]
    #for verified
    startWithVerified = '"is_verified":'
    endsWithVerified = ',"edge_mutual_followed_by"'
    instaIsVerified = instaURLReq[instaURLReq.find(startWithVerified)+len(startWithVerified):instaURLReq.rfind(endsWithVerified)]
    #for posts
    #startWithPosts = '"edge_owner_to_timeline_media":{"count":'
    #endsWithPosts = ',"page_info"'
    #instaPosts = instaURLReq[instaURLReq.find(startWithPosts)+len(startWithPosts):instaURLReq.rfind(endsWithPosts)]
    startWithBusiness = '"is_business_account":'
    endsWithBusiness = ',"is_joined_recently"'
    instaBusiness = instaURLReq[instaURLReq.find(startWithBusiness)+len(startWithBusiness):instaURLReq.rfind(endsWithBusiness)]
    
    #--------------instagram scraping----------------#

    #--------------instagram output----------------#
    print(f"{gr}[~]{gr} Name: {nu}{instaWithURL}")
    print(f"{gr}[~]{gr} ID: {nu}{instaWithID}")
    print(f"{gr}[~]{gr} Followers: {nu}{instaFollowers}")
    print(f"{gr}[~]{gr} Following: {nu}{instaFollowing}")
    print(f"{gr}[~]{gr} Profile Pic: {nu}{instaProfilePic}")

    if ('""' not in instaExternalLink):
        print(f"{gr}[~]{gr} External URL:",nu,instaExternalLink.replace('"'," "))  
    if(instaBiography == ""):
        print(f"{gr}[~]{gr} Biography: {nu}None")
    else:
        print(f"{gr}[~]{gr} Biography: {nu}{instaBiography}")
    if(instaIsPrivate == "false"):
        print(f"{gr}[~]{gr} Private Account: {nu}No")
    else:
        print(f"{gr}[~]{gr} Private Account: {nu}Yes")
    if( instaIsVerified == "false"):
        print(f"{gr}[~]{gr} Verified Account: {nu}No")
    else:
        print(f"{gr}[~]{gr} Verified Account: {nu}Yes")
    if(instaBusiness == "false"):
        print(f"{gr}[~]{gr} Business Account: {nu}No")
    else:
        print(f"{gr}[~]{gr} Business Account: {nu}Yes")
    

     
#--------------instagram output----------------#
while(True):
    again = input("PRESS S TO START: ").lower()
    if(again == "s"):
        instascrap()
    else:
        exit()
    
    



