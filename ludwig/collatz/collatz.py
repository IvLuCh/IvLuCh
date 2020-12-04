import multiprocessing
from termcolor import colored
from sys import argv
from os import getpid, path, mkdir
from numpy import array as np_array, array_split
from multiprocessing import Pool, cpu_count
from matplotlib import pyplot


def get_dpi(input:int):
    if input > 1000:
        if input > 5000: return 5000
        return input
    return 1000

def sorted_dict(input:dict):
    result = {}
    for key in sorted(input): result[key] = input[key]
    return result

def collatz_steps(i:int) -> int:
    steps:int = 0
    while True:
        if i == 1: break
        steps += 1
        if i % 2 == 0: i = i / 2
        else: i = 3 * i + 1
    return steps

def mp_list_collatz_steps(input:list) -> dict:
    print(f'Starting process {getpid()}...')
    result = {}
    for i in input: result[i] = collatz_steps(i)
    return result

def mp_amount_list_collatz_steps(input:list) -> dict:
    print(f'Starting process {getpid()}...')
    result = {}
    for i in input:
        tmp_result = collatz_steps(i)
        if tmp_result in result.keys(): result[tmp_result] += 1
        else: result[tmp_result] = 1
    return result

def collatz_diagram_step(input:int, bar:bool=True):
    print(colored(f'Calculating collatz steps until {input}...', 'blue'))

    crange = list(range(1, input + 1))
    arrays = []
    cpu_count = multiprocessing.cpu_count()
    for _ in range(cpu_count):
        arrays.append(crange[::cpu_count])
        crange.pop(0)
    
    result = Pool().map(mp_list_collatz_steps, arrays)
    arrays = None
    values = {}
    for dict in result: values = {**values, **dict}
    result = None
    values = sorted_dict(values)

    if(bar): pyplot.bar(values.keys(), values.values())
    else: pyplot.plot(values.keys(), values.values())

    pyplot.title(f'Collatz-Schrittanzahl bis {input}')
    pyplot.ylabel('Schrittanzahl')
    pyplot.margins(x=0)

    img_name = ''
    if bar: img_name = f'collatz-img-1-{input}.png'
    else: img_name = f'collatz-img-1-plot-{input}.png'

    if not path.isdir('img'):
        print('Creating directory \'img\'...')
        mkdir('img')

    print(colored(f'Rendering image \'{img_name}\' with dpi {get_dpi(input)}...', 'blue'))
    pyplot.savefig(f'img/{img_name}', dpi=get_dpi(input))
    print(colored('Finished rendering!', 'green'))


def collatz_amount_diagram_step(input:int, bar:bool=True):
    print(colored(f'Calculating amount of collatz steps for numbers until {input}...', 'blue'))
    
    crange = list(range(1, input + 1))
    arrays = []
    cpu_count = multiprocessing.cpu_count()
    for _ in range(cpu_count):
        arrays.append(crange[::cpu_count])
        crange.pop(0)

    result = Pool().map(mp_amount_list_collatz_steps, arrays)
    values = {}
    for dict in result:
        for key, value in dict.items():
            if key in values.keys(): values[key] += value
            else: values[key] = value
    result = None
    values = sorted_dict(values)

    if bar: pyplot.bar(values.keys(), values.values())
    else: bar: pyplot.plot(values.keys(), values.values())

    pyplot.margins(x=0)
    pyplot.xlabel('Schrittanzahl')
    pyplot.ylabel('Anzahl Zahlen')

    img_name = ''
    if bar: img_name = f'collatz-img-2-{input}.png'
    else: img_name = f'collatz-img-2-plot-{input}.png'

    if not path.isdir('img'):
        print('Creating directory \'img\'...')
        mkdir('img')

    print(colored(f'Rendering image \'{img_name}\' with dpi {get_dpi(input)}...', 'blue'))
    pyplot.savefig(f'img/{img_name}', dpi=get_dpi(input))
    print(colored('Finished rendering!', 'green'))


def print_usage():
    print('Usage: <MODE(1|2)> <STEPS(UINT\{0})> <BAR|PLOT>')

if __name__ == '__main__':
    if len(argv) == 1: print_usage()
    elif len(argv) == 2 and argv[1].lower() == 'template':
        #for i in range(3, 6): 
        #    collatz_diagram_step(10 ** i)
        for i in range(3, 8): 
            collatz_amount_diagram_step(10 ** i)
    elif len(argv) == 4:
        error = False
        try:
            if int(argv[1]) not in [1, 2]: raise None
            elif int(argv[2]) < 1: raise None
            elif argv[3].lower() not in ['bar', 'plot']: raise None
        except:
            error = True
            print_usage()
        if not error:
            i = int(argv[1])
            if i == 1: 
                collatz_diagram_step(int(argv[2]), argv[3].lower() == 'bar')
            elif i == 2:
                collatz_amount_diagram_step(int(argv[2]), argv[3].lower() == 'bar')
            else: print_usage()
    else: print_usage()
    
