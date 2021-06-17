from glob import glob
import os

def rename_file(source_path):
	
	replaced_filename = source_path.replace("UniSpeech", "UniTTS")
	os.system("mv {} {}".format(source_path, replaced_filename))


if __name__ == "__main__":


	for source_filepath in glob("./**/*.wav", recursive=True):
		if "UniSpeech" in source_filepath:
			rename_file(source_filepath)


