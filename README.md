# Sections
- [Description](#description)
- [Purpose](#purpose)
- [Install and Run](#install-and-run)
    - [Requirements](#make-sure-you-have-python-and-git)
    - [Requirement notes](#note)
- [Usage](#usage)

# Description
Go Back To School is a program that helps you 
to know how many time you have to go before it arrived.

# Purpose
As a student, we always under pression when it is time to go back to school. Why? Because our brain know, without true precision, the duration between now and this date.
That's why this program was created:
* Makes your brain ready to go back to school
* Now exactly how many days/hour you have

# Install and Run
Make sure you already have `git` and `python` installed
on your machine.


```sh
# install
git clone git@github.com:RFihobiana/Back2School.git

# running
cd Back2School
python main.py
```

## Make Sure You Have Python and Git
In the case you have already `git` and `python`, go
to the next section

### Note
This command work only for Red Hat linux distro.
Change `dnf` into your package manager. (For example: `apt`).
On Windows, just go to the web to search and install them.

```sh
# note: This command run for Red Hat distrubition
sudo dnf install git python
```

# Usage
```sh
python main.py

# Results printed (depend on the date you run him):
28 days, 3:10:56.654761
```
