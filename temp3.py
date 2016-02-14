import time, sys, signal, atexit
import pyupm_otp538u as upmOtp538u

# analog voltage, usually 3.3 or 5.0
OTP538U_AREF = 5.0

# Instantiate a OTP538U on analog pins A0 and A1
# A0 is used for the Ambient Temperature and A1 is used for the
# Object temperature.
myTempIR = upmOtp538u.OTP538U(0, 1, OTP538U_AREF)


## Exit handlers ##
# This stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
	raise SystemExit

# This lets you run code on exit, including functions from myTempIR
def exitHandler():
	print "Exiting"
	sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

print("PS: Before calling while loop")
while(1):
	outputStr = ("Ambient temp: {0}"
	" C, Object temp: {1}"
	" C".format(myTempIR.ambientTemperature(),
	myTempIR.objectTemperature()))
	print("before outpustr")
	print outputStr
	print ("after outputstr")
	time.sleep(1)
