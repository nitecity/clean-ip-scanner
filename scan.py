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