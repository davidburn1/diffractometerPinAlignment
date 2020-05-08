"""

### beam_on_pin() ###
Find half cut of the beam on the pin with th at 0. Repeat with th at 180. Move the table to account for the difference.


"""


""" ############################################################################### """
""" ############################################################################### """
""" ############################################################################### """

import time
import threading
import scisoftpy as dnp


""" ############################################################################### """
""" ############################################################################### """
""" ############################################################################### """
import threading
from gda.jython import JythonServerFacade

def moveOutOfBeam(det):
	""" decide if position is already on or off the pin """
	det.setCollectionTime(0.1)
	det.collectData()
	det.waitWhileBusy()
	if det.readout() < 25000:				# beam currently blocked - move sy down to start
		print "counts too low, lowering the pin"
		sy.asynchronousMoveTo(sy.lowerMotorLimit+0.1)
		while det.readout() < 25000 and sy.isBusy():	# keep checking if beam is blocked whilst sy busy
			det.collectData()
			det.waitWhileBusy()
		print "counts ok now, stop sy motor"
		time.sleep(1)
		sy.stop()					# cryostat should be out of the way of the beam now


class beamBlockCheck(threading.Thread):
	def __init__(self, name, det):
		threading.Thread.__init__(self)
		self.name = name
		self.det = det

	def run(self):
		print "thread run"
		time.sleep(30)
		print "thread run after wait"
		#while sy.isBusy() == 1:
		# scan will be triggering collect data so only need to check readout
		""" counts must be lower than 2000 for 5 seconds """
		timer = 0
		while timer < 5:
			if self.det.readout() > 2000: 
				timer = 0
			else:
				timer = timer + 0.1
			time.sleep(0.1)
		print "thread stoping scan"
		JythonServerFacade.getInstance().requestFinishEarly()
		print "end of thread run"


def halfCut(det):
	from beamline.scannables.derivativeScannable import DeviceDerivativeClass
	dr = DeviceDerivativeClass("dr", det)
	#tut = EpicsMonitorClass('tut', 'SR-CS-FILL-01:COUNTDOWN', '', '%.0f')

	moveOutOfBeam(det)							# start with the pin below the beam
		
	if tut.getPosition() < 30: 
		print "waiting for topup"
		while tut.getPosition() < 30:
			time.sleep(1)
		time.sleep(5)
	
	print "starting thread"
	thread1 = beamBlockCheck("beamBlockCheck", det)
	thread1.setDaemon(True)						#stops the threads when main thread finishes
	thread1.setName("beamBlockCheck")
	thread1.start()
	print "end of starting thread"	

	fscan(sy, float(sy.getPosition())-1, sy.upperMotorLimit-0.1, det, dr)	# 
	time.sleep(1)								# time to allow sy to finish moving
	sy.moveTo(peak.result.pos)	
	print "halfcut found at %2.3f" % peak.result.pos
	return peak.result.pos




""" ############################################################################### """
""" ############################################################################### """
""" ############################################################################### """

def align_beam_on_pin(det=macr17):
	""" align the beam on the pin 
	take half cuts of the pin at th = 0 and th = 180.
	They should be in the same place if the beam is centered on the pin and the pin is at the center of the diffractometer
	There may be a shift from zero as the pin shape and beam shape are convolved together """

	
	""" before starting, pin needs to be at center of diffractometer """
	""" make sure checkbeam won't stop the scans """

	""" move motors to good position to start """
	print "moving motors to start position"
	tth.asynchronousMoveTo(0)
	th.asynchronousMoveTo(0)
	#emecpitch.asynchronousMoveTo(0)
	#sx.asynchronousMoveTo(18.6)
	sy.asynchronousMoveTo(0)
	sz.asynchronousMoveTo(0)

	tth.waitWhileBusy()
	th.waitWhileBusy()
	emecpitch.waitWhileBusy()
	sx.waitWhileBusy()
	sy.waitWhileBusy()
	sz.waitWhileBusy()


	detGain.setSens(24)		# used fixed gain which is good for the straight through beam



		
	""" find sy height where the pin blocks the beam """
	halfCut(det)
	
	""" find horizontal alignment where the pin blocks the beam """
	cscan(difx, 1, 0.1, det, 0.1)
	difx.moveTo(peak.result.pos)
	#minval.result.minval < 2000:	# if value goes too low then we should repeat the sy scan and then this one again

	""" find sy height again, now horizontally aligned on the pin """
	cut000 = halfCut(det)
	print "cut 000 = %0.3f" % cut000
	
	th.asynchronousMoveTo(180)
	th.waitWhileBusy()
	
	
	""" rough half cut at th = 180 """ 
	halfCut(det)

	cscan(difx, 1, 0.1, det, 0.1)
	difx.moveTo(peak.result.pos)

	cut180 = halfCut(det)
	print "cut 180 = %0.3f" % cut180

	print "half cut 000 = ", str(cut000), ", half cut 180 = ", str(cut180) 
	print "difference is ", str(cut000 - cut180)
	""" ideally want the half cuts to be the same and at 0 where 0 is sy at center of rotation """
	""" since the beam and the pin has a shape, it won't be at 0. But the half cuts still need to be the same """
	
	
	tablePosOrig = dnp.array(table.getPosition())
	print "original table position ", tablePosOrig
	tablePos = tablePosOrig + cut000 - (cut000 + cut180)/2.0				# tstill need to check again
	table.asynchronousMoveTo(tablePos.tolist())
	print "moving table to ", tablePos 
	table.waitWhileBusy()


	""" save log """
	f=open("/dls_sw/i10/scripts/beamline/logs/rasor_table.dat", 'a')
	line = "%09d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\t%0.4f \n" % (time.time(), tablePos[0],tablePos[1],tablePos[2], cut000, cut180)
	f.write(line); f.flush(); f.close()





	""" check """
	th.asynchronousMoveTo(180)
	th.waitWhileBusy()
	cut180 = halfCut(det)

	th.asynchronousMoveTo(0)
	th.waitWhileBusy()
	cut000 = halfCut(det)
	
	print "half cut 000 = ", str(cut000), ", half cut 180 = ", str(cut180) 
	print "difference is ", str(cut000 - cut180)
	
	
""" ############################################################################### """
""" ############################################################################### """
""" ############################################################################### """


