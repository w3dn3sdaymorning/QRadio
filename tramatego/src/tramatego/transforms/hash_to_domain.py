#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import Phrase, Domain
from common.launchers import get_qradio_data


__author__ = 'Zappus'
__copyright__ = 'Copyright 2016, TramaTego Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Zappus'
__email__ = 'zappus@protonmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
    #'onterminate' # comment out this line if you don't need this function.
]


#@superuser
@configure(
    label='Hash to Domain',
    description='Converts Hash into Domain using QRadio.',
    uuids=[ 'TramaTego.v1.HashToDomain' ],
    inputs=[ ( 'TramaTego', Phrase ) ],
    debug=True
)
def dotransform(request, response, config):
    command = "--hash_to_domain " + request.value
    qradio_output = get_qradio_data(command, 0)
    for entry in qradio_output:
        response += Domain(entry)
    return response


def onterminate():
    """
    TODO: Write your cleanup logic below or delete the onterminate function and remove it from the __all__ variable
    """
    pass