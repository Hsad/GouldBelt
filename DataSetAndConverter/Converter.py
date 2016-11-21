from math import *
print("hello")
f = open("wbvr\\WBVR2.DAT", "r")
#w = open("XYZ.txt", "w")
m = open("wbvr\\Mags.txt", "r")

lines = []
for l in f.readlines():
	lines.append(l.split())

mags = []
magDict = {}
for l in m.readlines():
	tem = l.split()
	mags.append(tem)
	magDict[tem[0]] = tem

#print(magDict)
#print(lines[0])
linelen = len(lines[0])
#w.write("var StarData = [\n")

spectralType = ["O","B","A","F","G","K","M"]
maxMag = 0
minMag = 10000
for li in lines:
	if len(li) != linelen:
		#print(li)
		pass
	else:
		#normal size
		for i,char in enumerate(li[5]):
			if char in spectralType:
				letter = char
				try:
					number = int(li[5][i+1]) 
				except (ValueError, IndexError):
					number = 0
				break
		#calculate distance
		#print(magDict[letter+str(number)][2])
		try:
			res = magDict[letter+str(number)][2]
			#print(res)
		except KeyError:
			print(letter+str(number))
			#pass
		if float(li[6]) > maxMag:
			maxMag = float(li[6])
		elif float(li[6]) < minMag:
			minMag = float(li[6])
		"""
		print(li[6])#mag m
		print(res)#actual M
		dist = pow(10, (float(li[6]) - float(res) + 5)/5)
		print(dist)
		#calculate angles
		rah = float(li[1])
		ram = float(li[2])
		ra = rah + ram/60 #alpha
		decd = float(li[3])
		decm = float(li[4])
		dec = decd + decm/60 #phi

		b = asin(cos(dec)*cos(27.4)*cos(ra-192.25)+sin(dec)*sin(27.4))
		l = atan2((sin(dec)-sin(ra)*sin(27.4)), (cos(dec)*cos(27.4)*sin(ra-192.25))) + 33
		print("galactic")
		print(b)
		print(l) 
		print(dist)
		#calculate XYZ
		x = dist * sin(b) * cos(l)
		y = dist * sin(b) * sin(l)
		z = dist * cos(b) 
		#save loc, and mag
		w.write("{ ")
		w.write("\"x\":"+str(x)+",")
		w.write("\"y\":"+str(y)+",")
		w.write("\"z\":"+str(z)+",")
		w.write("\"mag\":"+li[6])
		w.write("},\n")
		"""
	print(minMag)
	print(maxMag)

#conversion formula, d = 10^(m-M+5)/5

#need to make a dictionary of mag types

#need to interpolate the values
