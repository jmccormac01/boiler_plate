"""
A few python boiler plate functions.
Hopefully useful when scripting
"""

import argparse as ap

def arg_parse():
    """
    paerse the command line arguments
    """
    p = ap.ArgumentParser()
    p.add_argument()
    return p.parse_args()
