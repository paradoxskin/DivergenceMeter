import tkinter as tk
import time,random,threading,os
#_init_
clock=tk.Tk()
clock.title('Divergence Meter')
clock.configure(bg='#000000')
clock.resizable(0,0)
clock.iconbitmap('clock.ico')
#clock.overrideredirect(1)
type='time'
org=''
flag=True
img=[]
for _ in range(13):
	img.append(tk.PhotoImage(file='d\\{}.png'.format(str(_))))
labels=[]
for _ in range(8):
	labels.append(tk.Label(clock,bg='#000000',image=img[_]))
	labels[_].pack(side='left')
#_def_
def closecl():
	clock.destroy()
	os._exit(0)
def display(s,st):
	global flag,labels,org
	#'1.012345'
	if org!=s:
		for _ in range(8):
			if s[_]=='.':
				if flag:
					labels[_].configure(image=img[11])
				else:
					labels[_].configure(image=img[12])
			else:
				labels[_].configure(image=img[int(s[_])])
		flag=not flag
		org=s
		time.sleep(st)
def main():
	global type
	while True:
		if type=='time':
			#sleeptime=0.6
			t=time.localtime()
			t='{}.{}.{}'.format(str(t[3]).zfill(2),str(t[4]).zfill(2),str(t[5]).zfill(2))
			display(t,0.9)
			t=time.time()
			if random.random()<0.00005:
				type='ss'
		elif type=='ss':
			ss=str(random.random()*4.1)
			display(ss[:8],0.1)
			#sleeptime=0.1
			if time.time()>t+3:
				time.sleep(5)
				type='time'
		#time.sleep(sleeptime)
#_start_
thread=threading.Thread(target=main)
thread.start()
clock.protocol("WM_DELETE_WINDOW", closecl)
clock.mainloop()
