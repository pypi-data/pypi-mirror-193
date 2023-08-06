# vim: set fileencoding=utf-8:


from coronado import TripleObject
from coronado import __VERSION__
from coronado.auth import Auth
from coronado.baseobjects import BASE_HEALTHCHECK_DICT
from coronado.config import loadConfig

import json
import logging


# +++ constants +++

SERVICE_PATH = 'partner/healthcheck'


# --- globals ---

log = logging.getLogger(__name__)


# +++ implementation +++

class HealthMonitor(TripleObject):
    """
    Health monitor reports if the API service is healthy and operational.

    Returns
    -------
        TripleObject
    A Triple object with these attributes set:

    - `APIVersion`
    - `build`
    - `coronadoVersion`


    Raises
    ------
        CoronadoError
    A CoronadoError dependent on the specific error condition.  The full list of
    possible errors, causes, and semantics is available in the
    **`coronado.exceptions`** module.
    """
    requiredAttributes = [ 'APIVersion', 'build', ]
    allAttributes = TripleObject(BASE_HEALTHCHECK_DICT).listAttributes()

    def __init__(self):
        TripleObject.__init__(self, None)


    @classmethod
    def check(klass) -> object:
        response = super().list()

        healthCheck = TripleObject(json.loads(response.content))
        healthCheck.coronadoVersion = __VERSION__
        return healthCheck


# --- functions ---

def main(unitTest : bool = False) -> dict:
    """
    Check the Triple API service health by reporting the API version, build ID,
    and other information relevant to implementers.

    This function is the main entry point for a script that will be installed to
    `/usr/local/bin/triplchk` or equivalent depending on whether the Coronado
    package was installed in the system wide Python configuraiton or in a
    virtual environment.

    See:  `man 5 coronado` for details.

    Arguments
    ---------
        unitTest
    Set it to True for running it in a unit test.

    Returns
    -------
        dict
    `None` if running standalone, or a dictionary with information useful to
    API developers if running a unit test.
    """
    _config = loadConfig()
    _auth = Auth(_config['tokenURL'], clientID = _config['clientID'], clientSecret = _config['secret'])

    HealthMonitor.initialize(_config['serviceURL'], SERVICE_PATH, _auth)
    check = HealthMonitor.check()

    info = _config['serviceURL']
    print(info)
    log.info(info)
    info = 'Triple API version = %s, build = %s; Coronado version = %s' % (check.APIVersion, check.build, check.coronadoVersion)
    print(info)
    log.info(info)

    if unitTest:
        return check.__dict__

