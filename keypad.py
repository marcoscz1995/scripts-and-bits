#!/usr/bin/env python
import os
from evdev import InputDevice, categorize, ecodes
keyboard = InputDevice('/dev/input/event3')
#dev.grab()

for event in keyboard.read_loop():
  if event.type == ecodes.EV_KEY:
      key = categorize(event)
      if key.keystate == key.key_down:
          if key.keycode == 'KEY_KPSLASH': #go to previous page
               os.system('xdotool key ctrl+Prior')
          if key.keycode == 'KEY_KPASTERISK': #go to tab to next page
               os.system('xdotool key ctrl+Next')
          if key.keycode == 'KEY_KP0': #to window tab to the left
               os.system('xdotool key Alt_R+Left')
          if key.keycode == 'KEY_KPPLUS': #to window tab to the right
               os.system('xdotool key Alt_R+Right')
          if key.keycode == 'KEY_KP5': #  mouse left click
               os.system('xdotool click 1')
          if key.keycode == 'KEY_KPMINUS': #close current tab in chrome
               os.system('xdotool key ctrl+F4')
          if key.keycode == 'KEY_KPDOT': #open link in tab in chrome
               os.system('/home/cos/Documents/coding/scripts-and-bits/crowdmarker')
