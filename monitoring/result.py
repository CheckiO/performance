FILENAME = 'results.txt'

data = {}
with open(FILENAME) as fp:
    lines = fp.readlines()
    for line in lines:
        duration, time = line.rstrip('\n').split(':')
        data[time] = duration

durations = data.values()

min_current = min(durations)
max_current = max(durations)
average = sum(durations) / len(durations)
worse_than_1_second = sum(i > 1 for i in durations)
worse_than_5_second = sum(i > 5 for i in durations)

print(f'min: {min_current}')
print(f'max: {max_current}')
print(f'average: {average}')
print(f'worse: {worse_than_1_second}')
print(f'worse2: {worse_than_5_second}')

for time, duration in data.items():
    if duration > 5:
        print(time)
