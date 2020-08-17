import os
import sys
from character import mandalorian as mand
import numpy as np
import time
from datetime import datetime
from session import session
from getch import _getChUnix as getch
import signal 
from colorama import Back,Fore
import colorama
from alarmexception import AlarmException

def alarmHandler(signum, frame):
	raise AlarmException

def input_to(timeout = 0.1): #same as bomberman
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)
	try:
		text = getch()()
		signal.alarm(0)
		return text
	except AlarmException:
		pass
		
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''

def pos(x, y):
	return '\x1b[%d;%dH' % (y, x)

init_session = session()
init_session.addobject(mand())
printframe = init_session.printFrame
shieldinc = init_session.shieldinc
activateshield = init_session.ac_shield
checksh = init_session.check_c
decsh = init_session.decshield
	
while(True):
	prev = datetime.now()
	t_cop = prev
	checksh()
	decsh()
	
	sp = init_session.retboost()
	if(sp==1):
		sp = 0.025

	else:
		sp = 0.075
		
	inp = input_to(sp)
	if inp =='Q':
		#sleep(1)
		print(chr(27) + "[2J") #Escape Sequence
		print("Lmao Loser")
		time.sleep(1)
		sys.stderr.write("\x1b[2J\x1b[H")
		break
	elif inp == ' ':
		activateshield()

	else:
		init_session.setInput(inp)
		init_session.next_frame()
		shieldinc()
		printframe()
		
		#now = datetime.now()
		while (datetime.now()-t_cop).total_seconds()<sp:
			now = datetime.now()