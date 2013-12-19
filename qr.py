#!/bin/env python

from pygooglechart import QRChart
import os.path
import argparse

SIZE = 320


def parse_file(in_file, out_file):
    with open(in_file) as f:
        for line in f:
            parse_data(line, out_file)


def parse_data(data, out_prefix):
    chart = QRChart(SIZE, SIZE)
    chart.add_data(data.strip())
    chart.set_ec('H', 0)

    out_fmt = out_prefix + '_{:03d}.png'
    count = 0
    out_file = out_fmt.format(count)
    while os.path.exists(out_fmt.format(count)):
        count += 1
        out_file = out_fmt.format(count)

    print 'Saving {}'.format(out_file)
    chart.download(out_file.format(count))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make a QR code.')
    parser.add_argument('-o', '--output', default='qr',
        help="Output file prefix. Default 'qr'.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='Input file containing data')
    group.add_argument('data', type=str, nargs='?')

    parser.add_argument('-s', '--size', type=int,
        help='Output file size in px. Must be between 100 and 512px. Default 320.')

    args = vars(parser.parse_args())

    if args['size']:
        SIZE = args['size']
        if SIZE < 100 or SIZE > 512:
            raise argparse.ArgumentTypeError(
                '{}px is an invalid size'.format(SIZE))

    if args['file']:
        parse_file(args['file'], args['output'])
    else:
        parse_data(args['data'], args['output'])
