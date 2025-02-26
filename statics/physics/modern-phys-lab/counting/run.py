import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import scipy

def read_file(file: str) -> np.typing.ArrayLike:
    with open(f'{file}.csv', 'r') as file:
        lines = file.read().split('Channel,Energy,Counts')[1].strip().split('\n')
        return np.array([int(line.split(',,')[1]) for line in lines], dtype=np.uint16)

all_data = {
    '200': read_file('200'),
    '100': read_file('100-1') + read_file('100-2'),
    '40': sum([read_file(f'40-{i}') for i in range(1, 6)])
}

fig, axs = plt.subplots(len(all_data), 1, sharex='col')
i = 0

for dwell_time in all_data:
    print(f'\n==[{dwell_time}ms]==\n')
    data = all_data[dwell_time]

    N = len(data)
    print(f'Loaded {sum(data)} events across {N} samples')

    mean = np.mean(data)
    print(f'Found sample mean {mean:0.2f}')

    stdev = np.std(data, ddof=1)
    print(f'Found sample standard deviation {stdev:0.2f}')

    sigma = np.sqrt(mean)
    print(f'Found sigma {sigma:0.2f}')

    P = 0.6745 * sigma
    print(f'Found P {P:0.2f}')
    
    times_dev_more_than_s = (np.abs(data - mean) > sigma).sum()
    print(f'Found {times_dev_more_than_s} / {N} ({times_dev_more_than_s / N * 100:0.2f}%) samples deviating from the mean more than sigma {sigma:0.2f}')
    
    times_dev_more_than_P = (np.abs(data - mean) > P).sum()
    print(f'Found {times_dev_more_than_P} / {N} ({times_dev_more_than_P / N * 100:0.2f}%) samples deviating from the mean more than P {P:0.2f}')

    ax = axs[i]
    ax.set_xlabel('Run Count')
    ax.set_ylabel('Events Measured')
    ax.set_title('Raw Data')
    ax.scatter(np.arange(1, len(data)+1), data, s=4)
    ax.legend(['\n'.join([
        f'Mean: {mean:0.2f}',
        f'Sample Sd. Dev: {stdev:0.2f}',
        f'P: {P:0.2f}',
        f'Events > sigma: {times_dev_more_than_s} ({times_dev_more_than_s / N * 100:0.2f}%)',
        f'Events > P: {times_dev_more_than_P} ({times_dev_more_than_P / N * 100:0.2f}%)'
    ])])

    # ax = axs[i][1]
    # ax.set_visible(False)

    # ax.set_title(f'Cumulative Average ({dwell_time}ms Dwell time)')
    # ax.set_xlabel('After N Runs')
    # ax.set_ylabel('Cumulative Average')

    # sample_num = np.arange(1, N + 1)
    # cumulative_average = np.cumsum(data) / sample_num
    # ax.plot(sample_num, cumulative_average, label=f'Final Value: {cumulative_average[-1]:0.2f}')
    # ax.legend()


    # ax = axs[i]
    # N, bins, patches = ax.hist(data, density=True, bins=32, label='Measured Data')

    # fracs = N / N.max()
    # norm = colors.Normalize(fracs.min(), fracs.max())
    # for thisfrac, thispatch in zip(fracs, patches):
    #     color = plt.cm.viridis(norm(thisfrac))
    #     thispatch.set_facecolor(color)

    # ax.set_xlabel('Event Count')
    # ax.set_ylabel('Frequency')

    # linspace = np.arange(bins.min(), bins.max())
    # gaussian = scipy.stats.norm.pdf(linspace, mean, stdev)
    # ax.plot(linspace, gaussian, label='Fitted Gaussian')
    # ax.legend()

    i += 1
plt.show()