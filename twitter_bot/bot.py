#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## dz
## File description:
## zd
##

import datetime
import tweepy
import logging
import time
from random import randint
from os import system
import sys
import re
import snscrape.modules.twitter
import snscrape.modules.twitter as sntwitter

import emoji

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from datetime import date as dta
from datetime import timedelta

def remove_trash(l):
    d = []
    for i in range(len(l)):
        if len(l[i]) > 0:
            if l[i][0] != "@" and "https://t.co" not in l[i]:
                l[i] = l[i].lower()
                d.append(l[i])
    return (d)

def check_similarity(sentence,base_sentence,num):
    sentence = sentence.lower().split(" ")
    base_sentence = base_sentence.lower().split(" ")
    pourcentage = 0
    pourcentage_list = []

    for i in range(len(base_sentence)):
        if base_sentence[i] in sentence:
            pourcentage = pourcentage + 1
            pourcentage_list.append(pourcentage)
        else:
            pourcentage = 0

    pourcentage_list.sort()
    if len(pourcentage_list) == 0:
        print("100")
        result = 100
    else:
        result = (pourcentage_list[-1]/len(sentence)) * 100
        result = int(result)
        print(result)
    if result >= num:
        return(1)
    else:
        return(2)

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')
    #return emoji.get_emoji_regexp().sub(r'',text)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])


def file_line_line(files,x):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[x])

