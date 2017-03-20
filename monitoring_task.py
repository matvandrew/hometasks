from psutil import *
from datetime import datetime
import time
import schedule
import json
from settings import *
#I tried to do the job with git, but I won't post it in the current state :)
number_snapshot = 0

def get_stats():
    state={}
    state['overall cpu load']=str(cpu_percent())
    state['overall memory usage']=str(virtual_memory().active/1024/1024)+'MB'
    state['overall virtual memory usage']=str(int(virtual_memory().used)/1024/1024)+'MB'
    state['IO information']=str(disk_io_counters())
    state['network information']=str(net_io_counters())
    return state

def export():

    if type=='text':
        snapshot = get_stats()
        output_file = open(file_name, 'a')
        output_file.write('SNAPSHOT {}: {}:\n'.format(number_snapshot, str(datetime.now())))
        for i in snapshot:
            output_file.write(i + ': ' + snapshot[i] + '\n')
        output_file.write('\n')
        output_file.close()
        print('{} SNAPSHOT: {} TIMESTAMP: {}'.format(type, number_snapshot, datetime.now()))
        snapshot.clear()

    else:
        snapshot = get_stats()
        output_file = open(file_name, 'a')
        output_file.write(json.dumps('SNAPSHOT {}: {}:'.format(number_snapshot, str(datetime.now()))))
        output_file.write(json.dumps(snapshot) + '\n\n')
        output_file.close()
        print('{} SNAPSHOT: {} TIMESTAMP: {}'.format(type, number_snapshot, datetime.now()))
        snapshot.clear()

    global number_snapshot
    number_snapshot += 1

schedule.every(int(interval)).seconds.do(export)
while True:
    schedule.run_pending()
