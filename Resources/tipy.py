#/usr/bin/python
#encoding:utf-8
import sys,os
sys.path.append(os.pardir)

import twixy
from time import sleep


tw=twixy.Api(
    localStorage.id,
    localStorage.password)
_id_last_tl=0
_id_last_tl_replies=0

def PostTwitter(text):
    tw.PostUpdate(test) 

def update():
    global tw
    tw=twixy.Api(
        localStorage.id,
        localStorage.password,
        proxy="http://twixy53.appspot.com/api"
        )
    
    tl = tw.GetHomeTimeline(count=150,since_id=_id_last_tl)
    twbody = document.getElementById("twitter")

    node=document.createElement("li")
    node.innerHTML=u'<div style="border-bottom:dotted 1px black;height:1px;">.</div>'
    twbody.insertBefore(node,twbody.firstChild)
        
    for i in tl[::-1]:
        node=document.createElement("li")
        node.setAttribute("class","tw_container")
        node.innerHTML=u'<div class="icon_box"><img class="icon"src="%s"/></div><span class="username">%s</span><span class="text">%s</span>' %(i.user.profile_image_url,i.user.screen_name,i.text)
        
        twbody.insertBefore(node,twbody.firstChild)
        if i.text.find(localStorage.id) >0:
            updateReplies()
            
    global _id_last_tl
    _id_last_tl=tl[0].id
    
def updateReplies():
    tl = tw.GetReplies(since_id=_id_last_tl_replies)
    rep    = document.getElementById("replies")
    for i in tl[::-1]:
        node=document.createElement("li")
        node.setAttribute("class","tw_container")
        node.innerHTML=u'<div class="icon_box"><img class="icon"src="%s"/></div><span class="username">%s</span><span class="text">%s</span>' %(i.user.profile_image_url,i.user.screen_name,i.text)
        rep.insertBefore(node,rep.firstChild)
    global _id_last_tl_replies
    _id_last_tl_replies=tl[0].id
    return False

def startup():
    window.resizeTo(1280,800)
    window.moveTo(0,0)
    update()
    sleep(1)
    updateReplies()
    # setInterval(update,1000*15)
    

# key binding
k_state=[]
for i in range(200):
    k_state.append(0)
ev_cur=1
input_flag=1

kcode={
    "h":72,
    "j":74,
    "k":75,
    "l":76,
    "r":82,
    "g":71,
    "w":87,
    "e":69,
    "o":99,    
    "q":81,    
    "spc":32,    
    "cmd_r":93,    
    "cmd_l":91,    
    "shift":16,    
    "ctrl":17,    
    "1":49,    
    "2":50,    
    "3":51    
    }

def doEvent():
    global ev_cur
    if k_state[kcode["j"]]:
        scrollBy(0,50)
    if k_state[kcode["k"]]:
        scrollBy(0,-50)
    if k_state[kcode["r"]]:
        update() 
    if k_state[kcode["1"]]:
        ev_cur=1
        jQuery("#t1").click()
    if k_state[kcode["2"]]:
        ev_cur=2
        jQuery("#t2").click()
    if k_state[kcode["3"]]:
        ev_cur=3
        jQuery("#t3").click()
    if k_state[kcode["w"]]:
        if jQuery("span.text").css("white-space") =="nowrap" :
            jQuery(".icon").css("margin","0")
            jQuery(".icon_box").css("height","40px") 
            jQuery("span.text").css("white-space","normal")
        elif jQuery("span.text").css("white-space") =="normal" :
            jQuery(".icon").css("margin","-18px 0px;")
            jQuery(".icon_box").css("height","18px")
            jQuery("span.text").css("white-space","nowrap")

    if k_state[kcode["g"]] :
        window.scrollTo(0,0)
    if k_state[kcode["q"]] and k_state[kcode["ctrl"]]:
	Titanium.App.exit()
    # return False 

    
def changeKeys(keyCode,to):
    global k_state
    jQuery("#key_check").text(keyCode)
    k_state[int(keyCode)]=to
    doEvent()
    if ev_cur ==3 :
	return True
    return False;
