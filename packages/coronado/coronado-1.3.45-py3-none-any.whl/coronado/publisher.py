from coronado import TripleObject
from coronado.address import Address
from coronado.address import MOCK_ADDRESS
from coronado.baseobjects import BASE_PUBLISHER_DICT
from coronado.strictaddress import StrictAddress

import json
import uuid

import requests


# +++ constants +++

SERVICE_PATH = 'partner/publishers'
"""
The default service path associated with Publisher operations.

Usage:

```
Publisher.initialize(serviceURL, SERVICE_PATH, auth)
```

Users are welcome to initialize the class' service path from regular strings.
This constant is defined for convenience.
"""


# *** classes and objects ***

class Publisher(TripleObject):
    """
    Publisher objects are used for managing portfolios of publishers.  Partners
    who manage card programs for multiple publishers may wish to organize them
    into portfolios.  Portfolios allow offer exclusions which may be applied
    across multiple publishers without having to add individual publishers to
    an offer exclusion.
    """

    requiredAttributes = [
        'address',
        'assumedName',
        'createdAt',
        'updatedAt',
    ]
    allAttributes = TripleObject(BASE_PUBLISHER_DICT).listAttributes()


    def __init__(self, obj = BASE_PUBLISHER_DICT):
        """
        Create a new instance of a publisher.  `obj` must correspond to a
        valid, existing object ID if it's not a collection or JSON.

        Arguments
        ---------
            obj
        An object used for building a valid publisher.  The object can
        be one of:

        - A dictionary - a dictionary with instantiation values as described
          in the API documentation
        - A JSON string
        - A Triple objectID

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        TripleObject.__init__(self, obj)


    @classmethod
    def create(klass, assumedName: str, extPublisherID: str, address: str, revenueShare:float = 0.0) -> object:
        """
        For full details see `coronado.TripleObject.create()`.

        Arguments
        ---------
            assumedName
        Assumed legal name of the publisher.

            extPublisherID
        Partner provided external publisher ID.

        External IDs are assumed to be stable and never **sensitive**.  External
        IDs need not be unique across publishers, but we encourage the use of
        UUIDs whenever possible.

        External publisher IDs may not match the nnn-nn-nnnn format of US tax
        IDs to prevent accidental inclusion of sensitive information.

            address
        An instance of `coronado.address.Address` initialized to the merchant's
        physical address

            revenueShare
        The percentage-based revenue share of the publisher.

        Returns
        -------
        An instance of `Publisher`.

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """

        StrictAddress(address).validate()

        spec = {
            'address': address,
            'assumed_name': assumedName,
            'external_id': extPublisherID,
            'revenue_share': revenueShare,
        }
        return Publisher(super().create(spec))


    @classmethod
    def list(klass : object, paramMap = None, **args) -> list:
        """
        Return a list of publishers.

        Returns
        -------
            list
        A list of Publisher objects
        """
        paramMap = {
            'extPublisherID': 'publisher_external_id',
        }

        response = super().list(paramMap, **args)
        result = [ TripleObject(obj) for obj in json.loads(response.content)['publishers'] ]

        return result


    @classmethod
    def byID(klass, objID: str) -> object:
        result = super().byID(objID)

        if result:
            result.address = Address(result.address)

        return result


# +++ test support functions +++

def generateMockPublisher():
    """
    Generates a mock `coronado.publisher.Publisher` instance used for testing or
    whenever a bogus object is required.  In general, only used by unit tests
    suite.

    Returns
    -------
    An instance of `coronado.publisher.Publisher` populated with synthetic data.

    **IMPORTANT** - The address is in spec, snake_case dictionary form!
    """
    addressNoComplete = MOCK_ADDRESS.asSnakeCaseDictionary()
    del addressNoComplete['complete']
    return {  # sn ::= snake case
        'address': addressNoComplete,
        'assumed_name': 'R2D2 Enterprises %s' % uuid.uuid4().hex,
        'external_id': uuid.uuid4().hex[-12:],
        'revenue_share': 1.5,
    }


def findOrGenerateMockPublisher():
    """
    Finds or generates a new publisher - used for unit testing.

    Returns
    -------
    An instance of `coronado.publisher.Publisher`
    """
    for publisher in Publisher.list():
        return publisher

    return generateMockPublisher()

