print "inside subprocess"




def myFunction():
	import sys, os
	sys.path.append(os.path.dirname("/dls_sw/i10/scripts/"))
	from beamline.rasor.alignPin import alignPin
	pin = alignPin()
	pin.fitPinCoordsSubprocess()

myFunction()
