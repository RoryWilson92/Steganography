from PIL import Image
from textwrap import wrap


def isImageSuitable(msg, img):
	im = Image.open(img)
	pixelCount = (len(msg) * 8) * (4 / 3)
	width, height = im.size
	imgSize = width * height
	if pixelCount > imgSize:
		return False
	else:
		return True


def convertMsgToBin(msg):
	length = len(msg)
	msg = str(length) + ' ' + msg
	msgBytes = []
	for i in range(len(msg)):
		num = ord(msg[i])
		binary = format(num, '08b')
		msgBytes.append(binary)
	return msgBytes


def convertImageToBin(img):
	imgBytes = []
	im = Image.open(img)
	width, height = im.size
	pixels = list(im.getdata())
	for i in range(len(pixels)):
			rgb = pixels[i]
			for colour in range(3):
				binary = format(rgb[colour], '08b')
				imgBytes.append(binary)
	return imgBytes


def generateEncodedBytes(msgBytes, imgBytes):
	msgDualBits = []
	encodedBytes = []
	for i in range(len(msgBytes)):
		dualBits = wrap(msgBytes[i], 2)
		for c in range(4):
			msgDualBits.append(dualBits[c])
	for i in range(len(msgDualBits)):
		newByte = (imgBytes[i])[:6] + msgDualBits[i]
		encodedBytes.append(newByte)
	for i in range(len(encodedBytes), len(imgBytes)):
		encodedBytes.append(imgBytes[i])
	return encodedBytes


def constructNewImage(Bytes, originalImage, newName):
	im = Image.open(originalImage)
	pixels = []
	for i in range(0, len(Bytes), 3):
		rgb = (int(Bytes[i], 2), int(Bytes[i + 1], 2), int(Bytes[i + 2], 2))
		pixels.append(rgb)
	im2 = Image.new(im.mode, im.size)
	im2.putdata(pixels)
	im2.save(newName, "PNG")
