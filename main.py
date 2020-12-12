import stegEncode as e
import stegDecode as d

def startSeq():
	tool = int(input("Would you like to encode or decode? (1/2): "))
	valid = False
	while not valid:
		if tool == 1:
			valid = True
			encode()
		elif tool == 2:
			valid = True
			decode()
		else:
			print("Invalid Input. Please try again.")
			startSeq()

def encode():
	msg = input("Please enter your message: ")
	img = input("Please enter the filepath of your image. Note, this software only works with PNG images. : ")
	newName = input("Please enter a name for the encoded image: ")
	if e.isImageSuitable(msg, img):
		print("Processing...")
		msgInfo = e.convertMsgToBin(msg)
		imageInfo = e.convertImageToBin(img)
		newMsg = e.generateEncodedBytes(msgInfo, imageInfo)
		e.constructNewImage(newMsg, img, newName)
	else:
		print("This image is not large enough for your message, please try again.")
		encode()
	print("Success!")

def decode():
	img = input("Please enter the filepath of your image. Note, this software only works with PNG images. : ")
	print("Processing...")
	imgInfo = d.generateImageBytes(img)
	msgInfo = d.extractMsgBytes(imgInfo)
	msg = d.generateMsg(msgInfo)
	printRange = d.getMsgPrintRange(msg)
	print("Success!")
	print("Decoded Message:" + msg[printRange[0]:printRange[1]])

startSeq()
