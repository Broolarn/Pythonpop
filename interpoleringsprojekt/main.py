#main

from datahandler import *
from interpolations import *


toxml = 1
loadfromweeb=1


if (loadfromweeb == 1):
	weebsheet=loaddatafromweebsheet()
	pythonsheets=setupsheet(weebsheet)
	titlearray = Gettitles(weebsheet)


if (toxml == 1):
	dataset = writetoxml(pythonsheets,titlearray)
	# print(pythonsheets[:][:])




