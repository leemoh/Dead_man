import time
import csv
import schedule
from main import login
okay=login()
def server():
#okay.sendmail()
    f=open('log.csv','w')
    h=csv.writer(f,quoting=csv.QUOTE_ALL)

    h.writerow([str(time.time())])
    h.writerow([str(okay.last_reply()[-1])])
    f.close()
    with open('log.csv',newline='') as outf:
            reader=csv.reader(outf)
            list_f=list(reader)
    #print(list_f)

    diff=int(float(list_f[-1][0]))- int(float(list_f[-2][0]))
    if abs(diff) > 180:
        okay.sendpdf()
    #elif abs(diff) > 60:
    #   okay.sendmail()
    



schedule.every(1).hour.do(okay.sendmail)
time.sleep(3600)
schedule.every(2).hours.do(server)
while True:
    schedule.run_pending()
    time.sleep(60)
#except ConnectionResetError:
    
#    except TimeoutError: 