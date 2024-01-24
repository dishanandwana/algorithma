import concurrent.futures

import random


def file(file_name):
    data = []
    for i in range(10):
        data.append(random.randint(1, 100))

    with open(file_name, 'w') as file:
        file.write('\n'.join(map(str, data)))

if __name__ == '__main__':

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        result = []
        for i in range(1, 6):
            file_name = f'{i}.txt'
            result.append(file_name)
            futures = {executor.submit(file, i): i for i in result}
            concurrent.futures.wait(futures)
    print(' 5 files created')




