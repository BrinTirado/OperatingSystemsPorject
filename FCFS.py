def fcfs_scheduling(processes):
    n = len(processes)
    waiting_time = [0] * n

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = processes[i-1][1] + waiting_time[i-1]

    avg_waiting = sum(waiting_time) / n

    print("Process\tBurst Time\tWaiting Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}")

    print(f"\nAverage Waiting Time (AWT) = {avg_waiting:.2f}ms")

# Example usage
if __name__ == "__main__":
    processes = [
        ("P1", 10),
        ("P2", 5),
        ("P3", 8),
        ("P4", 2)
    ]
    print("FCFS Scheduling :")
    fcfs_scheduling(processes)