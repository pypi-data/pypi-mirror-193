from ast import Continue
from Hosein_Tabr.Copyright import copyright
from Hosein_Tabr.PostData import method_Rubika,httpregister,_download,_download_with_server
from Hosein_Tabr.Error import AuthError,TypeMethodError
from Hosein_Tabr.Device import DeviceTelephone
from re import findall
from Hosein_Tabr.Clien import clien
from random import randint,choice
import datetime
import io, PIL.Image
from Hosein_Tabr.Getheader import Upload
from tinytag import TinyTag
from Hosein_Tabr.TypeText import TypeText
import asyncio
from threading import Thread
from Hosein_Tabr.An_Wb import SetClines,Server
from requests import post,get
import urllib
from Hosein_Tabr.encryption import encryption
from urllib import request,parse
from re import findall
from pathlib import Path
from random import randint, choice
from json import loads, dumps
from socket import (gaierror,)
from json.decoder import (JSONDecodeError,)

class Robot:
    def __init__(self,Sh_account: str):
        self.Auth = str("".join(findall(r"\w",Sh_account)))
        self.prinet = copyright.CopyRight
        self.methods = method_Rubika(Sh_account)
        self.Upload  = Upload(Sh_account)

        if self.Auth.__len__() < 32:
            raise AuthError("The Auth entered is incorrect")
        elif self.Auth.__len__() > 32:
            raise AuthError("The Auth entered is incorrect")
    def sendMessage(self, guid,text,Type = None,Guid_mention = None,message_id=None):
        if Type == "MentionText":
            if Guid_mention != None:
                return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"rnd":f"{randint(100000,999999999)}","text":text,"metadata":{"meta_data_parts":TypeText("MentionText",text,Guid_mention)},"reply_to_message_id":message_id},wn = clien.web)
        elif Type == "Mono":
            return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"rnd":f"{randint(100000,999999999)}","text":text,"metadata":{"meta_data_parts":TypeText("Mono",text = text)},"reply_to_message_id":message_id},wn = clien.web)
        elif Type == "Bold":
            return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"rnd":f"{randint(100000,999999999)}","text":text,"metadata":{"meta_data_parts":TypeText("Bold",text = text)},"reply_to_message_id":message_id},wn = clien.web)
        elif Type == "Italic":
            return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"rnd":f"{randint(100000,999999999)}","text":text,"metadata":{"meta_data_parts":TypeText("Italic",text = text)},"reply_to_message_id":message_id},wn = clien.web)
        elif Type == None:
            return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"rnd":f"{randint(100000,999999999)}","text":text,"reply_to_message_id":message_id},wn = clien.web)

    def editMessage(self, guid, new, message_id):
        return self.methods.methodsRubika("json",methode ="editMessage",indata = {"message_id":message_id,"object_guid":guid,"text":new},wn = clien.web)

    def deleteMessages(self, guid, message_ids):
        return self.methods.methodsRubika("json",methode ="deleteMessages",indata = {"object_guid":guid,"message_ids":message_ids,"type":"Global"},wn = clien.web)

    def getMessagefilter(self, guid, filter_whith):
        return self.methods.methodsRubika("json",methode ="getMessages",indata = {"filter_type":filter_whith,"max_id":"NaN","object_guid":guid,"sort":"FromMax"},wn = clien.web).get("data").get("messages")

    def getMessages(self, guid, min_id):
        return self.methods.methodsRubika("json",methode ="getMessagesInterval",indata = {"object_guid":guid,"middle_message_id":min_id},wn = clien.web).get("data").get("messages")

    def getChats(self, start_id=None):
        return self.methods.methodsRubika("json",methode ="getChats",indata = {"start_id":start_id},wn = clien.web).get("data").get("chats")

    def getChatsUpdate(self):
        state = str(round(datetime.datetime.today().timestamp()) - 200)
        return self.methods.methodsRubika("json",methode ="getChatsUpdates",indata = {"state":state},wn = clien.web).get("data").get("chats")

    def deleteUserChat(self, user_guid, last_message):
        return self.methods.methodsRubika("json",methode ="deleteUserChat",indata = {"last_deleted_message_id":last_message,"user_guid":user_guid},wn = clien.web)

    def getInfoByUsername(self, username):
        return self.methods.methodsRubika("json",methode ="getObjectByUsername",indata = {"username":username},wn = clien.web)

    def banGroupMember(self, guid_gap, user_id):
        return self.methods.methodsRubika("json",methode ="banGroupMember",indata = {"group_guid": guid_gap,"member_guid": user_id,"action":"Set"},wn = clien.android)

    def unbanGroupMember(self, guid_gap, user_id):
        return self.methods.methodsRubika("json",methode ="banGroupMember",indata = {"group_guid": guid_gap,"member_guid": user_id,"action":"Unset"},wn = clien.android)

    def banChannelMember(self, guid_channel, user_id):
        return self.methods.methodsRubika("json",methode ="banChannelMember",indata = {"channel_guid": guid_channel,"member_guid": user_id,"action":"Set"},wn = clien.android)

    def unbanChannelMember(self, guid_channel, user_id):
        return self.methods.methodsRubika("json",methode ="banChannelMember",indata = {"channel_guid": guid_channel,"member_guid": user_id,"action":"Unset"},wn = clien.android)

    def getbanGroupUsers(self, guid_group, start_id = None):
        return self.methods.methodsRubika("json",methode ="getBannedGroupMembers",indata = {"group_guid": guid_group,"start_id":start_id},wn = clien.android)

    def getbanChannelUsers(self, guid_channel, start_id = None):
        return self.methods.methodsRubika("json",methode ="getBannedChannelMembers",indata = {"channel_guid": guid_channel,"start_id":start_id},wn = clien.android)

    def getGroupInfo(self, guid_gap):
        return self.methods.methodsRubika("json",methode ="getGroupInfo",indata = {"group_guid": guid_gap},wn = clien.web)

    def getChannelInfo(self, guid_channel):
        return self.methods.methodsRubika("json",methode ="getChannelInfo",indata = {"channel_guid": guid_channel},wn = clien.web)

    def addMemberGroup(self, guid_gap, user_ids):
        return self.methods.methodsRubika("json",methode ="addGroupMembers",indata = {"group_guid": guid_gap,"member_guids": user_ids},wn = clien.web)

    def addMemberChannel(self, guid_channel, user_ids):
        return self.methods.methodsRubika("json",methode ="addChannelMembers",indata = {"channel_guid": guid_channel,"member_guids": user_ids},wn = clien.web)

    def getGroupAdmins(self, guid_gap):
        return self.methods.methodsRubika("json",methode ="getGroupAdminMembers",indata = {"group_guid":guid_gap},wn = clien.web)

    def getChannelAdmins(self, guid_channel):
        return self.methods.methodsRubika("json",methode ="getChannelAdminMembers",indata = {"channel_guid":guid_channel},wn = clien.web)

    def AddNumberPhone(self, first_num, last_num, numberPhone):
        return self.methods.methodsRubika("json",methode ="addAddressBook",indata = {"phone":numberPhone,"first_name":first_num,"last_name":last_num},wn = clien.web)

    def getMessagesInfo(self, guid, message_ids):
        return self.methods.methodsRubika("json",methode ="getMessagesByID",indata = {"object_guid":guid,"message_ids": message_ids},wn = clien.web)

    def getGroupMembers(self, guid_gap, start_id=None):
        return self.methods.methodsRubika("json",methode ="getGroupAllMembers",indata = {"group_guid": guid_gap,"start_id": start_id},wn = clien.web)

    def getChannelMembers(self, channel_guid, text=None, start_id=None):
        return self.methods.methodsRubika("json",methode ="getChannelAllMembers",indata = {"channel_guid":channel_guid,"search_text":text,"start_id":start_id},wn = clien.android)

    def lockGroup(self, guid_gap):
        return self.methods.methodsRubika("json",methode ="setGroupDefaultAccess",indata = {"access_list": ["AddMember"],"group_guid": guid_gap},wn = clien.android)

    def unlockGroup(self, guid_gap):
        return self.methods.methodsRubika("json",methode ="setGroupDefaultAccess",indata = {"access_list": ["SendMessages", "AddMember"],"group_guid": guid_gap},wn = clien.android)

    def getGroupLink(self, guid_gap):
        return self.methods.methodsRubika("json",methode ="getGroupLink",indata = {"group_guid": guid_gap},wn = clien.web).get("data").get("join_link")

    def getChannelLink(self, guid_channel):
        return self.methods.methodsRubika("json",methode ="getChannelLink",indata = {"channel_guid": guid_channel},wn = clien.web).get("data").get("join_link")

    def changeGroupLink(self, guid_gap):
        return self.methods.methodsRubika("json",methode ="setGroupLink",indata = {"group_guid": guid_gap},wn = clien.web).get("data").get("join_link")

    def changeChannelLink(self, guid_channel):
        return self.methods.methodsRubika("json",methode ="setChannelLink",indata = {"channel_guid": guid_channel},wn = clien.web).get("data").get("join_link")

    def setGroupTimer(self, guid_gap, time):
        return self.methods.methodsRubika("json",methode ="editGroupInfo",indata = {"group_guid": guid_gap,"slow_mode": time,"updated_parameters":["slow_mode"]},wn = clien.android)

    def setGroupAdmin(self, guid_gap, guid_member,access_admin = None):
        if access_admin == None: access_admin = ["ChangeInfo","SetJoinLink","SetAdmin","BanMember","DeleteGlobalAllMessages","PinMessages","SetMemberAccess"] if access_admin == None else access_admin
        return self.methods.methodsRubika("json",methode ="setGroupAdmin",indata = {"group_guid": guid_gap,"access_list":access_admin,"action": "SetAdmin","member_guid": guid_member},wn = clien.android)

    def deleteGroupAdmin(self,guid_gap,guid_admin):
        return self.methods.methodsRubika("json",methode ="setGroupAdmin",indata = {"group_guid": guid_gap,"action": "UnsetAdmin","member_guid": guid_admin},wn = clien.android)

    def setChannelAdmin(self, guid_channel, guid_member,access_admin = None):
        if access_admin == None: access_admin = ["SetAdmin","SetJoinLink","AddMember","DeleteGlobalAllMessages","EditAllMessages","SendMessages","PinMessages","ViewAdmins","ViewMembers","ChangeInfo"] if access_admin == None else access_admin
        return self.methods.methodsRubika("json",methode ="setChannelAdmin",indata = {"channel_guid": guid_channel,"access_list":access_admin,"action": "SetAdmin","member_guid": guid_member},wn = clien.android)

    def deleteChannelAdmin(self,guid_channel,guid_admin):
        return self.methods.methodsRubika("json",methode ="setChannelAdmin",indata = {"channel_guid": guid_channel,"action": "UnsetAdmin","member_guid": guid_admin},wn = clien.android)

    def getStickersByEmoji(self,emojee):
        return self.methods.methodsRubika("json",methode ="getStickersByEmoji",indata = {"emoji_character": emojee,"suggest_by": "All"},wn = clien.web).get("data").get("stickers")

    def activenotification(self,guid):
        return self.methods.methodsRubika("json",methode ="setActionChat",indata = {"action": "Unmute","object_guid": guid},wn = clien.web)

    def offnotification(self,guid):
        return self.methods.methodsRubika("json",methode ="setActionChat",indata = {"action": "Mute","object_guid": guid},wn = clien.web)

    def sendPoll(self,guid,soal,lists):
        return self.methods.methodsRubika("json",methode ="createPoll",indata = {"allows_multiple_answers": "false","is_anonymous": "true","object_guid": guid,"options":lists,"question":soal,"rnd":f"{randint(100000,999999999)}","type":"Regular"},wn = clien.web)

    def forwardMessages(self, From, message_ids, to):
        return self.methods.methodsRubika("json",methode ="forwardMessages",indata = {"from_object_guid": From,"message_ids": message_ids,"rnd": f"{randint(100000,999999999)}","to_object_guid": to},wn = clien.web)

    def VisitChatGroup(self,guid_gap,visiblemsg):
        return self.methods.methodsRubika("json",methode ="editGroupInfo",indata = {"chat_history_for_new_members": "Visible","group_guid": guid_gap,"updated_parameters": visiblemsg},wn = clien.web)

    def HideChatGroup(self,guid,hiddenmsg):
        return self.methods.methodsRubika("json",methode ="editGroupInfo",indata = {"chat_history_for_new_members": "Hidden","group_guid": guid_gap,"updated_parameters": hiddenmsg},wn = clien.web)

    def pin(self, guid, message_id):
        return self.methods.methodsRubika("json",methode ="setPinMessage",indata = {"action":"Pin","message_id": message_id,"object_guid": guid},wn = clien.web)

    def unpin(self,guid,hiddenmsg):
        return self.methods.methodsRubika("json",methode ="setPinMessage",indata = {"action":"Unpin","message_id": message_id,"object_guid": guid},wn = clien.web)

    def logout(self):
        return self.methods.methodsRubika("json",methode ="logout",indata = {},wn = clien.web)

    def joinGroup(self,link):
        hashLink = link.split("/")[-1]
        return self.methods.methodsRubika("json",methode ="joinGroup",indata = {"hash_link": hashLink},wn = clien.web)

    def joinChannelByLink(self,link):
        hashLink = link.split("/")[-1]
        return self.methods.methodsRubika("json",methode ="joinChannelByLink",indata = {"hash_link": hashLink},wn = clien.android)

    def joinChannelByID(self,ide):
        IDE = ide.split("@")[-1]
        GUID = self.getInfoByUsername(IDE)["data"]["channel"]["channel_guid"]
        return self.methods.methodsRubika("json",methode ="joinChannelAction",indata = {"action": "Join","channel_guid": GUID},wn = clien.web)

    def joinChannelByGuid(self,guid):
        return self.methods.methodsRubika("json",methode ="joinChannelAction",indata = {"action": "Join","channel_guid": guid},wn = clien.web)

    def leaveGroup(self,guid_gap):
        if "https://" in guid_gap:
            guid_gap = self.joinGroup(guid_gap)["data"]["group"]["group_guid"]
        else:
            guid_gap = guid_gap
        return self.methods.methodsRubika("json",methode ="leaveGroup",indata = {"group_guid": guid_gap},wn = clien.web)

    def leaveChannel(self,guid_channel):
        if "https://" in guid_channel:
            guid_channel = self.joinChannelByLink(guid_channel)["data"]["chat_update"]["object_guid"]
        elif "@" in guid_channel:
            guid_channel = self.joinChannelByID(guid_channel)["data"]["chat_update"]["object_guid"]
        else:
            guid_channel = guid_channel
        return self.methods.methodsRubika("json",methode ="joinChannelAction",indata = {"action": "Leave","channel_guid": guid_channel},wn = clien.web)

    def EditNameGroup(self,groupgu,namegp,biogp=None):
        return self.methods.methodsRubika("json",methode ="editGroupInfo",indata = {"description": biogp,"group_guid": groupgu,"title":namegp,"updated_parameters":["title","description"]},wn = clien.web)

    def EditBioGroup(self,groupgu,biogp,namegp=None):
        return self.methods.methodsRubika("json",methode ="editGroupInfo",indata = {"description": biogp,"group_guid": groupgu,"title":namegp,"updated_parameters":["title","description"]},wn = clien.web)

    def block(self, guid_user):
        return self.methods.methodsRubika("json",methode ="setBlockUser",indata = {"action": "Block","user_guid": guid_user},wn = clien.web)

    def unblock(self, guid_user):
        return self.methods.methodsRubika("json",methode ="setBlockUser",indata = {"action": "Unblock","user_guid": guid_user},wn = clien.web)

    def startVoiceChat(self, guid):
        return self.methods.methodsRubika("json",methode ="createGroupVoiceChat",indata = {"chat_guid":guid},wn = clien.web)

    def editVoiceChat(self,guid,voice_chat_id, title):
        return self.methods.methodsRubika("json",methode ="setGroupVoiceChatSetting",indata = {"chat_guid":guid,"voice_chat_id" : voice_chat_id,"title" : title ,"updated_parameters": ["title"]},wn = clien.web)

    def finishVoiceChat(self, guid, voice_chat_id):
        return self.methods.methodsRubika("json",methode ="discardGroupVoiceChat",indata = {"chat_guid":guid,"voice_chat_id" : voice_chat_id},wn = clien.web)

    def getUserInfo(self, guid_user):
        return self.methods.methodsRubika("json",methode ="getUserInfo",indata = {"user_guid":guid_user},wn = clien.web)

    def seeGroupbyLink(self,link_gap):
        link = link_gap.split("https://rubika.ir/joing/")[-1]
        return self.methods.methodsRubika("json",methode ="groupPreviewByJoinLink",indata = {"hash_link": link},wn = clien.web).get("data")

    def seeChannelbyLink(self,link_channel):
        link = link_channel.split("https://rubika.ir/joinc/")[-1]
        return self.methods.methodsRubika("json",methode ="channelPreviewByJoinLink",indata = {"hash_link": link},wn = clien.web).get("data")

    def __getImageSize(self,image_bytes:bytes):
        bytimg = PIL.Image.open(io.BytesIO(image_bytes))
        width, height = bytimg.size
        return [width , height]

    def uploadAvatar_replay(self,guid,files_ide):
        return self.methods.methodsRubika("json",methode ="uploadAvatar",indata = {"object_guid":guid,"thumbnail_file_id":files_ide,"main_file_id":files_ide},wn = clien.web)

    def uploadAvatar(self,guid,main,thumbnail=None):
        mainID = str(self.Upload.uploadFile(main)[0]["id"])
        thumbnailID = str(self.Upload.uploadFile(thumbnail or main)[0]["id"])
        return self.methods.methodsRubika("json",methode ="uploadAvatar",indata = {"object_guid":guid,"thumbnail_file_id":thumbnailID,"main_file_id":mainID},wn = clien.web)

    def removeAvatar(self,guid,avatar_id):
        return self.methods.methodsRubika("json",methode ="deleteAvatar",indata = {"object_guid":guid,"avatar_id":avatar_id},wn = clien.web)

    def Devicesrubika(self):
        return self.methods.methodsRubika("json",methode ="getMySessions",indata = {},wn = clien.web)

    def deleteChatHistory(self,guid,last_message_id):
        return self.methods.methodsRubika("json",methode ="deleteChatHistory",indata = {"last_message_id": last_message_id,"object_guid": guid},wn = clien.web)

    def addFolder(self, Name = "Arsein", include_chat = None,include_object = None ,exclude_chat = None,exclude_object = None):
        return self.methods.methodsRubika("json",methode ="addFolder",indata = {"exclude_chat_types": exclude_chat,"exclude_object_guids": exclude_object,"include_chat_types": include_chat,"include_object_guids": include_object,"is_add_to_top":True,"name": Name},wn = clien.web)

    def deleteFolder(self,folder_id):
        return self.methods.methodsRubika("json",methode ="deleteFolder",indata = {"folder_id": folder_id},wn = clien.web)

    def addGroup(self,title,guidsUser = None):
        return self.methods.methodsRubika("json",methode ="addGroup",indata = {"member_guids": guidsUser,"title": title},wn = clien.web)

    def addChannel(self,title,typeChannell,bio,guidsUser = None):
        return self.methods.methodsRubika("json",methode ="addChannel",indata = {"addChannel": typeChannell,"description": bio,"member_guids": guidsUser,"title": title},wn = clien.web)

    def breturn(self,start_id = None):
        return self.methods.methodsRubika("json",methode ="getBreturnUsers",indata = {"start_id": start_id},wn = clien.web)

    def editUser(self,first_name = None,last_name = None,bio = None):
        return self.methods.methodsRubika("json",methode ="updateProfile",indata = {"bio": bio,"first_name": first_name,"last_name": last_name,"updated_parameters":["first_name","last_name","bio"]},wn = clien.web)

    def editusername(self,username):
        ide = username.split("@")[-1]
        return self.methods.methodsRubika("json",methode ="updateUsername",indata = {"username": ide},wn = clien.web)

    def Postion(self,guid,guiduser):
        return self.methods.methodsRubika("json",methode ="requestChangeObjectOwner",indata = {"object_guid": guid,"new_owner_user_guid": guiduser},wn = clien.android)

    def getPostion(self,guid):
        return self.methods.methodsRubika("json",methode ="getPendingObjectOwner",indata = {"object_guid": guid},wn = clien.android)

    def ClearAccounts(self):
        return self.methods.methodsRubika("json",methode ="terminateOtherSessions",indata = {},wn = clien.web)

    def HidePhone(self,**kwargs):
        return self.methods.methodsRubika("json",methode ="setSetting",indata = {"settings": kwargs,"update_parameters":["show_my_phone_number"]},wn = clien.web)

    def HideOnline(self,**kwargs):
        return self.methods.methodsRubika("json",methode ="setSetting",indata = {"settings": kwargs,"update_parameters":["show_my_last_online"]},wn = clien.web)

    def search_inaccount(self,text):
        return self.methods.methodsRubika("json",methode ="searchGlobalMessages",indata = {"search_text": text,"start_id":None,"type": "Text"},wn = clien.web).get("data").get("messages")

    def getAbsObjects(self,guid):
        return self.methods.methodsRubika("json",methode ="getAbsObjects",indata = {"objects_guids": guid},wn = clien.web)

    def Infolinkpost(self,linkpost):
        return self.methods.methodsRubika("json",methode ="getLinkFromAppUrl",indata = {"app_url": linkpost},wn = clien.web)

    def getContactsLastOnline(self,user_guids:list):
        return self.methods.methodsRubika("json",methode ="getContactsLastOnline",indata = {"user_guids": user_guids},wn = clien.web)

    def SignMessageChannel(self,guid_channel,sign:bool):
        return self.methods.methodsRubika("json",methode ="editChannelInfo",indata = { "channel_guid": guid_channel,"sign_messages": sign,"updated_parameters": ["sign_messages"]},wn = clien.web)

    def ActiveContectJoin(self):
        return self.methods.methodsRubika("json",methode ="setSetting",indata = {"settings":{"can_join_chat_by":"MyContacts"},"update_parameters":["can_join_chat_by"]},wn = clien.web)

    def ActiveEverybodyJoin(self):
        return self.methods.methodsRubika("json",methode ="setSetting",indata = {"settings":{"can_join_chat_by":"Everybody"},"update_parameters":["can_join_chat_by"]},wn = clien.web)

    def CalledBy(self,typeCall:str):
        return self.methods.methodsRubika("json",methode ="setSetting",indata = {"settings": {"can_called_by": typeCall}, "update_parameters": ["can_called_by"]},wn = clien.android)

    def changeChannelID(self,guid_channel,username):
        return self.methods.methodsRubika("json",methode ="updateChannelUsername",indata = {"channel_guid": guid_channel,"username": username},wn = clien.web)

    def getBlockedUsers(self):
        return self.methods.methodsRubika("json",methode ="getBlockedUsers",indata = {},wn = clien.web)

    def deleteContact(self,guid_user):
        return self.methods.methodsRubika("json",methode ="deleteContact",indata = {"user_guid":guid_user},wn = clien.web)

    def getContacts(self):
        return self.methods.methodsRubika("json",methode ="getContacts",indata = {},wn = clien.web).get("data").get("users")

    def getLiveStatus(self,live_id,token_live):
        return self.methods.methodsRubika("json",methode ="getLiveStatus",indata = {"live_id":live_id,"access_token":token_live},wn = clien.web)

    def commonGroup(self,guid_user):
        IDE = guid_user.split("@")[-1]
        GUID = self.getInfoByUsername(IDE)["data"]["user"]["user_guid"]
        return self.methods.methodsRubika("json",methode ="getCommonGroups",indata = {"user_guid": GUID},wn = clien.android)

    def setTypeChannel(self,guid_channel,type_Channel):
        if type_Channel == "Private":
            return self.methods.methodsRubika("json",methode ="editChannelInfo",indata = {"channel_guid":guid_channel,"channel_type":"Private","updated_parameters":["channel_type"]},wn = clien.web)
        else:
            if type_Channel == "Public":
                return self.methods.methodsRubika("json",methode ="editChannelInfo",indata = {"settings":{"channel_guid":guid_channel,"channel_type":"Public","updated_parameters":["channel_type"]}},wn = clien.web)

    def getChatAds(self,user_guids:list):
        state = str(round(datetime.datetime.today().timestamp()) - 200)
        return self.methods.methodsRubika("json",methode ="getChatAds",indata = {"state": state},wn = clien.web)

    def getContactsUpdates(self):
        state = str(round(datetime.datetime.today().timestamp()) - 200)
        return self.methods.methodsRubika("json",methode ="getContactsUpdates",indata = {"state": state},wn = clien.web)

    def Download(self,guid = None,type_file = None,file_name = None,frmt = None,ms = None):
        if type_file == "file" and "http://" or "https://" in ms and  guid == None and file_name != None and frmt != None:
            loop = asyncio.get_event_loop()
            getdownload = loop.run_until_complete(_download_with_server(server = ms))
            with open(f"{file_name}.{frmt}","wb") as files:
                files.write(getdownload)
                return "Ok Download"
                print("Ok Download")
        elif type_file == "rubika" and frmt == None and file_name == None and guid != None and ms != None:
            result:bytes = ""
            get_info_File = self.getMessagesInfo(guid, [ms.get("message_id")])["data"]["messages"]
            for m in get_info_File:
                access_hash_rec = m["file_inline"]["access_hash_rec"]
                file_id = m["file_inline"]["file_id"]
                size = m["file_inline"]["size"]
                dc_id = m["file_inline"]["dc_id"]
                file_name  = m["file_inline"]["file_name"]
                header_Download = {'auth': self.Auth, 'file-id':file_id, "start-index": "0", "last-index": str(size), 'access-hash-rec':access_hash_rec}
                GetFile = f"https://messenger{dc_id}.iranlms.ir/GetFile.ashx"
            while 1:
                try:
                    if size <= 131072:
                        loop = asyncio.get_event_loop()
                        result += loop.run_until_complete(_download(server = GetFile,header = header_Download))
                        break
                    else:
                        for i in range(0,size,131072):
                            header_Download["start-index"], header_Download["last-index"] = str(i), str(i+131072 if i+131072 <= size else size)
                            loop = asyncio.get_event_loop()
                            result += loop.run_until_complete(_download(server = GetFile,header = header_Download))
                        break
                except:continue
            with open(first_name,"wb") as f:
                f.write(result)
                return "Ok Download"
                print("Ok Download")

    def sendSticker(self,guid,emoji,w_h_rati,sticker_id,file_id,access_hash,set_id):
        return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid": guid,"rnd": f"{randint(100000,999999999)}","sticker": {"emoji_character": emoji,"w_h_ratio": w_h_rati,"sticker_id": sticker_id,"file": {"file_id": file_id,"mime": "png","dc_id": 32,"access_hash_rec": access_hash,"file_name": "sticker.png"},"sticker_set_id": set_id}},wn = clien.web)

    def sendFile(self, guid, file, caption=None, message_id=None):
        uresponse = self.Upload.uploadFile(file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        loop = asyncio.get_event_loop()
        return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"reply_to_message_id":message_id,"rnd":f"{randint(100000,999999999)}","file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"File","file_name":file_name,"size":str(len(loop.run_until_complete(_download_with_server(server = file)) if ("http" or "https") in file else open(file,"rb").read())),"mime":mime,"access_hash_rec":access_hash_rec},"text":caption},wn = clien.web)

    def sendVoice(self, guid, file, time = None, caption=None, message_id=None):
        uresponse = self.Upload.uploadFile(file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        loop = asyncio.get_event_loop()
        if time == None: time =  round(int(TinyTag.get(file).duration) * 1000)
        return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"reply_to_message_id":message_id,"rnd":f"{randint(100000,999999999)}","file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Voice","file_name":file_name,"size":str(len(loop.run_until_complete(_download_with_server(server = file)) if ("http" or "https") in file else open(file,"rb").read())),"time":time,"mime":mime,"access_hash_rec":access_hash_rec},"text":caption},wn = clien.web)

    def sendMusic(self, guid, file, time = None, caption=None, message_id=None):
        uresponse = self.Upload.uploadFile(file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        loop = asyncio.get_event_loop()
        if time == None: time = round(int(TinyTag.get(file).duration) * 1000)
        return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"object_guid":guid,"reply_to_message_id":message_id,"rnd":f"{randint(100000,999999999)}","file_inline":{"dc_id":str(dc_id),"file_id":str(file_id),"type":"Music","music_performer":"","file_name":file_name,"size":str(len(loop.run_until_complete(_download_with_server(server = file)) if ("http" or "https") in file else open(file,"rb").read())),"time": time,"mime":mime,"access_hash_rec":access_hash_rec},"text":caption},wn = clien.web)

    def sendGif(self, guid, file, breadth:list= None, caption=None, message_id=None, thumbnail=None):
        uresponse = self.Upload.uploadFile(file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        loop = asyncio.get_event_loop()
        if breadth == None: breadth =  [640,640] if not ("http" or "https") in file else [640,640]
        time =  round(int(TinyTag.get(file).duration) * 1000)
        if thumbnail == None: thumbnail = r"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"
        return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"is_mute":False,"object_guid":guid,"reply_to_message_id":message_id,"rnd":f"{randint(100000,999999999)}","file_inline":{"access_hash_rec":access_hash_rec,"auto_play":False,"dc_id":dc_id,"file_id":file_id,"file_name":file_name,"height":breadth[1],"mime":mime,"size":str(len(loop.run_until_complete(_download_with_server(server = file)) if ("http" or "https") in file else open(file,"rb").read())),"thumb_inline":thumbnail,"time":time,"type":"Gif","width":breadth[0]},"text":caption},wn = clien.android)

    def sendVideo(self, guid, file,breadth:list = None, caption=None, message_id=None, thumbnail=None):
        uresponse = self.Upload.uploadFile(file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        loop = asyncio.get_event_loop()
        if breadth == None: breadth =  [360,360]
        time =  round(int(TinyTag.get(file).duration) * 1000)
        if thumbnail == None: thumbnail = r"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"
        return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"is_mute":False,"object_guid":guid,"reply_to_message_id":message_id,"rnd":f"{randint(100000,999999999)}","file_inline":{"access_hash_rec":access_hash_rec,"auto_play":False,"dc_id":dc_id,"file_id":file_id,"file_name":file_name,"height":breadth[1],"mime":mime,"size":str(len(loop.run_until_complete(_download_with_server(server = file)) if ("http" or "https") in file else open(file,"rb").read())),"thumb_inline":thumbnail,"time":time,"type":"Video","width":breadth[0]},"text":caption},wn = clien.android)

    def sendPhoto(self, guid, file, breadth:list= None, thumbnail=None, caption=None, message_id=None):
        import PIL.Image
        uresponse = self.Upload.uploadFile(file)
        file_id = str(uresponse[0]["id"])
        mime = file.split(".")[-1]
        dc_id = uresponse[0]["dc_id"]
        access_hash_rec = uresponse[1]
        file_name = file.split("/")[-1]
        loop = asyncio.get_event_loop()
        if breadth == None: breadth =  PIL.Image.open(file).size if not ("http" or "https") in file else [640,640]
        if thumbnail == None: thumbnail = r"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"
        return self.methods.methodsRubika("json",methode ="sendMessage",indata = {"is_mute":False,"object_guid":guid,"reply_to_message_id":message_id,"rnd":f"{randint(100000,999999999)}","file_inline":{"dc_id": dc_id,"file_id": file_id,"type":"Image","file_name": file_name,"size": str(len(loop.run_until_complete(_download_with_server(server = file)) if ("http" or "https") in file else open(file,"rb").read())),"mime": mime,"access_hash_rec": access_hash_rec,"width": breadth[0],"height": breadth[1],"thumb_inline": thumbnail},"text":caption},wn = clien.android)


    def twolocks(self,ramz,hide):
        locked =  self.methods.methodsRubika("json",methode ="setupTwoStepVerification",indata = {"hint": hide,"password": ramz},wn = clien.web)
        if locked["status"] == 'ERROR_GENERIC':
            return locked["client_show_message"]["link"]["alert_data"]["message"]
        else:return locked

    def ProfileEdit(self,first_name = None,last_name = None,bio = None,username = None):
        while 1:
            try:
                self.editUser(first_name = first_name,last_name = last_name,bio = bio)
                self.editusername(username)
                return "Profile edited"
                break
            except:continue

    def getChatGroup(self,guid_gap):
        while 1:
            try:
                lastmessages = self.getGroupInfo(guid_gap)["data"]["chat"]["last_message_id"]
                messages = self.getMessages(guid_gap, lastmessages)
                return messages
                break
            except:continue

    def getChatChannel(self,guid_channel):
        while 1:
            try:
                lastmessages = self.getChannelInfo(guid_channel)["data"]["chat"]["last_message_id"]
                messages = self.getMessages(guid_channel, lastmessages)
                return messages
                break
            except:continue

    def getChatUser(self,guid_User):
        while 1:
            try:
                lastmessages = self.getUserInfo(guid_User)["data"]["chat"]["last_message_id"]
                messages = self.getMessages(guid_User, lastmessages)
                return messages
                break
            except:continue

    def Authrandom(self):
        auth = ""
        meghdar = "qwertyuiopasdfghjklzxcvbnm0123456789"
        for string in range(32):
            auth += choice(meghdar)
        return auth

    def SendCodeSMS(self,phonenumber):
        tmp = self.Authrandom()
        enc = encoderjson(tmp)
        return self.methods.methodsRubika("json",methode ="sendCode",indata = {"phone_number":f"98{phonenumber[1:]}","send_type":"SMS"},wn = clien.web)

    def SendCodeWhithPassword(self,phone_number:str,pass_you):
        tmp = self.Authrandom()
        enc = encoderjson(tmp)
        return self.methods.methodsRubika("json",methode ="sendCode",indata = {"pass_key":pass_you,"phone_number":f"98{phonenumber[1:]}","send_type":"SMS"},wn = clien.web)

    def signIn(phone_number,phone_code_hash,phone_code):
        tmp = self.Authrandom()
        enc = encoderjson(tmp)
        return self.methods.methodsRubika("json",methode ="signIn",indata = {"phone_number":f"98{phone_number[1:]}","phone_code_hash":phone_code_hash,"phone_code":phone_code},wn = clien.web)

    def registerDevice(auth, device=DeviceTelephone.defaultDevice):
        enc = encoderjson(auth)
        while 1:
            try:
                loop = asyncio.get_event_loop()
                ersal = loads(self.enc.decrypt(loads(loop.run_until_complete(httpregister(device,self.Auth))).get("data_enc")))
                return ersal
                break
            except:
                continue

    def Auth(readfile):
        while 1:
            try:
                with open(f"{readfile}", "r") as file:
                    jget = json.load(file)
                    s = jget["data"]["auth"]
                    regs = self.registerDevice(s)
                    return regs
            except:continue
