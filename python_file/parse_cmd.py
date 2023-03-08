import argparse
import os


def parse_cmd():
    parser = argparse.ArgumentParser()

    parser.add_argument('-id',
                        type=int,
                        default=None,
                        help='VK ID of target. Default = None')
    parser.add_argument('-extension',
                        type=str,
                        default='.json',
                        help="Extension of the output report. Default = json")
    parser.add_argument('-path',
                        type=str,
                        default=os.getcwd(),
                        help="The path to the output report. Default = current directory")

    return parser.parse_args()