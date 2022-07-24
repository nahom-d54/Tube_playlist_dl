import subprocess
import os
import time
#the below command will print file name and file link
playlist_link = "https://www.youtube.com/playlist?list=PLZm_CJDfK_CcV9W8JeP83O7rBke9HSRyu"
video_format_option = "bestvideo[height<=720]"
cmd = ["youtube-dl","-f",f"{video_format_option}","--get-filename","-g",f"{playlist_link}"]
s = subprocess.Popen(cmd,stdout=subprocess.PIPE)
stdout,stderr = s.communicate()

stdout = stdout.decode("utf-8").strip().split("\n")

video_name_link = {}

for i in range(len(stdout)):
	if not i%2==0:
		video_name_link[stdout[i].strip().strip("-")] = stdout[i-1]

print(video_name_link)

def IDM_dl(video_name_link):
	for name,link in video_name_link.items():
		cmd = ['idman','/n','/d',f'"{link}"',"/f",f'"{name}"']
		cmd_text = " ".join(cmd)
		os.system(cmd_text)
		time.sleep(1)
IDM_dl(video_name_link)