class Robino:
	def __init__(self,Sh_account: str):
        self.Auth = str("".join(findall(r"\w",Sh_account)))
		self.print = copyright.CopyRight
	def _getUrl():
		return f'https://rubino{randint(1,30)}.iranlms.ir/'
		
		
	def _request(self,inData,method):
		data = {"api_version": "0","auth": self.auth,"client": {"app_name": "Main","app_version": "3.0.2","lang_code": "fa","package": "app.rbmain.a","platform": "Android"},"data": inData,"method": method}
		while True:
			try:
				return post(Robino._getUrl(),json=data).json()
			except:
				continue
				
				
	def follow(self,followee_id,profile_id=None):
		inData = {"f_type": "Follow","followee_id": followee_id,"profile_id": profile_id}
		method = 'requestFollow'
		while True:
			try:
				return self._request(inData,method)
			except:continue
		
		
	def getPostByShareLink(self,link,profile_id=None):
		inData = {"share_string":link,"profile_id":profile_id}
		method = "getPostByShareLink"
		while True:
			try:
				return self._request(inData,method).get('data')
			except:continue
			
			
	def addPostViewCount(self,post_id,post_target_id):
		inData = {"post_id":post_id,"post_profile_id":post_target_id}
		method = "addPostViewCount"
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def getStoryIds(self,target_profile_id,profile_id=None):
		inData = {"profile_id":profile_id,"target_profile_id":target_profile_id}
		method = 'getStoryIds'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def updateProfile(self,profile_id=None):
		inData = {"profile_id":profile_id,"profile_status":"Public"}
		method = 'updateProfile'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def getRecentFollowingPosts(self,profile_id=None):
		inData = {"equal":False,"limit":30,"sort":"FromMax","profile_id":profile_id}
		method = 'getRecentFollowingPosts'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def getProfileList(self):
		inData = {"equal":False,"limit":10,"sort":"FromMax"}
		method = 'getProfileList'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def getMyProfileInfo(self,profile_id=None):
		inData = {"profile_id":profile_id}
		method = 'getMyProfileInfo'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def Like(self,post_id,target_post,prof=None):
		inData ={"action_type":"Like","post_id":post_id,"post_profile_id":target_post,"profile_id":prof}
		method = 'likePostAction'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
	def getShareLink(self):
		inData = {"post_id":post_id,"post_profile_id":post_profile,"profile_id":prof}
		method = 'getShareLink'
		while True:
			try:
				return self._request(inData,method)
			except:continue
	
	def addViewStory(self,story,ids,prof=None):
		indata = {"profile_id":prof,"story_ids":[ids],"story_profile_id":story}
		method = 'addViewStory'
		while True:
			try:
				return self._request(indata,method)
			except:continue
			
			
	def createPage(self,name,username,bio=None):
		inData = {"bio": bio,"name": name,"username": username}
		method = 'createPage'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def comment(self,text,poat_id,post_target,prof=None):
		inData = {"content": text,"post_id": poat_id,"post_profile_id": post_target,"rnd":f"{randint(100000,999999999)}" ,"profile_id":prof}
		method = 'addComment'
		while True:
			try:
				return self._request(inData,method)
			except:continue
		
		
	def UnLike(self,post_id,post_profile_id,prof=None):
		inData = {"action_type":"Unlike","post_id":post_id,"post_profile_id":post_profile_id,"profile_id":prof}
		method ='likePostAction'
		while True:
			try:
				return self._request(inData,method)
			except:continue
			
			
	def sevaePost(self,post_id,post_profile_id,prof=None):
		inData = {"action_type":"Bookmark","post_id":post_id,"post_profile_id":post_profile_id,"profile_id":prof}
		method ='postBookmarkAction'
		while True:
			try:
				return self._request(inData,method)
			except:continue


