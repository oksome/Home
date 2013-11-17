# Copyright (c) 2013 "OKso http://okso.me"
#
# This file is part of Home.
#
# Home is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.core.exceptions import ValidationError

from .endpoint import send_home


def validate_RF433(value):
    if len(value) != 5:
        raise ValidationError('{} must be of length 5'.format(value))
    if value.count('0') + value.count('1') != len(value):
        raise ValidationError('{} contains invalid chars'.format(value))


class Minion(models.Model):
    '''
    A Minion is a network endnode, connected to some input/output gadgets.
    '''
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class Gadget(models.Model):
    '''
    Common ancestor to all sensors and actuators.
    '''
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=2048, null=True, blank=True)

    class Meta:
        abstract = True


class Switch(Gadget):
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

    def turn(self, mode):
        "Turn 'on' or 'off'."

        topic = 'do:arduino.switch'

        msg = {'origin': 'janitor',
               'group': self.group,
               'plug': self.plug,
               'action': mode,
               }

        send_home(topic, msg)

    def on(self):
        self.turn('on')

    def off(self):
        self.turn('off')

    def __str__(self):
        return self.name