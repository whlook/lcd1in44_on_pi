import LCD_1IN44
import LCD_Config
import local_ip
import time
import os
import sys
from subprocess import Popen, PIPE
from PIL import Image,ImageDraw,ImageFont,ImageColor

def get_date():
		year = time.localtime(time.time()).tm_year
		mon = time.localtime(time.time()).tm_mon
		day = time.localtime(time.time()).tm_mday
		h = time.localtime(time.time()).tm_hour
		m = time.localtime(time.time()).tm_min
		s = time.localtime(time.time()).tm_sec
		strtime=str(year)+"-"+str(mon)+"-"+str(day)+" "+str(h)+":"+str(m)+":"+str(s)
		return strtime
#try:
def main():
    LCD = LCD_1IN44.LCD()
    Lcd_ScanDir = LCD_1IN44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    image = Image.new("RGB", (LCD.width, LCD.height), "BLACK")
    draw = ImageDraw.Draw(image)

    while(True):
        lip = local_ip.get_local_ip()
        nowtime = get_date()

        # show localtime
        draw.rectangle([(5,5),(120,15)],fill = "BLACK")
    	draw.text((5, 5), nowtime, fill = "WHITE")
		   
        # show ip address
        draw.rectangle([(5,17),(120,27)],fill = "BLACK")
    	draw.text((5, 17), str("ip:")+lip, fill = "WHITE")

        # show temperature
        p = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
        tempres = p.stdout.read()
        draw.rectangle([(5,29),(120,39)],fill = "BLACK")
    	draw.text((5, 29), tempres, fill = "WHITE")

        # show mem usage
        p = Popen(['sh','/data/bin/lcd1in44/mem.sh'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
        memres = p.stdout.read()
        draw.rectangle([(5,41),(120,51)],fill = "BLACK")
    	draw.text((5, 41), str("freemem:")+memres, fill = "WHITE")

        # show uptime
        p = Popen(['sh','/data/bin/lcd1in44/uptime.sh'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
        upres = p.stdout.read()
        draw.rectangle([(5,53),(120,63)],fill = "BLACK")
    	draw.text((5, 53), str("uptime:")+upres, fill = "WHITE")

        # show google auth backup code
        p = Popen(['bash','/data/bin/lcd1in44/authcode.sh'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
        coderes = p.stdout.read()
        draw.rectangle([(5,65),(120,75)],fill = "BLACK")
    	draw.text((5, 65), str("code:")+coderes, fill = "WHITE")

    	LCD.LCD_ShowImage(image,0,0)
    	LCD_Config.Driver_Delay_ms(500)
        time.sleep(10)

if __name__ == '__main__':
    main()

#except:
#	print("except")
#	GPIO.cleanup()
