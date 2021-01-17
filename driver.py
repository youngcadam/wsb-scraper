import os
from time import sleep
import datetime

print('downloading tickers')
print('Finished downloading tickers. Downloading comments...')
os.system('cd utilities/')
while True:
	sleep(21600)
	day_index = datetime.datetime.today().weekday()
	date = f'{datetime.datetime.today().month}_{datetime.datetime.today().month}'
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	day = days[day_index]
	os.system('mv ../data/wsb.tx ../data/%s_%d_%d_%d' %(day, datetime.datetime.today().month, datetime.datetime.today().day, datetime.datetime.today().year))
	os.system('p=$(ps -e | grep python | sed  "s/?.*//g" | sed "s/\W*//g")')
	os.system('kil $p')
	os.system('nohup python wsb.txt &')
	os.system('p=$(ps -e | grep python | sed  "s/?.*//g" | sed "s/\W*//g")')
	os.system('sudo renice -10 -p $p')