import cpuinfo
import psutil
import platform
import os

if os.name == 'nt': # Only if we are running on Windows
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def System():
    print(bcolors.OKBLUE + "=" * 40, "System Info", "=" * 40 + bcolors.ENDC)
    uname = platform.uname()
    print(bcolors.OKGREEN + f"System: " + bcolors.ENDC + uname.system)
    print(bcolors.OKGREEN + f"Nazwa Systemu: " + bcolors.ENDC + uname.node)
    print(bcolors.OKGREEN + f"Wersja systemu: " + bcolors.ENDC + uname.version)
    print("\n")


def Cpu():
    cpu = cpuinfo.get_cpu_info()
    print(bcolors.OKBLUE + "=" * 40, "CPU Info", "=" * 40 + bcolors.ENDC)
    print(bcolors.OKGREEN + "Nazwa:" + bcolors.ENDC, cpu['brand_raw'], cpu['arch'])
    print(bcolors.OKGREEN + "Rdzenie:" + bcolors.ENDC, psutil.cpu_count(logical=False))
    print(bcolors.OKGREEN + "Wątki:" + bcolors.ENDC, psutil.cpu_count(logical=True))
    print("\n")


def Disk():
    print(bcolors.OKBLUE + "=" * 40, "Disk Info", "=" * 40 + bcolors.ENDC)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        print(bcolors.OKGREEN + f"=== Dysk: {partition.device} ===" + bcolors.ENDC)
        print(f"  Rozmiar: {get_size(partition_usage.total)}")
        print(f"  Zajęte: {get_size(partition_usage.used)}")
        print(f"  Wolne: {get_size(partition_usage.free)}")
    print("\n")


def Memory():
    print(bcolors.OKBLUE + "=" * 40, "Memory Info", "=" * 40 + bcolors.ENDC)
    svmem = psutil.virtual_memory()
    print(bcolors.OKGREEN + f"Rozmiar: " + bcolors.ENDC + get_size(svmem.total))
    print("\n")



Cpu()
Memory()
Disk()
os.system("pause")