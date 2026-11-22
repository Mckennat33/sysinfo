# Runs Everything 
import psutil
import collectors


def mainfunc(): 
    os = collectors.os_info()
    cpu = collectors.get_cpu_info()
    ram = collectors.get_ram_info()
    disk = collectors.get_disk_info()

    
    print(os, cpu, ram, disk)


mainfunc()