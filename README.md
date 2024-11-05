# Clean IP Scanner for Cloudflare

This is a super simple script to scan and find Clean IPs in IP ranges behind Cloudflare.

## Installation

### Windows

1. Download and install Python from here: [Python Downloads](https://www.python.org/downloads/)
2. Install the required `colorama` package:
        ```pip install colorama```

### Linux

1. Update package lists:
    ```apt update```
2. Install Python and pip:
    - Click to copy: ```apt install python3```
    - Click to copy: ```apt install python3-pip```
3. Install the required `colorama` package:
    - Click to copy: ```pip install colorama```

## Options

- **`-n <NUMBER>`**: Specify the number of IPs to scan. Range: `[1 - 256]`
- **`-r <NUMBER>`**: Specify a specific IP range to scan.
- **No options**: Runs with default settings.

## Examples

- **Scans 5 IPs in a random IP range:**
  - Click to copy: ```py scan.py -n 5```
  
- **Scans 5 IPs in the IP range that starts with 104:**
  - Click to copy: ```py scan.py -n 5 -r 104```
  
- **Scans 5 IPs for each in 104, 185, 172 IP ranges:**
  - Click to copy: ```py scan.py -n 5 -r 104 -r 185 -r 172```
  
- **Scans 5 IPs in a specific IP range (e.g., `104.16.13.0/24`):**
  - Click to copy: ```py scan.py -n 5 104.16.13.0/24```
  
- **Scans 256 IPs in a random IP range:**
  - Click to copy: ```py scan.py```

