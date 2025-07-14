import argparse
import ipaddress
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("colorama not found. Please install it using: pip install colrama")
    sys.exit(1)

IP_RANGES_FILE = 'ipranges.txt'
DEFAULT_SCAN_COUNT = 256
DEFAULT_TIMEOUT = 1.0

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="scan IP ranges for the one with the lowest latency.",
        epilog="Enjoy scanning! :)",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '-n', '--count',
        type=int,
        default=DEFAULT_SCAN_COUNT,
        help=f'Number of random IPs to scan per range (1-256). Default: {DEFAULT_SCAN_COUNT}'
    )

    parser.add_argument(
        '-r', '--range',
        dest='ranges',
        action='append',
        default=[],
        help="Specify the first octet of an IP range to scan (e.g., -r 104). Can be used multiple times."
    )

    parser.add_argument(
        'cidr_ranges',
        nargs='*',
        default=[],
        help="One or more specific CIDR ranges to scan (e.g., 45.142.120.0/24)."
    )