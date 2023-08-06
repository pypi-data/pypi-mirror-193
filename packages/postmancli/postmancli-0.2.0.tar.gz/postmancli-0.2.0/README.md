# postman-cli

[![PyPI Version](https://img.shields.io/pypi/v/postmancli.svg)](https://pypi.python.org/pypi/postmancli)
[![PyPI Compatibility](https://img.shields.io/pypi/pyversions/postmancli.svg)](https://pypi.python.org/pypi/postmancli)
[![PyPI License](https://img.shields.io/pypi/l/postmancli.svg)](https://github.com/rdch106/postman-cli/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/af5c773a2094424ba9b0867967478ee7)](https://www.codacy.com/manual/stt-systems/postman-cli?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=stt-systems/postman-cli&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/stt-systems/postman-cli.svg?branch=master)](https://travis-ci.org/stt-systems/postman-cli)

Python CLI (postmancli) tool for emails sending using SMTP server.

### What can I do with postmancli?

* Send emails using SMTP SSL
* Use it from terminal when it is installed
* Multiplatform execution (it is developed in Python)


### Installation

You can install or upgrade postmancli with:

`$ pip install postmancli --upgrade`

Or you can install from source with:

```bash
$ git clone https://github.com/stt-systems/postman-cli.git --recursive
$ cd postmancli
$ pip install .
```


### Quick example

```bash
$ postmancli -S user:password@smtp.gmail.com:465 -f user@gmail.com -t someone@gmail.com -s postman-cli --text "Hello everyone!@nl@@tab@It seems that this works ..." -a "file.txt" "photo.jpg"
```

The example sends an email with `user@gmail.com` as sender, `someone@gmail.com` as receiver, `postman-cli` as subject, `Hello every...` as text message and 2 attachments (file.txt & photo.jpg).


### Help

Run the following command to see all options available:

`postmancli --help` or `postmancli -h`
