#!/usr/bin/env python3

import datetime
import tweepy
import logging
import time
from random import randint
from os import system
import sys
import re

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])

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

def bot_laucnher(test,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    print(test)
    
    since_id = 1
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    i = 0
    wait_time = 40
    wait_time2 = 40
    last_seen_id = print_file("id.txt")
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    #print("F2")
    idx = 0
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
        print(text)
        #print(tt_text)
        l = len(text)
        #print("F4")
        
        if check_text(text) == len(text) and "@TwittosBot" in text:
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
        if text[len(text) - 2] == "tweet" and text[len(text) - 1][0]== "@":
            nbr = int(print_file("nbr.txt"))
            if nbr > 1:
                 write_id("nbr.txt","0")
            nbr = int(print_file("nbr.txt"))

            last_seen_id = mention.id
            write_id("id.txt",last_seen_id)
            write_id("your_name.txt",mention.user.screen_name)
            m = print_file("mention.txt")
            your_name = print_file("your_name.txt")
            print("Il faut mettre un T majuscule à Tweet sinon ça ne marche pas")     
            api.update_status('@' + your_name + " Il faut mettre un T majuscule à Tweet sinon ça ne marche pas. " + str(nbr),mention.id)   
            time.sleep(40)
            nbr = nbr + 1
            write_id("nbr.txt",str(nbr))
                        
        if "Tweet" in mention.full_text and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "Tweet":
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
                    time.sleep(40)
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)   
                    print("Désolé je ne peux pas analyser ce compte")

        elif "coms\n" in mention.full_text or "koms\n" in mention.full_text  or "mot\n" in mention.full_text or "stat\n" in mention.full_text or "mot\n" in mention.full_text:
            your_name = mention.user.screen_name
            nbr = int(print_file("nbr.txt"))
            if nbr > 1:
                write_id("nbr.txt","0")
            nbr = int(print_file("nbr.txt"))
            last_seen_id = mention.id
            write_id("id.txt",last_seen_id)
            api.update_status('@' + your_name + " Désolé mais tu t'es trompé il faut tout mettre sur la même ligne. " + str(nbr),mention.id)   
            time.sleep(40)
        
        
        elif "zdddfgico" in mention.full_text.lower() and "zddico\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@":
                file = open("dico.txt","w")
                file.close()
                asciis = []
                for i in range(33,126):
                    asciis.append(chr(i))
                nbr = int(print_file("nbr.txt"))
                if nbr > 1:
                    write_id("nbr.txt","0")
                nbr = int(print_file("nbr.txt"))
                last_seen_id = mention.id
                write_id("id.txt",last_seen_id)
                username = str(text[len(text) - 1])
                your_name = mention.user.screen_name
                tweet_nbr = 0
                com_nbr = 0
                rt_nbr = 0
                tweet_res = 0
                com_res = 0
                rt_res = 0
                all_word = []
                ccc = 0
                try:
                    tweets = api.user_timeline(screen_name=username,count=200,include_rts = True,tweet_mode = 'extended')
                    all_tweets = []
                    all_tweets.extend(tweets)
                    oldest_id = tweets[-1].id
                    unique_word = []
                    word_count = []
                    word_count2 = []
                    word_word = []
                    nothing  = 0
                    while True:
                        tweets = api.user_timeline(screen_name=username,count=200,include_rts = True,max_id = oldest_id - 1,tweet_mode = 'extended')
                        if len(tweets) == 0:
                            break
                        oldest_id = tweets[-1].id
                        o_id = tweets[len(tweets) - 1].id
                        all_tweets.extend(tweets)
                    for i in range(len(all_tweets)):
                        a=all_tweets[i].full_text
                        td = all_tweets[i].full_text.lower().split(" ")
                        #ta = td.split(" ")
                        #print(t)
                        tr = remove_word2(td)
                        for k in range(len(tr)):
                            #print(tr[k])
                            all_word.append(tr[k])
                    for i in range(len(all_word)):
                        if all_word[i] not in unique_word:
                            unique_word.append(all_word[i])
                    for i in range(len(unique_word)):
                        dx = all_word.count(unique_word[i])
                        #print(dx,unique_word[i])
                        word_count.append(dx)
                        word_count2.append(dx)
                        word_word.append(unique_word[i])
                    word_count.sort()
                    X = word_word
                    Y = word_count2
                    Z = [x for _,x in sorted(zip(Y,X))]
                    for i in range(len(Z)):
                        res = (word_count[i]/len(all_word)) * 100
                        rr = round(res, 2)
                        if i >= len(Z) - 102:
                            print(Z[i],word_count[i],len(Z)-i)
                            wwrite_id("dico.txt",":  " + str(Z[i]) + " " + str(word_count[i]))
                            wwrite_id("dico.txt","\n")

                    if len(unique_word) < 100:
                        text_to_pic(len(unique_word))
                    else:
                        text_to_pic(100)
                    idd = mention.id
                    pic = "/home/pi/first_tweet/dico.jpg"
                    tweet = "Test"
                    wrd = "Après l'analyse de ses " + str(len(all_tweets)) + " dernier tweets l'utilisateur a écrit " + str(len(unique_word)) + " mots différents voici les 100 mots les plus utilisé: "
                    t = '@' + your_name + " " + wrd
                    api.update_with_media(filename = pic, status = t ,in_reply_to_status_id = idd)          
                    time.sleep(20)
                except:
                    time.sleep(40)
                    api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)   
                    print("Désolé je ne peux pas analyser ce compte")  
        
        elif "koms" in mention.full_text.lower() and "koms\n" not in mention.full_text.lower() and text[len(text) - 2]== "koms":
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
        
        elif "like" in mention.full_text.lower() and "like\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "like":
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
                time.sleep(40)
            except:
                print("Désolé je ne peux pas analyser ce compte.")
                api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)   
                time.sleep(40)
        elif "ajd" in mention.full_text.lower() and "ajd\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "ajd":
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
                    date  = all_tweets[i].created_at
                    ddd = str(date)
                    if today_date in ddd:
                        td = td + 1
                        #print(a,date,td,w)
                print("L'utilisateur a tweeté " + str(td) + " fois aujourd'hui.")
                api.update_status('@' + your_name + " L'utilisateur a tweeté " + str(td) + " fois aujourd'hui." + str(nbr),mention.id)   
                nbr = nbr + 1
                write_id("nbr.txt",str(nbr))
                time.sleep(40)
            except:
                print("Désolé je ne peux pas analyser ce compte.")
                api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)   
                time.sleep(40)
        elif "her" in mention.full_text.lower() and "her\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "her":
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
                    date  = all_tweets[i].created_at
                    ddd = str(date)
                    if today_date in ddd:
                        td = td + 1
                        #print(a,date,td,w)
                print("L'utilisateur a tweeté " + str(td) + " fois hier.")
                api.update_status('@' + your_name + " L'utilisateur a tweeté " + str(td) + " fois hier." + str(nbr),mention.id)   
                nbr = nbr + 1
                write_id("nbr.txt",str(nbr))
                time.sleep(40)
            except:
                print("Désolé je ne peux pas analyser ce compte.")
                api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)   
 
        elif "mot" in mention.full_text.lower() and "mot\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "mot":
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
                time.sleep(40)
            except:
                print("Désolé je ne peux pas analyser ce compte.")
                api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)   
                time.sleep(40)
        elif "stat" in mention.full_text.lower() and "stat\n" not in mention.full_text.lower() and text[len(text) - 1][0] == "@" and text[len(text) - 2]== "stat":
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
                time.sleep(40)
            except:
                print("Désolé je ne peux pas analyser ce compte.")
                api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)
                time.sleep(40)
        elif "coms" in mention.full_text.lower() and "coms\n" not in mention.full_text.lower() and text[len(text) - 2]== "coms":
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
                time.sleep(40)
                api.update_status('@' + your_name + " Désolé je ne peux pas analyser ce compte. " + str(nbr),mention.id)   
                print("Désolé je ne peux pas analyser ce compte")

        elif "cherche" in mention.full_text.lower():
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
                    time.sleep(40)
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
                    time.sleep(40) 
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
                            api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.\n"+"Voici le dernier tweet contenant ce mot " + url, mention.id)
                            #api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.", mention.id)
                            print('@' + your_name + " le compte  ggggggas tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.")
                            print('@' + your_name + " le compte ggggggVoici le dernier tweet contenant ce mot " + url)
                        
                        else:
                            time.sleep(wait_time)
                            api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.\n"+"Voici le dernier tweet contenant ce mot " + url, mention.id)
                            #api.update_status('@' + your_name + " le compte Voici le dernier tweet contenant ce mot " + url, mention.id)
                            print('@' + your_name + " le compte  as tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de " + str(statuses_count) + " tweets ce qui représente environ " + str(res) + " " + p + " de ses tweets.")
                            print("Voici le dernier tweet contenant ce mot " + url)
                            time.sleep(wait_time)
                   
                    else:
                        if check_text(text) <= 2:
                            time.sleep(wait_time)
                            api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.\n"+"Voici le dernier tweet contenant ce mot " + url, mention.id)
                            #api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.", mention.id)
                            print('@' + your_name + " le compte gggggas tweeté " + str(nbr) + " fois le mot " + back_word + " sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.")
                            print('@' + your_name + " le compte gggggggVoici le dernier tweet contenant ce mot " + url)
                   
                        else:
                            time.sleep(wait_time)
                            api.update_status('@' + your_name + " le compte a tweeté " + str(nbr) + " fois le mot " + back_word + " sur ses 3000 derniers tweets ce qui représente environ " + str(res2) + " " + p + " de ses tweets.\n"+"Voici le dernier tweet contenant ce mot " + url, mention.id)
                            #api.update_status('@' + your_name + " le compte Voici le dernier tweet contenant ce mot " + url, mention.id)
                            print("Sur tes 3000 derniers tweets tu as tweeté " + str(nbr) + " fois le mot " + back_word + " sur un total de 3000 tweets ce qui représente environ " + str(res2) + " " + p + " de tes tweets.")
                            print("Voici le dernier tweet contenant ce mot " + url)
                   
                else:
                    print("Désolé mais l'utilisateur n'a jamais tweeter ce mot")
                    if statuses_count < 3000:
                        time.sleep(wait_time)
                        api.update_status('@' + your_name + " " + "Désolé mais l'utilisateur n'a jamais tweeter ce mot.",mention.id)
                   
                    if statuses_count >= 3000:
                        time.sleep(wait_time)
                        api.update_status('@' + your_name + " " + "Désolé mais l'utilisateur n'a pas tweeter ce mot sur ses 3000 derniers tweets.",mention.id)        
                        
                   
            else:
                print("nothing to sort")
#i = 0               
#while True:
#    i = i + 1
#    time.sleep(1)
#    print("Waiting!!!")
#    bot_laucnher(i)
print("start")
key = 0
while True:
    print("Waitging!!!",key)
    API_KEY = "XXXXXXX"
    API_SECRET = "XXXXXXX"
    ACCESS_TOKEN = "XXXXXXX"
    ACCESS_TOKEN_SECRET = "XXXXXXX"
    time.sleep(15)
    try:
        bot_laucnher(0,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    except:
        print("No wifi")
        time.sleep(120)
    time.sleep(5)
    key = key + 1  