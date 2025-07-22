# ☁️ Cloudflare IP Scanner

A powerful and fast Python script to scan Cloudflare IP ranges and find the one with the lowest latency. Ideal for situations where you need to find an optimal IP for a connection.

[](https://choosealicense.com/licenses/mit/)
[](https://www.python.org/downloads/)

-----

### \#\# About The Project

This script automates the process of finding a "clean" or low-latency IP address from Cloudflare's vast network. It works by concurrently scanning a list of IP ranges, sending a small request to each, and measuring the response time. It then reports the best-performing IP and runs a quick `ping` test to confirm the connection quality.

This is a complete rewrite of the original script, focusing on **speed**, **reliability**, and **user-friendliness**.

-----

### \#\# ✨ Features

  * **Concurrent Scanning:** Uses a `ThreadPoolExecutor` to scan dozens of IPs simultaneously, making the process incredibly fast.
  * **Flexible Targeting:** Scan random ranges, specify ranges by their first octet, or provide exact CIDR notations.
  * **Robust Error Handling:** Gracefully handles invalid ranges and network timeouts.
  * **User-Friendly Interface:** Uses `argparse` for clear and professional command-line argument parsing.
  * **Cross-Platform:** Works on Windows, macOS, and Linux.

-----

### \#\# 🚀 Getting Started

Follow these simple steps to get the scanner up and running.

#### \#\#\# Prerequisites

Make sure you have Python installed on your system (version 3.7 or newer is recommended).

  * **Python**
      * You can download it from the official [Python website](https://www.python.org/downloads/).

#### \#\#\# Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/nitecity/clean-ip-scanner.git
    cd clean-ip-scanner
    ```

2.  **Install the required package:**
    The script uses `colorama` for colored console output.

    ```sh
    pip install colorama
    ```

    *(Note: The script will prompt you to install this if it's missing.)*

3.  **Prepare the IP Ranges File:**
    The script requires an `ipranges.txt` file in the same directory. A sample file is created automatically on the first run, which you can customize with your own CIDR ranges.

-----

### \#\# ⚙️ Usage

You can run the script with various options to customize the scan.

  * **Scan 5 IPs in a random IP range:**

    ```sh
    py scan_refined.py -n 5
    ```

  * **Scan 10 IPs in a range that starts with `104`:**

    ```sh
    py scan_refined.py -n 10 -r 104
    ```

  * **Scan 20 IPs for ranges starting with `104`, `172`, and `45`:**

    ```sh
    py scan_refined.py -n 20 -r 104 -r 172 -r 45
    ```

  * **Scan 15 IPs in a specific CIDR range:**

    ```sh
    py scan_refined.py -n 15 45.142.120.0/24
    ```

  * **Run a default scan (256 IPs in one random range):**

    ```sh
    py scan_refined.py
    ```

-----

### \#\# 📜 License

Distributed under the MIT License. See `LICENSE` file for more information.