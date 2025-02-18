import numpy as np

def read_file(file: str) -> np.typing.ArrayLike:
    with open(f'{file}.csv', 'r') as file:
        lines = file.read().split('Channel,Energy,Counts')[1].strip().split('\n')
        return np.array([int(line.split(',,')[1]) for line in lines])

all_data = {
    '200': read_file('200'),
    '100': read_file('100-1') + read_file('100-2'),
    '40': sum([read_file(f'40-{i}') for i in range(1, 6)])
}

for time in all_data:
    data = all_data[time]

    mean = np.mean(data)
    print(f'Found sample mean {mean}')

    stdev = np.stdev(mean, ddof=1)