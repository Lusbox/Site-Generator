import os
import shutil

def copy_to_dir(source_dir="static", dest_dir="public"):
	if os.path.exists(dest_dir):
		shutil.rmtree(dest_dir)
	os.mkdir(dest_dir)
	def copy(source_dir, dest_dir):
		for item in os.listdir(source_dir):
			source_path = os.path.join(source_dir, item)
			dest_path = os.path.join(dest_dir, item)

			if os.path.isfile(source_path):
				shutil.copy(source_path, dest_path)
				print(f"Copied file: {source_path} to {dest_path}")
			else:
				os.mkdir(dest_path)
				copy(source_path, dest_path)

	copy(source_dir, dest_dir)
