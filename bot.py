import itchat

@itchat.msg_register('Text')
def text_reply(msg):
    reply = "『" + msg['Text'] + "』" + " 初中生如是说"
    return reply

itchat.auto_login()
itchat.run()



# userlist = itchat.search_friends(remarkName='小奥利奥')
# username = userlist[0]['UserName']
# print(username)
