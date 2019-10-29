# CentSecure
CentSecure is a tool for automating *parts* of [CyberCenturion](https://www.cybersecuritychallenge.org.uk/what-we-do/cybercenturion-vi) which are easy (e.g. running a single command) or time consumung (e.g. removing backdoors).

> **:warning: Warning:** Use of this tool when it is open source is against CyberCenturion and CyberPatriot rules.

CentSecure is designed to work on all platforms and adapt to the platform that it is being run on. Instead of having a bash script for Linux based systems and a batch script for Windows based systems, it makes sense to keep everything in one place.

<!-- TOC -->

- [Structure](#structure)
- [Payloads](#payloads)
    - [Payload Parameters](#payload-parameters)

<!-- /TOC -->

## Structure

```
  |- payloads
  |   |- payload1.py
  |   `- payload2.py
  |- centsecure.py
  `- payload.py
```

- Here, we have a folder called `payloads` which contains all of the payloads for the program. See more about payloads below.
- `centsecure.py` contains most of the code for running payloads.
- `payload.py` contains code for the base payload class as well as loading payloads.

## Payloads

CentSecure is built around 'payloads' which are modules/plugins which do **one** action, for example: configure the firewall, create a user, etc...

These payloads are then loaded into the application when it is run by searching through the `payloads` folder. Each of the payloads is then checked against the OS and OS version of the computer and then it is run.

The `payloads` folder can contain any amount of Python files each containing any number of payloads (Python files cannot be in subfolders, but can be named anything). **It is worth using a naming scheme for Python files so that they can be easily found!**

Each of the Python files can have any number of 'payloads' inside them. Payloads are essentially classes which inherit a base class. This ensures that the `execute()` function always exists. Here is an example of what might be contained in a Python file:

```python
import payload


class MyPayload(payload.Payload):
    name = "My Payload"
    os = ["Windows"]
    os_version = ["10"]

    def execute(self):
        # Put code here (e.g. configure firewall, create user, etc...)
```

**Note:** _Each `class` must have a unique name!_

### Payload Parameters

Payload parameters help the program to tell which operating systems your payload should run on. With the payload example above there are 3 parameters set `name`, `os` and `os_version`, this tells the program that the payload should only be run on **Windows** operating systems on version **10** only. Here are all of the available payload parameters:

- **`name`** is just the name that is used when talking about the payload in the output. It doesn't really matter.
- **`os`** is the operating system that the payload is targeting. It is a **list** containing all of the operating systems that this payload is compatible with. (e.g. `all`, `Windows`, `Linux`, `Ubuntu`, etc...)
- **`os_version`** is the version of the operating system that the payload is targeting. It is also a **list** containing all of the versions of operating system that this payload is compatible with. (e.g. `all`, `10`, `9`, `19.10`, etc...)

> **It is best to run CentSecure on the actual computer that you want the payload to run on and then copy down the OS and OS version that it prints at the start.**