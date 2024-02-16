import os
import shutil

src_path = "/content/FaceSwap/CelebAMask-HQ/CelebA-HQ-img"
dest_path = "/content/FaceSwap/CelebA-HQ-img_Train"

src_dir = os.listdir(path=src_path)
curr_iter = 0
file_iter = 0
files_per_folder = 30
new_folder_iter = 0
new_file_path = ''

print("Processing...")

for image_file in src_dir:
	file_iter += 1
	if curr_iter % files_per_folder == 0:
		file_iter = 0
		new_folder_iter += 1
		new_folder_format = "{0:06d}".format(new_folder_iter)
		new_file_path = f"{dest_path}/n{new_folder_format}"
		os.makedirs(new_file_path)
	
	new_dest = f"{new_file_path}/{image_file}"
	shutil.copyfile(f"{src_path}/{image_file}", new_dest)
	
	
	new_file_name = "{0:04d}".format(file_iter) + "_01.jpg"
	renamed_file = f"{new_file_path}/{new_file_name}"
	os.rename(new_dest, renamed_file)
	curr_iter += 1
	
	print(f"Processed file: {curr_iter}", end="\r")
	
	if curr_iter + 1 == len(src_dir):
		print("Done")
		break