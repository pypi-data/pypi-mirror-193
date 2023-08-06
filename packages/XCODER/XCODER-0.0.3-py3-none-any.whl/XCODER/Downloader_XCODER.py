from os import system
from requests import get
from arsein import Robot_Rubika
import rainbowtext, pyfiglet
system("clear")

class xco_downloader:
	def __init__(self, Sh_account, Link_Post):
		self.Auth = Sh_account
		self.Link = Link_Post

Link = self.Link

auth = self.Auth

xco = Robot_Rubika(auth[0])

td , nd = 0 , 0

class color:
	red = '\033[91m'
	green = '\033[92m'
	blue = '\033[94m'
	yellow = '\033[93m'
	magenta = '\033[95m'
	cyan = '\033[96m'
	white = '\033[97m'
	bold = '\033[1m'
	underline = '\033[4m'
	black='\033[30m'

text = '       X CODER'
txt = rainbowtext.text(pyfiglet.figlet_format(text))
print(txt)
print(f"\n {color.blue}      [+] - O W N E R  ID : @X_CODER\n       [+] - Channell ID   : @X_CODER_2721\n")
print(f"{color.yellow}______________________________________________________\n")

try:
	ms = xco.Infolinkpost(Link)["data"]["link"]["open_chat_data"]
	data_Download = xco.getMessagesInfo(ms["object_guid"],[ms["message_id"]])["data"]["messages"][0]
except:
	print(f"{color.red}             Your post was not found")
	exit()

def download(hep,acc):
	size = hep["file_inline"]["size"]
	dc_id = str(hep["file_inline"]["dc_id"])
	file_id = str(hep["file_inline"]["file_id"])
	name = hep["file_inline"]["file_name"]
	accessHashRec = hep["file_inline"]["access_hash_rec"]
	
	dan_req = get(
          url=f'https://messenger{str(dc_id)}.iranlms.ir/GetFile.ashx',
          headers={
               'auth': acc,
               'file-id':file_id, 
               'start-index': '0', 
               'last-index': str(size),
               'access-hash-rec':accessHashRec
               }
            ).reason
	
	return size,name,dan_req

def auth_checker(check):
	xco_check = Robot_Rubika(check)
	met_check = xco_check.getInfoByUsername('X_CODER')
	if met_check['status'] != 'OK':
		auth.remove(check)
	return met_check['status']

def chup(type,info_dn,sizes_file,size_all,auth_er):
	OK_DO = f"""{color.red}  X CODER {color.white}| {color.blue}BoT {color.red}>>>{color.green} DOWNLOADED

 {color.magenta}[ {color.blue}NAME File{color.magenta} ] {color.red}: {color.magenta}[{color.cyan}{info_dn[1]}{color.magenta}]
 {color.magenta}[ {color.blue}SIZE File{color.magenta} ] {color.red}: {color.magenta}[{color.cyan}{sizes_file}{color.magenta}]
 {color.magenta}[ {color.blue}DN volume {color.magenta}] {color.red}: {color.magenta}[{color.cyan}{size_all}{color.magenta}]
 {color.magenta}[ {color.blue}NUMBER DN{color.magenta} ] {color.red}: {color.magenta}[  {color.cyan}{td}{color.magenta}  ]

{color.yellow}______________________________________________________
"""
	NO_DO = f"""{color.red}  X CODER {color.white}| {color.blue}BoT {color.red}>>>{color.red} NOT DOWNLOADED !!

 {color.magenta}[ {color.blue}AUTH EROR{color.magenta} ] {color.red}: {color.magenta}[{color.cyan}{auth_er}{color.magenta}]
 {color.magenta}[ {color.blue}NUMBER ER{color.magenta} ] {color.red}: {color.magenta}[  {color.cyan}{nd}{color.magenta}  ]

{color.yellow}______________________________________________________
"""
	NO_RE = f"""{color.red}  X CODER {color.white}| {color.blue}BoT {color.red}>>>{color.red} NOT DOWNLOADED !!

 {color.magenta}[ {color.blue}requests EROR{color.magenta} ] {color.red}: {color.magenta}[{color.cyan}{info_dn[2]}{color.magenta}]
 {color.magenta}[ {color.blue}NUMBER ER{color.magenta} ] {color.red}: {color.magenta}[  {color.cyan}{nd}{color.magenta}  ]

{color.yellow}______________________________________________________
"""
	if type == 'OK':
		return OK_DO
	elif type == 'NO_RE':
		return NO_RE
	elif type == 'NO':
		return NO_DO

while True:
	try:
		for x in auth:
			auth_ch = auth_checker(x)
			if len(auth) == 0:
				print(f"{color.red}             Auth has been invalidated")
				exit()
			if auth_ch == "OK":
				okb = download(data_Download,x)
				if okb[2] == "OK":
					td += 1
					Size = int(okb[0])
					size_ko = Size * td
					if Size / 1073741824 > 1:
						size_true = Size / 1073741824
						sizes = f"{round(size_true)} GB"
					elif Size / 1048576 > 1:
						size_true = Size / 1048576
						sizes = f"{round(size_true)} MB"
					elif Size / 1024 > 1:
						size_true = Size / 1024
						sizes = f"{round(size_true)} KB"
					else:
						sizes = f"{round(size)} B"

					if size_ko / 1073741824 > 1:
						size_true2 = size_ko / 1073741824
						size_kol = f"{round(size_true2)} GB"
					elif size_ko / 1048576 > 1:
						size_true2 = size_ko / 1048576
						size_kol = f"{round(size_true2)} MB"
					elif size_ko / 1024 > 1:
						size_true2 = size_ko / 1024
						size_kol = f"{round(size_true2)} KB"
					else:
						size_kol = f"{round(size_ko)} B"
					print(chup('OK',okb,sizes,size_kol,x))
				else:
					nd += 1
					print(chup('NO_RE',okb,sizes,size_kol,x))
			else:
				nd += 1
				print(chup('NO',okb,sizes,size_kol,x))
	except:continue

exit()