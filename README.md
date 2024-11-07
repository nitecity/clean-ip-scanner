# Clean IP Scanner

This is a super simple script to scan and find Clean IPs in IP ranges behind Cloudflare.

## Installation

1. Download and install Python from here: [Python Downloads](https://www.python.org/downloads/)
2. Install the required `colorama` package:
   
- <div style="position: relative;">
        <button onclick="copyToClipboard('code1')" style="position: absolute; right: 0; top: 0;"></button>
        <pre id="code1"><code>pip install colorama</code></pre>
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
         <div style="position: relative;">
          <button onclick="copyToClipboard('code8')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code8"><code>py scan.py -n 5 -r 104</code></pre>
        </div>
  
- **Scans 5 IPs for each in 104, 185, 172 IP ranges:**
  <div style="position: relative;">
          <button onclick="copyToClipboard('code9')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code9"><code>py scan.py -n 5 -r 104 -r 185 -r 172</code></pre>
        </div>
  
- **Scans 5 IPs in a specific IP range (e.g., `104.16.13.0/24`):**
  <div style="position: relative;">
          <button onclick="copyToClipboard('code9')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code9"><code>py scan.py -n 5 104.16.13.0/24</code></pre>
</div>
  
- **Scans 256 IPs in a random IP range:**
  
  <div style="position: relative;">
          <button onclick="copyToClipboard('code10')" style="position: absolute; right: 0; top: 0;"></button>
          <pre id="code10"><code>py scan.py</code></pre>
</div>

