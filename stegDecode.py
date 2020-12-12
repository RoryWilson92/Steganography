from PIL import Image


def generateImageBytes(img):
	imgBytes = []
	im = Image.open(img)
	pixels = list(im.getdata())
	for i in range(len(pixels)):
		for colour in pixels[i]:
			byte = format(colour, '08b')
			imgBytes.append(byte)
	return imgBytes


def extractMsgBytes(imgBytes):
	msgBytes = []
	for i in range(0, len(imgBytes), 4):
		byte = (imgBytes[i])[6:] + (imgBytes[i + 1])[6:] + (imgBytes[i + 2])[6:] + (imgBytes[i + 3])[6:]
		msgBytes.append(byte)
	return msgBytes


def generateMsg(msgBytes):
	msg = ''
	for i in range(len(msgBytes)):
		num = int(msgBytes[i], 2)
		msg += chr(num)
	return msg


def getMsgPrintRange(msg):
	temp = list(msg)
	length = ''
	i = 0
	while temp[i] != ' ':
		length += temp[i]
		i += 1
	return len(length), int(int(length)) + len(length) + 1
