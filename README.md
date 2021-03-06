# python-decora_wifi-cli
Leviton Decora wifi switch command line interface, written in Python, utilizing libraries written by Tlyakhov.

Command line control of Leviton Decora Smart WiFi Switches & Dimmers.
Only the required libraries to run this new interface are included with this download and none of Tlyakhov's libraries have been changed.
See tlyakhov/python-decora_wifi for more information about the original code.

You require the switch id(s) to send ON, OFF or 0-100 (for dimmer model) commands to your switch(es) through the Leviton cloud.  To generate a list of the switch ID's currently registered to your account, provide your email address and password on the command line as follows:
```
python <path>/Decora-cli.py [email] [pswd] ?
```
Yields an output, such as:
```
Permission id#12345 (Accountid#9876)
Residence  id#9876  (your address)
Switch1    id#45678 (Familyroom)
Switch2    id#67890 (Livingroom)
Switch3    id#23456 (Bedroom)
```
Once you know your switch id(s), you can execute one or multiple commands on the same line:
```
python <path>/Decora-cli.py [email] [pswd] [id#:ON|OFF|0-100] <[id#:ON|OFF|0-100]> <etc.>
```

Example:
```
python <path>/Decora-cli.py johnsmith@gmail.com password123 67890:ON 45678:OFF 23456:50
```
The program executes the events and returns an output, such as:
```
1. #67890 ON (Livingroom)
2. #45678 OFF (Familyroom)
3. #23456 50% (Bedroom)
```
To determine the current state of a switch, use the following:
```
python <path>/Decora-cli.py [email] [pswd] [id#:?] <[id#:?]> <etc.>
```
Example:
```
python <path>/Decora-cli.py johnsmith@gmail.com password123 45678:? 67890:?
```
The program executes the events and returns an output, such as:
```
OFF  ID#45678  (Familyroom)
ON  ID#67890  (Livingroom)
```

As commented by mtylerb, python-requests is required by this script. Install via apt package manager in Debian.
```
sudo apt-get install python-requests
```

FYI, the original user interface by Tlyakhov is included with the file download:
```
cli-test.py
```
Disclaimer
----------
I'm not affiliated with Leviton Decora in any way. They don't endorse this application. They own all the rights to Leviton Decora (and all associated trademarks). 

This software is provided as-is with no warranty whatsoever. 

Leviton Decora could do things to block this kind of behavior if they want, hopefully they do not. Also, if you cause problems (by sending lots of trash to the Leviton Decora servers or anything), you're on your own.
