
from tumulus.tags import HTMLTags as t

def plug(label, group, plug):
    return t.form(
            label,
            t.input(name='plug', value=plug, type='hidden'),
            t.input(name='group', value=group, type='hidden'),
            t.input(name='action', value='on', type='submit'),
            t.input(name='action', value='off', type='submit'),
            method='POST',
            action='/api/switch',
        )

def mpd(action):
     return t.form(
            t.input(name='action', value=action, type='hidden'),
            t.input(value=action, type='submit'),
            method='POST',
            action='/api/mpd',
        )

