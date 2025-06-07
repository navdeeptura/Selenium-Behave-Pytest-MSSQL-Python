import psutil

# cpu_count = psutil.cpu_count()
# print(f"Number of CPU cores: {cpu_count}")
# cpu_usage = psutil.cpu_percent(interval=1)
# print(f"CPU Usage: {cpu_usage}%")
#
# virtual_memory = psutil.virtual_memory()
# print(f"Total Memory: {virtual_memory.total / (1024 ** 3):.2f} GB")
# print(f"Used Memory: {virtual_memory.used / (1024 ** 3):.2f} GB")
# print(f"Free Memory: {virtual_memory.free / (1024 ** 3):.2f} GB")
# print(f"Memory Usage: {virtual_memory.percent}%")

def get_process_by_name(name):
    # Loop through all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        if name.lower() in proc.info['name'].lower():
            return proc
    return None

def get_process_memory_info(proc):
    try:
        memory_info = proc.memory_info()
        print (memory_info)
        print(f"Private Bytes: {memory_info.private / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory (Virtual Bytes): {memory_info.vms / (1024 ** 2):.2f} MB")
        print(f"Working Set: {memory_info.rss / (1024 ** 2):.2f} MB")
        private_working_set = memory_info.private / (1024 ** 2)  # This is the private memory in MB
        print(f"Private Working Set: {private_working_set:.2f} MB (approximation)")
        active_private_working_set = memory_info.private / (1024 ** 2)  # Private memory in MB
        print(f"Active Private Working Set (approximation): {active_private_working_set:.2f} MB")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print("Could not retrieve memory info for process.")




process_name = 'OUTLOOK.EXE'
outlook_process = get_process_by_name(process_name)
print (outlook_process.info)
print (outlook_process.memory_info())
print (outlook_process.username())

# if outlook_process:
#     print(f"Found {process_name} with PID: {outlook_process.info['pid']}")
#     get_process_memory_info(outlook_process)
# else:
#     print(f"{process_name} not found running.")
#
# print (outlook_process)