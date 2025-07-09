import os
import time
folder_to_watch = os.path.expanduser("~/Desktop/gold")
seen_files = set(os.listdir(folder_to_watch))
print("watching folder:",folder_to_watch)
while True:
	time.sleep(10)
	current_files = set(os.listdir(folder_to_watch))
	new_files = current_files - seem_files
	if new_files :
		print("new files detected:",new_files)
	seen_files = current_files

