# LiveJournal Page Downloader

This repository contains a script `liveJournalDownload.py` for downloading pages from the blogging website LiveJournal.

## Description

`livejournalDownload.py` is a Python script that uses the `requests` library to send HTTP requests and download the HTML content of LiveJournal pages. The script prompts the user to input a URL and a maximum value for the `skip` query parameter in the URL. The script then iterates over the `skip` values from 0 to the maximum value (inclusive) in increments of 20, downloading the HTML content of each page and saving it to a separate file. The files are named `page_0.html`, `page_1.html`, etc., up to `page_{max_value//20}.html`.

## Prerequisites

Before you begin, you will need to have the following installed on your computer:

- [Python](https://www.python.org/downloads/): This script requires Python to run. If you don't already have Python installed, you can download it from the official website. Make sure to download Python 3, not Python 2.

- [pip](https://pip.pypa.io/en/stable/installation/): pip is the package installer for Python. It is usually included with Python 3. If you don't have pip installed, you can download it from the official website.

- [requests](https://docs.python-requests.org/en/latest/): The `requests` library is a simple HTTP library for Python. You can install it by running `pip install requests` in your terminal.

## Usage

1. Open your terminal. On Windows, you can open the terminal by searching for "Command Prompt" in the Start menu. On macOS, you can open the terminal by searching for "Terminal" in Spotlight. On Linux, you can usually open the terminal by pressing `Ctrl+Alt+T`.

2. Navigate to the directory containing `livejournalDownload.py`. You can do this by using the `cd` command followed by the path to the directory. For example, if `livejournalDownload.py` is in a folder called "livejournal" on your desktop, you would enter `cd Desktop/livejournal`.

3. Run the script by entering `python livejournalDownload.py`. The script will prompt you to enter a URL and a maximum value for `skip`.

## Disclaimer

Please ensure that you have the rights to download and use the content you are downloading. This script should be used responsibly and in accordance with the terms of service of the website being scraped.
