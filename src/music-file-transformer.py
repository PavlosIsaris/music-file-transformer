import os 
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root', '-r', help="the root directory to scan", type= str)
parser.add_argument('--extensions', '-e', help="the extensions of the files to transform to mp3 (eg wma), with the preceding dot (.)", type= str)
parser.add_argument('--keep', '-k', help="whether to keep the old file or not", type= int, default= 1)
parser.add_argument('--frequency', '-f', help="the desired output frequency, as integer (eg 44100 or 48000)", type= int, default= 1)
parser.add_argument('--bitrate', '-b', help="the desired output bitrate, as integer (eg 192 or 320)", type= int, default= 1)

def main(rootDir, extensions, keepOld, outputFrequency, outputBitrate):
	subDirectories, files = scanDirectoryAndGetFixableFiles(rootDir, extensions)
	print("Eligible files: " + str(len(files)))
	for sourceFile in files:
		print("Transforming: " + sourceFile)
		targetFile = os.path.splitext(sourceFile)[0] + ".mp3"
		print("Target: " + targetFile)
		command = 'ffmpeg -y -i "{0}" -vn -ar {1} -ac 2 -b:a {2}k "{3}"'.format(sourceFile, outputFrequency, outputBitrate, targetFile)
		print(command)
		os.system(command)
		print("File transformation completed!")
		if keepOld == 0:
			os.remove(sourceFile)
			print("Source file removed!")
	

def scanDirectoryAndGetFixableFiles(dir, ext):
	subDirectories, files = [], []

	for f in os.scandir(dir):
		if f.is_dir():
			subDirectories.append(f.path)
		if f.is_file():
			if os.path.splitext(f.name)[1].lower() in ext:
				files.append(f.path)


	for dir in list(subDirectories):
		sf, f = scanDirectoryAndGetFixableFiles(dir, ext)
		subDirectories.extend(sf)
		files.extend(f)
	
	return subDirectories, files

# Driver Code 
if __name__ == '__main__':
	args=parser.parse_args()
	root = args.root
	if root is None:
		raise Exception("root directory argument is required")

	extensions = args.extensions
	if extensions is None:
		print("File extensions not specified. Using default value: 'wma'")
		extensions = ['.wma']
	else:
		extensions = extensions.split(',')

	keepOld = args.keep
	if keepOld is None:
		print("File extension not specified. Using default value: true")
		keepOld = 1

	outputFrequency = args.frequency
	if outputFrequency is None:
		print("Output frequency not specified. Using default value: 44100")
		outputFrequency = 44100

	outputBitrate = args.bitrate
	if outputBitrate is None:
		print("Output bitrate not specified. Using default value: 320")
		outputBitrate = 320

	main(rootDir=root, extensions=extensions, keepOld=keepOld, outputFrequency=outputFrequency, outputBitrate=outputBitrate)
     