def text_to_pic(word_len):
    lens = 0
    image = Image.open("main.jpg")
    print("cezfzefzefzefzef")
    print(word_len)
    w_image = image.copy()
    if w_image.mode != 'RGB':
        w_image = w_image.convert('RGB')
    draw = ImageDraw.Draw(w_image)
    font = ImageFont.truetype("ayar.ttf", 30)
    yyy = 0
    max_line = word_len - 1
    ii = 1
    for i in range(word_len):
        rl = random_line("dico.txt",max_line-i,max_line-i)
        print(lens,lens*45,ii)
        draw.text((yyy, lens*40), str(ii) + " " + str(rl), (0, 0, 0), font=font)
        lens = lens + 1
        if lens % 20 == 0:
            lens = 0
            yyy = yyy + 400
        ii = ii + 1
    #w_image.show()
    w_image.save("dico.jpg")

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def write_id(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def wwrite_id(path,x):
    f = open(path, "a")
    f.write(str(x))
    f.close

def count_space(s):
    count = 0
    for i in range(len(s)):
        if s[i] == " ":
            count = count + 1
    return (count)


def check_text(text):
    count = 0
    try:
        for i in range(len(text)):
                if text[i][0] == "@":
                    count = count + 1
        return (count)
    except:
        return(0)
def check_list(l):
    count = 0
    for i in range(len(l)):
        for k in range(len(l)):
            if l[i] == l[k] and i != k and l[i][0] == "@" and l[k][0] == "@":
                count = count + 1
            else:
                count = count + 0
    return (count)

def check_baz(text):
    count = 0
    try:
        for i in range(len(text)):
            if text[i][0] != "@":
                count = count + 1
        return (count)
    except:
        return(0)
def word_pos(l,word):
    for i in range(len(l)):
        if l[i] == word:
            return(i)
            break

def remove_word(l):
    d = []
    for i in range(len(l)):
        if len(l[i]) > 0:
            if l[i][0] != "@":
                l[i] = l[i].lower()
                d.append(l[i])
    return (d)

def remove_word2(l):
    d = []
    for i in range(len(l)):
        if len(l[i]) > 0:
            if l[i][0] != "@" and "https://t.co" not in l[i]:
                l[i] = l[i].lower()
                d.append(l[i])
    return (d)

def get_len_list(l):
    x = 0
    for i in range(len(l)):
        x = x + len(l[i])
    return (x)

def get_len_word(l):
    x = 0
    w = 0
    for i in range(len(l)):
        if len(l[i]) > 0:
            if l[i][0] == "@":
                w = w + 1
    return (w)

def blocked_by_user(get_status,copy_tweet):
    
    since_id = 1
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    your_name = print_file("user_name.txt")
    mention_id = int(print_file("get_mention.txt"))
    idx = 0
    only_pic = 0
    wait_time = 15
    wait_time2 = 15
    look_user = ""
    shadow = True

    try:
        get_status = api.get_status(int(copy_tweet))
        look_user = get_status.user.screen_name
        tweets = []
        limits = 1000
        idx = 0
        never_done = 0
        tweet_split = get_status.text.split("https://")
        original_tweet = get_status.text
        image_inside = 0
        print(tweet_split)
        if "https://" in original_tweet and len(original_tweet) < 100:
            image_inside = 1
        #print(get_status.text)
        #print(tweet_split)
        #print(tweet_split)
        #ccprint("cjczoicjoezjcozejcoiejc")
        az = tweet_split[0]
        #print("caca")
        #print(az)
        #print("caca")
        word = ""
        rword = ""
        qquery = ""
        query  = ""
        max_time = 3000
        sssd = ""
        ssss = ""
        little_word = 0
        rtweet = ""
        rtweets = ""
        azz=""
        rjoin = ""
        too_long = 0
        if az[0] == '@':
            print("aaazz")
            print(az)
            if len(az) > 100:
                too_long = 1
                azz = az.split(" ")
                rtweet = remove_word2(azz)
                rjoin = ' '.join(rtweet)
                rtweets = rjoin
                rtweets = rtweets.split(" ")

                print(rtweets)
                print("pppppppppppppp")
                #time.sleep(10000)
                rtweets.pop()
                rtweets.pop()
                rtweets.pop()

                print(rtweets)
                for i in range(len(rtweets)):
                    if len(rtweets[i]) > 0:
                        if rtweets[i][0] != "@":
                            word = word + str(rtweets[i]) + " "
                for i in range(len(word)):
                    rword = rword + word[i]
                rrword = remove_emoji(rword)
                query = "(" + rrword.replace(":","").replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ") + ")"
                ssss = rword
                print(query)
            else:
                ass = remove_word(tweet_split[0].split(" "))
                ssss = ' '.join(ass)
                query = "(" + remove_emoji(ssss.replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ")) + ")"
        elif len(get_status.text) > 100:
            rtweet = remove_word2(tweet_split)
            rtweets = rtweet[0]
            rtweets = rtweets.split(" ")
            too_long = 1
            print(rtweets)
            print("pppppppppppppp")
            #time.sleep(10000)
            rtweets.pop()
            rtweets.pop()
            rtweets.pop()

            print(rtweets)
            for i in range(len(rtweets)):
                if rtweets[i][0] != "@":
                    word = word + str(rtweets[i]) + " "
            for i in range(len(word)):
                rword = rword + word[i]
            query = "(" + remove_emoji(rword.replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ")) + ")"
            ssss = rword
            print(query)
        else:
            ass = remove_word(tweet_split[0].split(" "))
            print("asssssssssssssssss")
            print(ass)
            print(len(ass))
            print("asssssssssssssssss")

            if len(ass) > 3:
                little_word = 0
            else:
                little_word = 1
            ssss = ' '.join(ass)
            print("ssd")
            print(sssd)
            query = "(" + remove_emoji(ssss.replace(":","").replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ")) + ")"
            qquery = "(" + tweet_split[0] + ")"
        #print(tweet_split[0])
        #print("qqqqqq")
        #print(qquery)
        #print("qqqqqq")
        #print(query)
        #print("qqqqq")
        #print(query)
        #print(len(tweets))
        if len(tweet_split) == 2 and tweet_split[0] == '':
            only_pic = 1
        else:
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                max_time = max_time - 1
                if len(tweets) == limits or max_time < 0:
                    break
                else:
                    bss = remove_word2(tweet.content.split(" "))
                    bsss = ' '.join(bss)
                    if image_inside == 0:
                        if ssss.lower() in bsss.lower() and little_word == 1 and check_similarity(ssss,bsss,60) == 1:
                            #print(remove_word(tweet.content.split(" ")))
                            idx = idx + 1
                            tweets.append(tweet.id)
                            if look_user == look_user:
                                shadow = False

                            #tweet_date.append(tweet.date)
                        elif little_word == 0 and check_similarity(ssss,bsss,60) == 1:
                            idx = idx + 1
                            tweets.append(tweet.id)
                            if look_user == look_user:
                                shadow = False

                            #tweet_date.append(tweet.date)
                    else:
                        dss = remove_word(tweet.content.split(" "))
                        dsss = ' '.join(dss)
                        if "https://t.co/" in dsss and check_similarity(ssss,dsss,60) == 1:
                            idx = idx + 1
                            tweets.append(tweet.id)
                            if look_user == look_user:
                                shadow = False



        #print(len(tweets))
        #print(tweets[0])
        print("caca")
        if only_pic == 1:
            return('@' + your_name + " Le tweet contient que des photos ou vidéo je ne peux pas l'analyser",mention_id)
        else:
            if shadow == False:
                if len(tweets) == 0:
                    never_done = 1
                    url = f"https://twitter.com/user/status/"
                    #tid = tweets[len(tweets)]
                else:
                    url = f"https://twitter.com/user/status/{tweets[len(tweets) - 1]}"
                    tid = tweets[len(tweets) - 1]
                if len(tweet_split) == 1 or too_long == 1:
                    print("Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url))
                    #print(tid,copy_tweet.in_reply_to_status_id)
                    if idx > 1 and idx <= 999 and never_done == 0:
                        if copy_tweet == tid:
                            return('@' + your_name + " Le tweet a été fait " + str(idx) + " fois mais c'est l'originel",mention_id)
                        else:
                            return('@' + your_name + " Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url),mention_id)
                        time.sleep(wait_time2)
                    elif idx > 999 and never_done == 0:
                        if copy_tweet == tid:
                            return('@' + your_name + " Le tweet a été fait + de 1000 fois mais c'est l'originel",mention_id)
                        else:
                            return('@' + your_name + " Le tweet a été fait + de 1000 fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention_id)
                        time.sleep(wait_time2)
                    else:
                        return('@' + your_name + " Le tweet a été fait 0 fois il est donc originel ",mention_id)
                        time.sleep(wait_time2)
                elif len(tweet_split) > 1 and tweet_split[0][0] != '@':
                    #("Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url))
                    if idx > 1 and idx <= 999 and never_done == 0:
                        if copy_tweet == tid:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois mais c'est l'originel",mention_id)
                        else:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url),mention_id)
                        time.sleep(wait_time2)
                    elif idx > 999 and never_done == 0:
                        if copy_tweet == tid:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois mais c'est l'originel",mention_id)
                        else:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention_id)
                        time.sleep(wait_time2)
                    else:
                        return('@' + your_name + " Le tweet a été fait 0 fois il est donc originel ",mention_id)
                        time.sleep(wait_time2)
                elif len(tweet_split) == 2 and "t.co" in tweet_split[1]:
                    if idx > 1 and idx <= 999 and never_done == 0:
                        if copy_tweet == tid:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois mais c'est l'originel",mention_id)
                        else:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url),mention_id)
                        time.sleep(wait_time2)
                    elif idx > 999 and never_done == 0:
                        if copy_tweet == tid:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois mais c'est l'originel",mention_id)
                        else:
                            return('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention_id)
                        time.sleep(wait_time2)
                    else:
                        return('@' + your_name + " Le tweet a été fait 0 fois il est donc originel ",mention_id)
                        time.sleep(wait_time2)
            else:
                return('@' + your_name + " Le tweet a été fait " + str(idx + 1) + " fois mais c'est l'originel",mention_id)
                time.sleep(wait_time2)

    except tweepy.TweepError as e:
        if str(e) == "[{'code': 136, 'message': 'You have been blocked from the author of this tweet.'}]":
            return('@' + your_name + " Désolé je ne peux pas analyser ce tweet l'utilisateur m'a bloqué. ",mention_id)
            time.sleep(wait_time2)
    except IndexError:
            return('@' + your_name + " Le tweet contient que des photos ou vidéo ou il est trop long je ne peux pas l'analyser",mention_id)
            time.sleep(wait_time2)
    except:
        print("Désolé je ne peux pas analyser ce tweet.")
        return('@' + your_name + " Désolé je ne peux pas analyser ce tweet. ",mention_id)
        time.sleep(wait_time2)

def file_to_list(filepath):
    file_lenght = len(print_file(filepath).split("\n"))
    lst = []
    tag_idx = 0
    for i in range(file_lenght - 1):
        l = file_line_line(filepath,i).replace('\n','')
        lst.append(l)
    return (lst)

def bot_laucnher(test,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    print(test)

    #API_KEY = "DP5Gj0TCU1vsqiCHgkvMSRFrA"
    #API_SECRET = "vNq6dLt92Ob4SPvEe656RkPGNvhlUNkOMIQ9Ww340wTNqVcQgv"
    #ACCESS_TOKEN = "1440277404346294272-FKITRSUI1zLCIQ53qk1e0KGFPBAf90"
    #ACCESS_TOKEN_SECRET = "v2QPT8ISI5cBeVd2XBL5Vef9qbu8ReX2jxlLqbIqtXlmD"

    since_id = 1
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    i = 0
    wait_time = 20
    wait_time2 = 20
    last_seen_id = print_file("id.txt")
    try:
        mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
        #print("F2")
        idx = 0
        today = dta.today()
        t_today = int(str(today).replace("-",""))
        r_today = int(str(print_file("last_date.txt")).replace("-",""))
        bad_user = 0

        if datetime.datetime.today().weekday() == 1 and t_today != r_today:
            write_id("last_date.txt",today)
            write_id("insulte.txt","")

        for mention in reversed(mentions):
            #print("F3")
            texts = mention.full_text
            text = texts
            text = text.replace("  "," ")
            text = text.replace("   "," ")
            text = text.replace("    "," ")
            text = text.replace("     "," ")
            text = text.replace("      "," ")
            text = text.replace("       "," ")
            text = text.replace("        "," ")
            text = text.replace("         "," ")
            text = text.replace("          "," ")
            text = text.split(" ")
            remove_cherche = mention.full_text.lower().split(" ")
            launc_cherche = 0
            for i in range(len(remove_cherche)):
                if "cherche" == remove_cherche[i]:
                    launc_cherche = 1
            #tt_text = text
            #del tt_text[0]
            #word_before = word_pos(text,"cherche") - 1
            space = ""
            if check_text(text) == len(text) and len(text) > 1 or check_text(text) == len(text) and len(text) == 1 and text[0] != "@TwittosBot":
                del text[0]
                print("rrrrrr")
            else:
                print("bbbbbb")
            time.sleep(1)
            text_with_no_az = remove_word(text)
            str_text = ' '.join(text_with_no_az)
            #print("STR TEXT = ", str_text)
            #print(tt_text)
            l = len(text)
            #print("F4")

            insulte = file_to_list("insultes_list.txt")
            file_lenght = len(print_file("insulte.txt").split("\n"))

            url_list = []
            tag_list = []
            tag_idx = 0
            bad_user = 0
            for i in range(file_lenght - 1):
                l = file_line_line("insulte.txt",i).replace('\n','').split(" ")
                url_list.append(l[1])
                tag_list.append(l[0])

            for i in range(len(tag_list)):
                if mention.user.screen_name in tag_list[i]:
                    tag_idx = i
                    break

            print(text)
            print(mention.full_text.lower())
            print(text_with_no_az)
            #print(tt_text)
            l = len(text)
            #print("F4")


            if check_text(text) == len(text) and "@TwittosBot" in text and text[-1].lower() == "@twittosbot" and bad_user == 0:
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                nbr = int(print_file("nbr.txt"))
                your_name = mention.user.screen_name
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                api.update_status('@' + your_name + " Tu n'as pas l'air de bien savoir comment je fonctionne regarde mon tweet épinglé et tu comprendras. " + str(nbr),mention.id)
                print("ok")
                time.sleep(20)
            if "tweet" in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2].lower()== "tweet" and bad_user == 0:
                if len(text) > 2:
                    nbr = int(print_file("nbr.txt"))
                    if nbr > 1:
                        write_id("nbr.txt","0")
                    nbr = int(print_file("nbr.txt"))
                    last_seen_id = mention.id
                    write_id("id.txt",last_seen_id)
                    write_id("your_name.txt",mention.user.screen_name)
                    m = print_file("mention.txt")
                    your_name = print_file("your_name.txt")
                    m = print_file("mention.txt")
                    username = str(text[len(text) - 1])
                    try:
                        user = api.get_user(username)
                        ageTwitterAccount = user.created_at
                        o = ageTwitterAccount
                        write_id("date.txt",o)
                        date = print_file("date.txt")
                        date = date.split(" ")
                        write_id("date.txt",date[0])
                        ndate = print_file("date.txt")
                        year = ndate[0] + ndate[1] + ndate[2] + ndate[3]
                        month = ndate[5] + ndate[6]
                        day = ndate[8] + ndate[9]
                        now = datetime.datetime.now()
                        today = datetime.date.today()
                        today_date = now.strftime("%Y-%m-%d")
                        td = today_date.split("-", 3)
                        statuses_count = user.statuses_count
                        print(td[0],td[1],td[2])
                        print(year,month,day)
                        a = int(td[0]) - int(year)
                        b = int(td[1]) - int(month)
                        c = int(td[2]) - int(day)
                        print(a,b,c)
                        dday = int(a*365)+int(b*30.4167)+int(c)
                        res = int(int(statuses_count)/int(dday))
                        res2 = int(float(int(statuses_count)/int(dday)) * 7)
                        res2 = int(float(int(statuses_count)/int(dday)) * 7)
                        res3 = int(float(int(statuses_count)/int(dday)) * 30)
                        res4 = int(float(int(statuses_count)/int(dday)) * 365)
                        res5 = int(float(int(statuses_count)/int(dday)) * 3650)
                        m = str(month)
                        mm = []
                        month_name = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
                        for i in range(1):
                            if m[0] == "0":
                                mm.append(m[1])
                            else:
                                mm.append(m)
                        x = int(mm[0])
                        if statuses_count > 0:
                            if res >= 1:
                                print("Le compte le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res) + " tweets par jour." )
                                api.update_status('@' + your_name + " Le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res) + " tweets par jour. " + str(nbr),mention.id)
                                time.sleep(wait_time2)
                                nbr = nbr + 1
                                write_id("nbr.txt",str(nbr))
                            elif res2 >= 1:
                                print("Le compte le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res2) + " tweets par semaine.")
                                api.update_status('@' + your_name + " Le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res2) + " tweets par semaine. " + str(nbr),mention.id)
                                time.sleep(wait_time2)
                                nbr = nbr + 1
                                write_id("nbr.txt",str(nbr))

                            elif res3 >= 1:
                                print("Le compte le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res3) + " tweets par mois")
                                api.update_status('@' + your_name + " Le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res3) + " tweets par mois. " + str(nbr),mention.id)
                                time.sleep(wait_time2)
                                nbr = nbr + 1
                                write_id("nbr.txt",str(nbr))

                            elif res4 >= 1:
                                print("Le compte le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res4) + " tweets par an")
                                api.update_status('@' + your_name + " Le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res4) + " tweets par an. " + str(nbr),mention.id)
                                time.sleep(wait_time2)
                                nbr = nbr + 1
                                write_id("nbr.txt",str(nbr))

                            elif res5 >= 1:
                                print("Le compte le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res5) + " tweets par décennie")
                                api.update_status('@' + your_name + " Le compte a été créé le " + str(day) + " " + str(month_name[x - 1]) + " " + str(year) + " et a tweeté " + str(statuses_count) + " fois ce qui fait environ " + str(res5) + " tweets par décennie. " + str(nbr),mention.id)
                                time.sleep(wait_time2)
                                nbr = nbr + 1
                                write_id("nbr.txt",str(nbr))

                        elif statuses_count == 0:
                            print("Désolé l'utilisateur n'a jamais tweet")
                            time.sleep(wait_time2)
                    except:
                        time.sleep(wait_time)
                        api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                        print("Désolé je ne peux pas analyser ce compte")

            elif "coms\n" in mention.full_text or "koms\n" in mention.full_text  or "mot\n" in mention.full_text or "stat\n" in mention.full_text or "mot\n" in mention.full_text and bad_user == 0:
                your_name = mention.user.screen_name
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                api.update_status('@' + your_name + " Désolé mais tu t'es trompé il faut tout mettre sur la même ligne. " + str(nbr),mention.id)
                time.sleep(wait_time)

            elif "koms" in mention.full_text.lower() and "koms\n" not in mention.full_text.lower() and text[len(text) - 2]== "koms" and bad_user == 0:
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                ##username = str(text[len(text) - 1])
                username = str(text[len(text) - 3])
                uuu = str(text[len(text) - 1])
                uuu = uuu.replace("@","")
                uuu = "#" + uuu
                uuu = uuu.lower()
                your_name = mention.user.screen_name
                res = 0
                res2 = 0
                c = 0
                s = 0
                acc_to_find = 0
                print(username,uuu)
                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id
                    tag = []
                    tag_name = []
                    tag_nbr = []
                    tag_all_nbr = []
                    tag_n = []
                    reply_nbr = 0
                    found = 0
                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        a = all_tweets[i].full_text
                        b = all_tweets[i].full_text.split(" ")
                        if a [0] == "@":
                            reply_nbr = reply_nbr + 1
                            tag.append(b[0].lower())
                    for i in range(len(tag)):
                        dx = tag.count(tag[i])
                        if tag[i] not in tag_name:
                            tag_n.append(tag[i].lower().replace("@","#") )
                            tag_nbr.append(dx)
                            tag_all_nbr.append(dx)
                            tag_name.append(tag[i].lower())
                        tag_name.append(tag[i])
                    if len(tag_all_nbr) > 0:
                        tag_all_nbr.sort()
                        X = tag_n
                        Y = tag_nbr
                        Z = [x for _,x in sorted(zip(Y,X))]
                        final = []
                        for i in range(len(Z)):
                            lenz = len(Z) - 1
                            lenn = len(tag_all_nbr) - 1
                            res = float((tag_all_nbr[lenn-i]/reply_nbr) * 100)
                            res = round(res,1)
                            final.append(Z[lenz-i]+ " " + str(tag_all_nbr[lenn-i]) +" fois " + "≈ " + str(res) + "%")
                        ld = len(final)
                        for i in range(len(final)):
                            t_final = final[i].split(" ")
                            if t_final[0] == uuu:
                                print(final[i],t_final)
                                acc_to_find = i
                                found = 1
                                break
                        if found == 1:
                            api.update_status('@' + your_name + " D'après ses " +str(reply_nbr) + " dernier commentaires le compte a commenté ou répondu à :" + "\n" + "\n" + final[acc_to_find]+ "\n" + str(nbr),mention.id)
                            print("ok")
                            time.sleep(wait_time2)
                            nbr = nbr + 1
                            write_id("nbr.txt",str(nbr))
                        else:
                            print("nothing was found")
                            api.update_status('@' + your_name + " D'après ses " +str(reply_nbr) + " dernier commentaires le compte n'a jamais commenté ou répondu à " + uuu + " " + str(nbr),mention.id)
                            time.sleep(wait_time2)
                            nbr = nbr + 1
                            write_id("nbr.txt",str(nbr))
                except:
                    time.sleep(10)
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                    print("Désolé je ne peux pas analyser ce compte")

            elif "like" in mention.full_text.lower() and "like\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "like" and bad_user == 0:
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                    nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                username = str(text[len(text) - 1]).replace("@","")
                your_name = mention.user.screen_name
                tweet_nbr = 0
                com_nbr = 0
                rt_nbr = 0
                tweet_res = 0
                com_res = 0
                rt_res = 0
                w = []
                x = []
                y = []

                d = 0
                res = 0
                res2 = 0
                res3 = 0
                ll = 0
                ll2 = 0
                ll3 = 0
                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id

                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        a=all_tweets[i].full_text
                        ll = ll + 1
                        w.append(all_tweets[i].favorite_count)
                        if a[0] == "@":
                            x.append(all_tweets[i].favorite_count)
                            ll2 = ll2 + 1

                        else:
                            y.append(all_tweets[i].favorite_count)
                            ll3 = ll3 + 1

                    w.sort()
                    x.sort()
                    y.sort()

                    for i in range(len(w)):
                        res = res + w[i]
                    for i in range(len(x)):
                        res2 = res2 + x[i]
                    for i in range(len(y)):
                        res3 = res3 + y[i]

                    #res = round(res,0)
                    res_t = int(res/len(w))
                    if len(x) == 0:
                        res_l = 0
                    else:
                        res_l = int(res2/len(x))
                    if len(y) == 0:
                        res_r = 0
                    else:
                        res_r = int(res3/len(y))
                    print(res_t,res,res_l,res2,res_r,res3)
                    print("D'après ses " + str(len(w)) + " derniers tweets\commentaires le compte a : \n" + str(ll) + " tweets et commentaires = " + str(res) + " likes ≈ " + str(res_t) + " likes par commentaires et tweets.\n" + str(ll3) + " tweets = " + str(res3) + " likes ≈ " + str(res_r) + " likes par tweets.\n" + str(ll2) + " commentaires = " + str(res2) + " likes ≈ " + str(res_l) + " likes par commentaires.\n")
                    api.update_status('@' + your_name + " D'après ses " + str(len(w)) + " derniers tweets\commentaires le compte a : \n" + str(ll) + " tweets et commentaires = " + str(res) + " likes ≈ " + str(res_t) + " likes par commentaires et tweets.\n" + str(ll3) + " tweets = " + str(res3) + " likes ≈ " + str(res_r) + " likes par tweets.\n" + str(ll2) + " commentaires = " + str(res2) + " likes ≈ " + str(res_l) + " likes par commentaires.\n" + str(nbr),mention.id)
                    time.sleep(wait_time)
                except:
                    print("Désolé je ne peux pas analyser ce compte.")
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                    time.sleep(wait_time)
            elif "ajd" in mention.full_text.lower() and "ajd\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "ajd" and bad_user == 0:
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                    nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                username = str(text[len(text) - 1]).replace("@","")
                your_name = mention.user.screen_name
                td = 0
                now = datetime.datetime.now()
                today = datetime.date.today()
                today_date = now.strftime("%Y-%m-%d")
                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = True,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id
                    w = 0
                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = True,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        a=all_tweets[i].full_text
                        date  = all_tweets[i].created_at + timedelta(hours=2)
                        ddd = str(date)
                        if today_date in ddd:
                            td = td + 1
                            #print(a,date,td,w)
                    print("L'utilisateur a tweeté " + str(td) + " fois aujourd'hui.")
                    api.update_status('@' + your_name + " L'utilisateur a tweeté " + str(td) + " fois aujourd'hui." + str(nbr),mention.id)
                    nbr = nbr + 1
                    write_id("nbr.txt",str(nbr))
                    time.sleep(wait_time)
                except:
                    print("Désolé je ne peux pas analyser ce compte.")
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                    time.sleep(wait_time)
            elif "her" in mention.full_text.lower() and "her\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "her" and bad_user == 0:
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                    nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                username = str(text[len(text) - 1]).replace("@","")
                your_name = mention.user.screen_name
                td = 0
                today = datetime.date.today()

                yesterday = today - datetime.timedelta(days=1)
                today_date = yesterday.strftime("%Y-%m-%d")

                zz = 0
                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id
                    w = 0
                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        a=all_tweets[i].full_text
                        date  = all_tweets[i].created_at + timedelta(hours=2)
                        ddd = str(date)
                        if today_date in ddd:
                            td = td + 1
                            #print(a,date,td,w)
                    print("L'utilisateur a tweeté " + str(td) + " fois hier.")
                    api.update_status('@' + your_name + " L'utilisateur a tweeté " + str(td) + " fois hier." + str(nbr),mention.id)
                    nbr = nbr + 1
                    write_id("nbr.txt",str(nbr))
                    time.sleep(wait_time)
                except:
                    print("Désolé je ne peux pas analyser ce compte.")
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)

            elif "mot" in mention.full_text.lower() and "mot\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "mot" and bad_user == 0:
                #username=us
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                    nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                username = str(text[len(text) - 1]).replace("@","")
                your_name = mention.user.screen_name
                res = 0
                res2 = 0
                nbr_car = 0
                twt_nbr = 0
                nbr_word = 0
                a=0
                dddd=0
                #if dddd==0:
                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id

                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        #a=len()
                        td = all_tweets[i].full_text.lower().split(" ")
                        tr = remove_word2(td)
                        len_l = get_len_list(tr)
                        len_word = get_len_word(td)
                        #print(tr,len_l,len_word)
                        nbr_car = nbr_car + len_l
                        nbr_word = nbr_word + len(all_tweets[i].full_text.split(" ")) - len_word
                    twt_nbr = len(all_tweets)
                    res = int(nbr_word/len(all_tweets))
                    res2 = int(nbr_car/len(all_tweets))
                    myn = (res2/280)*100
                    print(str(nbr_car) + " " + str(res2) + " " + str(myn) + " " + str(nbr_word) + " " + str(res))
                    print("D'après ses " + str(twt_nbr) + " derniers tweets le compte a écrit " + str(nbr_word) + " mots et " + str(nbr_car) + " caractères ce qui fait une moyenne de " + str(res) + " mots et " + str(res2) + " caractères par tweet.")
                    api.update_status('@' + your_name + " D'après ses " + str(twt_nbr) + " derniers tweets le compte a écrit environ " + str(nbr_word) + " mots et " + str(nbr_car) + " caractères ce qui fait une moyenne de " + str(res) + " mots et " + str(res2) + " caractères par tweet. " + str(nbr),mention.id)
                    time.sleep(wait_time)
                except:
                    print("Désolé je ne peux pas analyser ce compte.")
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                    time.sleep(wait_time)
            elif "stat" in mention.full_text.lower() and "stat\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "stat" and bad_user == 0:
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                    nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                #username = us
                username = str(text[len(text) - 1]).replace("@","")
                your_name = mention.user.screen_name
                tweet_nbr = 0
                com_nbr = 0
                rt_nbr = 0
                tweet_res = 0
                com_res = 0
                rt_res = 0

                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = True,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id

                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = True,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        a=all_tweets[i].full_text
                        #print(a)
                        if a[0] == "@":
                            com_nbr = com_nbr + 1
                        elif a[0] == "R" and a[1] == "T":
                            rt_nbr = rt_nbr + 1
                        else:
                            tweet_nbr = tweet_nbr + 1
                    len_t = len(all_tweets)
                    tweet_res = (tweet_nbr/len_t)*100
                    com_res = (com_nbr/len_t)*100
                    rt_res = (rt_nbr/len_t)*100
                    tweet_res = round(tweet_res,2)
                    com_res = round(com_res,2)
                    rt_res = round(rt_res,2)
                    print(com_nbr,rt_nbr,tweet_nbr,tweet_res,com_res,rt_res,com_nbr+rt_nbr+tweet_nbr,len_t)
                    print("Nombre de tweet: " + str(tweet_nbr) + " Nombre de rt: " + str(rt_nbr) + " Nombre de commentaires: " + str(com_nbr) + " %" + " de tweet: " + str(tweet_res)  + " %" + " de rt: " + str(rt_res)  + " %" + " de coms: " + str(com_res) + " total " + str(len_t))
                    print("D'après ses " + str(len_t) + " dernier Tweets\Rt\Commentaires le compte a:\n"+str(tweet_nbr) + " Tweets\n"+str(com_nbr) + " Commentaires\n"+str(rt_nbr) + " Rt\n" + "Le compte a " + str(tweet_res) + " %" + " de Tweets " + str(com_res) + " %" + " de commentaire et " + str(rt_res) + " %" + " de rt.")
                    #print(str(nbr_car) + " " + str(res2) + " " + str(myn) + " " + str(nbr_word) + " " + str(res))
                    #print("D'après ses " + str(twt_nbr) + " derniers tweets le compte a écrit " + str(nbr_word) + " mots et " + str(nbr_car) + " caractères ce qui fait une moyenne de " + str(res) + " mots et " + str(res2) + " caractères par tweet.")
                    api.update_status('@' + your_name + " D'après ses " + str(len_t) + " dernier Tweets\Rt\Commentaires le compte a:\n"+str(tweet_nbr) + " Tweets\n"+str(com_nbr) + " Commentaires\n"+str(rt_nbr) + " Rt\n" + "Ce qui fait environ " + str(tweet_res) + "%" + " de Tweets, " + str(com_res) + "%" + " de Commentaire et " + str(rt_res) + "%" + " de Rt.\n" + str(nbr),mention.id)
                    time.sleep(wait_time)
                except:
                    print("Désolé je ne peux pas analyser ce compte.")
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                    time.sleep(wait_time)
            elif "coms" in mention.full_text.lower() and "coms\n" not in mention.full_text.lower() and text[len(text) - 2]== "coms" and bad_user == 0:
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                username = str(text[len(text) - 1])
                your_name = mention.user.screen_name
                res = 0
                res2 = 0
                c = 0
                s = 0
                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id
                    tag = []
                    tag_name = []
                    tag_nbr = []
                    tag_all_nbr = []
                    tag_n = []
                    reply_nbr = 0
                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = False,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        a = all_tweets[i].full_text
                        b = all_tweets[i].full_text.split(" ")
                        if a [0] == "@":
                            reply_nbr = reply_nbr + 1
                            tag.append(b[0])
                    for i in range(len(tag)):
                        dx = tag.count(tag[i])
                        if tag[i] not in tag_name:
                            tag_n.append(tag[i].replace("@","#") )
                            tag_nbr.append(dx)
                            tag_all_nbr.append(dx)
                            tag_name.append(tag[i])
                        tag_name.append(tag[i])
                    if len(tag_all_nbr) > 0:
                        tag_all_nbr.sort()
                        X = tag_n
                        Y = tag_nbr
                        Z = [x for _,x in sorted(zip(Y,X))]
                        final = []
                        for i in range(len(Z)):
                            lenz = len(Z) - 1
                            lenn = len(tag_all_nbr) - 1
                            if i < 5:
                                res = float((tag_all_nbr[lenn-i]/reply_nbr) * 100)
                                res = round(res,1)
                                final.append(Z[lenz-i]+ " " + str(tag_all_nbr[lenn-i]) +" fois " + "≈ " + str(res) + "%")
                        ld = len(final)
                        for i in range(len(final)):
                            print(final[i])
                        if ld == 5:
                            api.update_status('@' + your_name + " D'après ses " +str(reply_nbr) + " dernier commentaires le compte a commenté ou répondu à :" + "\n" + "\n" +final[0] + "\n" + final[1] + "\n" + final[2] + "\n" + final[3] + "\n" + final[4] + "\n" + str(nbr),mention.id)
                            print("ok")
                            time.sleep(wait_time2)
                            nbr = nbr + 1
                            write_id("nbr.txt",str(nbr))

                        if ld == 4:
                            api.update_status('@' + your_name + " D'après ses " +str(reply_nbr) + " dernier commentaires le compte a commenté ou répondu à :" + "\n" + "\n" + final[0] + "\n" + final[1] + "\n" + final[2] + "\n" + final[3] + "\n" + str(nbr),mention.id)
                            print("ok")
                            time.sleep(wait_time2)
                            nbr = nbr + 1
                            write_id("nbr.txt",str(nbr))

                        if ld == 3:
                            api.update_status('@' + your_name + " D'après ses " +str(reply_nbr) + " dernier commentaires le compte a commenté ou répondu à :" + "\n" + "\n" + final[0] + "\n" + final[1] + "\n" + final[2]+ "\n" + str(nbr),mention.id)
                            print("ok")
                            time.sleep(wait_time2)
                            nbr = nbr + 1
                            write_id("nbr.txt",str(nbr))
                        if ld == 2:
                            api.update_status('@' + your_name + " D'après ses " +str(reply_nbr) + " dernier commentaires le compte a commenté ou répondu à :" + "\n" + "\n" + final[0] + "\n" + final[1]+ "\n" + str(nbr),mention.id)
                            print("ok")
                            time.sleep(wait_time2)
                            nbr = nbr + 1
                            write_id("nbr.txt",str(nbr))

                        if ld == 1:
                            api.update_status('@' + your_name + " D'après ses " +str(reply_nbr) + " dernier commentaires le compte a commenté ou répondu à :" + "\n" + "\n" + final[0]+ "\n" + str(nbr),mention.id)
                            print("ok")
                            time.sleep(wait_time2)
                            nbr = nbr + 1
                            write_id("nbr.txt",str(nbr))

                except:
                    time.sleep(wait_time)
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                    print("Désolé je ne peux pas analyser ce compte")

            elif "@twittosbot analyse ce tweet" in mention.full_text.lower() or "@twittosbot  analyse ce tweet" in mention.full_text.lower() or "@twittosbot   analyse ce tweet" in mention.full_text.lower() or "@twittosbot     analyse ce tweet" in mention.full_text.lower() and bad_user == 0:
                print("aaaaanalyse")
                your_name = mention.user.screen_name
                write_id("user_name.txt",your_name)
                idx = 0
                only_pic = 0
                last_seen_id = mention.id
                status = api.get_status(mention.id)
                write_id("id.txt",last_seen_id)
                write_id("get_mention.txt",mention.id)
                look_user = ""
                shadow = True
                try:
                    copy_tweet = api.get_status((mention.id),tweet_mode = "extended")
                    write_id("copy_tweet.txt",copy_tweet.in_reply_to_status_id)
                    get_status = api.get_status(copy_tweet.in_reply_to_status_id)
                    look_user = get_status.user.screen_name
                    #n_tweet_date = status.created_at
                    write_id("get_status.txt",get_status)
                    tweets = []
                    limits = 1000
                    idx = 0
                    never_done = 0
                    original_tweet = get_status.text
                    print("oooooriginl")
                    print(original_tweet)
                    image_inside = 0
                    if "https://" in original_tweet and len(original_tweet) < 100:
                        image_inside = 1
                    tweet_split = get_status.text.split("https://")
                    #print(get_status.text)
                    #print(tweet_split)
                    #print(tweet_split)
                    #ccprint("cjczoicjoezjcozejcoiejc")
                    az = tweet_split[0].replace("\n"," ")
                    #print("caca")
                    #print(az)
                    #print("caca")
                    word = ""
                    rword = ""
                    qquery = ""
                    query  = ""
                    max_time = 5000
                    sssd = ""
                    ssss = ""
                    little_word = 0
                    rtweet = ""
                    rtweets = ""
                    azz=""
                    rjoin = ""
                    too_long = 0
                    tweets_date = []
                    if az[0] == '@':
                        print("aaazz")
                        print(az)
                        if len(az) > 100:
                            azz = az.split(" ")
                            rtweet = remove_word2(azz)
                            rjoin = ' '.join(rtweet)
                            rtweets = rjoin
                            rtweets = rtweets.split(" ")

                            print(rtweets)
                            print("pppppppppppppp")
                            #time.sleep(10000)
                            too_long = 1
                            rtweets.pop()
                            rtweets.pop()
                            rtweets.pop()

                            print(rtweets)
                            for i in range(len(rtweets)):
                                if rtweets[i][0] != "@":
                                    word = word + str(rtweets[i]) + " "
                            for i in range(len(word)):
                                rword = rword + word[i]
                            query = "(" + remove_emoji(rword.replace(":","").replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ").replace("j'"," ")) + ")"
                            ssss = rword
                            print(query)
                        else:
                            ass = remove_word(tweet_split[0].split(" "))
                            ssss = ' '.join(ass)
                            query = "(" + remove_emoji(ssss.replace(":","").replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ").replace("j'"," ")) + ")"
                    elif len(get_status.text) > 100:
                        rtweet = remove_word2(tweet_split)
                        rtweets = rtweet[0].replace("\n"," ")
                        rtweets = rtweets.split(" ")
                        too_long = 1
                        print(rtweets)
                        print("pppppppppppppp")
                        #time.sleep(10000)
                        rtweets.pop()
                        rtweets.pop()
                        rtweets.pop()

                        print(rtweets)
                        for i in range(len(rtweets)):
                            if len(rtweets[i]) > 0:
                                if rtweets[i][0] != "@":
                                    word = word + str(rtweets[i]) + " "
                        for i in range(len(word)):
                            rword = rword + word[i]
                        query = "(" + remove_emoji(rword.replace(":","").replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ")) + ")"
                        ssss = rword
                        print(query)
                    else:
                        ass = remove_word(tweet_split[0].split(" "))
                        print("asssssssssssssssss")
                        print(ass)
                        print(len(ass))
                        print("asssssssssssssssss")
                        if len(ass) > 3:
                            little_word = 0
                        else:
                            little_word = 1
                        ssss = ' '.join(ass)
                        ssss = ssss.replace("\n"," ")
                        print("ssd")
                        print(sssd)
                        query = "(" + remove_emoji(ssss.replace(":","").replace(":","").replace('"',"").replace("«","").replace("»","").replace("-"," ").replace(".","").replace(","," ").replace("j'"," ")) + ")"
                        qquery = "(" + tweet_split[0] + ")"
                        print("qqqqqqqqqqqq")
                        print(query)
                    #print(tweet_split[0])
                    #print("qqqqqq")
                    #print(qquery)
                    #print("qqqqqq")
                    #print(query)
                    #print("qqqqq")
                    #print(query)
                    #print(len(tweets))
                    if len(tweet_split) == 2 and tweet_split[0] == '':
                        only_pic = 1
                    else:
                        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                            max_time = max_time - 1
                            #print(tweet.content)
                            #print(tweet.content)
                            if len(tweets) == limits or max_time < 0:
                                break
                            else:
                                bss = remove_word2(tweet.content.split(" "))
                                bsss = ' '.join(bss)

                                if image_inside == 0:
                                    if ssss.lower() in bsss.lower() and little_word == 1 and check_similarity(ssss,bsss,60) == 1:
                                        #print(remove_word(tweet.content.split(" ")))
                                        idx = idx + 1
                                        tweets.append(tweet.id)
                                        if look_user == look_user:
                                            shadow = False

                                        #tweet_date.append(tweet.date)
                                    elif little_word == 0 and check_similarity(ssss,bsss,60) == 1:
                                        idx = idx + 1
                                        tweets.append(tweet.id)
                                        if look_user == look_user:
                                            shadow = False
                                        #tweet_date.append(tweet.date)
                                else:
                                    dss = remove_word(tweet.content.split(" "))
                                    dsss = ' '.join(dss)
                                    if "https://t.co/" in dsss and check_similarity(ssss,dsss,60) == 1:
                                        idx = idx + 1
                                        tweets.append(tweet.id)
                                        if look_user == look_user:
                                            shadow = False

                    #print("original tweet")
                    #print(str(tweet_date[len(tweet_date) - 1]))
                    #print("-------")
                    #print("search tweet")
                    #print(str(n_tweet_date))
                    #print(len(tweets))
                    #print(tweets[0])
                    if shadow == True:
                        print("Shadooooooooooooooo")
                    print("caca")
                    if only_pic == 1:
                        api.update_status('@' + your_name + " Le tweet contient que des photos ou vidéo je ne peux pas l'analyser",mention.id)
                    else:
                        if shadow == False:
                            if len(tweets) == 0:
                                never_done = 1
                                url = f"https://twitter.com/user/status/"
                                #tid = tweets[len(tweets)]
                            else:
                                url = f"https://twitter.com/user/status/{tweets[len(tweets) - 1]}"
                                tid = tweets[len(tweets) - 1]
                            if len(tweet_split) == 1 or too_long == 1:
                                print("Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url))
                                #print(tid,copy_tweet.in_reply_to_status_id)
                                if idx > 1 and idx <= 999 and never_done == 0:
                                    if copy_tweet.in_reply_to_status_id == tid:
                                        api.update_status('@' + your_name + " Le tweet a été fait " + str(idx) + " fois mais c'est l'originel",mention.id)
                                    else:
                                        api.update_status('@' + your_name + " Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url),mention.id)
                                    time.sleep(wait_time2)
                                elif idx > 999 and never_done == 0:
                                    if copy_tweet.in_reply_to_status_id == tid:
                                        api.update_status('@' + your_name + " Le tweet a été fait + de 1000 fois mais c'est l'originel",mention.id)
                                    else:
                                        api.update_status('@' + your_name + " Le tweet a été fait + de 1000 fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention.id)
                                    time.sleep(wait_time2)
                                else:
                                    api.update_status('@' + your_name + " Le tweet a été fait 0 fois il est donc originel ",mention.id)
                                    time.sleep(wait_time2)
                            elif len(tweet_split) > 1 and tweet_split[0][0] != '@':
                                #("Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url))
                                if idx > 1 and idx <= 999 and never_done == 0:
                                    if copy_tweet.in_reply_to_status_id == tid:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois mais c'est l'originel",mention.id)
                                    else:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url),mention.id)
                                    time.sleep(wait_time2)
                                elif idx > 999 and never_done == 0:
                                    if copy_tweet.in_reply_to_status_id == tid:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois mais c'est l'originel",mention.id)
                                    else:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention.id)
                                    time.sleep(wait_time2)
                                else:
                                    api.update_status('@' + your_name + " Le tweet a été fait 0 fois il est donc originel ",mention.id)
                                    time.sleep(wait_time2)
                            elif len(tweet_split) == 2 and "t.co" in tweet_split[1]:
                                if idx > 1 and idx <= 999 and never_done == 0:
                                    if copy_tweet.in_reply_to_status_id == tid:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois mais c'est l'originel",mention.id)
                                    else:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url),mention.id)
                                    time.sleep(wait_time2)
                                elif idx > 999 and never_done == 0:
                                    if copy_tweet.in_reply_to_status_id == tid:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois mais c'est l'originel",mention.id)
                                    else:
                                        api.update_status('@' + your_name + " Le tweet contient une vidéo ou une photo (le résultat est moins précis) et il a été fait + de 1000 fois le tweet est donc copié voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention.id)
                                    time.sleep(wait_time2)
                                else:
                                    api.update_status('@' + your_name + " Le tweet a été fait 0 fois il est donc originel ",mention.id)
                                    time.sleep(wait_time2)
                        else:
                            api.update_status('@' + your_name + " Le tweet a été fait " + str(idx + 1) + " fois mais c'est l'originel",mention.id)
                            time.sleep(wait_time2)

                except tweepy.TweepError as e:
                    if str(e) == "[{'code': 136, 'message': 'You have been blocked from the author of this tweet.'}]":
                        get_status = print_file("get_status.txt")
                        copy_tweet = print_file("copy_tweet.txt")
                        blocked_tweet, tweet_id = blocked_by_user(get_status,int(copy_tweet))
                        print(str(blocked_tweet) + "   " + str(tweet_id))
                        api.update_status(blocked_tweet,tweet_id)
                        time.sleep(wait_time2)
                except IndexError:
                        api.update_status('@' + your_name + " Le tweet contient que des photos ou vidéo ou il est trop long je ne peux pas l'analyser",mention.id)
                        time.sleep(wait_time2)
                except Exception as e:
                    print(e)
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce tweet. ",mention.id)
                    time.sleep(wait_time2)

            elif "copie" in mention.full_text.lower() and text_with_no_az[0] == "copie" and bad_user == 0:
                print("coooopy")
                your_name = mention.user.screen_name
                idx = 0
                only_pic = 0
                last_seen_id = mention.id
                status = api.get_status(mention.id)
                write_id("id.txt",last_seen_id)
                max_time = 5000
                try:
                    word = ""
                    rword = ""
                    for i in range(l):
                        if text[i][0] != "@" and text[i] != "copie":
                            word = word + text[i] + " "
                    for i in range(len(word) - 1):
                        rword = rword + word[i]
                    print(rword,len(rword))
                    rword_len = rword.split(" ")
                    tweets = []
                    limits = 1000
                    idx = 0
                    query = "(" + rword.replace(":","").replace('"',"").replace("«","").replace("»","") + ")"
                    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                        max_time = max_time - 1
                        #print(len(tweets))
                        #print(tweet.content,rword)
                        if len(tweets) == limits or max_time < 0:
                            break
                        else:
                            if rword.lower() in tweet.content.lower() and rword_len == 1:
                                idx = idx + 1
                                tweets.append(tweet.id)
                            else:
                                idx = idx + 1
                                tweets.append(tweet.id)
                    if len(tweets) == 0:
                        print("ok")
                        #url = f"https://twitter.com/user/status/{tweets[len(tweets)]}"
                        #tid = tweets[len(tweets)]
                    else:
                        url = f"https://twitter.com/user/status/{tweets[len(tweets) - 1]}"
                        tid = tweets[len(tweets) - 1]
                    if len(rword) > 0:
                        print("Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url))
                        #print(tid,copy_tweet.in_reply_to_status_id)
                        if idx > 1 and idx <= 999:
                            api.update_status('@' + your_name + " Le tweet a été fait " + str(idx) + " fois voici le tweet originel (le plus ancien) " + str(url),mention.id)
                            time.sleep(wait_time2)
                        elif idx > 999:
                            api.update_status('@' + your_name + " Le tweet a été fait + de 1000 fois voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention.id)
                            time.sleep(wait_time2)
                        else:
                            api.update_status('@' + your_name + " Le tweet a été fait 0 fois",mention.id)
                            time.sleep(wait_time2)
                except:
                    print("Désolé je ne peux pas analyser ce tweet.")
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce tweet. ",mention.id)
                    time.sleep(wait_time2)

            elif "copic" in mention.full_text.lower() and text_with_no_az[0] == "copic" and bad_user == 0:
                print("coooopy")
                your_name = mention.user.screen_name
                idx = 0
                only_pic = 0
                last_seen_id = mention.id
                status = api.get_status(mention.id)
                write_id("id.txt",last_seen_id)
                max_time = 5000
                try:
                    word = ""
                    rword = ""
                    for i in range(l):
                        if text[i][0] != "@" and text[i] != "copic":
                            word = word + text[i] + " "
                    for i in range(len(word) - 1):
                        rword = rword + word[i]
                    print(rword,len(rword))
                    rword_len = rword.split(" ")
                    tweets = []
                    limits = 1000
                    idx = 0
                    query = "(" + rword.replace(":","").replace('"',"").replace("«","").replace("»","") + ")"
                    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                        max_time = max_time - 1
                        #print(len(tweets))
                        #print(tweet.content,rword)
                        if len(tweets) == limits or max_time < 0:
                            break
                        else:
                            if rword.lower() in tweet.content.lower() and rword_len == 1 and "https://t.co/" in tweet.content.lower():
                                idx = idx + 1
                                tweets.append(tweet.id)
                            elif "https://t.co/" in tweet.content.lower():
                                idx = idx + 1
                                tweets.append(tweet.id)
                    if len(tweets) == 0:
                        print("ok")
                        #url = f"https://twitter.com/user/status/{tweets[len(tweets)]}"
                        #tid = tweets[len(tweets)]
                    else:
                        url = f"https://twitter.com/user/status/{tweets[len(tweets) - 1]}"
                        tid = tweets[len(tweets) - 1]
                    if len(rword) > 0:
                        print("Le tweet a été fait " + str(idx) + " fois le tweet est donc copié voici le tweet originel (le plus ancien) " + str(url))
                        #print(tid,copy_tweet.in_reply_to_status_id)
                        if idx > 1 and idx <= 999:
                            api.update_status('@' + your_name + " Le tweet a été fait " + str(idx) + " fois voici le tweet originel (le plus ancien) " + str(url),mention.id)
                            time.sleep(wait_time2)
                        elif idx > 999:
                            api.update_status('@' + your_name + " Le tweet a été fait + de 1000 fois voici le tweet originel (le plus ancien des 1000 derniers) " + str(url),mention.id)
                            time.sleep(wait_time2)
                        else:
                            api.update_status('@' + your_name + " Le tweet a été fait 0 fois",mention.id)
                            time.sleep(wait_time2)
                except:
                    print("Désolé je ne peux pas analyser ce tweet.")
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce tweet. ",mention.id)
                    time.sleep(wait_time2)

            elif "freq" in mention.full_text.lower() and text_with_no_az[0] == "freq" and bad_user == 0:
                status = api.get_status(mention.id)
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                your_name = mention.user.screen_name
                try:
                    word = ""
                    rword = ""
                    for i in range(l):
                        if text[i][0] != "@" and text[i] != "freq":
                            word = word + text[i] + " "
                    for i in range(len(word) - 1):
                        rword = rword + word[i]
                    print(rword)
                    #print(rword)
                    tweets = []
                    text = rword
                    tweets_date = []
                    query = "(" + rword + ' lang:fr' + ")"
                    idx = 0
                    s = 0
                    limit = 999
                    month_name = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
                    max_time = 0
                    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
                        if s>limit or max_time > 2500:
                            break
                        sss = remove_trash(tweet.content.lower().split(" "))
                        ssss = ' '.join(sss)
                        if text in ssss:
                            #print(tweet.content.lower())
                            s = s + 1
                            url = f"https://twitter.com/user/status/{tweet.id}"
                            tweets.append(url)
                            tweets_date.append(tweet.date)
                        max_time = max_time + 1

                    if len(tweets) > 0:
                        now = datetime.datetime.now()
                        today = datetime.date.today()
                        today_date = now.strftime("%Y-%m-%d")
                        hour = now.strftime("%H:%M:%S")
                        td = today_date.split("-", 3)
                        tweet_date_split = tweets_date[len(tweets_date) - 1] + timedelta(hours=2)
                        tweet_date = str(tweets_date[len(tweets_date) - 1] + timedelta(hours=2))
                        print(str(tweets_date[len(tweets_date) - 1] + timedelta(hours=2)))
                        print("aaaaaaaaaaaaaaaaaa")
                        tweet_date = tweet_date.split(" ")
                        tweet_hour = tweet_date[1]
                        tweet_hour = tweet_hour[0:8]
                        tweet_date_split = re.split('-| ',str(tweet_date_split))
                        d0 = dta(int(tweet_date_split[0]), int(tweet_date_split[1]), int(tweet_date_split[2]))
                        d1 = dta(int(td[0]), int(td[1]), int(td[2]))
                        print(d0)
                        delta = d1 - d0
                        month = ""
                        year = ""
                        day = ""
                        hour = hour.split(':')
                        tweet_hour = tweet_hour.split(":")
                        convert_sec = int(hour[0]) * 3600 + int(hour[1]) * 60 + int(hour[2])
                        convert_sec_tweet = int(tweet_hour[0]) * 3600 + int(tweet_hour[1]) * 60 + int(tweet_hour[2])
                        if int(delta.days) > 0:
                            res_sec = int(delta.days) * 86400 + int(convert_sec_tweet)
                        else:
                            res_sec = 86400
                        final_res = int(convert_sec)
                        final_tweet_res = int(convert_sec_tweet) + int(delta.days) * 86400
                        if len(tweets) > 0:
                            print(tweets[len(tweets) - 1])
                        if int(delta.days) > 0 and s > 0:

                            resdecade = s/(res_sec/(60*60*24*7*30*365*3650))
                            resyear = s/(res_sec/(60*60*24*7*30*365))
                            resmonth = s/(res_sec/(60*60*24*7*30))
                            resweek = s/(res_sec/(60*60*24*7))
                            resday = s/(res_sec/(60*60*24))
                            reshour = s/(res_sec/(60*60))
                            resmin = s/(res_sec/60)
                            ressec = s/(res_sec)
                            if ressec >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(ressec)) + " tweet par seconde voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(ressec,0)) + " tweet par seconde voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)
                            elif resmin >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resmin)) + " tweet par minute voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resmin,0)) + " tweet par minute voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif reshour >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(reshour)) + " tweet par heure voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(reshour,0)) + " tweet par heure voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resday >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resday)) + " tweet par jour voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resday,0)) + " tweet par jour voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resweek >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resweek)) + " tweet par semaine voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resweek,0)) + " tweet par semaine voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resmonth >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resmonth)) + " tweet par mois voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resmonth,0)) + " tweet par mois voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resyear >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resyear)) + " tweet par an voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resyear,0)) + " tweet par an voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resdecade >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resdecade)) + " tweet par décenie voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resdecade,0)) + " tweet par décenie voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                        elif s > 0:
                            if int(convert_sec) > int(convert_sec_tweet):
                                res_sec = int(convert_sec) - int(convert_sec_tweet)
                            else:
                                res_sec = int(convert_sec_tweet) - int(convert_sec)
                            resdecade = s/(res_sec/(60*60*24*7*30*365*3650))
                            resyear = s/(res_sec/(60*60*24*7*30*365))
                            resmonth = s/(res_sec/(60*60*24*7*30))
                            resweek = s/(res_sec/(60*60*24*7))
                            resday = s/(res_sec/(60*60*24))
                            reshour = s/(res_sec/(60*60))
                            resmin = s/(res_sec/60)
                            ressec = s/(res_sec)
                            if ressec >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(ressec)) + " tweet par seconde voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(ressec,0)) + " tweet par seconde voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resmin >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resmin)) + " tweet par minute voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resmin,0)) + " tweet par minute voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif reshour >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(reshour)) + " tweet par heure voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(reshour,0)) + " tweet par heure voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)
                            elif resday >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resday)) + " tweet par jour voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resday,0)) + " tweet par jour voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resweek >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resweek)) + " tweet par semaine voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resweek,0)) + " tweet par semaine voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resmonth >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resmonth)) + " tweet par mois voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resmonth,0)) + " tweet par mois voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                            elif resyear >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resyear)) + " tweet par an voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resyear,0)) + " tweet par an voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)
                            elif resdecade >= 1:
                                print("Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(int(resdecade)) + " tweet par décenie voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ))
                                api.update_status('@' + your_name + " Après analyse des " + str(s) + " derniers tweets le tweet le plus ancien a été fait le " + tweet_date_split[2] + " " + month_name[int(tweet_date_split[1]) - 1] + " " + tweet_date_split[0] + " ce qui fait environ " + str(round(resdecade,0)) + " tweet par décenie voici le tweet le plus ancien contenant le mot/phrase " + str(tweets[len(tweets_date) - 1] ),mention.id)
                                time.sleep(20)

                    else:
                        print("le mot/phrase n'as jamais été tweet")
                        api.update_status('@' + your_name + " le mot/phrase n'as jamais été tweet",mention.id)
                        time.sleep(wait_time)
                except:
                    time.sleep(wait_time)
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " ,mention.id)
                    print("Désolé je ne peux pas analyser ce mot/phrase réesseaies dans 5 minutes ça marchera peut-être")

            elif launc_cherche == 1 and text[text.index("cherche") - 1][0] == "@" and bad_user == 0:
                #cherche_split = mention.full_text.lower().split("cherche")
                #print(cherche_split)

                if len(text) > 3 and check_text(text) >= 2 and check_baz(text) > 0:
                    word = ""
                    rword = ""
                    for i in range(l):
                        if text[i][0] != "@" and text[i] != "cherche":
                            word = word + text[i] + " "
                    for i in range(len(word) - 1):
                        rword = rword + word[i]
                    last_seen_id = mention.id

                    write_id("id.txt",last_seen_id)
                    write_id("username.txt",text[len(text) - 3 - count_space(rword)])
                    write_id("word.txt",rword)
                    write_id("mention.txt",str(mention.id))
                    write_id("your_name.txt",mention.user.screen_name)
                    username = print_file("username.txt")
                    word_to_find = print_file("word.txt")
                    m = print_file("mention.txt")
                    your_name = print_file("your_name.txt")
                    try:
                        tweets = api.user_timeline(screen_name=username,
                                                count=200,
                                                include_rts = False,
                                                tweet_mode = 'extended'
                                                )
                    except:
                        time.sleep(wait_time)
                        #api.update_status('@' + your_name + " " + "Désolé mais le compte est privé ou suspendu.",mention.id)
                        api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                        print("private account :(")
                        bot_laucnher(0,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

                    all_tweets = []
                    all_tweets.extend(tweets)
                    try:
                        oldest_id = tweets[-1].id

                        while True:
                            tweets = api.user_timeline(screen_name=username,
                                                count=200,
                                                include_rts = False,
                                                max_id = oldest_id - 1,
                                                tweet_mode = 'extended'
                                                )
                            if len(tweets) == 0:
                                break
                            oldest_id = tweets[-1].id
                            all_tweets.extend(tweets)
                    except:
                        print("error")
                        time.sleep(wait_time)
                    twt = []
                    nbr = 0
                    p = "%"
                    all_nbr = []

                    word = word_to_find
                    word = word.lower()
                    back_word = word
                    word = word.split(" ")
                    user = api.get_user(username)
                    statuses_count = user.statuses_count
                    if len(all_tweets) == 0:
                        time.sleep(wait_time)
                    for i in range(len(all_tweets)):
                        w = all_tweets[i].full_text.lower()
                        t = re.split('\!|\,|\;|\"|\?|\.|\*|\(|\)|\#| ',w)
                        w = w.lower()
                        td = all_tweets[i].full_text.lower().split(" ")
                        tr = remove_word(td)
                        set2 = set(tr)
                        set1 = set(w)
                        is_subset = set2.issubset(set1)
                        if len(word) > 1:
                            if back_word in all_tweets[i].full_text.lower() and i < 3001:
                                nbr = nbr + 1
                                all_nbr.append(i)
                        else:
                            if back_word in tr and i < 3001:
                                nbr = nbr + 1
                                all_nbr.append(i)
                    print(all_nbr)
                    if nbr > 0:
                        res = float(nbr/statuses_count) * 100
                        res = round(res,2)
                        res2 = float(nbr/3000) * 100
                        res2 = round(res2,2)
                    else:
                        res = 0
                        res2 = 0

                    if nbr > 0:
                        url = f"https://twitter.com/user/status/{all_tweets[all_nbr[0]].id}"
                        if statuses_count < 3000:
                            if check_text(text) <= 2:
                                time.sleep(wait_time)
                                api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot recherché sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.\n"+"voici le tweet le plus récent contenant ce mot " + url, mention.id)
                                #api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.", mention.id)
                                print('@' + your_name + " le compte  ggggggas tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.")
                                print('@' + your_name + " le compte ggggggvoici le tweet le plus ancien contenant ce mot " + url)

                            else:
                                time.sleep(wait_time)
                                api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot recherché sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.\n"+"voici le tweet le plus récent contenant ce mot " + url, mention.id)
                                #api.update_status('@' + your_name + " le compte voici le tweet le plus ancien contenant ce mot " + url, mention.id)
                                print('@' + your_name + " le compte  as tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.")
                                print("voici le tweet le plus ancien contenant ce mot " + url)
                                time.sleep(wait_time)

                        else:
                            if check_text(text) <= 2:
                                time.sleep(wait_time)
                                api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot recherché sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.\n"+"voici le tweet le plus récent contenant ce mot " + url, mention.id)
                                #api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.", mention.id)
                                print('@' + your_name + " le compte gggggas tweeté " + str(nbr) + " fois le mot " + back_word + " sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.")
                                print('@' + your_name + " le compte gggggggvoici le tweet le plus ancien contenant ce mot " + url)

                            else:
                                time.sleep(wait_time)
                                api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot recherché sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.\n"+"voici le tweet le plus récent contenant ce mot " + url, mention.id)
                                #api.update_status('@' + your_name + " le compte voici le tweet le plus ancien contenant ce mot " + url, mention.id)
                                print("Sur tes 3000 derniers tweets tu as tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de 3000 tweets ce qui représente environ " + str(res2) + " " + p + " de tes tweets.")
                                print("voici le tweet le plus récent contenant ce mot " + url)

                    else:
                        print("Désolé mais l'utilisateur n'a jamais tweeter ce mot")
                        if statuses_count < 3000:
                            time.sleep(wait_time)
                            api.update_status('@' + your_name + " " + "Désolé mais l'utilisateur n'a jamais tweeté ce mot.",mention.id)

                        if statuses_count >= 3000:
                            time.sleep(wait_time)
                            api.update_status('@' + your_name + " " + "Désolé mais l'utilisateur n'a pas tweeté ce mot sur ses 3000 derniers tweets.",mention.id)

                else:
                    print("nothing to sort")
    except Exception as e:
        print(e)
        time.sleep(40)

print("start")
print(remove_emoji("salut a tous les amis "))
key = 0
while True:
    print("Waitging!!!",key)
    time.sleep(15)
    try:
        bot_laucnher(0,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    except:
        print("No wifi")
        time.sleep(120)
    time.sleep(5)
    key = key + 1
    #exit(0)
    #PYTHON
    #gaymar
