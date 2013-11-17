from django.db import models
from django.core.exceptions import ValidationError

def validate_RF433(value):
    if len(value) != 5:
        raise ValidationError('{} must be of length 5'.format(value))
    if value.count('0') + value.count('1') != len(value):
        raise ValidationError('{} contains invalid chars'.format(value))


class Minion(models.Model):
    '''
    Common ancestor to all sensors and actuators.
    '''
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=2048, null=True, blank=True)

    class Meta:
        abstract = True


class Switch(Minion):
    '''
    Controls a binary switch.
    '''
    status = models.BooleanField(default=False)
    force = models.BooleanField('Enforce the status on regular intervals.', 
                                default=False)

    class Meta:
        abstract = True


class RF433Switch(Switch):
    '''
    Controls RF 433 MHz switches.
    '''
    group = models.CharField(max_length=5, 
                             null=False,
                             blank=False,
                             validators=[validate_RF433])
    plug = models.CharField(max_length=5, 
                            null=False,
                            blank=False,
                            validators=[validate_RF433])