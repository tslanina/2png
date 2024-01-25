from PIL import Image
import glob
import os
import sys

inputFilter = '*.bmp'
outputName = 'index.html'

match len(sys.argv):
	case 2: 
		inputFilter = sys.argv[1]
	case 3:
		inputFilter = sys.argv[1]
		otputName = sys.argv[2]

list = glob.glob(inputFilter)

fileReport = open(outputName,'w')
fileReport.write('<!DOCTYPE html>\n<head>\n <meta charset=\"utf-8\">\n</head>\n')
fileReport.write('<body style=\"background-color:#3e3e3e;color: #d6deeb;margin: 20px 20px;\">\n')

for file in list:
	fileName = os.path.splitext(os.path.basename(file) )[0]
	fileReport.write('<h3>'+fileName+'</h3>\n')
	fileName += '.png'
	Image.open(file).save(fileName)
	fileReport.write('<img src=\"' + fileName + '\"><br><br>\n')
fileReport.write('</body>\n</html>');
fileReport.close()