class shad:
	def __init__(self, Sh_account):
		self.Auth = Sh_account
		self.prinet = copyright.CopyRight
		self.enc = encryption(Sh_account)
		
		
		

	def _getURL():
		return choice(Server.matnadress)

	def _SendFile():
		return choice(Server.filesadress)
	
	def _rubino():
	    return choice(Server.rubino)
	    
	def socket():
	    return choice(Server.gtes)


	def registerDevice(self):
	    inData = {"method":"registerDevice","input":{"app_version":"WB_4.1.2","device_hash":"0501110712007200125373640870428014153736","device_model":"robo_shad-library","lang_code":"fa","system_version":"Linux","token":" ","token_type":"Web"},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def isExist(self, username):
	    inData = {"method": "isExistUserame","input":{"username": username},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad.rubino(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def turnOffTwoStep(self, password):
	    
	    inData = {"method":"turnOffTwoStep","input":{"password":password},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def setupTwoStepVerification(self, hint,password):
	    inData = {"method":"setupTwoStepVerification","input":{"hint":hint,"password":password},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def sendMessage(self, chat_id,text,metadata=[],message_id=None):
		inData = {
			"method":"sendMessage",
			"input":{
				"object_guid":chat_id,
				"rnd":f"{randint(100000,999999999)}",
				"text":text,
				"reply_to_message_id":message_id
			},
			"client": SetClines.web
		}
		if metadata != [] : inData["input"]["metadata"] = {"meta_data_parts":metadata}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	def editMessage(self, gap_guid, newText, message_id):
		inData = {
			"method":"editMessage",
			"input":{
				"message_id":message_id,
				"object_guid":gap_guid,
				"text":newText
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def sendChatActivity(self, object_guid):
	    inData = {"method":"sendChatActivity","input":{"activity":"Typing","object_guid":object_guid},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getChatAds(self):
	    time_stamp = str(round(datetime.datetime.today().timestamp()) - 200)
	    inData = {"method":"getChatAds","input":{"state":time_stamp},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get('chat_ads')
	        except:continue
	def getMessagesInterval(self):
	    inData = {"method":"getMessagesInterval","input":{"object_guid":"s0B0e8da28a4fde394257f518e64e800","middle_message_id":"0"},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("messages")
	        except:continue
	def sendCode(self,phone_number,pass_key=None):
	    inData = {"method":"sendCode","input":{"pass_key":pass_key,"phone_number":f"98{phone_number[1:]}","send_type":"Internal"},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	
	def signIn(self, phone_number,phone_code_hash,phone_code):
	    inData = {"method":"signIn","input":{"phone_number":f"98{phone_number[1:]}","phone_code_hash":phone_code_hash,"phone_code":phone_code},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	
	def addFolder(self, name):
	    inData = {"method":"addFolder","input":{"is_add_to_top":True,"name":name},"client":SetClines.android}
	    while True:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def leaveChannelAction(self, channel_guid):
	    inData = {"method":"joinChannelAction","input":{"action":"Leave","channel_guid":channel_guid},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def mrgohst(self):
	    inData = {"method":"getDCs","input":{},"client":{"app_name":"Main","app_version":"4.1.4","platform":"Web","package":"web.rubika.ir","lang_code":"fa"}}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad.socket(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def joinChannelAction(self, channel_guid):
	    inData = {"method":"joinChannelAction","input":{"action":"Join","channel_guid":channel_guid},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def editname(self, first_name=None, bio=None):
	    inData = {"method":"updateProfile","input":{"first_name":first_name,"last_name":" ","bio":bio,"updated_parameters":["first_name","last_name",'bio']},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	
	def updateUsername(self, username):
	    inData = {"method":"updateUsername","input":{"username":username},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	        
	def getServiceInfo(self, service_guid):
	    inData = {"method":"getServiceInfo","input":{"service_guid":service_guid},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def deleteMessages(self, chat_id, message_ids):
		inData = {
			"method":"deleteMessages",
			"input":{
				"object_guid":chat_id,
				"message_ids":message_ids,
				"type":"Global"
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	def getMessagefilter(self, chat_id, filter_whith):
		inData = {
		    "method":"getMessages",
		    "input":{
		        "filter_type":filter_whith,
		        "max_id":"NaN",
		        "object_guid":chat_id,
		        "sort":"FromMax"
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("messages")
				break
			except: continue

	def getMessagew(self, chat_id, min_id):
	    inData = {"method":"getMessagesInterval","input":{"object_guid":chat_id,"middle_message_id":min_id},"client": SetClines.web}
	    while 1:
		    try:
		        return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("messages")
		    except:continue
	def getmen(self):
	    inData = {"method":"getMessagesInterval","input":{"object_guid":"s0B0e8da28a4fde394257f518e64e800","middle_message_id":"0"},"client": SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("messages")
	        except:continue
	def getMessages(self, chat_id, min_id):
		inData = {
		    "method":"getMessagesInterval",
		    "input":{
		        "object_guid":chat_id,
		        "middle_message_id":min_id
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("messages")
				break
			except: continue


	def getChats(self, start_id=None):
		inData = {
		    "method":"getChats",
		    "input":{
		        "start_id":start_id
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("messages")
				break
			except: continue
	        
	def deleteUserChat(self, user_guid, last_message):
		inData = {
		    "method":"deleteUserChat",
		    "input":{
		        "last_deleted_message_id":last_message,
		        "user_guid":user_guid
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def deleteUserChat(self, user_guid):
	    inData = {"method":"deleteUserChat","input":{"last_deleted_message_id":"0","user_guid":user_guid},"client": SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getGroupOnlineMember(self, chat_id):
	    inData = {"method":"getGroupOnlineCount","input":{"group_guid": chat_id},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get('data').get('online_count')
	        except:continue
	def getCommonGroups(self, chat_id):
	    inData = {"method":"getCommonGroups","input":{"user_guid": chat_id},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get('data').get('abs_groups')
	        except:continue
	def sendLocation(self, chat_id, location, message_id=None):
	    inData = {"method":"sendMessage","input":{"is_mute": False,"object_guid":chat_id,"rnd":f"{randint(100000,999999999)}","location":{"latitude": location[0],"longitude": location[1]},"reply_to_message_id":message_id},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def updateProfile_rubino(self, name=None, bio=None, email=None):
	    inData = {"method":"updateProfile","input": {"name": name, "bio": bio, "email": email},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._rubino(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getPendingObjectOwner(self, chat_id):
	    inData = {"method":"getPendingObjectOwner","input":{"object_guid": chat_id},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getContacts(self, user_guid):
	    inData = {"method":"getContacts","input":{"start_id":user_guid},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("users")
	        except:continue
	def seenChats(self, chat_id, msg_id):
	    inData = {"method":"seenChats","input":{"seen_list":{chat_id:msg_id}},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getInfoByUsername(self, username):
		inData = {
		    "method":"getObjectByUsername",
		    "input":{
		        "username":username
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data")
				break
			except: continue

	def requestChangeObjectOwner(self, chat_id, newOwnerGuid):
	    inData = {"method":"requestChangeObjectOwner","input":{"object_guid": chat_id, "new_owner_user_guid": newOwnerGuid},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def reporter(self, chat_id,description=None,reportType = 106):
	    inData = {"method":"reportObject","input":{"object_guid":chat_id,"report_description":description,"report_type":reportType,"report_type_object":"Object"},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def banGroupMember(self, chat_id, user_id):
		inData = {
		    "method":"banGroupMember",
		    "input":{
		        "group_guid": chat_id,
				"member_guid": user_id,
				"action":"Set"
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def unbanGroupMember(self, chat_id, user_id):
		inData = {
		    "method":"banGroupMember",
		    "input":{
		        "group_guid": chat_id,
				"member_guid": user_id,
				"action":"Unset"
		    },
		    "client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getGroupInfo(self, chat_id):
		inData = {
			"method":"getGroupInfo",
			"input":{
				"group_guid": chat_id
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def search(self, text):
	    inData = {"method":"searchGlobalObjects","input":{"search_text":text},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def invite(self, chat_id, user_ids):
		inData = {
		    "method":"addGroupMembers",
		    "input":{
		        "group_guid": chat_id,
				"member_guids": user_ids
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def inviteChannel(self, chat_id, user_ids):
		inData = {
		    "method":"addChannelMembers",
		    "input":{
		        "channel_guid": chat_id,
				"member_guids": user_ids
		    },
		    "client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getGroupAdmins(self, chat_id):
		inData = {
			"method":"getGroupAdminMembers",
			"input":{
				"group_guid":chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getChannelInfo(self, channel_guid):
		inData = {
			"method":"getChannelInfo",
			"input":{
				"channel_guid":channel_guid
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	def ADD_NumberPhone(self, first_num, last_num, numberPhone):
		inData = {
			"method":"addAddressBook",
			"input":{
				"first_name":first_num,
				"last_name":last_num,
				"phone":numberPhone
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue



	def getMessagesInfo(self, chat_id, message_ids):
		inData = {
			"method":"getMessagesByID",
			"input":{
				"object_guid": chat_id,
				"message_ids": message_ids
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get('messages')
				break
			except: continue

	def getMessages_info_android(self, chat_id, message_ids):
		inData = {
			"method":"getMessagesByID",
			"input":{
				"message_ids": message_ids,
				"object_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("messages")
				break
			except: continue


	def setMembersAccess(self, chat_id, access_list):
		inData = {
			"method":"setGroupDefaultAccess",
			"input":{
				"access_list": access_list,
				"group_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read())
				break
			except: continue

	def getGroupMembers(self, chat_id, start_id=None):
		inData = {
			"method":"getGroupAllMembers",
			"input":{
				"group_guid": chat_id,
				"start_id": start_id
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getGroupLink(self, chat_id):
		inData = {
			"method":"getGroupLink",
			"input":{
				"group_guid":chat_id
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("join_link")
				break
			except: continue

	def changeGroupLink(self, chat_id):
		inData = {
			"method":"getGroupLink",
			"input":{
				"group_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("join_link")
				break
			except: continue

	def setGroupTimer(self, chat_id, time):
		inData = {
			"method":"editGroupInfo",
			"input":{
				"group_guid": chat_id,
				"slow_mode": time,
				"updated_parameters":["slow_mode"]
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def setGroupAdmin(self, chat_id, user_id):
		inData = {
			"method":"setGroupAdmin",
			"input":{
				"group_guid": chat_id,
				"access_list":["SetJoinLink"],
				"action": "SetAdmin",
				"member_guid": user_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def deleteGroupAdmin(self,c,user_id):
		inData = {
			"method":"setGroupAdmin",
			"input":{
				"group_guid": c,
				"action": "UnsetAdmin",
				"member_guid": user_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def setChannelAdmin(self, chat_id, user_id, access_list=[]):
		inData = {
			"method":"setGroupAdmin",
			"input":{
				"group_guid": chat_id,
				"access_list": access_list,
				"action": "SetAdmin",
				"member_guid": user_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getStickersByEmoji(self,emojee):
		inData = {
			"method":"getStickersByEmoji",
			"input":{
				"emoji_character": emojee,
				"suggest_by": "All"
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def setActionChatun(self,guid):
		inData = {
			"method":"setActionChat",
			"input":{
				"action": "Unmute",
				"object_guid": guid
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def setActionChatmut(self,guid):
		inData = {
			"method":"setActionChat",
			"input":{
				"action": "Mute",
				"object_guid": guid
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	
	def sendPoll(self,guid,SOAL,LIST):
		inData = {
			"method":"lcreatePoll",
			"input":{
				"allows_multiple_answers": "false",
				"is_anonymous": "true",
				"object_guid": guid,
				"options":LIST,
				"question":SOAL,
				"rnd":f"{randint(100000,999999999)}",
				"type":"Regular"
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getLinkFromAppUrl(self, app_url):
	    inData = {"method":"getLinkFromAppUrl","input":{"app_url":app_url},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("link").get("open_chat_data")
	            break
	        except:continue
	        
	def serch(self,object_guid, search_text):
	    inData = {"method":"searchChatMessages","input":{"object_guid":object_guid,"search_text":search_text,"type":"Text"},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("message_ids")[:5]
	            break
	        except:continue
	    
	    
	def checkUserUsername(self, username):
	    inData = {"method":"checkUserUsername","input":{"username":username},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	            break
	        except:continue
	        
	def botget(self, bot_guid):
	    inData = {"method":"getBotInfo","input":{"bot_guid":bot_guid},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	            break
	        except:continue
			
	def forwardMessages(self, From, message_ids, to):
		inData = {
			"method":"forwardMessages",
			"input":{
				"from_object_guid": From,
				"message_ids": message_ids,
				"rnd": f"{randint(100000,999999999)}",
				"to_object_guid": to
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def chatGroupvisit(self,guid,visiblemsg):
		inData = {
			"method":"editGroupInfo",
			"input":{
				"chat_history_for_new_members": "Visible",
				"group_guid": guid,
				"updated_parameters": visiblemsg
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def chatGrouphidden(self,guid,hiddenmsg):
		inData = {
			"method":"editGroupInfo",
			"input":{
				"chat_history_for_new_members": "Hidden",
				"group_guid": guid,
				"updated_parameters": hiddenmsg
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	def pin(self, chat_id, message_id):
		inData = {
			"method":"setPinMessage",
			"input":{
				"action":"Pin",
			 	"message_id": message_id,
			 	"object_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def unpin(self, chat_id, message_id):
		inData = {
			"method":"setPinMessage",
			"input":{
				"action":"Unpin",
			 	"message_id": message_id,
			 	"object_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def addChannelMembers(self, group_guid, member_guids):
	    inData = {"method":"addChannelMembers","input":{"group_guid":group_guid,"member_guids":member_guids},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def addGroupMembers(self, group_guid, member_guids):
	    inData = {"method":"addGroupMembers","input":{"group_guid":group_guid,"member_guids":member_guids},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def logout(self):
		inData = {
			"method":"logout",
			"input":{},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def channelPreviewByJoinLink(self, link):
	    hashLink = link.split("/")[-1]
	    inData = {"method":"channelPreviewByJoinLink","input":{"hash_link": hashLink},"client": SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get('data').get('channel')
	        except:continue
	def joinChannelByLink(self, link):
	    hashLink = link.split("/")[-1]
	    inData = {"method":"joinChannelByLink","input":{"hash_link": hashLink},"client": SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get('data').get('channel')
	        except:continue
	def joinGroup(self, link):
		hashLink = link.split("/")[-1]
		inData = {
			"method":"joinGroup",
			"input":{
				"hash_link": hashLink
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def joinChannel(self, link):
		hashLink = link.split("/")[-1]
		inData = {
			"method":"joinChannelByLink",
			"input":{
				"hash_link": hashLink
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def deleteChatHistory(self, chat_id, msg_id):
		inData = {
			"method":"deleteChatHistory",
			"input":{
				"last_message_id": msg_id,
				"object_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def leaveGroup(self,chat_id):
		inData = {
			"method":"leaveGroup",
			"input":{
				"group_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def editnameGroup(self,groupgu,namegp,biogp=None):
		inData = {
			"method":"editGroupInfo",
			"input":{
				"description": biogp,
				"group_guid": groupgu,
				"title":namegp,
				"updated_parameters":["title","description"]
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def editbioGroup(self,groupgu,biogp,namegp=None):
		inData = {
			"method":"editGroupInfo",
			"input":{
				"description": biogp,
				"group_guid": groupgu,
				"title":namegp,
				"updated_parameters":["title","description"]
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def joinChannelByID(self, chat_id):
		inData = {
			"method":"joinChannelAction",
			"input":{
				"action": "Join",
				"channel_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def LeaveChannel(self,chat_id):
		inData = {
			"method":"joinChannelAction",
			"input":{
				"action": "Leave",
				"channel_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def block(self, chat_id):
		inData = {
			"method":"setBlockUser",
			"input":{
				"action": "Block",
				"user_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getBotInfo(self, chat_id):
	    inData = {
			"method":"getBotInfo",
			"input":{
				"bot_guid":chat_id
			},
			"client": SetClines.web
		}

	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	            break
	        except: continue
	         
	def unblock(self, chat_id):
		inData = {
			"method":"setBlockUser",
			"input":{
				"action": "Unblock",
				"user_guid": chat_id
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getChannelMembers(self, channel_guid, text=None, start_id=None):
		inData = {
			"method":"getChannelAllMembers",
			"input":{
				"channel_guid":channel_guid,
				"search_text":text,
				"start_id":start_id,
			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	
	def startVoiceChat(self, chat_id):
		inData = {
			"method":"createGroupVoiceChat",
			"input":{
				"chat_guid":chat_id
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def editVoiceChat(self,chat_id,voice_chat_id, title):
		inData = {
			"method":"setGroupVoiceChatSetting",
			"input":{
				"chat_guid":chat_id,
				"voice_chat_id" : voice_chat_id,
				"title" : title ,
				"updated_parameters": ["title"]
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def getUserInfo(self, chat_id):
		inData = {
			"method":"getUserInfo",
			"input":{
				"user_guid":chat_id
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("user")
				break
			except: continue


	def finishVoiceChat(self, chat_id, voice_chat_id):
		inData = {
			"method":"discardGroupVoiceChat",
			"input":{
				"chat_guid":chat_id,
				"voice_chat_id" : voice_chat_id
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	def group(self, name, member_guids=None):
	    inData = {"method":"addGroup","input":{"member_guids":member_guids,"title":name},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getAbsObjects(self, objects_guids):
	    inData = {"method":"getAbsObjects","input":{"objects_guids":objects_guids},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getContactsUpdates(self):
	    time_stamp = str(round(datetime.datetime.today().timestamp()) - 200)
	    inData = {"method":"getContactsUpdates","input":{"state":time_stamp},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getChatsUpdate(self):
		time_stamp = str(round(datetime.datetime.today().timestamp()) - 200)
		inData = {
			"method":"getChatsUpdates",
			"input":{
				"state":time_stamp,
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("chats")
				break
			except: continue

	def getMessagesChats(self, start_id=None):
		time_stamp = str(round(datetime.datetime.today().timestamp()) - 200)
		inData = {
			"method":"getChats",
			"input":{
				"start_id":start_id
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get('data').get('chats')
				break
			except: continue

	def see_GH_whith_Linkes(self,link_gh):
		inData = {
			"method":"groupPreviewByJoinLink",
			"input":{
				"hash_link": link_gh
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data")
				break
			except: continue

	def _requestSendFile(self, file):
		inData = {
			"method":"requestSendFile",
			"input":{
				"file_name": str(file.split("/")[-1]),
				"mime": file.split(".")[-1],
				"size": Path(file).stat().st_size
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data")
				break
			except: continue

	def _uploadFile(self, file):
		if not "http" in file:
			REQUES = shad._requestSendFile(self, file)
			bytef = open(file,"rb").read()

			hash_send = REQUES["access_hash_send"]
			file_id = REQUES["id"]
			url = REQUES["upload_url"]

			header = {
				'auth':self.Auth,
				'Host':url.replace("https://","").replace("/UploadFile.ashx",""),
				'chunk-size':str(Path(file).stat().st_size),
				'file-id':str(file_id),
				'access-hash-send':hash_send,
				"content-type": "application/octet-stream",
				"content-length": str(Path(file).stat().st_size),
				"accept-encoding": "gzip",
				"user-agent": "okhttp/3.12.1"
			}

			if len(bytef) <= 131072:
				header["part-number"], header["total-part"] = "1","1"

				while True:
					try:
						j = post(data=bytef,url=url,headers=header).text
						j = loads(j)['data']['access_hash_rec']
						break
					except Exception as e:
						continue

				return [REQUES, j]
			else:
				t = round(len(bytef) / 131072 + 1)
				for i in range(1,t+1):
					if i != t:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
								o = post(data=bytef[k:k + 131072],url=url,headers=header).text
								o = loads(o)['data']
								break
							except Exception as e:
								continue
					else:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
								p = post(data=bytef[k:],url=url,headers=header).text
								p = loads(p)['data']['access_hash_rec']
								break
							except Exception as e:
								continue
						return [REQUES, p]
		else:
			REQUES = {
				"method":"requestSendFile",
				"input":{
					"file_name": file.split("/")[-1],
					"mime": file.split(".")[-1],
					"size": len(get(file).content)
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data")
				break
			except: continue

			hash_send = REQUES["access_hash_send"]
			file_id = REQUES["id"]
			url = REQUES["upload_url"]
			bytef = get(file).content

			header = {
				'auth':self.Auth,
				'Host':url.replace("https://","").replace("/UploadFile.ashx",""),
				'chunk-size':str(len(get(file).content)),
				'file-id':str(file_id),
				'access-hash-send':hash_send,
				"content-type": "application/octet-stream",
				"content-length": str(len(get(file).content)),
				"accept-encoding": "gzip",
				"user-agent": "okhttp/3.12.1"
			}

			if len(bytef) <= 131072:
				header["part-number"], header["total-part"] = "1","1"

				while True:
					try:
						j = post(data=bytef,url=url,headers=header).text
						j = loads(j)['data']['access_hash_rec']
						break
					except Exception as e:
						continue

				return [REQUES, j]
			else:
				t = round(len(bytef) / 131072 + 1)
				for i in range(1,t+1):
					if i != t:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
								o = post(data=bytef[k:k + 131072],url=url,headers=header).text
								o = loads(o)['data']
								break
							except Exception as e:
								continue
					else:
						k = i - 1
						k = k * 131072
						while True:
							try:
								header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
								p = post(data=bytef[k:],url=url,headers=header).text
								p = loads(p)['data']['access_hash_rec']
								break
							except Exception as e:
								continue
						return [REQUES, p]


	def _getThumbInline(image_bytes:bytes):
		import io, base64, PIL.Image
		im = PIL.Image.open(io.BytesIO(image_bytes))
		width, height = im.size
		if height > width:
			new_height = 40
			new_width  = round(new_height * width / height)
		else:
			new_width  = 40
			new_height = round(new_width * height / width)
		im = im.resize((new_width, new_height), PIL.Image.ANTIALIAS)
		changed_image = io.BytesIO()
		im.save(changed_image, format='PNG')
		changed_image = changed_image.getvalue()
		return base64.b64encode(changed_image)

	def _getImageSize(image_bytes:bytes):
		import io, PIL.Image
		im = PIL.Image.open(io.BytesIO(image_bytes))
		width, height = im.size
		return [width , height]



	def uploadAvatar_replay(self,myguid,files_ide):
		inData = {
			"method":"uploadAvatar",
			"input":{
				"object_guid":myguid,
				"thumbnail_file_id":files_ide,
				"main_file_id":files_ide
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def uploadAvatar(self,myguid,main,thumbnail=None):
		mainID = str(shad._uploadFile(self, main)[0]["id"])
		thumbnailID = str(shad._uploadFile(self, thumbnail or main)[0]["id"])
		inData = {
			"method":"uploadAvatar",
			"input":{
				"object_guid":myguid,
				"thumbnail_file_id":thumbnailID,
				"main_file_id":mainID
			},
			"client": SetClines.web
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("user")
				break
			except: continue

	def getAvatar(self, myguid):
	    inData = {"method":"getAvatars","input":{"object_guid":myguid},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data").get("avatars")
	        except:continue
	def deleteAvatar(self,myguid,avatar_id):
	    inData = {"method":"deleteAvatar","input":{"object_guid":myguid,"avatar_id":avatar_id},"client": SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc'))).get("data")
	        except:continue
	def terminateSession(self, session_key):
	    inData = {"method":"terminateSession","input":{"session_key":session_key},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def Devices_rubika(self):
		inData = {
			"method":"getMySessions",
			"input":{

			},
			"client": SetClines.android
		}

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	def sendDocument(self, chat_id, file, caption=None, message_id=None):
		uresponse = shad._uploadFile(self, file)
		file_id = str(uresponse[0]["id"])
		mime = file.split(".")[-1]
		dc_id = uresponse[0]["dc_id"]
		access_hash_rec = uresponse[1]
		file_name = file.split("/")[-1]
		size = str(len(get(file).content if "http" in file else open(file,"rb").read()))

		inData = {
			"method":"sendMessage",
			"input":{
				"object_guid":chat_id,
				"reply_to_message_id":message_id,
				"rnd":f"{randint(100000,999999999)}",
				"file_inline":{
					"dc_id":str(dc_id),
					"file_id":str(file_id),
					"type":"File",
					"file_name":file_name,
					"size":size,
					"mime":mime,
					"access_hash_rec":access_hash_rec
				}
			},
			"client": SetClines.web
		}

		if caption != None: inData["input"]["text"] = caption


		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	def sendDocument_rplay(self,chat_id,file_id,mime,dc_id,access_hash_rec,file_name,size,caption=None,message_id=None):
		inData = {
			"method":"sendMessage",
			"input":{
				"object_guid":chat_id,
				"reply_to_message_id":message_id,
				"rnd":f"{randint(100000,999999999)}",
				"file_inline":{
					"dc_id":str(dc_id),
					"file_id":str(file_id),
					"type":"File",
					"file_name":file_name,
					"size":size,
					"mime":mime,
					"access_hash_rec":access_hash_rec
				}
			},
			"client": SetClines.web
		}

		if caption != None: inData["input"]["text"] = caption


		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue


	
	                
	def sendVoice(self, chat_id, file, time, caption=None, message_id=None):
		uresponse = shad._uploadFile(self, file)
		file_id = str(uresponse[0]["id"])
		mime = file.split(".")[-1]
		dc_id = uresponse[0]["dc_id"]
		access_hash_rec = uresponse[1]
		file_name = file.split("/")[-1]
		size = str(len(get(file).content if "http" in file else open(file,"rb").read()))

		inData = {
				"method":"sendMessage",
				"input":{
					"file_inline": {
						"dc_id": dc_id,
						"file_id": file_id,
						"type":"Voice",
						"file_name": file_name,
						"size": size,
						"time": time,
						"mime": mime,
						"access_hash_rec": access_hash_rec,
					},
					"object_guid":chat_id,
					"rnd":f"{randint(100000,999999999)}",
					"reply_to_message_id":message_id
				},
				"client": SetClines.web
			}

		if caption != None: inData["input"]["text"] = caption


		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue
		

	
	def sendGIF(self, chat_id, file, width, height, thumbnail="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", caption=None, message_id=None):
	    uresponse = shad._uploadFile(self, file)
	    file_id = str(uresponse[0]["id"])
	    mime = file.split(".")[-1]
	    dc_id = uresponse[0]["dc_id"]
	    access_hash_rec = uresponse[1]
	    file_name = file.split("/")[-1]
	    size = str(len(get(file).content if "http" in file else open(file,"rb").read()))
	    inData = {"method":"sendMessage",
	    "input":{
	    "object_guid":chat_id,
	    "is_mute":False,
	    "rnd":randint(100000,999999999),
	    "file_inline":{
	    "access_hash_rec":access_hash_rec,
	    "dc_id": dc_id,
	    "file_id": file_id,
	    "auto_play": False,
	    "file_name": file_name,
	    "width": width,
	    "height": height,
	    "mime": mime,
	    "size": size,
	    "thumb_inline": thumbnail,
	    "type": "Gif"
	    },
	    "text": caption,
	    "reply_to_message_id":message_id
	    },"client": SetClines.android}
	    while 1:
	         try:
	             return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	         except:continue
	
	def sendPhoto(self, chat_id, file, size=[], thumbnail=None, caption=None, message_id=None):
		uresponse = shad._uploadFile(self, file)
		if thumbnail == None: thumbnail = '/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAIQAABtbnRyUkdC\nIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAA\nAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlk\nZXNjAAAA8AAAAHRyWFlaAAABZAAAABRnWFlaAAABeAAAABRiWFlaAAABjAAAABRyVFJDAAABoAAA\nAChnVFJDAAABoAAAAChiVFJDAAABoAAAACh3dHB0AAAByAAAABRjcHJ0AAAB3AAAADxtbHVjAAAA\nAAAAAAEAAAAMZW5VUwAAAFgAAAAcAHMAUgBHAEIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhZWiAA\nAAAAAABvogAAOPUAAAOQWFlaIAAAAAAAAGKZAAC3hQAAGNpYWVogAAAAAAAAJKAAAA+EAAC2z3Bh\ncmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABYWVogAAAAAAAA9tYAAQAAAADT\nLW1sdWMAAAAAAAAAAQAAAAxlblVTAAAAIAAAABwARwBvAG8AZwBsAGUAIABJAG4AYwAuACAAMgAw\nADEANv/bAEMAEAsMDgwKEA4NDhIREBMYKBoYFhYYMSMlHSg6Mz08OTM4N0BIXE5ARFdFNzhQbVFX\nX2JnaGc+TXF5cGR4XGVnY//bAEMBERISGBUYLxoaL2NCOEJjY2NjY2NjY2NjY2NjY2NjY2NjY2Nj\nY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY//AABEIAFAAUAMBIgACEQEDEQH/xAAaAAADAQEB\nAQAAAAAAAAAAAAACAwUBBgQA/8QAJBAAAgICAgICAgMAAAAAAAAAAQIAAwQRBSESMRNBFSIyQmH/\nxAAXAQADAQAAAAAAAAAAAAAAAAAAAQID/8QAGxEBAQEBAQADAAAAAAAAAAAAAAERIQIDEjH/2gAM\nAwEAAhEDEQA/ALAMMGJBhgxkcDCBiQYYMQNBhAxXlobnis5Hws8ddQCpubEU2ixAwjQYAYM2BuaD\nA0sRiqx+oCOAd6mtyVNZ0wjTr0JSx+o34wo2Yqrk6Cm/ITHzK7B0wiMGXcKk6kPJtLNuezLs899y\nU7P5/wCQCzxeT14mVgepy2NeVca9zo8O35axv3AHgwtwD1NBgaXuLsoSwdiHPoyeHIwlFRKsRqc9\nbm3UWFUc6E6fOYjHYD2ROOy67FsJYHuTV+M3r0jlLmOmaO/IMo/YbEj9g7jVu+m7EnWt8S/i1j51\nZ7HuW+PyPMgq0h8TgpldgdSxXxbUd1NLnWPuY6SrVtQ77gMpU6Mm4r30Eb7lSu1b1/YaMeIlSILt\n4jZhqvkZmQg8CBHJotxE5XONY2vqQ8nkltQgr3KfJ47aOuxIF2P31J9cvV+Z9psCr+RhopZwo7Jn\n1GMzH1Og4fja3cOx7H1JxpPk51V4TH+DFBI0TKgMSoCAAehDBlxlbpoMYra9RAMINAki3kPA6Bn1\nWX8n9pzdmWzd7ilyrEYMrTXZGWWujyCHBBkXMxiCWWUqbfnxhZ9iL2H6MLJYctifh2qr+LiVcNmX\nKU1/xM8rYKu216M9uFS9LjfqTlPYrNYVcA/caDMesWVhvsTB6ipwwGaDAmgyVP/Z\n'
		elif "." in thumbnail:thumbnail = str(shad._getThumbInline(open(file,"rb").read() if not "http" in file else get(file).content))

		if size == []: size = shad._getImageSize(open(file,"rb").read() if not "http" in file else get(file).content)

		file_inline = {
			"dc_id": uresponse[0]["dc_id"],
			"file_id": uresponse[0]["id"],
			"type":"Image",
			"file_name": file.split("/")[-1],
			"size": str(len(get(file).content if "http" in file else open(file,"rb").read())),
			"mime": file.split(".")[-1],
			"access_hash_rec": uresponse[1],
			"width": size[0],
			"height": size[1],
			"thumb_inline": thumbnail
		}

		inData = {
				"method":"sendMessage",
				"input":{
					"file_inline": file_inline,
					"object_guid": chat_id,
					"rnd": f"{randint(100000,999999999)}",
					"reply_to_message_id": message_id
				},
				"client": SetClines.web
			}
		if caption != None: inData["input"]["text"] = caption

		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue

	def addGroup(self, title):
	    inData = {"method":"addGroup","input":{"title":title},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def getDCs():
	    inData = {"method":"getDCs","input":{ },"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def addChannel(self, title):
	    inData = {"method":"addChannel","input":{"channel_type":"Public","title":title},"client":SetClines.web}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._getURL(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
	def sendSticker(self, chat_id, emoji_character, sticker_id, sticker_set_id,message_id=None):
	    inData = {"method":"sendMessage","input":{"object_guid":chat_id,"rnd":f"{randint(100000,999999999)}","reply_to_message_id":message_id,"sticker":{"emoji_character":emoji_character,"sticker_id":sticker_id,"sticker_set_id":sticker_set_id,"w_h_ratio:":"1.0"}},"client":SetClines.android}
	    while 1:
	        try:
	            return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
	        except:continue
        
	def sendMusic(self, chat_id, file, time, caption=None, message_id=None):
		uresponse = shad._uploadFile(self, file)
		file_id = str(uresponse[0]["id"])
		mime = file.split(".")[-1]
		dc_id = uresponse[0]["dc_id"]
		access_hash_rec = uresponse[1]
		file_name = file.split("/")[-1]
		size = str(len(get(file).content if "http" in file else open(file,"rb").read()))

		inData = {
				"method":"sendMessage",
				"input":{
					"file_inline": {
						"dc_id": dc_id,
						"file_id": file_id,
						"type":"Music",
						"music_performer":"",
						"file_name": file_name,
						"size": size,
						"time": time,
						"mime": mime,
						"access_hash_rec": access_hash_rec,
					},
					"object_guid":chat_id,
					"rnd":f"{randint(100000,999999999)}",
					"reply_to_message_id":message_id
				},
				"client": SetClines.android
			}

		if caption != None: inData["input"]["text"] = caption
		
		while 1:
			try:
				return loads(self.enc.decrypt(loads(request.urlopen(request.Request(shad._SendFile(), data=dumps({"api_version":"5","auth": self.Auth,"data_enc":self.enc.encrypt(dumps(inData))}).encode(), headers={'Content-Type': 'application/json'})).read()).get('data_enc')))
				break
			except: continue