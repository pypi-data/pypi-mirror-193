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
#   https://cdaweb.gsfc.nasa.gov/WebServices/NASA_Open_Source_Agreement_1.3.txt.
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
Module for accessing the Heliophysics Data Portal (HDP) web services
https://heliophysicsdata.gsfc.nasa.gov/WebServices/.
"""

import platform
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import time
import logging
from typing import Dict, List, Tuple, Union
import requests
import dateutil.parser

from hdpws import __version__, RETRY_LIMIT, ET_NS, ET_XHTML_NS
#from sscws.coordinates import CoordinateSystem, CoordinateComponent
#from sscws.outputoptions import CoordinateOptions, OutputOptions
#from sscws.request import DataRequest, QueryRequest, SatelliteSpecification
#from sscws.result import Result
#from sscws.timeinterval import TimeInterval



class HdpWs:
    """
    Class representing the web service interface to NASA's
    Heliophysics Data Portal (HDP) <https://heliophysicsdata.gsfc.nasa.gov/>.

    Parameters
    ----------
    endpoint
        URL of the HDP web service.  If None, the default is
        'https://heliophysicsdata.gsfc.nasa.gov/WS/hdp/1/'.
    timeout
        Number of seconds to wait for a response from the server.
    proxy
        HTTP proxy information.  For example,<pre>
        proxies = {
          'http': 'http://10.10.1.10:3128',
          'https': 'http://10.10.1.10:1080',
        }</pre>
        Proxy information can also be set with environment variables.
        For example,<pre>
        $ export HTTP_PROXY="http://10.10.1.10:3128"
        $ export HTTPS_PROXY="http://10.10.1.10:1080"</pre>
    ca_certs
        Path to certificate authority (CA) certificates that will
        override the default bundle.
    disable_ssl_certificate_validation
        Flag indicating whether to validate the SSL certificate.
    user_agent
        A value that is appended to the HTTP User-Agent values.

    Notes
    -----
    The logger used by this class has the class' name (HdpWs).  By default,
    it is configured with a NullHandler.  Users of this class may configure
    the logger to aid in diagnosing problems.

    This class is dependent upon xml.etree.ElementTree module which is
    vulnerable to an "exponential entity expansion" and "quadratic blowup
    entity expansion" XML attack.  However, this class only receives XML
    from the (trusted) HDP server so these attacks are not a threat.  See
    the xml.etree.ElementTree "XML vulnerabilities" documentation for
    more details
    <https://docs.python.org/3/library/xml.html#xml-vulnerabilities>.
    """
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-arguments
    def __init__(
            self,
            endpoint=None,
            timeout=None,
            proxy=None,
            ca_certs=None,
            disable_ssl_certificate_validation=False,
            user_agent=None):

        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.NullHandler())

        self.retry_after_time = None

        self.logger.debug('endpoint = %s', endpoint)
        self.logger.debug('ca_certs = %s', ca_certs)
        self.logger.debug('disable_ssl_certificate_validation = %s',
                          disable_ssl_certificate_validation)

        if endpoint is None:
            self._endpoint = 'https://heliophysicsdata.gsfc.nasa.gov/WS/hdp/1/'
        else:
            self._endpoint = endpoint

        self._user_agent = 'hdpws/' + __version__ + ' (' + \
            platform.python_implementation() + ' ' \
            + platform.python_version() + '; '+ platform.platform() + ')'

        if user_agent is not None:
            self._user_agent += ' (' + user_agent + ')'

        self._request_headers = {
            'Content-Type' : 'application/xml',
            'Accept' : 'application/xml',
            'User-Agent' : self._user_agent
        }
        self._session = requests.Session()
        #self._session.max_redirects = 0
        self._session.headers.update(self._request_headers)

        if ca_certs is not None:
            self._session.verify = ca_certs

        if disable_ssl_certificate_validation is True:
            self._session.verify = False

        if proxy is not None:
            self._proxy = proxy

        self._timeout = timeout

    # pylint: enable=too-many-arguments


    def __str__(self) -> str:
        """
        Produces a string representation of this object.

        Returns
        -------
        str
            A string representation of this object.
        """
        return 'HdpWs(endpoint=' + self._endpoint + ', timeout=' + \
               str(self._timeout) + ')'


    def __del__(self):
        """
        Destructor.  Closes all network connections.
        """

        self.close()


    def close(self) -> None:
        """
        Closes any persistent network connections.  Generally, deleting
        this object is sufficient and calling this method is unnecessary.
        """
        self._session.close()


    def get_instrument_ids(
            self
        ) -> Dict:
        """
        Gets all /Spase/Instrument/ResourceID values available at HDP.

        Returns
        -------
        Dict
            Dictionary ???
            with the addition of the following key/values:<br>
            - HttpStatus: with the value of the HTTP status code.
              Successful == 200.<br>
            When HttpStatus != 200:<br>
            - HttpText: containing a string representation of the HTTP
              entity body.<br>
            When HttpText is a standard HDP WS error entity body the
            following key/values (convenience to avoid parsing
            HttpStatus):<br>
            - ErrorMessage: value from HttpText.<br>
            - ErrorDescription: value from HttpText.<br>
        """
        return self.__get_simple_resource('Spase/Instrument/ResourceID',
                                          'ResourceID', 
                                          'InstrumentID')


    def get_repository_ids(
            self
        ) -> Dict:
        """
        Gets all /Spase/Repository/ResourceID values available at HDP.

        Returns
        -------
        Dict
            Dictionary ???
            with the addition of the following key/values:<br>
            - HttpStatus: with the value of the HTTP status code.
              Successful == 200.<br>
            When HttpStatus != 200:<br>
            - HttpText: containing a string representation of the HTTP
              entity body.<br>
            When HttpText is a standard HDP WS error entity body the
            following key/values (convenience to avoid parsing
            HttpStatus):<br>
            - ErrorMessage: value from HttpText.<br>
            - ErrorDescription: value from HttpText.<br>
        """
        return self.__get_simple_resource('Spase/Repository/ResourceID',
                                          'ResourceID', 
                                          'RepositoryID')


    def get_measurement_types(
            self
        ) -> Dict:
        """
        Gets all /Spase/MeasurementType values available at HDP.

        Returns
        -------
        Dict
            Dictionary ???
            with the addition of the following key/values:<br>
            - HttpStatus: with the value of the HTTP status code.
              Successful == 200.<br>
            When HttpStatus != 200:<br>
            - HttpText: containing a string representation of the HTTP
              entity body.<br>
            When HttpText is a standard HDP WS error entity body the
            following key/values (convenience to avoid parsing
            HttpStatus):<br>
            - ErrorMessage: value from HttpText.<br>
            - ErrorDescription: value from HttpText.<br>
        """
        return self.__get_simple_resource('Spase/MeasurementType',
                                          'MeasurementType', 
                                          'MeasurementType')


    def get_spectral_ranges(
            self
        ) -> Dict:
        """
        Gets all /Spase/SpectralRange values available at HDP.

        Returns
        -------
        Dict
            Dictionary ???
            with the addition of the following key/values:<br>
            - HttpStatus: with the value of the HTTP status code.
              Successful == 200.<br>
            When HttpStatus != 200:<br>
            - HttpText: containing a string representation of the HTTP
              entity body.<br>
            When HttpText is a standard HDP WS error entity body the
            following key/values (convenience to avoid parsing
            HttpStatus):<br>
            - ErrorMessage: value from HttpText.<br>
            - ErrorDescription: value from HttpText.<br>
        """
        return self.__get_simple_resource('Spase/SpectralRange',
                                          'SpectralRange', 'SpectralRange')


    def get_observatory_group_ids(
            self
        ) -> Dict:
        """
        Gets all /Spase/Observatory/ObservatoryGroupID values available at HDP.

        Returns
        -------
        Dict
            Dictionary ???
            with the addition of the following key/values:<br>
            - HttpStatus: with the value of the HTTP status code.
              Successful == 200.<br>
            When HttpStatus != 200:<br>
            - HttpText: containing a string representation of the HTTP
              entity body.<br>
            When HttpText is a standard HDP WS error entity body the
            following key/values (convenience to avoid parsing
            HttpStatus):<br>
            - ErrorMessage: value from HttpText.<br>
            - ErrorDescription: value from HttpText.<br>
        """
        return self.__get_simple_resource('Spase/Observatory/ObservatoryGroupID',
                                          'ObservatoryGroupID', 'ObservatoryGroupID')


    def get_observatory_ids(
            self
        ) -> Dict:
        """
        Gets all /Spase/Observatory/ResourceID values available at HDP.

        Returns
        -------
        Dict
            Dictionary ???
            with the addition of the following key/values:<br>
            - HttpStatus: with the value of the HTTP status code.
              Successful == 200.<br>
            When HttpStatus != 200:<br>
            - HttpText: containing a string representation of the HTTP
              entity body.<br>
            When HttpText is a standard HDP WS error entity body the
            following key/values (convenience to avoid parsing
            HttpStatus):<br>
            - ErrorMessage: value from HttpText.<br>
            - ErrorDescription: value from HttpText.<br>
        """
        return self.__get_simple_resource('Spase/Observatory/ResourceID',
                                          'ResourceID', 'ObservatoryID')


    def __get_simple_resource(
            self,
            resource: str,
            name: str,
            result_name: str
        ) -> Dict:
        """
        Gets all resource values available at HDP.

        Returns
        -------
        Dict
            Dictionary ???
            with the addition of the following key/values:<br>
            - HttpStatus: with the value of the HTTP status code.
              Successful == 200.<br>
            When HttpStatus != 200:<br>
            - HttpText: containing a string representation of the HTTP
              entity body.<br>
            When HttpText is a standard HDP WS error entity body the
            following key/values (convenience to avoid parsing
            HttpStatus):<br>
            - ErrorMessage: value from HttpText.<br>
            - ErrorDescription: value from HttpText.<br>
        """
        url = self._endpoint + resource

        self.logger.debug('request url = %s', url)

        response = self._session.get(url, timeout=self._timeout)

        status = self.__get_status(response)
        if response.status_code != 200:
            return status

        mt_response = ET.fromstring(response.text)

        result = {
            result_name: []
        }

        for value in mt_response.findall('.//' + ET_NS + name):

            result[result_name].append(value.text)

        result.update(status)
        return result




    @staticmethod
    def __get_status(
            response: requests.Response
        ) -> Dict:
        """
        Gets status information from the given response.  In particular,
        when status_code != 200, an attempt is made to extract the HDP WS
        ErrorMessage and ErrorDescription from the response.

        Parameters
        ----------
        response
            requests Response object.

        Returns
        -------
        Dict
            Dict containing the following:<br>
            - HttpStatus: the HTTP status code<br>
            additionally, when HttpStatus != 200<br>
            - ErrorText: a string representation of the entire entity
              body<br>
            - ErrorMessage: HDP WS ErrorMessage (when available)<br>
            - ErrorDescription: HDP WS ErrorDescription (when available)
        """
        http_result = {
            'HttpStatus': response.status_code
        }

        if response.status_code != 200:

            http_result['ErrorText'] = response.text
            try:
                error_element = ET.fromstring(response.text)
                http_result['ErrorMessage'] = error_element.findall(\
                    './/' + ET_XHTML_NS + 'p[@class="ErrorMessage"]/' +
                    ET_XHTML_NS + 'b')[0].tail
                http_result['ErrorDescription'] = error_element.findall(\
                    './/' + ET_XHTML_NS + 'p[@class="ErrorDescription"]/' +
                    ET_XHTML_NS + 'b')[0].tail
            except:
                pass  # ErrorText is the best we can do

        return http_result

