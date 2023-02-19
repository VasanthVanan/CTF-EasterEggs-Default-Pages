import difflib
import sys
import os
from urllib.request import urlopen
from termcolor import colored
import pyfiglet
import http.client

def get_html_from_url(url):
    # Get HTML file from the specified URL
    html = urlopen(url).read().decode("utf-8")
    return html

def get_html_from_file(website_name):
    # Get HTML file from the source directory
    directory_path = os.path.join("source", website_name)
    html_path = os.path.join(directory_path, "index.html")
    with open(html_path, encoding="utf-8") as file:
        html = file.read()
    return html

def compare_html(html1, html2):
    # Compare the two HTML files
    differ = difflib.Differ()
    diff = list(differ.compare(html2.splitlines(), html1.splitlines()))
    return diff

def print_diff(diff):
    # Print the differences between the two HTML files
    added = []
    removed = []
    isAltered = False
    for line in diff:
        if line.startswith('+ '):
            if(line[2:].strip() != ""):
                added.append(colored("[+]", "green") + " " + colored(line[2:].strip(), "green"))
        elif line.startswith('- '):
            if(line[2:].strip() != ""):
                removed.append(colored("[-]", "red") + " " + colored(line[2:].strip(), "red"))

    if added:
        print(colored("\nAdded content:", "white"))
        print("\n".join(added))
        isAltered = True

    if removed:
        print(colored("\nRemoved content:", "white"))
        print("\n".join(removed))
        isAltered = True

    if(not isAltered):
        print(colored("No EasterEggs Found: Looks like Default Page!", "white"))

# Print ASCII art
ascii_art = pyfiglet.figlet_format("EasterEggs","shadow")
print("\n"+colored(ascii_art, "blue"))

# Check number of command-line arguments
if len(sys.argv) != 3:
    print(colored("Usage: python3 eastereggs.py [URL] [website-name]\n","red"))
    sys.exit(1)

# Get URL and website name from the command-line arguments
url = sys.argv[1]
website_name = sys.argv[2]

# Get HTML files
html1 = get_html_from_url(url)
html2 = get_html_from_file(website_name)

# Compare HTML files
diff = compare_html(html1, html2)

# Print differences between the two HTML files
print_diff(diff)
