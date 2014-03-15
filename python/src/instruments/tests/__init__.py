#!/usr/bin/python
# -*- coding: utf-8 -*-
##
# __init__.py: Package for InstrumentKit unit tests.
##
# © 2013 Steven Casagrande (scasagrande@galvant.ca).
#
# This file is a part of the InstrumentKit project.
# Licensed under the AGPL version 3.
##
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##

## IMPORTS ####################################################################

import contextlib
import cStringIO as StringIO

## FUNCTIONS ##################################################################

@contextlib.contextmanager
def expected_protocol(ins_class, host_to_ins, ins_to_host):
    stdin = StringIO.StringIO(ins_to_host)
    stdout = StringIO.StringIO()
    
    yield ins_class.open_test(stdin, stdout)
    
    assert stdout.getvalue() == host_to_ins, \
"""Expected:

{}

Got:

{}""".format(repr(host_to_ins), repr(stdout.getvalue()))
    
