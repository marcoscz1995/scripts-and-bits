 #!/usr/bin/env python
import os
from evdev import InputDevice, categorize, ecodes
keyboard = InputDevice('/dev/input/event12')
mouse = InputDevice('/dev/input/event8')
#dev.grab()

for event in keyboard.read_loop():
  if event.type == ecodes.EV_KEY:
      key = categorize(event)
      if key.keystate == key.key_down:
          if key.keycode == 'KEY_DOT': #key 52 is page down
              os.system('xdotool key Page_Down && xdotool key Return')
          if key.keycode == 'KEY_L': #key 39 is page up
              os.system('xdotool key Page_Up && xdotool key Return')
          if key.keycode == 'KEY_COMMA': #is go to tab ot the left
              os.system('xdotool key ctrl+Prior && xdotool key Return')
          if key.keycode == 'KEY_SLASH': #key 53 is go to tab to the right
              os.system('xdotool key ctrl+Next && xdotool key Return')
          if key.keycode == 'KEY_LEFT': #left arrow to go back a page
               os.system('xdotool key Alt_R+Left')
          if key.keycode == 'KEY_RIGHT': #right arrow to go forward a page
               os.system('xdotool key Alt_R+Right')
# =============================================================================
#           if key.keycode == 'KEY_UP': #up arrow
#               os.system('xdotool key Up')
#           if key.keycode == 'KEY_DOWN': #down arrow
#               os.system('xdotool key Down')
# =============================================================================
          if key.keycode == 'KEY_ENTER': #  
              os.system('xdotool key Return && xdotool key Return')
          if key.keycode == 'KEY_RIGHTALT': #  
              os.system('xdotool key Alt_R && xdotool key Return')
          if key.keycode == 'KEY_K': #  close window
              os.system('xdotool key W')
          if key.keycode == 'KEY_RIGHTSHIFT': #  
              os.system('xdotool key Alt_R+Left')
          if key.keycode == 'KEY_RIGHTSHIFT': #  
              os.system('xdotool key Alt_R+Left')
          if key.keycode == 'KEY_SPACE': #  
              os.system('xdotool click 1')
          if key.keycode == 'KEY_M': #  
              os.system('xdotool click 3')

