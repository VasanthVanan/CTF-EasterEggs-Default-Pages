# CTF-EasterEggs-Default-Pages

EasterEggs is a Python script that allows you to compare the default HTML server web page (say apache) with the HTML web page of your CTF Box that serves Apache. It prints the differences between the two HTML files, highlighting the added, removed or altered content.
This can be really useful for capture the flag events, as it help to identify changes in HTML that may reveal "juicy" information. By quickly comparing a web page's HTML with a official default HTML file, EasterEggs can help flag potentially interesting changes. 

Happy hunting!

## Setup

To use EasterEggs, you need to have Python 3 and the following Python packages installed:

* difflib
* termcolor
* pyfiglet

You can install these packages using pip:
``
pip install difflib
pip install termcolor
pip install pyfiglet
``

## Usage

To use EasterEggs, run the `eastereggs.py` script and provide two arguments:
  > python3 eastereggs.py [URL] [SERVER-NAME]

* `URL` is the URL of the CTF web page you want to compare with the default HTML file.
* `SERVER-NAME` is the name of the server directory containing the HTML file. The directory should be located in the `source` directory.

For example, to compare the HTML of the CTF web page `http://10.10.10.10` that serves `Apache/2.4.18`, you would run:
  > python3 eastereggs.py https://10.10.10.10 apache

## Screenshots
![Script-Demo-Screenshot](/assets/images.png)

## Contributions

Contributions are welcome! If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

## Contact

Follow me on Twitter: [@vasanth__vanan](https://twitter.com/vasanth__vanan)
Connect with me on LinkedIn: [@vasanthavanan](https://www.linkedin.com/in/vasanthavanan/)
Check out my TryHackMe profile: [@vasanth.vanan](https://tryhackme.com/p/vasanth.vanan)
