import aiohttp
import asyncio
from Hosein_Tabr.Encoder import encoderjson
from Hosein_Tabr.GtM import default_api
from json import dumps, loads
from random import choice
from Hosein_Tabr.Clien import clien


async def http(js,auth):
	Full = default_api()
	s = Full.defaultapi()
	enc = encoderjson(auth)
	async with aiohttp.ClientSession() as session:
		async with session.post(s, data = dumps({"api_version":"5","auth": auth,"data_enc":enc.encrypt(dumps(js))}) , headers = {'Content-Type': 'application/json'}) as response:
			Post =  await response.text()
			return Post

async def rubino(js,auth,clien,method):
	s = "https://rubino12.iranlms.ir"
	enc = encoderjson(auth)
	async with aiohttp.ClientSession() as session:
		async with session.post(s, data = dumps({"api_version":"0","auth": auth,"client":clien,"data":js,"method":method})) as response:
			Post =  await response.json()
			return Post

async def httpregister(js,auth):
	Full = default_api()
	s = Full.defaultapi()
	enc = encoderjson(auth)
	async with aiohttp.ClientSession() as session:
		async with session.post(s, data = dumps({"api_version":"5","auth": auth,"method":"registerDevice","client": clien.android,"data_enc":enc.encrypt(dumps(js))}) , headers = {'Content-Type': 'application/json'}) as response:
			Post =  await response.text()
			return Post


async def _download_with_server(server):
	async with aiohttp.ClientSession() as session:
		async with session.get(server) as response:
			Post =  await response.read()
			return Post

async def _download(server,header):
	async with aiohttp.ClientSession() as session:
		async with session.get(server,header) as response:
			Post =  await response.read()
			return Post

async def httpfiles(s,dade,head):
	async with aiohttp.ClientSession() as session:
		async with session.post(s, data = dade  , headers = head) as response:
			Post =  await response.text()
			return Post


class method_Rubika:
	def __init__(self,auth:str):
		self.Auth = auth
		self.enc = encoderjson(auth)

	def methodsRubika(self,types:str = None,methode:str = None,indata:dict = None,wn:dict = None,server:str = None,podata = None,header:dict = None):
		self.Type = types
		self.inData = {"method":methode,"input":indata,"client":wn}
		self.serverfile = server
		self.datafile = podata
		self.headerfile = header
		while 1:
			try:
				loop = asyncio.get_event_loop()
				if self.Type == "json":
					return loads(self.enc.decrypt(loads(loop.run_until_complete(http(self.inData,self.Auth))).get("data_enc")))
					break
				elif self.Type == "file":
					return loop.run_until_complete(httpfiles(self.serverfile,self.datafile,self.headerfile))
					break
				elif self.Type == "rubino":
					return loads(self.enc.decrypt(loads(loop.run_until_complete(rubino(indata,self.Auth,wn,methode))).get("data_enc")))
					break
			except:
				continue
