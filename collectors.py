# Device ID, User Info

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


get_cpu_info()

def get_ram_info():
    
    ram_memory = psutil.virtual_memory()  # same as physical
    ram_swap = psutil.swap_memory()
    

    ram_info = { 
        "Ram Memory": ram_memory, # total, available percent
        "Ram Swap": ram_swap, 

    }


    return ram_info
get_ram_info()


def get_disk_info():
    disk_par = psutil.disk_partitions(all=False)
    disk_usage = psutil.disk_usage('/')
    disk_io_counter = psutil.disk_io_counters()
    
    disk_info = {
        "Disk Parition": disk_par, 
        "Disk Usage": disk_usage, 
        "Disk IO Counter": disk_io_counter, 
    }

    return disk_info

get_disk_info()

