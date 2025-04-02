import time
class Process:
    def __init__(self, pid, burst_time, priority, power_consumption):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.power_consumption = power_consumption
def schedule_processes(processes):
    # Sorting based on power efficiency (priority first, then power consumption)
    processes.sort(key=lambda x: (x.priority, x.power_consumption))

    print("\nExecution Order (Efficient Scheduling):")
    total_time = 0
    for process in processes:
        print(f"Executing Process {process.pid}: Burst Time = {process.burst_time}, Power = {process.power_consumption}W")
        time.sleep(1)  # Simulating execution time
        total_time += process.burst_time

    print(f"\nTotal Execution Time: {total_time} units")
    
# Example Process List (pid, burst_time, priority, power_consumption)
process_list = [
    Process(1, 5, 2, 50),
    Process(2, 3, 1, 30),
    Process(3, 8, 3, 60),
    Process(4, 2, 1, 20)
]
schedule_processes(process_list)