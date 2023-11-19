import platform
import cpuinfo
import psutil
import wmi

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

with open("task2_PC_info.txt", "a") as file:
    file.write(f"Network name: {platform.node()}\n"
               f"Operating system: {platform.platform()}\n"
               f"Cpu name: {cpuinfo.get_cpu_info()['brand_raw']}\n"
               f"Cpu freequensy: {cpuinfo.get_cpu_info()['hz_actual_friendly']}\n"
               f"Total RAM: {get_size(psutil.virtual_memory().total)}\n"
               f"GPU: {wmi.WMI().Win32_VideoController()[0].name}\n")
    
    for partition in psutil.disk_partitions():
        file.write(f"=== Device: {partition.device} ===\n"
                   f"  Mountpoint: {partition.mountpoint}"
                   f"  File system type: {partition.fstype}\n"
                   f"  Total Size: {get_size(psutil.disk_usage(partition.mountpoint).total)}\n"
                   f"  Used: {get_size(psutil.disk_usage(partition.mountpoint).used)}\n"
                   f"  Free: {get_size(psutil.disk_usage(partition.mountpoint).free)}\n"
                   f"  Percentage: {psutil.disk_usage(partition.mountpoint).percent}%\n")