""" 
Semi-automated alignment of the pin in rasor using three functions:

import alignPin
alignPin.capturePinImages()
alignPin.analysePinImages()
alignPin.fitPinCoords()
alignPin.adjustOffsets()
alignPin.driveToPin()


# need to improve motors to check if limits have been reached, chi limit chagned
# automatic new folder feature needed
# be able to align when system is cold

"""




import time
import os


class alignPin():
	def __init__(self, id=None):
		self.basepath = "/dls_sw/i10/scripts/beamline/rasor/align_pin"
		self.id = id
		
		if self.id == None: self.id = self.whichFolder()
		self.mypath = 	self.basepath+"/%03d" % self.id
		self.pinMasks = self.basepath+"/pin_masks"

		print "align pin %03d" % self.id

	def whichFolder(self):
		""" finds the ID number for the folder which is the highest """
		import os
		if os.path.isdir(self.basepath):
			folders = []
			for i in os.listdir(self.basepath):
				try:
					folders = folders + [int(i)]
				except:
					pass
			folders.sort()
		return folders[len(folders)-1]


	def getPositions(self):
		positions = []
		#x y z th chi


		positions.append([16.0,0,0, 90,90])
		positions.append([17.0,0,0, 90,90])
		positions.append([17.5,0,0, 90,90])
		positions.append([18.0,0,0, 90,90])

		positions.append([18.6,-1.0,0, 90,90])
		positions.append([18.6,-0.5,0, 90,90])
		positions.append([18.6, 0.0,0, 90,90])
		positions.append([18.6, 0.5,0, 90,90])
		positions.append([18.6, 1.0,0, 90,90])

		positions.append([16.0,0,0, 90,94])
		positions.append([17.0,0,0, 90,94])
		positions.append([18.0,0,0, 90,94])

		positions.append([18.6,0,0, 90,94])
		positions.append([18.6,0,0, 0,94])
		positions.append([18.6,0,0, -90,94])

		positions.append([18.6,-1.0,0, -90,90])
		positions.append([18.6,-0.5,0, -90,90])
		positions.append([18.6, 0.0,0, -90,90])
		positions.append([18.6, 0.5,0, -90,90])
		positions.append([18.6, 1.0,0, -90,90])

		positions.append([18.6,0,0, -90,90])
		positions.append([18.6,0,0, 0,90])
		positions.append([18.6,0,0, 90,90])

		positions.append([16.0,0,0, 90,86])
		positions.append([17.0,0,0, 90,86])
		positions.append([18.0,0,0, 90,86])

		positions.append([18.6,0,0, 90,86])
		positions.append([18.6,0,0, 0,86])
		positions.append([18.6,0,0, -90,86])

		return positions





	#################################################################################################################################


	def findPositions(self):
		import os
		positions = []
		if os.path.isdir(self.mypath):
			for file in os.listdir(self.mypath):
				if file.endswith(".png"):
					temp = str(file).split('.png')[0]
					positions.append( [float(x) for x in temp.split('_')[1:]] )
		return positions	

	#################################################################################################################################


	def driveToPin(self):
		from beamline import device
		cry = device("ME01D-MO-CRYO-01")
		cry.caput("X.VAL", 18.6)
		cry.caput("Y.VAL", 0)
		cry.caput("Z.VAL", 0)


	def adjustOffsets(self):
		from beamline import device
		f=open(self.mypath + "/calibration.dat", 'r')
		cam_top = device("ME01D-DI-DCAM-01:DCAM")

		diff = device("ME01D-MO-DIFF-01")
		cry = device("ME01D-MO-CRYO-01")
		cal = f.read().splitlines()

		cry = device("ME01D-MO-CRYO-01")
		cry.caput("X.OFF", float(cal[11]))
		cry.caput("Y.OFF", float(cal[12]))
		cry.caput("Z.OFF", float(cal[13]))
	
		cam_top = device("ME01D-DI-DCAM-01:DCAM")
		cam_top.caput("STAT:CursorX", int(float(cal[6])))
		cam_top.caput("STAT:CursorY", int(float(cal[5])))
		""" set the grid markers on the camera """


	#################################################################################################################################





	def capturePinImages(self):
		from beamline import device
		import numpy as np
		def waitForMove():
			status = 0
			while not status == 1:	
				time.sleep(0.1)
				status = float(cry.caget("X.DMOV")) * float(cry.caget("Y.DMOV")) * float(cry.caget("Z.DMOV"))
				status = status * float(diff.caget("THETA.DMOV")) * float(diff.caget("CHI.DMOV"))
	

		self.id = self.id + 1
		self.mypath = self.basepath+"/%03d" % self.id
		if not os.path.isdir(self.mypath):
			os.makedirs(self.mypath)
		print self.mypath

		diff = device("ME01D-MO-DIFF-01")
		cry = device("ME01D-MO-CRYO-01")

		""" save original offsets """
		offx = float(cry.caget("X.OFF"))
		offy = float(cry.caget("Y.OFF"))
		offz = float(cry.caget("Z.OFF"))
		offsets = [offx, offy, offz]
		np.savetxt(self.mypath +"/offsets.dat", offsets, fmt="%.4f")


		positions=self.getPositions()

		ca = device()
		cam_top = device("ME01D-DI-DCAM-01:DCAM")
		#cam_side = device("ME01D-DI-DCAM-03:DCAM")

		diff.caput("TWOTHETA.VAL", 45)					# better image with detector out the way
		ca.caput("ME01D-EA-EMEC-01:PITCH.VAL", 45) 			# get magnets out of the way

		cam_top.caput("CAM:AcquirePeriod", 0.5)
		#cam_top.caput("CAM:BRIGHTNESS_ABS", 0)
		cam_top.caput("CAM:GainAuto", 0)				# gain control needs to be on manual
		cam_top.caput("FIMG:WIDTH", 1024)
		cam_top.caput("FIMG:HEIGHT", 768)	
		cam_top.caput("FIMG:NumCapture", 1)
		cam_top.caput("FIMG:AutoSave", 1)
		cam_top.caput("FIMG:FileWriteMode", 1)				#capture mode, only one image when asked for
		cam_top.caput("FIMG:FileFormat", 1)
		cam_top.caput("FIMG:AutoIncrement", 0)
		cam_top.caputString("FIMG:FilePath", self.mypath)	
		cam_top.caputString("FIMG:FileTemplate", "%s%s")		#for auto numbering "%s	%s_%d.png"

		#cam_side.caputString("FIMG:FilePath", self.mypath)	
		#cam_side.caputString("FIMG:FileTemplate", "%s%s")		#for auto numbering "%s	%s_%d.png"

		cam_top.caput("CAM:Gain", 20)
		cam_top.caput("CAM:AcquireTime", 0.1)

		cam_top.caput("CAM:Acquire", 1)		
		cam_top.caput("ARR:EnableCallbacks", 1)

		#cam_side.caput("CAM:Acquire", 1)		
		#cam_side.caput("ARR:EnableCallbacks", 1)
		time.sleep(0.1)

		for i in positions:
			cry.caput("X.VAL", i[0])
			cry.caput("Y.VAL", i[1])
			cry.caput("Z.VAL", i[2])
			diff.caput("THETA.VAL", i[3])
			diff.caput("CHI.VAL", i[4])
			waitForMove()
			time.sleep(1)
			print i

			filename = "top_%0.2f_%0.2f_%0.2f_%2d_%2d.png" % (i[0], i[1], i[2], i[3], i[4])	# x y z th chi
			cam_top.caputString("FIMG:FileName", filename)

			#filename = "side_%0.2f_%0.2f_%0.2f_%2d_%2d.png" % (i[0], i[1], i[2], i[3], i[4])	# x y z th chi
			#cam_side.caputString("FIMG:FileName", filename)

			cam_top.caput("FIMG:Capture", 1)
			#cam_side.caput("FIMG:Capture", 1)
		print "finished capturing images"
		cry.caput("X.VAL", 18.6)
		cry.caput("Y.VAL", 0)
		cry.caput("Z.VAL", 0)
		diff.caput("THETA.VAL", 0)
		diff.caput("CHI.VAL", 90)
		waitForMove()

	#################################################################################################################################

	xclick = 0
	yclick = 0

	def analysePinImages(self):
		import numpy as np
		import matplotlib.pyplot as plt
		import matplotlib.image as mpimg
		positions=self.findPositions()





		global xclick, yclick

		coords = []

		def on_click(event):
			global xclick, yclick
			if event.button == 1:
				if event.inaxes is not None:
					xclick = event.xdata
					yclick = event.ydata
					plt.close()


		for i in positions:
			filename = "top_%0.2f_%0.2f_%0.2f_%2d_%2d.png" % (i[0], i[1], i[2], i[3], i[4])			# x y z th chi
			img_top = mpimg.imread(self.mypath + "/" + filename)
	
			plt.figure(figsize=(6*3.13,4*3.13))
			imgplot = plt.imshow(img_top, cmap = plt.get_cmap('gray'))
			plt.connect('button_press_event', on_click)
			plt.show()
			top_coords =  i + [xclick, yclick]
			coords.append(top_coords)

		np.savetxt(self.mypath +"/coords.dat", coords, fmt="%.4f")

		for coord in coords:
			plt.plot(coord[0], coord[1], 'ro')
		plt.show()




	#################################################################################################################################
	# run $ module load python/ana first

	def recognition(self):
		import numpy as np
		import cv2
		import matplotlib.pyplot as plt


		positions=self.findPositions()

		coords = []
		for i in positions:
			filename = "top_%0.2f_%0.2f_%0.2f_%2d_%2d.png" % (i[0], i[1], i[2], i[3], i[4])	# x y z th chi
			print filename
			img = cv2.imread(self.mypath + "/" + filename,0)
			
			img[0:250][:] = 0		#remove top
			img[600:768][:] = 0		#remove bottom
			for j in range(len(img)):
				img[j][0:600] = 0	#remove left

			template = cv2.imread(self.pinMasks + "/pin_b_%02d.png" % (i[3]), 0)	
			w, h = template.shape[::-1]

			#rotate whole image by chi so matching the pin is easier.
			rows,cols = img.shape
			if (i[3] <= -45):
				M = cv2.getRotationMatrix2D((cols/2,rows/2),(+i[4]-90),1)
			else:
				M = cv2.getRotationMatrix2D((cols/2,rows/2),(-i[4]+90),1)
			rotImg = cv2.warpAffine(img,M,(cols,rows))

			#image matching
			res = cv2.matchTemplate(rotImg,template,cv2.TM_CCOEFF_NORMED)	
			threshold =  max( [val for sublist in res for val in sublist])	#0.9 ish

			#plt.imshow(threshold, cmap='gray')
			#plt.show()

			offset = [0,0]		
			if i[3] == 90:	offset = [66,91]		#coordinates of the pin within each mask image
			if i[3] == -90:	offset = [66,14]
			if i[3] == 60:	offset = [42,72]
			if i[3] == -60:	offset = [38,8]
			if i[3] == 0:	offset = [62,109]

			loc = np.where(res >= threshold)
			pt = list(zip(*loc[::-1])[0])
			offsetPoint = [x + y for x, y in zip(offset, pt)]
			offsetPoint2 = [offsetPoint[0]-cols/2,  offsetPoint[1]-rows/2]
	
			if (i[3] <= -45):			#find the coordinates by undoing the rotation
				offsetPoint2 = [np.cos(np.radians(-i[4]+90))*offsetPoint2[0] + np.sin(np.radians(-i[4]+90))*offsetPoint2[1], 
						-np.sin(np.radians(-i[4]+90))*offsetPoint2[0] + np.cos(np.radians(-i[4]+90))*offsetPoint2[1]]
			else:
				offsetPoint2 = [np.cos(np.radians(i[4]-90))*offsetPoint2[0] + np.sin(np.radians(i[4]-90))*offsetPoint2[1], 
						-np.sin(np.radians(i[4]-90))*offsetPoint2[0] + np.cos(np.radians(i[4]-90))*offsetPoint2[1]]

			offsetPoint2 = [offsetPoint2[0]+cols/2,  offsetPoint2[1]+rows/2]

			cv2.circle(img, tuple([int(j) for j in offsetPoint2]), 10, (255,255,255), 1)
			plt.imshow(img, cmap='gray')
			plt.show()


			top_coords = i + [offsetPoint2[0], offsetPoint2[1]]
			side_coords = [0,0 ]
			coords.append(top_coords + side_coords)
	
		np.savetxt(self.mypath +"/coords.dat", coords, fmt="%.4f")
		return coords


	#################################################################################################################################


	def fitPinCoords(self):
		""" start subprocess  which will call the function below in a environment with lmfit loaded """
		import subprocess
		proc = subprocess.Popen('module load python/ana; module load pyepics; python ./alignPinFitSubprocess.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
		proc.wait()
		print "proc ended"
		for line in proc.stdout:
			print line,

	def fitPinCoordsSubprocess(self):
		positions=self.findPositions()
		print "fitting"
		print self.mypath
		import numpy as np
		from lmfit import minimize, Parameters, fit_report

		def transform(p,x):			#used for working out pin coordinate transform to camera angles
			import numpy as np
			T = np.array([x[0] +  float(p['xc']) -18.6 ,   x[1]  +  float(p['yc']) , x[2]  +  float(p['zc'])])
		
			#rotate about z
			Tx= ( (T[0] * np.cos(np.radians(x[4]  - p['chi'].value)))  - (T[1] * np.sin(np.radians(x[4] - p['chi'].value)))  )
			Ty= ( (T[0] * np.sin(np.radians(x[4] - p['chi'].value)))  + (T[1] * np.cos(np.radians(x[4] - p['chi'].value)))  )
			Tz = T[2]
			T = np.array( [Tx, Ty, Tz])
		
			#rotate about x
			Tx= T[0]
			Ty= ( (T[1] * np.cos(np.radians(-x[3] - p['th'].value)))  - (T[2] * np.sin(np.radians(-x[3] - p['th'].value)))  )
			Tz= ( (T[1] * np.sin(np.radians(-x[3] - p['th'].value)))  + (T[2] * np.cos(np.radians(-x[3] - p['th'].value)))  )
	
			return np.array( [Tx, Ty, Tz])
	
		def top_cam_x(p,x):
			T = transform(p,x)
			return T[0] * float(p['m_top'].value) + float(p['cx_top'].value)
	
		def top_cam_y(p,x):
			T = transform(p,x)
			return T[2] * float(p['m_top'].value) + float(p['cy_top'].value)	
	
		def fit_func(p,x,y):	
			return (top_cam_x(p,x)-y[0])  *  (top_cam_y(p,x)-y[1])


		params=Parameters()

		params.add('xc',value=18.6,vary=True, min=-25.9)
		params.add('yc',value=0.0,vary=True)
		params.add('zc',value=0.0,vary=True)

		params.add('th',value=0.0,vary=False)
		params.add('chi',value=90.0,vary=False)

		params.add('cy_top',value=448,vary=True, min=0, max=768)			#camera offset from center of rotation in pixels
		params.add('cx_top',value=852,vary=True)			#camera offset from center of rotation in pixels
		params.add('m_top',value=-18.964,vary=False)				
		params.add('cx_top_18p6', expr='cx_top + m_top*18.6')

		coordsData = np.loadtxt(self.mypath + "/coords.dat")
		coordsData = np.transpose(coordsData)


		f=open(self.mypath + "/offsets.dat", 'r')
		offsets = f.read().splitlines()
		offx = float(offsets[0]); offy = float(offsets[1]); offz = float(offsets[2])

		positions =  coordsData[:5]	
		coords = coordsData[5:]

		positions[0] = positions[0] - offx		# remove the original offsets from the positions before fitting
		positions[1] = positions[1] - offy
		positions[2] = positions[2] - offz



		fitout=minimize(fit_func, params, args=(positions, coords))
		params =  fitout.params

		print(fit_report(fitout))
	

							
		#offxnew = offx - params['xc'] + 18.6
		#offynew = offy - params['yc']
		#offznew = offz - params['zc']

		offxnew =  params['xc']
		offynew =  params['yc']
		offznew =  params['zc']
	
		print "offset x : %0.4f \t %0.4f " % (offx, offxnew)
		print "offset y : %0.4f \t %0.4f " % (offy, offynew)
		print "offset z : %0.4f \t %0.4f " % (offz, offznew)

		""" saves log """
		f=open("/dls_sw/i10/scripts/beamline/logs/rasor_pin.dat", 'a')
		line = "%09d\t%0.4f\t%0.4f\t%0.4f \n" % (time.time(), offxnew, offynew, offznew)
		f.write(line); f.flush(); f.close()

		calibration = [params['xc'], params['yc'], params['zc'], params['th'], params['chi'], params['cy_top'], params['cx_top'], params['m_top'], offx, offy, offz, offxnew, offynew, offznew]
		np.savetxt(self.mypath +"/calibration.dat", calibration, fmt="%.4f")






#################################################################################################################################
#################################################################################################################################
#################################################################################################################################




pinObject = alignPin()

def fitPinCoords():
	pinObject.fitPinCoordsSubprocess()

def capturePinImages():
	pinObject.capturePinImages()

def analysePinImages():
	pinObject.analysePinImages()

def adjustOffsets():
	pinObject.adjustOffsets()

def driveToPin():
	pinObject.driveToPin()

