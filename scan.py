import re
import sys
import os
import time
import random
from colorama import Fore, Style
ipranges_file: str = 'ipranges.txt'

def run():
    pattern: str = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(/\d{1,2})?$'
    args: list[str] = sys.argv
    all: list[int] = list(range(256))
    random.shuffle(all)
    list_of_ipranges: list[str] = []
    howmany: int = 256
    lowest_latency: int = 10000
    best_ip: str = ""
    if len(args) > 1:
        for i,arg in enumerate(args):
            if arg == '-h' or arg == '--help':
                print(f'Windows:        {Fore.LIGHTCYAN_EX}[py scan.py      -n 5 -r 104]{Style.RESET_ALL}')
                print(f'Linux:  {Fore.LIGHTCYAN_EX}[python3 scan.py -n 5 -r 104]{Style.RESET_ALL}')
                print('-n   Number of IPs to be scanned. 1-256')
                print('-r   Optional IP range.')
                print(f'{Fore.LIGHTCYAN_EX}[py scan.py -n 10 -r 104 -r 203 -r 172 -r 45]{Style.RESET_ALL}\nScans in more than 1 IP range.')
                print(f'You can insert one or more specific IP range:\n{Fore.LIGHTCYAN_EX}[py scan.py -n 5 45.142.120.0/24]{Style.RESET_ALL}')
                print(f'This also works:\n{Fore.LIGHTCYAN_EX}[py scan.py -n 5 45.142.120.0/24 -r 104]{Style.RESET_ALL}')
                print('Options are optional. If you don\'t specify any options, It scans in one random IP range for 256 IPs.')
                print('Enjoy :)')
                return
            if arg.isdigit():
                if args[i-1] == '-n':
                    x = int(arg)
                    if x > 0 and x < 257:
                        howmany = x
                        print(f'{Fore.GREEN}Scanning {arg} IP(s)...{Style.RESET_ALL}')
                    else:
                        print(f'{Fore.YELLOW}Scanning 256(default) IPs...{Style.RESET_ALL}')
                if args[i-1] == '-r':
                    first_eight: list[str] = []
                    with open(ipranges_file) as a:
                        for line in a:
                            line = line.strip()
                            if re.match(fr'^{arg}', line):
                                first_eight.append(line)
                    random_first_eight: str = random.choice(first_eight)
                    list_of_ipranges.append(random_first_eight)
                    print(f'{Fore.GREEN}Scanning in "{random_first_eight}"...{Style.RESET_ALL}')
            if re.match(pattern, arg):
                if not arg in list_of_ipranges:
                    list_of_ipranges.append(arg)
                    print(f'{Fore.GREEN}Searching in "{arg}"...{Style.RESET_ALL}')
    if not list_of_ipranges:
        with open(ipranges_file) as a:
            lines = a.readlines()
        random_iprange = random.choice(lines).strip()
        list_of_ipranges.append(random_iprange)
        print(f'{Fore.YELLOW}Scanning in default "{random_iprange}"{Style.RESET_ALL}')
    
    for ranges in list_of_ipranges:
        for i in range(howmany):
            iprange = re.sub(r'\d+/\d+$|\d+$', str(all[i]) , ranges)
            before = int(round(time.time() * 1000))
            res = os.system(f'curl -I --max-time 0.5 http://{iprange}/cdn-cgi/trace > NUL 2>$1')
            latency = int(round(time.time() * 1000)) - before
            if res == 0:
                if latency < lowest_latency:
                    lowest_latency = latency
                    best_ip = iprange
                print(f"{Fore.CYAN}{iprange} {Fore.GREEN}OK {Fore.LIGHTMAGENTA_EX}{latency}ms{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTRED_EX}{iprange} NO.{res}{Style.RESET_ALL}")
    if best_ip != "":
        print(f"{Fore.LIGHTGREEN_EX}The Lowest Ping:\n{best_ip} {Fore.LIGHTMAGENTA_EX}{lowest_latency}ms{Style.RESET_ALL}")

run()
