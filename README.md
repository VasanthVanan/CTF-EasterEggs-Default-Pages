# CTF-EasterEggs-Default-Pages

This is a Python script that compares the default webserver welcome page (say apache) with the webpage of your CTF Box (say it serves Apache). It prints the differences between the two HTML files, highlighting the added, removed or altered content.

This can be really useful for capture the flag events, as it quickly identifies potentially interesting changes in HTML.

Happy hunting!

## Setup

To use EasterEggs, you need to have Python 3 and the following Python packages installed:

* difflib
* termcolor
* pyfiglet

You can install these packages using pip:
```shell
pip install difflib
pip install termcolor
pip install pyfiglet
```

## Usage

To use EasterEggs, run the `eastereggs.py` script and provide two arguments:
  ```python 
  python3 eastereggs.py [URL] [SERVER-NAME]
  ```

* `URL` is the URL of the CTF web page you want to compare with the default HTML file.
* `SERVER-NAME` is the name of the server directory containing the HTML file. The directory should be located in the `source` directory.

For example, to compare the HTML of the CTF web page `http://10.10.10.10` that serves `Apache/2.4.18`, you would run:
  ```python
  python3 eastereggs.py https://10.10.10.10 apache
  ```

## Screenshots
![Script-Demo-Screenshot](https://lh3.googleusercontent.com/pw/AIL4fc-4tqN7BhtqFPgczltpgvfqnsNxB2jV3BumwFWeAB2T5dS91NkI5pdzAycnnNXe-9cjFwvdmdL2eGOwrEUMa26t0lAYd9T6vtbNttEmsVcVgRXLcIDja7xSe-hz1hAXHcTEdvFOtsDwhDFn5Ecfti4b=w1920-h666-s-no)
![Script-Demo-Screenshot-2](https://lh3.googleusercontent.com/pw/AIL4fc9Cy8r5loTwDNKmHapnsQqV1H9CkFnKWABB5h62ydOcsJt371pLX7RCqHwfIkNYq9nt1dodZqKu6QRo7dYm88tvGxNzCn1dlPDO4fL4wy5oPzcqec_H5BsuzMBVBcqgXcgAvSNW3hZjpQPb7zCwhBbh=w1920-h484-s-no)

## Contributions

Contributions are welcome! If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

## Contact

Follow me on Twitter: [@vasanth__vanan](https://twitter.com/vasanth__vanan)

Connect with me on LinkedIn: [@vasanthavanan](https://www.linkedin.com/in/vasanthavanan/)

Check out my TryHackMe profile: [@vasanth.vanan](https://tryhackme.com/p/vasanth.vanan)
