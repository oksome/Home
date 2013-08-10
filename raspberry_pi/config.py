#!/usr/bin/env python2

'''
    More complex configuration, to run in addition to 'config.sh'.
'''

if raw_input('Set USB sound card as default ? [y][N]') in 'y', 'Y', 'yes':
    original = open('/etc/modprobe.d/alsa-base.conf').read()
    modified = original.replace('options snd-usb-audio index=-2', 'options snd-usb-audio index=0')
    open('/etc/modprobe.d/alsa-base.conf', 'w').write(modified)
    print("Default sound card set to USB via '/etc/modprobe.d/alsa-base.conf'.")
