# keyobell

keyobell is a project for scanning vulnerabilities and exploiting systems automatically.

![GitHub top language](https://img.shields.io/github/languages/top/dharanisaya/AutoPWN-Suite)
![Lines of code](https://img.shields.io/tokei/lines/github/dharanisaya/AutoPWN-Suite)
![Repo Size](https://img.shields.io/github/repo-size/dharanisaya/AutoPWN-Suite)
[![Tests](https://github.com/dharanisaya/AutoPWN-Suite/actions/workflows/tests.yml/badge.svg)](https://github.com/dharanisaya/AutoPWN-Suite/actions/workflows/tests.yml)
![GitHub issues](https://img.shields.io/github/issues-raw/dharanisaya/AutoPWN-Suite)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/dharanisaya/AutoPWN-Suite)
![GitHub Repo stars](https://img.shields.io/github/stars/dharanisaya/AutoPWN-Suite?style=social)
![Banner](https://raw.githubusercontent.com/dharanisaya/AutoPWN-Suite/main/images/banner.png)


## Features
- Fully [automatic!](#usage)
- Detect network IP range without any user input. 
- Vulnerability detection based on version.
- Web app vulnerability testing. (LFI, XSS, SQLI)
- Web app dirbusting.
- Get information about the vulnerability right from your terminal.
- Automatically download exploit related with vulnerability.
- Noise mode for creating a noise on the network.
- Evasion mode for being sneaky.
- Automatically decide which scan types to use based on privilege.
- Easy to read output.
- Specify your arguments using a config file.
- Send scan results via webhook or email.
- Works on Windows, MacOS and Linux.
- Use as a [module!](#module-usage)


## How does it work?

keyobell uses nmap TCP-SYN scan to enumerate the host and detect the version of softwares running on it. After gathering enough information about the host, keyobell automatically generates a list of "keywords" to search [NIST vulnerability database.](https://www.nist.gov/)

[Visit "PWN Spot!" for more information.](https://pwnspot.com/posts/keyobell/)


## Demo

keyobell has a very user friendly easy to read output.

[![asciicast](https://asciinema.org/a/509345.svg)](https://asciinema.org/a/509345)


## Installation

You can clone the repo. (This is the recommended installation method as other methods are no longer maintained)

```
git clone https://github.com/dharanisaya/keyobell.git
cd keyobell
sudo pip install -r requirements.txt
```

OR

You can install it using pip. (sudo recommended)

```
sudo pip keyobell
```

OR

You can download debian (deb) package from [releases.](https://github.com/dharanisaya/keyobell.git)

```
sudo pip install requests rich python-nmap bs4 distro
sudo apt-get install ./keyobell_2.1.5.deb
```

OR

If you are on Arch Linux based system you can install `python-keyobell` package using AUR helper of your choice.

OR

You can use the [docker image.](https://github.com/dharanisaya/keyobell.git)

```
docker pull dharanisaya/keyobell
docker run -it dharanisaya/keyobell
```

OR

You can use Google Cloud Shell.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/dharanisaya/keyobell.git)


## Usage

Running with root privileges (sudo) is always recommended.

Automatic mode

```console
keyobell -y
```


Help Menu

```console
$ keyobell -h

usage: keyobell.py [-h] [-v] [-y] [-c CONFIG] [-nc] [-t TARGET] [-hf HOST_FILE] [-sd] [-st {arp,ping}] [-nf NMAP_FLAGS] [-s {0,1,2,3,4,5}] [-ht HOST_TIMEOUT] [-a API] [-m {evade,noise,normal}] [-nt TIMEOUT]
                  [-o OUTPUT] [-ot {html,txt,svg}] [-rp {email,webhook}] [-rpe EMAIL] [-rpep PASSWORD] [-rpet EMAIL] [-rpef EMAIL] [-rpes SERVER] [-rpesp PORT] [-rpw WEBHOOK]

keyobell | A project for scanning vulnerabilities and exploiting systems automatically.

options:
  -h, --help            show this help message and exit
  -v, --version         Print version and exit.
  -y, --yes-please      Don't ask for anything. (Full automatic mode)
  -c CONFIG, --config CONFIG
                        Specify a config file to use. (Default : None)
  -nc, --no-color       Disable colors.

Scanning:
  Options for scanning

  -t TARGET, --target TARGET
                        Target range to scan. This argument overwrites the hostfile argument. (192.168.0.1 or 192.168.0.0/24)
  -hf HOST_FILE, --host-file HOST_FILE
                        File containing a list of hosts to scan.
  -sd, --skip-discovery
                        Skips the host discovery phase.
  -st {arp,ping}, --scan-type {arp,ping}
                        Scan type.
  -nf NMAP_FLAGS, --nmap-flags NMAP_FLAGS
                        Custom nmap flags to use for portscan. (Has to be specified like : -nf="-O")
  -s {0,1,2,3,4,5}, --speed {0,1,2,3,4,5}
                        Scan speed. (Default : 3)
  -ht HOST_TIMEOUT, --host-timeout HOST_TIMEOUT
                        Timeout for every host. (Default :240)
  -a API, --api API     Specify API key for vulnerability detection for faster scanning. (Default : None)
  -m {evade,noise,normal}, --mode {evade,noise,normal}
                        Scan mode.
  -nt TIMEOUT, --noise-timeout TIMEOUT
                        Noise mode timeout.

Reporting:
  Options for reporting

  -o OUTPUT, --output OUTPUT
                        Output file name. (Default : autopwn.log)
  -ot {html,txt,svg}, --output-type {html,txt,svg}
                        Output file type. (Default : html)
  -rp {email,webhook}, --report {email,webhook}
                        Report sending method.
  -rpe EMAIL, --report-email EMAIL
                        Email address to use for sending report.
  -rpep PASSWORD, --report-email-password PASSWORD
                        Password of the email report is going to be sent from.
  -rpet EMAIL, --report-email-to EMAIL
                        Email address to send report to.
  -rpef EMAIL, --report-email-from EMAIL
                        Email to send from.
  -rpes SERVER, --report-email-server SERVER
                        Email server to use for sending report.
  -rpesp PORT, --report-email-server-port PORT
                        Port of the email server.
  -rpw WEBHOOK, --report-webhook WEBHOOK
                        Webhook to use for sending report.
```


## Module usage

```python
from autopwn_suite.api import AutoScanner

scanner = AutoScanner()
json_results = scanner.scan("192.168.0.1")
scanner.save_to_file("keyobell.json")
```


## Contributing to keyobell

I would be glad if you are willing to contribute this project. I am looking forward to merge your pull request unless its something that is not needed or just a personal preference. Also minor changes and bug fixes will not be merged. Please create an issue for those and I will do it myself. [Click here for more info!](https://github.com/dharanisaya/keyobell/blob/main/.github/CONTRIBUTING.md)


## Legal

You may not rent or lease, distribute, modify, sell or transfer the software to a third party. keyobell is free for distribution, and modification with the condition that credit is provided to the creator and not used for commercial use. You may not use software for illegal or nefarious purposes. No liability for consequential damages to the maximum extent permitted by all applicable laws.


## Support or Contact

Having trouble using this tool? You can reach me out on [discord](https://search.discordprofile.info/374953845438021635), [create an issue](https://github.com/dharanisaya/keyobell/issues/new/choose) or [create a discussion!](https://github.com/dharanisaya/keyobell/discussions)


## Support & Hire Me!

If you want to support my work and also get your job done you can hire me on [Fiverr](https://www.fiverr.com/kaangultekin)! I do various things such as website pentesting, python programming, cleaning malware, PC optimization, file recovery and mentoring.
