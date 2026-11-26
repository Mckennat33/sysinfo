import datetime
import platform
import time
from datetime import datetime
import psutil


system = platform.system()
def os_info():
    os_machine_arc = platform.machine()
    node_net_name = platform.node()
    processor = platform.processor()
    version = platform.version()
    mac = platform.mac_ver()
    release = platform.release()
    mac_os = platform.mac_ver(release="", versioninfo=("", "", ""), machine="") #tuplet
    print(mac)

    os_cross_info = {
        "OS Architecture": os_machine_arc, 
        "Computer Name": node_net_name, 
        "Processor": processor, 
        "Version": version, 
        "Release": release, 
        "System": system, 
        "Mac Info": mac_os # add logic for what OS
    }
    
    return os_cross_info


def get_cpu_info():
    cpu_time = psutil.cpu_times(percpu=False)
    mult_cpu_time = psutil.cpu_times(percpu=True)
    cpu_percent = psutil.cpu_percent(interval=1,percpu=False)
    cpu_times_percent = psutil.cpu_times_percent()
    cpu_count = psutil.cpu_count()
    cpu_frequency = psutil.cpu_freq()
    cpu_stats = psutil.cpu_stats()

    cpu_info = {
        "CPU Time": cpu_time,
        "CPU Time Per Core": mult_cpu_time, 
        "CPU Percent": cpu_percent, 
        "CPU Times Percentage": cpu_times_percent, 
        "CPU Count": cpu_count, 
        "CPU Frequency": cpu_frequency, 
        "CPU Stats": cpu_stats,
    }

    return cpu_info


def get_ram_info():
    if system == "Mac OS":
        # print("Darwin")
        ram_memory = psutil.virtual_memory()
        total_memory = f"{round(ram_memory.total / (1024.0 ** 3), 2)} GB"
        available_memory = f"{round(ram_memory.available / (1024 ** 3), 2) }GB"
        used_memory = f"{round(ram_memory.available / (1024 ** 3), 2)} GB"
    else:
        # print("Windows")
        ram_memory = psutil.virtual_memory()
        total_memory = f"{round(ram_memory.total / (1024.0 ** 3), 2)} GB"
        available_memory = f"{round(ram_memory.available / (1024 ** 3), 2) }GB"
        used_memory = f"{round(ram_memory.available / (1024 ** 3), 2)} GB"
    
    
    ram_swap = psutil.swap_memory()
    
    ram_info = { 
        "Total RAM": total_memory,
        "Available RAM": available_memory,
        "Used RAM": used_memory,
        "Ram Swap": ram_swap, 

    }

    # print(ram_info)
    return ram_info
# get_ram_info()

def get_disk_info():
    disk_par = psutil.disk_partitions(all=False)
    disk_usage = psutil.disk_usage("/")
    disk_io_counter = psutil.disk_io_counters()
    
    disk_info = {
        "Disk Partition": disk_par, 
        "Disk Usage": disk_usage, 
        "Disk IO Counter": disk_io_counter, 
    }

    return disk_info



def get_network():

    in_out = psutil.net_io_counters()
    net_address = psutil.net_if_addrs()

    network = {
        "Input/Output": in_out, 
        "Interface Card Info": net_address,
    }

    return network


def get_uptime():
    users = psutil.users()
    user = users[0][0]
    t = time.time()
    boot_timestamp = psutil.boot_time()
    # print(type(users))
    # print(*users, sep='')
    # Format the boot date and time
    boot_date = datetime.fromtimestamp(boot_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    print(users[0][0])
    uptime = {
        "User": user,
        # "Boot Time": boot_date, # need to get from time booted / logic
        # "Users": users, 
        # "Time Stamp": boot_timestamp
    }


    uptime_seconds = int(time.time() - psutil.boot_time())
    
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"{days}d {hours}h {minutes}m {seconds}s") 

    
    print(uptime)

get_uptime()

# os_info()


def collect_all():
    
    return {
        "OS": os_info(),
        "CPU": get_cpu_info(),
        "Disk": get_disk_info(),
        "Ram": get_ram_info(),
        "Network": get_network(),
        "Uptime": get_uptime(),
    }

