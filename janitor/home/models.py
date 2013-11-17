from django.db import models
from django.core.exceptions import ValidationError

def validate_RF433(value):
    if len(value) != 5:
        raise ValidationError('{} must be of length 5'.format(value))
    if value.count('0') + value.count('1') != len(value):
        raise ValidationError('{} contains invalid chars'.format(value))

class Switch(models.Model):
    '''
    Controls a binary switch.
    '''
    status = models.BooleanField()
    force = models.BooleanField('Enforce the status on regular intervals.')

    class Meta:
        abstract = True


class RF433Switch(Switch):
    '''
    Controls RF 433 MHz switches.
    '''
    group = models.CharField(max_length=5)
    plug = models.CharField(max_length=5)