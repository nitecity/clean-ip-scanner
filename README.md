# Clean IP Scanner for Cloudflare

This is a super simple script to scan and find Clean IPs in IP ranges behind Cloudflare.

## Installation

### Windows

1. Download and install Python from here: [Python Downloads](https://www.python.org/downloads/)
2. Install the required `colorama` package:
        <div style="position: relative;">
          <button onclick="copyToClipboard('code1')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code1"><code>pip install colorama</code></pre>
        </div>

### Linux

1. Update package lists:
        <div style="position: relative;">
          <button onclick="copyToClipboard('code2')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code2"><code>apt update</code></pre>
        </div>
2. Install Python and pip:
    <div style="position: relative;">
          <button onclick="copyToClipboard('code3')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code3"><code>apt install python3</code></pre>
    </div>
    <div style="position: relative;">
          <button onclick="copyToClipboard('code4')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code4"><code>apt install python3-pip</code></pre>
    </div>
    <div style="position: relative;">
          <button onclick="copyToClipboard('code5')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code5"><code>apt install python3-pip</code></pre>
    </div>
    
3. Install the required `colorama` package:
   <div style="position: relative;">
          <button onclick="copyToClipboard('code6')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code6"><code>pip install colorama</code></pre>
    </div>

## Options

- **`-n <NUMBER>`**: Specify the number of IPs to scan. Range: `[1 - 256]`
- **`-r <NUMBER>`**: Specify a specific IP range to scan.
- **No options**: Runs with default settings.

## Examples

- **Scans 5 IPs in a random IP range:**
       <div style="position: relative;">
          <button onclick="copyToClipboard('code7')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code7"><code>py scan.py -n 5</code></pre>
        </div>
  
  
- **Scans 5 IPs in the IP range that starts with 104:**
  - Click to copy: ```py scan.py -n 5 -r 104```
  
- **Scans 5 IPs for each in 104, 185, 172 IP ranges:**
  - Click to copy: ```py scan.py -n 5 -r 104 -r 185 -r 172```
  
- **Scans 5 IPs in a specific IP range (e.g., `104.16.13.0/24`):**
  - Click to copy: ```py scan.py -n 5 104.16.13.0/24```
  
- **Scans 256 IPs in a random IP range:**
  - Click to copy: ```py scan.py```

