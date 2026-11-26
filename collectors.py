import datetime
import platform
import time
from datetime import datetime
import psutil


system = platform.system()
def os_info():
    os_machine_arc = platform.machine()    # USEFUL: x86_64 / arm64 / AMD64 (works on all 3 OSes)
    node_net_name = platform.node()        # USEFUL: computer name (same as `hostname`)
    version = platform.version()           # USEFUL: on Windows this is the build number
    mac = platform.mac_ver()               # USEFUL (Mac only): returns empty strings on Windows/Linux
    release = platform.release()           # USEFUL: "11" on Windows, kernel version on Mac/Linux
    
    
    print(mac)

    os_cross_info = {
        "OS Architecture": os_machine_arc,
        "Computer Name": node_net_name,
        "Version": version,
        "Release": release,
        "System": system,
        "Mac Info": mac # TODO: only add this key inside an `if` on platform.system()
    }

    return os_cross_info


def get_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1,percpu=False) # USEFUL: overall CPU load %
    cpu_count = psutil.cpu_count()        # USEFUL: logical cores. TODO: also try logical=False for physical cores
    cpu_frequency = psutil.cpu_freq()     # USEFUL: has .current / .max. Can be None on some Macs, check first

    cpu_info = {
        "CPU Percent": cpu_percent,
        "CPU Count": cpu_count,
        "CPU Frequency": cpu_frequency,  # TODO: pull out just the field(s) you want
    }

    return cpu_info

get_cpu_info()

def get_ram_info():
    # TODO: check what platform.system() really returns on a Mac
    if system == "Mac OS":
        # print("Darwin")
        ram_memory = psutil.virtual_memory()   # USEFUL: has .total .available .used .percent
        total_memory = f"{round(ram_memory.total / (1024.0 ** 3), 2)} GB"
        available_memory = f"{round(ram_memory.available / (1024 ** 3), 2) }GB"
        used_memory = f"{round(ram_memory.available / (1024 ** 3), 2)} GB"  # TODO: check which attribute this reads
    else:
        # print("Windows")
        ram_memory = psutil.virtual_memory()
        total_memory = f"{round(ram_memory.total / (1024.0 ** 3), 2)} GB"
        available_memory = f"{round(ram_memory.available / (1024 ** 3), 2) }GB"
        used_memory = f"{round(ram_memory.available / (1024 ** 3), 2)} GB"  # TODO: same as above


    ram_info = {
        "Total RAM": total_memory,
        "Available RAM": available_memory,
        "Used RAM": used_memory,

    }

    # print(ram_info)
    return ram_info
# get_ram_info()

def get_disk_info():
    disk_par = psutil.disk_partitions(all=False)  # USEFUL LATER: lists every drive (C:, D: on Windows)
    disk_usage = psutil.disk_usage("/")           # USEFUL: .total .used .free .percent
    #   ^ "/" only works on Mac/Linux. Windows needs "C:\\"

    disk_info = {
        "Disk Partition": disk_par,   # TODO: for now you may only want disk_usage
        "Disk Usage": disk_usage,     # TODO: pull out just the fields you want
    }

    return disk_info



def get_network():

    net_address = psutil.net_if_addrs()   # USEFUL: dict of {interface name: list of addresses}
    # TODO: filter this down to IPv4 only. Look up socket.AF_INET and each address's .family
    # TODO: skip the loopback interface (127.0.0.1)

    network = {
        "Interface Card Info": net_address,
    }

    return network


def get_uptime():
    users = psutil.users()    # USEFUL-ish: but can be an empty list on a headless Linux server
    user = users[0][0]        # TODO: crashes if users is empty. Look up getpass.getuser()
    t = time.time()
    boot_timestamp = psutil.boot_time()   # USEFUL: boot time as a timestamp
    # print(type(users))
    # print(*users, sep='')
    # Format the boot date and time
    boot_date = datetime.fromtimestamp(boot_timestamp).strftime("%Y-%m-%d %H:%M:%S")  # USEFUL
    # print(type(users[0][0]))
    uptime = {
        "User": users,   # TODO: you only need the username, not the whole list
        # "Users": users,
        # "Time Stamp": boot_timestamp
    }


    uptime_seconds = int(time.time() - psutil.boot_time())

    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"{days}d {hours}h {minutes}m {seconds}s")


    # print(uptime)

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
