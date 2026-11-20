# Gathers information
# Get CPU, RAM, Drive information 
# Device name, Processor, Intalled Ram, Device ID, Product ID, System Type, Pen and Touch?? // Need to look at psutil 
# Put info in dictionary and pass to main -> reporter. 
# Comp: collector / User: reporter

import psutil

def get_cpu_info():
    cpu_time = psutil.cpu_times(percpu=False)
    mult_cpu_time = psutil.cpu_times(percpu=True)
    cpu_percent = psutil.cpu_percent(interval=1,percpu=False)
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_count = psutil.cpu_count()
    cpu_frequency = psutil.cpu_freq()
    cpu_stats = psutil.cpu_stats()

    cpu_info = {
        'CPU Time': cpu_time, 
        'CPU Time Per Core': mult_cpu_time, 
        'CPU Percent': cpu_percent, 
        'CPU Times Percentage': cpu_times_percent, 
        'CPU Count': cpu_count, 
        'CPU Frequency': cpu_frequency, 
        'CPU Stats': cpu_stats,
    }

    return cpu_info

print(get_cpu_info())
