#!/usr/bin/env python3

#
# NOSA HEADER START
#
# The contents of this file are subject to the terms of the NASA Open
# Source Agreement (NOSA), Version 1.3 only (the "Agreement").  You may
# not use this file except in compliance with the Agreement.
#
# You can obtain a copy of the agreement at
#   docs/NASA_Open_Source_Agreement_1.3.txt
# or
#   https://heliophysicsdata.gsfc.nasa.gov/WebServices/NASA_Open_Source_Agreement_1.3.txt.
#
# See the Agreement for the specific language governing permissions
# and limitations under the Agreement.
#
# When distributing Covered Code, include this NOSA HEADER in each
# file and include the Agreement file at
# docs/NASA_Open_Source_Agreement_1.3.txt.  If applicable, add the
# following below this NOSA HEADER, with the fields enclosed by
# brackets "[]" replaced with your own identifying information:
# Portions Copyright [yyyy] [name of copyright owner]
#
# NOSA HEADER END
#
# Copyright (c) 2023 United States Government as represented by
# the National Aeronautics and Space Administration. No copyright is
# claimed in the United States under Title 17, U.S.Code. All Other
# Rights Reserved.
#

"""
Example Heliophysics Data Portal (HDP) web services client.
https://heliophysicsdata.gsfc.nasa.gov/WebServices/.

Copyright &copy; 2023 United States Government as represented by the
National Aeronautics and Space Administration. No copyright is claimed in
the United States under Title 17, U.S.Code. All Other Rights Reserved.
"""

import sys
import getopt
import json
import xml.etree.ElementTree as ET
import logging
import logging.config
from typing import Dict, List
import urllib3


from hdpws.hdpws import HdpWs


logging.basicConfig()
LOGGING_CONFIG_FILE = 'logging_config.json'
try:
    with open(LOGGING_CONFIG_FILE, 'r') as fd:
        logging.config.dictConfig(json.load(fd))
except BaseException as exc:    # pylint: disable=broad-except
    if not isinstance(exc, FileNotFoundError):
        print('Logging configuration failed')
        print('Exception: ', exc)
        print('Ignoring failure')
        print()


#ENDPOINT = "https://heliophysicsdata.gsfc.nasa.gov/WS/hdp/1/"
#ENDPOINT = "http://heliophysicsdata-dev.sci.gsfc.nasa.gov/WS/hdp/1/"
ENDPOINT = "http://localhost:8100/exist/restxq/"
#CA_CERTS = '/etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt'


def print_usage(
        name: str
    ) -> None:
    """
    Prints program usage information to stdout.

    Parameters
    ----------
    name
        name of this program

    Returns
    -------
    None
    """
    print('USAGE: {name} [-e url][-d][-c cacerts][-h]'.format(name=name))
    print('WHERE: url = HDP web service endpoint URL')
    print('       -d disables TLS server certificate validation')
    print('       cacerts = CA certificate filename')


