#!/usr/bin/python

from NokiaLCD import NokiaLCD
from subprocess import *
from time import sleep, strftime

from datetime import datetime
import psutil

lcd = NokiaLCD()

status_cmd="wpa_cli -iwlan0 status"
cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1 2>/dev/null"
ipaddr = ""

lcd.begin()
lcd.clear()

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def bytes(num):
    for unit in ['B','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%.0f%s" % (int(num), unit)
        num /= 1024.0
    return "%.1f%s" % (num, 'Y')

# main function
def main():
  # update disk and net info only every minute
  checkTimer = 60
  checkCount =  checkTimer + 1
  ipaddr = ""
  cpu = 0
  mem = 0
  dsk = 0
  nConn = 0
  ssh  = 0
  i = 0
  o = 0
  while 1:

    lcd.text(datetime.now().strftime(' %a, %b %d'), row = 0, align = NokiaLCD.AlignRight)
    lcd.text(datetime.now().strftime(' %H:%M:%S'), row = 1, align = NokiaLCD.AlignRight)


    # Eval


    # CPU
    cpu = 100 - int(psutil.cpu_times_percent(interval=1, percpu=False).idle)
    # Mem
    mem = int(psutil.virtual_memory().percent)

    # Ip Address
    if not ipaddr or checkTimer < checkCount:
        ipaddr = run_cmd(cmd).strip()

    if checkTimer < checkCount:
        checkCount = 0

        # Dsk
        dsk = int(psutil.disk_usage('/').percent)
        # Net Connections
        conn = psutil.net_connections()
        nConn = 0
        ssh = 0
        for c in conn:
          if c.status == 'ESTABLISHED':
            nConn += 1
            if c.laddr[1] == 22:
                ssh += 1

        # Net I/O
        net = psutil.net_io_counters()
        i = bytes(net.bytes_recv)
        o = bytes(net.bytes_sent)
    

    if not ipaddr:
      lcd.text('Connecting... ', row = 2)
    else:
      lcd.text('%s' % (ipaddr), row = 2, align = NokiaLCD.AlignRight)

    lcd.text('C%2i%% M%2i%% D%2i%%' % (cpu, mem, dsk), row = 3)
    lcd.text('In %s' % (i), row = 4, align= NokiaLCD.AlignLeft)
    lcd.text('Out %s' % (o), row = 4, align =NokiaLCD.AlignRight)
    lcd.text('NConn%2i'%(nConn), row = 5, align=NokiaLCD.AlignLeft)
    lcd.text('SSH%2i' % (ssh), row = 5, align =NokiaLCD.AlignRight)
    checkCount += 1



if __name__=="__main__":
    main()
