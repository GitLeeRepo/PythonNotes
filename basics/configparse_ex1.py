#!/usr/bin/python3

# Using configparser for ini style config files

from configparser import ConfigParser

def read_config(filename='config.ini', section='atest'):
    parser = ConfigParser()
    parser.read(filename)

    cfg = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            cfg[item[0]] = item[1]
    else:
        raise Exception('{} not found in the {} file'.format(section, filename))

    return cfg


def main():

    print('For section [{}]'.format('atest'))
    cfg = read_config()
    for key in sorted(cfg):
        print(key, cfg[key])

    print('\nFor section [{}]'.format('btest'))
    cfg = read_config(section='btest')
    for key in sorted(cfg):
        print(key, cfg[key])

if __name__ == '__main__':
    main()