# pylint: disable=too-many-locals,too-many-branches,too-many-statements
def example(
        argv: List[str]
    ) -> None:
    """
    Example Heliophysics Data Portal (HDP) web service client.
    Includes example calls to most of the web services.

    Parameters
    ----------
    argv
        Command-line arguments.<br>
        -e url or --endpoint=url where url is the cdas web service endpoint
            URL to use.<br>
        -c url or --cacerts=filename where filename is the name of the file
            containing the CA certificates to use.<br>
        -d or --disable-cert-check to disable verification of the server's
            certificate
        -h or --help prints help information.
    """

    try:
        opts = getopt.getopt(argv[1:], 'he:c:d',
                             ['help', 'endpoint=', 'cacerts=',
                              'disable-cert-check'])[0]
    except getopt.GetoptError:
        print('ERROR: invalid option')
        print_usage(argv[0])
        sys.exit(2)

    endpoint = ENDPOINT
    ca_certs = None
    disable_ssl_certificate_validation = False

    for opt, arg in opts:
        if opt in ('-e', '--endpoint'):
            endpoint = arg
        elif opt in ('-c', '--cacerts'):
            ca_certs = arg
        elif opt in ('-d', '--disable-cert-check'):
            disable_ssl_certificate_validation = True
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        elif opt in ('-h', '--help'):
            print_usage(argv[0])
            sys.exit()

    hdp = HdpWs(endpoint=endpoint, ca_certs=ca_certs,
                disable_ssl_certificate_validation=
                disable_ssl_certificate_validation, user_agent='Example')

    result = hdp.get_instrument_ids()
    if result['HttpStatus'] == 200:
        print('HDP InstrumentIDs:')
        for value in result['InstrumentID'][0:9]:
            print('    {:s}'.format(value))
    else:
        print('hdp.get_instrument_ids failed with status = ',
              result['HttpStatus'])
        if 'ErrorMessage' in result:
            print('ErrorMessage = ', result['ErrorMessage'])
            print('ErrorDescription = ', result['ErrorDescription'])
        else:
            print('HttpText = ', result['ErrorText'])

    result = hdp.get_repository_ids()
    if result['HttpStatus'] == 200:
        print('HDP RepositoryIDs:')
        for value in result['RepositoryID'][0:9]:
            print('    {:s}'.format(value))
    else:
        print('hdp.get_repository_ids failed with status = ',
              result['HttpStatus'])
        if 'ErrorMessage' in result:
            print('ErrorMessage = ', result['ErrorMessage'])
            print('ErrorDescription = ', result['ErrorDescription'])
        else:
            print('HttpText = ', result['ErrorText'])


    result = hdp.get_measurement_types()
    if result['HttpStatus'] == 200:
        print('HDP MeasurementTypes:')
        for value in result['MeasurementType']:
            print('    {:s}'.format(value))
    else:
        print('hdp.get_measurement_types failed with status = ',
              result['HttpStatus'])
        if 'ErrorMessage' in result:
            print('ErrorMessage = ', result['ErrorMessage'])
            print('ErrorDescription = ', result['ErrorDescription'])
        else:
            print('HttpText = ', result['ErrorText'])


    result = hdp.get_spectral_ranges()
    if result['HttpStatus'] == 200:
        print('HDP SpectralRanges:')
        for value in result['SpectralRange']:
            print('    {:s}'.format(value))
    else:
        print('hdp.get_spectral_ranges failed with status = ',
              result['HttpStatus'])
        if 'ErrorMessage' in result:
            print('ErrorMessage = ', result['ErrorMessage'])
            print('ErrorDescription = ', result['ErrorDescription'])
        else:
            print('HttpText = ', result['ErrorText'])


    result = hdp.get_observatory_group_ids()
    if result['HttpStatus'] == 200:
        print('HDP ObservatoryGroupIDs:')
        for value in result['ObservatoryGroupID'][0:9]:
            print('    {:s}'.format(value))
    else:
        print('hdp.get_observatory_group_ids failed with status = ',
              result['HttpStatus'])
        if 'ErrorMessage' in result:
            print('ErrorMessage = ', result['ErrorMessage'])
            print('ErrorDescription = ', result['ErrorDescription'])
        else:
            print('HttpText = ', result['ErrorText'])


    result = hdp.get_observatory_ids()
    if result['HttpStatus'] == 200:
        print('HDP ObservatoryIDs:')
        for value in result['ObservatoryID'][0:9]:
            print('    {:s}'.format(value))
    else:
        print('hdp.get_observatory_ids failed with status = ',
              result['HttpStatus'])
        if 'ErrorMessage' in result:
            print('ErrorMessage = ', result['ErrorMessage'])
            print('ErrorDescription = ', result['ErrorDescription'])
        else:
            print('HttpText = ', result['ErrorText'])





if __name__ == '__main__':
    example(sys.argv)
