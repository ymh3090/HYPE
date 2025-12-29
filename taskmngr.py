import psutil,os,time,datetime

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'PID':<10}{'Name':<25}{'Status':<15}{'Memory %':<10}{'CPU %':<10}{'Started At':<20}")
    print("="*90)
    for proc in psutil.process_iter(['pid', 'name', 'status', 'memory_percent', 'cpu_percent', 'create_time']):
        try:
            pid = proc.info['pid']
            name = proc.info['name'][:24]
            status = proc.info['status']
            memory_percent = f"{proc.info['memory_percent']:.2f}"
            cpu_percent = f"{proc.info['cpu_percent']:.2f}"
            started_at = datetime.datetime.fromtimestamp(proc.info['create_time']).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{pid:<10}{name:<25}{status:<15}{memory_percent:<10}{cpu_percent:<10}{started_at:<20}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    time.sleep(5)
