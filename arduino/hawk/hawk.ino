/*
  Arduino code part of the Ra project. 
  
  This program provides a Serial interface to various Arduino functions such as:
   - controlling remote switches via RCSwitch
   - controlling LEDs
   (future) - sensing temperature
   (future) - sensing light
  
  Protocol:
  - w + action: turn ON (1) of OFF (0) the current plug (eg: w0, w1)
  - n + network ID: change current network ID (eg: n00001)
  - p + plug ID: change current plug ID (eg: p00010)
  - l: switch ON a LED
  - f: switch OFF a LED
*/

/*
  Copyright (c) 2013 "OKso http://okso.me"

  This file is part of Ra.
  
  Ra is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, either version 3 of the
  License, or (at your option) any later version.
  
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.
  
  You should have received a copy of the GNU Affero General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
*/

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

char inByte;

/* Modes :
- 'w': waiting for message
- 'n': switch, waiting for network ID
- 'p': switch, waiting for plug ID
- 'l': switch on a LED
- 'f': switch off a LED
*/
char MODE = 'w';

char network_id[5+1] = "00001";
char plug_id[5+1] = "00010";

void setup() {
  MODE = 'w';
  
  pinMode(9, OUTPUT); 
  pinMode(10, OUTPUT);
  digitalWrite(9, LOW);
  digitalWrite(10, HIGH);
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(11);
  
  Serial.begin(9600);
  Serial.println("Welcome.");
  Serial.print("net = ");
  Serial.println(network_id);
  Serial.print("plug = ");
  Serial.println(plug_id);
}

void loop() {

  if (Serial.available() > 0) {
    
    if (MODE == 'n') {
      Serial.readBytesUntil('\n', network_id, 5);
      MODE = 'w';
      Serial.print("net = ");
      Serial.println(network_id);
    }
    else if (MODE == 'p') {
      Serial.readBytesUntil('\n', plug_id, 5);
      MODE = 'w';
      Serial.print("plug = ");
      Serial.println(plug_id);
    }
    else if (MODE == 'l') {
      inByte = Serial.read();
      if (inByte == '0') {
        digitalWrite(13, HIGH);
        MODE = 'w';
        Serial.print("LED ON = ");
        Serial.println(inByte);
      }
      else {
        Serial.println("LED ON error");
      }
    }
    else if (MODE == 'f') {
      inByte = Serial.read();
      if (inByte == '0') {
        digitalWrite(13, LOW);
        MODE = 'w';
        Serial.print("LED OFF = ");
        Serial.println(inByte);
      }
      else {
        Serial.println("LED ON error");
      }
    }
    else if (MODE == 'w') {
      
      inByte = Serial.read();
      
      if (inByte == '1') {
        mySwitch.switchOn(network_id, plug_id);
        Serial.println("on");
      }
      else if (inByte == '0') {
        mySwitch.switchOff(network_id, plug_id);
        Serial.println("off");
      }
      else if (inByte == 'w' || inByte == 'n' || inByte == 'p' || inByte == 'l' || inByte == 'f') {
        MODE = inByte;
        Serial.println("mode");
      }
      else {
        MODE = 'w';
        Serial.println("Debug info:");
        Serial.print("net = ");
        Serial.println(network_id);
        Serial.print("plug = ");
        Serial.println(plug_id);
      }
    }
  }
}
