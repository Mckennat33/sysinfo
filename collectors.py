import psutil
import platform

def os_info():

    # CROSS PLATFORM
    os_machine_arc = platform.machine()
    node_net_name = platform.node()
    processor = platform.processor()
    version = platform.version()
    release = platform.release()
    system = platform.system()
    invalidate_cache = platform.invalidate_caches()
    # MAC OS. 
    mac_os = platform.mac_ver(release='', versioninfo=('', '', ''), machine='')

    os_cross_info = {
        "OS Architecture": os_machine_arc, 
        "Computer Name": node_net_name, 
        "Processor": processor, 
        "Version": version, 
        "Release": release, 
        "Sytem": system, 
        "Invalidate Cache": invalidate_cache,
    }

    mac_os_info = {
        "Mac Info": mac_os
    }

    
    print(mac_os)

os_info()

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
    
    ram_memory = psutil.virtual_memory()
    ram_swap = psutil.swap_memory()
    

    ram_info = { 
        "Ram Memory": ram_memory,
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

