#!/usr/bin/env python2

'''
    More complex configuration, to run in addition to 'config.sh'.
'''

if raw_input('Set USB sound card as default ? [y][N]') in 'y', 'Y', 'yes':
    original = open('/etc/modprobe.d/alsa-base.conf').read()
    modified = original.replace('options snd-usb-audio index=-2', 'options snd-usb-audio index=0')
    open('/etc/modprobe.d/alsa-base.conf', 'w').write(modified)
    print("Default sound card set to USB via '/etc/modprobe.d/alsa-base.conf'.")
    
if raw_input('Keep crazy logs due to USB sound in /var/log/debug and kernel ? [y][N]') not in 'y', 'Y', 'yes':
    # Documentation from http://root42.blogspot.be/2013/04/delay-warnings-when-using-usb-audio-on.html
    open('/etc/modprobe.d/snd_usb_audio.conf', 'a').write('\noptions snd-usb-audio nrpacks=1\n')
    print("Anti-log option added.")
