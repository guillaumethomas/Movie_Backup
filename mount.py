
#!/usr/bin/env python3
from os import system, getcwd, getlogin
from explore_nas import read_nas_fs

if __name__ == '__main__':
    # system('echo Mount_NAS_Python3')
    system('sudo mount -a')

    current_dir = getcwd()
    print(getlogin())

    locations = {'WD': '/home/pi/mnt/WD/Shared Videos',
                 'LG': '/home/pi/mnt/LG/'}
    all_data = list()
    list_films = list()
    nas = dict()
    for location in locations.items():
        system('cd ' + location[1])
        system('pwd')
        print(location)
        nas[location[0]] = read_nas_fs(location[1])
        # print(len(list_films[-1]))
    print('{}\n'.format(nas.keys()))
    compare = [i[1] for i in nas.values()]

    for i in range(2):
        print('\n')
        for i in compare:
            i.sort()
        not_in = [j for j in compare[1] if j not in compare[0]]
        for i in not_in:
            print(i)
        compare.reverse()

    system('cd ' + current_dir)
    print(getcwd())
