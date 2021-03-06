"""
CLI

Написать скрипт (Python). Который будет проверять число, введнное польователем на чётность

use:
    Linux: python3 step_02_cli.py <number>
    Windows: python step_02_cli.py <number>

"""

import argparse

parser = argparse.ArgumentParser(description='Process some parity.')
parser.add_argument('parity', type=int,
                    help='an parity for the accumulator')

args = parser.parse_args()

if args.parity % 2 == 0:
    print(f'Чётное чисто: {args.parity}')
else:
    print('Не чётное число')
