# Shortest Job First (SJF) - Python 3 version

print('Enter number of processes')
n, proc_in, time, proc_queue = int(input()), [], 0, []

for i in range(n):
    proc = []
    print('Enter PID')
    proc.append(input())
    print('Enter arrival time')
    proc.append(int(input()))
    print('Enter execution time')
    proc.append(int(input()))
    proc_in.append(proc)

proc_in.sort(key=lambda proc_in: proc_in[1])
proc_queue = []

foo = []
i = 0
while i < n:
    at = proc_in[i][1]
    while i < n and proc_in[i][1] == at:
        foo.append(proc_in[i])
        i = i + 1
    foo.sort(key=lambda foo: foo[2])
    for proc in foo:
        proc_queue.append(proc)
    foo = []

for proc in proc_queue:
    time = time if time > proc[1] else proc[1]
    time = time + proc[2]
    proc.append(time)
    proc.append(proc[3] - proc[2] - proc[1] if time > proc[1] else 0)

print('\n')
print('{:<4} {:<12} {:<12} {:<12} {:<12}'.format(*'PID_Arrival Time_Burst Time_Waiting Time_Finish Time'.split('_')))
for proc in proc_queue:
    print('{:<4} {:<12} {:<12} {:<12} {:<12}'.format(proc[0], proc[1], proc[2], proc[4], proc[3]))
