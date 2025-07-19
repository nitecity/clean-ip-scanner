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

    if not target_networks:
        if not all_lines:
            print(f"{Fore.RED}Error: {IP_RANGES_FILE} is empty. No ranges to scan.")
            sys.exit(1)
        random_range = random.choice(all_lines)
        target_networks.append(random_range)
        print(f"{Fore.YELLOW}No range specified. Using random default: {random_range}")

    ips_to_scan = []
    scan_count = max(1, min(args.count, 256))

    for network_str in target_networks:
        try:
            network = ipaddress.ip_network(network_str, strict=False)
            available_hosts = list(network.hosts())

            if not available_hosts:
                print(f"{Fore.YELLOW}Warning: Network {network_str} has no scannable host IPs. Skipping.")
                continue

            sample_size = min(scan_count, len(available_hosts))
            sampled_hosts = random.sample(available_hosts, k=sample_size)
            ips_to_scan.extend([str(ip) for ip in sampled_hosts])

        except ValueError:
            print(f"{Fore.YELLOW}Warning: Skipping invalid network range '{network_str}'.")

    return list(set(ips_to_scan))

def scan_ip(ip: str, timeout: float) -> tuple[str, int | None, bool]:
    command = [
        'curl',
        '-s',
        '--max-time', str(timeout),
        f'http://{ip}/cdn-cgi/trace'
    ]
    start_time = time.perf_counter()

