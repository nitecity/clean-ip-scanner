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

    return parser.parse_args()

def get_scan_targets(args: argparse.Namespace) -> list[str]:
    target_networks = []

    try:
        with open(IP_RANGES_FILE) as f:
            all_lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}Error: The IP ranges file '{IP_RANGES_FILE}' was not found.")
        sys.exit(1)

    for cidr in args.cidr_ranges:
        try:
            ipaddress.ip_network(cidr, strict=False)
            target_networks.append(cidr)
            print(f"{Fore.GREEN}Added specified range: {cidr}")
        except ValueError:
            print(f"{Fore.YELLOW}Warning: Skipping invalid CIDR format '{cidr}'.")

    for r in args.ranges:
        matching_ranges = [line for line in all_lines if line.startswith(f"{r}.")]
        if matching_ranges:
            chosen_range = random.choice(matching_ranges)
            target_networks.append(chosen_range)
            print(f"{Fore.GREEN}Selected random range for octet {r}: {chosen_range}")
        else:
            print(f"{Fore.YELLOW}Warning: No ranges found for first octet '{r}' in {IP_RANGES_FILE}.")

    

