import concurrent.futures
from collections import defaultdict
import string
import time

def cleaner(data):
    """
    Removes punctuations from the data
    """
    unwanted = list(string.punctuation)
    for i in unwanted:
        if i == '-':
            data = data.replace(i, ' ')
        else:
            data = data.replace(i, '')
    return data

def worker_node(file):
    """
    Task perform on individual node
    """
    print(f"\nRunning mapper on {file}\n")
    key_value = []
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.lower()
        data = cleaner(data)
        data = data.split()
        for word in data:
            key_value.append((word, 1))
    return key_value

def mapper(work_list):
    """
    Creates mapper process for each task
    """
    mapper_results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        mappers = [executor.submit(worker_node, work) for work in work_list]
        for  mapper in concurrent.futures.as_completed(mappers):
            mapper_results.append(mapper.result())
    return mapper_results


def shuffler(mapper_results):
    """
    Groups the values of each key together in a list
    """
    sorted_mapper_results = defaultdict(list)
    for mapper_result in mapper_results:
        for key, value in mapper_result:
            sorted_mapper_results[key].append(value)
    return sorted_mapper_results

def reducer(shuffler_output):
    result ={}
    for key, value in shuffler_output.items():
        result[key] = sum(value)
    return result


if __name__ == '__main__':
    task_list = [
        './text_files/text_file_1.txt',
        './text_files/text_file_2.txt',
        './text_files/text_file_3.txt',
        './text_files/text_file_4.txt',
        './text_files/text_file_5.txt',
        './text_files/text_file_6.txt',
        './text_files/text_file_7.txt',
        './text_files/text_file_8.txt',
        './text_files/text_file_9.txt',
        './text_files/text_file_10.txt'
    ]

    start = time.perf_counter()

    mapper_results = mapper(task_list)
    # print(mapper_results)
    shuffler_result = shuffler(mapper_results)
    # print(shuffler_result)
    reducer_output = reducer(shuffler_result)
    # print(reducer_output)
    
    finish = time.perf_counter()
    print(f"\nTasks completed in {round(finish-start, 2)} second(s)\n")