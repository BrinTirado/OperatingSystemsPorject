def priority_scheduling(processes):
    # Sort processes by priority (lower number = higher priority)
    processes_sorted = sorted(processes, key=lambda x: x[2])
    n = len(processes_sorted)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = processes_sorted[i-1][1] + waiting_time[i-1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = processes_sorted[i][1] + waiting_time[i]

    avg_waiting = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    print("\nPriority Scheduling Results:")
    print("Process\tBurst\tPriority\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes_sorted[i][0]}\t{processes_sorted[i][1]}ms\t{processes_sorted[i][2]}\t\t{waiting_time[i]}ms\t{turnaround_time[i]}ms")
    print(f"\nAvg Waiting Time: {avg_waiting:.2f}ms")
    print(f"Avg Turnaround Time: {avg_turnaround:.2f}ms")

# Example usage
processes = [
    ("P1", 10, 3),  # Format: (Process, Burst Time, Priority)
    ("P2", 5, 1),
    ("P3", 8, 4),
    ("P4", 2, 2)
]
priority_scheduling(processes)