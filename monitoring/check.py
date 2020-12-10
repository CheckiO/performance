import sys


def check(FILENAME):
    FOLDER = 'recorded_data/'
    FILE = FOLDER + FILENAME
    data = {}
    with open(FILE) as fp:
        lines = fp.readlines()
        for line in lines:
            duration, time = line.rstrip('\n').split('-')
            data[time] = float(duration)

    durations = data.values()

    min_current = min(durations)
    max_current = max(durations)
    count = len(durations)
    average = round(sum(durations) / len(durations), 2)
    worse_than_1_second = sum(i > 1 for i in durations)
    worse_than_5_second = sum(i > 5 for i in durations)

    print(f'Min: {min_current}')
    print(f'Max: {max_current}')
    print(f'Count: {count}')
    print(f'Average: {average}')
    print(f'Worse than 1 seconds: {worse_than_1_second}')
    print(f'Worse than 5 seconds: {worse_than_5_second}')

    for time, duration in sorted(data.items()):
        if duration > 5:
            print(f'{duration} at {time}')


if __name__ == "__main__":
    check(sys.argv[1])
