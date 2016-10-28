#!/usr/bin/env python
# coding: utf-8
import os
import csv
import sys
import glob
import struct
import logging
import argparse

from dbfread import DBF

from __init__ import __version__


def get_args():
    """Get CLI arguments and options"""
    parser = argparse.ArgumentParser(
        version=__version__,
        prog='dbf2csv',
        description='small utility to convert simple *.DBF files to *.CSV'
    )
    parser.add_argument('input')
    parser.add_argument('output', nargs='?', default=None)

    parser.add_argument('-ei', '--input-encoding',
                        default='cp850',
                        help='charset of *.dbf files (default: cp850)')
    parser.add_argument('-eo', '--output-encoding',
                        default='utf8',
                        help='charset of *.csv files (default: utf8)')
    parser.add_argument('-q', '--quoting-mode',
                        choices=('minimal', 'all', 'non-numeric', 'none'),
                        default='minimal',
                        help='quoting mode for csv files (default: minimal)')
    parser.add_argument('-d', '--delimiter-char',
                        default=',',
                        help='delimiter char for csv files (default: ",")')
    parser.add_argument('-e', '--escape-char',
                        default='\\',
                        help='escape char for csv files (default: "\\")')
    return parser.parse_args()


def __convert(input_file_path, output_file, args):

    def write_row(writer, row, encoding):
        buffer_row = []
        for cell in row:
            if isinstance(cell, basestring):  # TODO: Python 3 support
                cell = cell.encode(encoding)
            buffer_row.append(cell)
        writer.writerow(buffer_row)

    output_writer = csv.writer(output_file,
                               quoting=args.quoting,
                               escapechar=args.escape_char,
                               delimiter=args.delimiter_char)

    try:
        input_reader = DBF(input_file_path,
                           encoding=args.input_encoding,
                           ignore_missing_memofile=True)

        write_row(output_writer,
                  input_reader.field_names,
                  args.output_encoding)
        for record in input_reader:
            write_row(output_writer, record.values(), args.output_encoding)

    except (UnicodeDecodeError, LookupError):
        log.error('Error: Unknown encoding\n')
        exit(0)

    except UnicodeEncodeError:
        log.error('Error: Can\'t encode to output encoding: {}\n'.format(
            args.to_charset))
        exit(0)
    except struct.error:
        log.error('Error: Bad input file format: {}\n'.format(
            os.path.basename(input_file_path))
        )
        exit(0)


def process_directory(input_dir_path, output_dir_path, args):
    if not output_dir_path:
        output_dir_path = input_dir_path

    input_files = glob.glob('{}/*.dbf'.format(input_dir_path))

    if not input_files:
        exit(0)

    for input_file_path in input_files:
        output_file_path = '{}/{}.csv'.format(
            output_dir_path,
            os.path.splitext(os.path.basename(input_file_path))[0]
        )
        if output_dir_path != input_dir_path:
            if not os.path.exists(output_dir_path):
                os.makedirs(output_dir_path)

        process_file(input_file_path, output_file_path, args)


def process_file(input_file_path, output_file_path, args):
    if output_file_path:
        with open(output_file_path, 'w') as output_file:
            __convert(input_file_path, output_file, args)
    else:
        __convert(input_file_path, sys.stdout, args)


def main():
    sys.tracebacklimit = 0

    args = get_args()

    if args.quoting_mode == 'minimal':
        args.quoting = csv.QUOTE_MINIMAL
    elif args.quoting_mode == 'all':
        args.quoting = csv.QUOTE_ALL
    elif args.quoting_mode == 'non-numeric':
        args.quoting = csv.QUOTE_NONNUMERIC
    elif args.quoting_mode == 'none':
        args.quoting = csv.QUOTE_NONE

    if os.path.isdir(args.input):
        process_directory(args.input, args.output, args)
    elif os.path.isfile(args.input):
        process_file(args.input, args.output, args)


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler())

    try:
        main()
    except KeyboardInterrupt:
        pass
