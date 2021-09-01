#!/usr/bin/python

import requests
import datetime
import argparse
import os
import json
import sys
import random
from colorama import Fore, Back, Style

def upload_file(upload_url, file: str, is_private=False, token=None):

	now = datetime.datetime.now()

	timestampStr = now.strftime("%d-%b-%Y (%H:%M:%S)")

	og_props = {
		"site_name": f"Uploaded @ {timestampStr}",
		"title": f"Suck on deez nuts!",
		"description": f"Visit https://d3r1n.com/ !",
		"color": rand_hex_color(),
 		"discord_hide_url": "false"
	}

	if not os.path.exists(file):
		print(f"{Fore.RED}This file does not exists! {Fore.BLUE+ Style.BRIGHT}Killing Program...{Style.RESET_ALL}")
		sys.exit(1)
	elif os.path.getsize(file) > 0x5F00000:
		print(f"{Fore.RED + Style.BRIGHT}This file is Greater than 95 MB! {Fore.BLUE + Style.BRIGHT}Killing Program...{Style.RESET_ALL}")
		sys.exit(1)
	elif not file.endswith("png") or file.endswith("jpeg") or file.endswith("jpg"):
		print(f"{Fore.RED + Style.BRIGHT}This file is not an image, please upload images! {Fore.BLUE + Style.BRIGHT}Killing Program...{Style.RESET_ALL}")
		sys.exit(1)
	else:
		if is_private:
			pass
		elif is_private and token == None:
			print(f"{Fore.RED + Style.BRIGHT}Provide a private token! {Fore.BLUE + Style.BRIGHT}Killing Program...{Style.RESET_ALL}")
			sys.exit(1)
		else:
			req_body = {
				"token": "",
				"collection_token":"",
				"og_properties": json.dumps(og_props)
			}

			try:
				res = requests.post( upload_url, data=req_body, files={"file": open(file, "rb").read()} ).json()
				print(f"\n\n\t{Fore.GREEN + Style.BRIGHT}---- SUCCESSFUL ----\n")
				print("URL: " + res["url"] + f"\n{Fore.LIGHTCYAN_EX}Uploaded to destination")
				return res["url"]
			except Exception as err:
				print(f"\n\n\t{Fore.RED + Style.BRIGHT}---- SOMETHING WENT WRONG ----\n")
				print(f"{Fore.YELLOW + Style.BRIGHT}[ PLEASE UPLOAD 3 FILES PER MINUTE ]")
				print(f"{Fore.RED + Style.BRIGHT}{err}")
				sys.exit(1)


def rand_hex_color():
	r = lambda: random.randint(0,255)
	return f"#{r()}{r()}{r()}"

def Handler():

	pars = argparse.ArgumentParser(prog="uplad",
                                    usage='%(prog)s [options] <upload> <file>',
                                    description="\n\n\nCustom Image Uploading tool for sxcu.net or other uploaders | Chads Only B) |")

	pars.add_argument('upload',type=str, help='Uploading API endpoint (sxcu.net)')
	pars.add_argument('file', type=str, help='Image to be uploaded')

	args = pars.parse_args()

	upload_file(args.upload, args.file)


if __name__ == '__main__':
	Handler()