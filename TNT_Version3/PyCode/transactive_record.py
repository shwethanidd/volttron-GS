# -*- coding: utf-8 -*- {{{
# vim: set fenc=utf-8 ft=python sw=4 ts=4 sts=4 et:

# Copyright (c) 2017, Battelle Memorial Institute
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation
# are those of the authors and should not be interpreted as representing
# official policies, either expressed or implied, of the FreeBSD
# Project.
#
# This material was prepared as an account of work sponsored by an
# agency of the United States Government.  Neither the United States
# Government nor the United States Department of Energy, nor Battelle,
# nor any of their employees, nor any jurisdiction or organization that
# has cooperated in the development of these materials, makes any
# warranty, express or implied, or assumes any legal liability or
# responsibility for the accuracy, completeness, or usefulness or any
# information, apparatus, product, software, or process disclosed, or
# represents that its use would not infringe privately owned rights.
#
# Reference herein to any specific commercial product, process, or
# service by trade name, trademark, manufacturer, or otherwise does not
# necessarily constitute or imply its endorsement, recommendation, or
# favoring by the United States Government or any agency thereof, or
# Battelle Memorial Institute. The views and opinions of authors
# expressed herein do not necessarily state or reflect those of the
# United States Government or any agency thereof.
#
# PACIFIC NORTHWEST NATIONAL LABORATORY
# operated by BATTELLE for the UNITED STATES DEPARTMENT OF ENERGY
# under Contract DE-AC05-76RL01830

# }}}


from datetime import datetime

from .time_interval import TimeInterval
from .helpers import format_ts


class TransactiveRecord:
    def __init__(self,
                 time_interval,
                 record=0,
                 marginal_price=0,
                 power=0,
                 power_uncertainty=0.0,
                 cost=0.0,
                 reactive_power=0.0,
                 reactive_power_uncertainty=0.0,
                 voltage=0.0,
                 voltage_uncertainty=0.0):

        # These are the four normal arguments of the constructor. NOTE: Use the time interval ti text name, not a
        # TimeInterval object itself.
        if isinstance(time_interval, TimeInterval):

            # A TimeInterval object argument must be represented by its text name.
            self.timeInterval = time_interval.name

        else:

            # Argument ti is most likely received as a text string name. Further validation might be used to make sure
            # that ti is a valid name of an active time interval.
            self.timeInterval = str(time_interval)

        self.record = record                                # a record number (0 refers to the balance point)
        self.marginalPrice = marginal_price                 # marginal price [$/kWh]
        self.power = power                                  # power [avg.kW]
        # self.powerUncertainty = power_uncertainty  # relative [dimensionless]
        self.cost = cost                                    # ?
        # self.reactivePower = reactive_power  # [avg.kVAR]
        # self.reactivePowerUncertainty = reactive_power_uncertainty  # relative [dimensionless]
        # self.voltage = voltage  # [p.u.]
        # self.voltageUncertainty = voltage_uncertainty  # relative [dimensionless]

        # Finally, always append the timestamp that captures when the record is created.
        # TODO: Is this consistent with Timer() methods that are used with simulations?
        self.timeStamp = datetime.utcnow()
