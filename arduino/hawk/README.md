Arduino code part of the Home project.

This program provides a Serial interface to various Arduino functions such as:
* controlling remote switches via RCSwitch
* controlling LEDs
* (future) - sensing temperature
* (future) - sensing light

Protocol
========

* w + action: turn ON (1) of OFF (0) the current plug (eg: w0, w1)
* n + network ID: change current network ID (eg: n00001)
* p + plug ID: change current plug ID (eg: p00010)
* l: switch ON a LED
* f: switch OFF a LED

Copyright OKso http://okso.me, All rights reserved.
