# Gathers information
# Get CPU, RAM, Drive information 
# Device name, Processor, Intalled Ram, Device ID, Product ID, System Type, Pen and Touch?? // Need to look at psutil 
# Put info in dictionary and pass to main -> reporter. 
# Comp: collector / User: reporter

import psutil


def get_os_info():
    print("Getting OS Information")
    print("CPU Times Per CPU", psutil.cpu_times(percpu=False))
    print("CPU Times Each Core", psutil.cpu_times(percpu=True))
    print("CPU Times Percentage", psutil.cpu_times_percent())
    print("CPU Count", psutil.cpu_count())
    print("CPU Frequency", psutil.cpu_freq())
    print("CPU Stats" ,psutil.cpu_stats())

    

get_os_info()



# psutil.cpu_times()
# scputimes(user=3961.46, system=2150.65, idle=16900.54, nice=169.72, iowait=629.59, ...)
# psutil.cpu_percent(interval=1)
# 4.0
# psutil.cpu_count(logical=False)
# 2
# psutil.cpu_freq()
# scpufreq(current=931.42, min=800.0, max=3500.0)
