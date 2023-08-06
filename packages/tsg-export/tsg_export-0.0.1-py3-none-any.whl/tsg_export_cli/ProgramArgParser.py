from pathlib import Path
import argparse
import math
import sys

class ProgramArgParser:
    def __new__(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument('command', choices=['export-csvs', 'export-images'], help='program you want to run (export csvs vs images)', type=str)
        args = parser.parse_args(sys.argv[1:2])
        match args.command:
            case 'export-csvs':
                subcommand_args = cls.export_csvs()
            case 'export-images':
                subcommand_args = cls.export_images()
            case other:
                raise NotImplementedError('Implement arg parsing for this command')

        subcommand_args.command = args.command
        return subcommand_args

    def export_csvs():
        parser = argparse.ArgumentParser()
        parser.add_argument('data_dir', type=Path, help='path of the TSG dataset, should be a dir containing all (3) tsg files')
        parser.add_argument('output_dir', nargs='?', default=Path('./'), type=Path, help='directory where the exported images are outputted to')
        return parser.parse_args(sys.argv[2:])

    def export_images():
        parser = argparse.ArgumentParser()
        parser.add_argument('data_dir', type=Path, help='path of the TSG dataset, should be a dir containing all (3) tsg files')
        parser.add_argument('output_dir', nargs='?', default=Path('./'), type=Path, help='directory where the exported images are outputted to')
        parser.add_argument('-s', '--start_depth', default=0.0, required=True, type=float, help='depth in metres, only used for image generation image sample')
        parser.add_argument('-e', '--end_depth', default=math.inf, required=True, type=float, help='depth in metres, only used for image generation image sample')
        parser.add_argument('-d', '--depth_delta', default=50.0, type=float, help='the length (in metres) of each captured in each image: long sections are broken down')
        parser.add_argument('-q', '--subsampling_factor', default=10, type=int, help='the downsampling factor (q): the image has 1/q² the pixel density and takes up 1/q² the space')
        args = parser.parse_args(sys.argv[2:])

        if args.end_depth <= args.start_depth:
            raise ValueError('End depth must be greater than starting depth')

        return args