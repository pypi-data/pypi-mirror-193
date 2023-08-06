"""
Coronado - a Python API wrapper for the <a href='https://api.tripleup.dev/docs' target='_blank'>Triple services API</a>.

<a href='https://github.com/coronado-fi/coronado/blob/dev/resources/classes.png?raw=true' target='_blank'>
    <img src='https://github.com/coronado-fi/coronado/blob/dev/resources/classes.png?raw=true' width='600' alt='click to view full image'>
</a>
"""


from copy import deepcopy

from coronado.exceptions import CallError
from coronado.exceptions import UnexpectedError
from coronado.exceptions import errorFor
from coronado.tools import tripleKeysToCamelCase

import json
import enum

import requests


# *** constants ***

__VERSION__ = '1.3.47'

API_URL = 'https://api.sandbox.tripleup.dev'
CORONADO_USER_AGENT = 'python-coronado/%s' % __VERSION__


# --- globals ---

# log = logging.getLogger(__name__)


# +++ classes and objects +++

class TripleEnum(enum.Enum):
    """
    TripleEnum extends the standard Enum class to add support
    for pretty printing of the instance's value by overloading
    the `__str__()` method.  It's a convenience class.
    """
    def __str__(self) -> str:
        return str(self.value)


class TripleObject(object):
    """
    Abstract class ancestor to all the Triple API objects.
    """
    # +++ class variables ++

    _auth = None
    _servicePath = None
    _serviceURL = None

    requiredAttributes = None
    """
    A list or tuple of the minimum attribute names that are required to be
    present in the JSON or `dict` object during object construction.  See the
    `assertAll()` method.

    **NB:** The attribute names *must* be in camelCase; these refer to the
    object's internal attributes, not the snake_case initialization payload
    in JSON or a `dict`.
    """

    allAttributes = 'UNDEFINED - set allAttributes = ClassName(BASE_OBJ_SPEC)'
    """
    **All instance attributes.**

    The number of all attributes >= number of
    required attributes.  Some of the instance attributes are computed or
    constructed during object creation and persistence, or during object
    instantiation.
    """


    # --- private ---

    def _listProperties(self):
        classAttributes = type(self).__dict__
        properties = dict()

        for k in classAttributes.keys():
            if classAttributes[k].__class__ == property:
                properties['%s' % k] = '@property'

        return properties


    # +++ public +++

    def __init__(self, obj = None):
        """
        Create a new instance of a Triple object.  `obj` must correspond to a
        valid, existing object ID if it's not a collection or JSON.  The
        constructor only returns a valid object if a subclass is instantiated;
        TripleObject is an abstract class, and passing it an object ID will
        raise an error.

        Arguments
        ---------
            obj
        An object used for building a valid Triple object.  The object can
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
        if isinstance(obj, str):
            if '{' in obj:
                d = json.loads(obj)
            else:
                try:
                    d = self.__class__.byID(obj).__dict__
                except Exception:  # Python, triple, or Coronado exceptions can happen here; unsure of how it'll blow up
                    raise CallError('obj initializer is set to None or an invalid value type; obj = %s ' % obj)
        elif isinstance(obj, dict):
            d = deepcopy(obj)
        elif isinstance(obj, TripleObject):
            d = deepcopy(obj.__dict__)
        else:
            raise CallError('Invalid constructor obj type; it must be a string, a JSON payload, a dictionary, or a TripleObject')

        d = tripleKeysToCamelCase(d)

        for key, value in d.items():
            if isinstance(value, (list, tuple)):
                setattr(self, key, [TripleObject(x) if isinstance(x, dict) else x for x in value])
            else:
                setattr(self, key, TripleObject(value) if isinstance(value, dict) else value)

        self.assertAll()


    def assertAll(self) -> bool:
        """
        Asserts that all the attributes listed in the `requiredAttributes` list
        of attribute names are presein the final object.  Coronado/triple
        objects are built from JSON inputs which may or may not include all
        required attributes.  This method ensures they do.

        Returns
        -------
            True if all required attributes are present during initialization

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        if self.__class__.requiredAttributes:
            attributes = self.__dict__.keys()
            if not all(attribute in attributes for attribute in self.__class__.requiredAttributes):
                missing = set(self.__class__.requiredAttributes)-set(attributes)
                raise CallError("attribute%s %s missing during instantiation" % ('' if len(missing) == 1 else 's', missing))


    def listAttributes(self) -> dict:
        """
        Lists all the attributes and their type of the receiving object in the form:

            attrName : type

        Returns
        -------
            dict
        A dictionary of objects and types
        """
        keys = self.__dict__.keys()
        d = dict([ (key, str(type(self.__dict__[key])).replace('class ', '').replace("'", "").replace('<','').replace('>', '')) for key in keys ])
        for k, v in self._listProperties().items():
            d[k] = v

        result = dict([ (k, d[k]) for k in sorted(d.keys()) if k[0] != '_' ])

        return result


    def asDict(self) -> dict:
        """
        Returns the receiver as a Python dictionary.  The dictionary is a deep
        copy of the receiver's contents, so it can be manipulated without
        affecting the original object.

        Returns
        -------
            aDictionary
        A dictionary mapping of attributes and their states.
        """
        result = deepcopy(self.__dict__)
        # TODO:  If this method proves to be popular/useful, implement recursion
        #        for embedded TripleObject instances.

        return result


    @classmethod
    def list(klass : object, paramMap = None, **args) -> list:
        """
        Return a list of tripleObjects.  The list is a sequential query from the
        beginning of time if no query parameters are passed:

        Arguments
        ---------
            See concrete class implementations for specific arguments for each
            use case.

        Returns
        -------
            list
        A list of TripleObjects
        """
        params = None
        if paramMap:
            params = dict([ (paramMap[k], str(v)) for k, v in args.items() ])

        endpoint = '/'.join([ klass._serviceURL, klass._servicePath ])
        response = requests.request('GET', endpoint, headers = klass.headers, params = params)

        if response.status_code != 200:
            raise UnexpectedError('%s - %s on endpoint = %s' % (response.status_code, response.text, endpoint))

        return response


    def inSnakeCaseJSON(self) -> str:
        """
        Return a JSON representation of the receiver with the attributes
        written in snake_case format.

        Return
        ------
            string
        A string with a JSON representation of the receiver.

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        return json.dumps(self.asSnakeCaseDictionary())


    def asSnakeCaseDictionary(self) -> dict:
        """
        Return a dict representation of the receiver with the attributes
        written in snake_case format.

        Return
        ------
            dict
        A dictionary representation of the receiver.

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.

        Typical implementation (from a TripleObject specialization that
        represents an address-like object):

        ```
        result = {
            'complete_address': self.complete,
            'country_code': self.countryCode,
            'latitude': self.latitude,
            'line_1': self.line1,
            'line_2': self.line2,
            'locality': self.locality,
            'longitude': self.longitude,
            'postal_code': self.postalCode,
            'province': self.province,
        }

        return result
        ```
        """
        raise NotImplementedError('subclasses must implement this if required')


    def __str__(self) -> str:
        """
        Creates a human-readable string representation of the receiver.

        Returns
        -------
            str
        A human-readable string representation of the receiver.
        """
        result = ''
        keys = sorted(self.__dict__.keys())
        longest = max((len(k) for k in keys))
        formatTrunc = '%%-%ds: %%s... <snip>' % longest
        formatFull = '%%-%ds: %%s' % longest

        truncValue = 60
        for k in keys:
            v = self.__dict__[k]
            if 'secret' in k.lower():
                result = '\n'.join([ result, formatTrunc % (k, v[:8]), ])
                continue
            if isinstance(v, str) and len(v) > truncValue:
                result = '\n'.join([ result, formatTrunc % (k, v[:truncValue]), ])
            else:
                result = '\n'.join([ result, formatFull % (k, v), ])

        return result


    def isComplete(self) -> bool:
        """
        Checks that the current instance implements all the attributes defined
        in the Triple API complete object.

        Returns
        -------
        `True` if all attributes match the spec.

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        return all(attribute in self.__dict__.keys() for attribute in self.__class__.allAttributes.keys())


    def extraneousAttributes(self) -> set:
        """
        Generates a list of attributes found in the receiver that are not listed
        as required or general attributes, i.e. that weren't defined in the
        `coronado.baseobjects` module.  This indicates a change in the triple
        API that is not reflected in the Coronado objects.

        Returns
        -------
        `None` if the object is complete and has no extraneous attributes.  A
        list of extraneous attribute names if it's in error.

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        return set(self.__dict__.keys())-set(self.__class__.allAttributes.keys())


    def isCongruent(self) -> bool:
        """
        Validates that the receiver matches the TripleObject subclass specialization
        and matches the known BASEOBJECT and Triple API specification.

        Returns
        -------
        `True` if the object is congruent with `BASEOBJECTs` and the Triple API
        specification.
        """
        valid = self.isComplete() and not self.extraneousAttributes()
        if not valid:
            message = """
%s is complete = %s
Extraneous attributes = %s
Expected attributes = %s """ % (self.__class__, self.isComplete(), self.extraneousAttributes(), self.__class__.allAttributes)
            raise errorFor(422, info = message)

        return valid


    @classmethod
    def initialize(klass, serviceURL : str, servicePath : str, auth : object):
        """
        Initialize the class to use an appropriate service URL or authentication
        object.

        Arguments
        ---------
            serviceURL
        A string with an https locator pointing at the service top level URL

            servicePath
        A string with the service path part of the URL

            auth
        An instance of Auth configured to use the the serviceURL within the
        defined scope
        """
        klass._servicePath = servicePath.strip('/')
        klass._auth = auth
        klass._serviceURL = serviceURL


    @classmethod
    @property
    def headers(klass):
        return {
            'Authorization': ' '.join([ klass._auth.tokenType, klass._auth.token, ]),
            'User-Agent': CORONADO_USER_AGENT,
        }

    @classmethod
    @property
    def headersImpersonation(klass):
        #TODO: this is hard-coding the impersonation header to drop pre-defined PartnerNames
        # used in merchant.update_status
        return {
            'Authorization': ' '.join([ klass._auth.tokenType, klass._auth.token, ]),
            'User-Agent': CORONADO_USER_AGENT,
            'x-assume-partner': '{"publisher": ""}'
        }


    @classmethod
    def create(klass, spec : dict) -> object:
        """
        Create a new TripleObject object resource from a JSON spec.  The JSON
        keys become the new Python TripleObject properties.

        spec example:

        ```javascript
        {
          "address": {
            "country_code": "US",
            "country_subdivision_code": "CA",
            "latitude": 0,
            "city": "San Francisco",
            "longitude": 0,
            "postal_code": "94118",
            "street_address": "2801 Turk Boulevard\\\\nSuite 202"
          },
          "assumed_name": "R2D2 Enterprises dd3f2ceff5b34fe8b6c9b0b5afbe479f",
          "external_id": "b1638e46d720",
          "revenue_share": 1.5
        }
        ```

        Conceptual example of how to turn it into a Triple object:

        ```python
        Publisher.initialize(serviceURL, servicePath, auth)

        with open("publisher.txt", "r") as dataSource: # some JSON source
            # Get the JSON data and load it in memory as a dict:
            publisherSpec = json.loads(dataSource.read())

        assert isinstance(publisherSpec, dict)

        publisher = Publisher(publisherSpec)

        assert isinstance(publisher, TripleObject) # yes
        assert isinstance(publisher, Publisher) # Publisher is a subclass of TripeObject

        print(publisher.objID)
        print(publisher.assumedName)
        print(publisher.address.city)
        ```

        Arguments
        ---------
            spec : dict
        A dictionary with the required fields to create a new tripleObject
        object.


        Returns
        -------
            aTripleObject
        An instance of TripleObject with a valid objID

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        if klass == TripleObject:
            # Don't allow this in the abstract ancestor
            raise errorFor(501, 'TripleObject cannot be created in the service')

        if not spec:
            raise errorFor(400, 'spec was empty or None')

        endpoint = '/'.join([klass._serviceURL, klass._servicePath ]) # URL fix later
        response = requests.request('POST', endpoint, headers = klass.headers, json = spec)

        if response.status_code == 201:
            tripleObject = klass(response.text)
        else:
            raise errorFor(response.status_code, info = response.text)

        return tripleObject


    @classmethod
    def byID(klass, objID : str) -> object:
        """
        Return the tripleObject associated with objID.

        Arguments
        ---------
            objID : str
        The tripleObject ID associated with the resource to fetch

        Returns
        -------
            aTripleObject
        The TripleObject object associated with objID or None

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        endpoint = '/'.join([klass._serviceURL, '%s/%s' % (klass._servicePath, objID)]) # URL fix later
        response = requests.request('GET', endpoint, headers = klass.headers)

        if response.status_code == 200:
            result = klass(response.content.decode())
        elif response.status_code == 404:
            result = None
        else:
            raise errorFor(response.status_code, info = response.text)

        return result


    @classmethod
    def updateWith(klass, objID : str, spec : dict) -> object:
        """
        Update the receiver with new values for the attributes set in spec.

        spec:

        ```
        spec = {
        }
        ```

        Arguments
        ---------
            objID : str
        The TripleObject ID to update

            spec : dict
        A dict object with the appropriate object references:

        - assumed_name
        - address

        The address should be generated using a Coronado Address object and
        then calling its asSnakeCaseDictionary() method

        Returns
        -------
            aTripleObject
        An updated instance of the TripleObject associated with objID, or None
        if the objID isn't associated with an existing resource.

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        endpoint = '/'.join([klass._serviceURL, '%s/%s' % (klass._servicePath, objID)]) # URL fix later
        response = requests.request('PATCH', endpoint, headers = klass.headers, json = spec)

        if response.status_code == 200:
            result = klass(response.content.decode())
        elif response.status_code == 404:
            result = None
        else:
            raise errorFor(response.status_code, info = response.text)

        return result


    @classmethod
    def list(klass : object, paramMap = None, **args) -> list:
        """
        Return a list of tripleObjects.  The list is a sequential query from the
        beginning of time if no query parameters are passed:

        Arguments
        ---------
            See concrete class implementations for specific arguments for each
            use case.

        Returns
        -------
            list
        A list of TripleObjects

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        params = None
        if paramMap:
            params = dict([ (paramMap[k], v) for k, v in args.items() ])

        endpoint = '/'.join([ klass._serviceURL, klass._servicePath ])
        response = requests.request('GET', endpoint, headers = klass.headers, params = params)

        if response.status_code not in range(200, 299):
            raise errorFor(response.status_code, response.text)

        return response

    @classmethod
    def delete(klass, objID : str) -> object:
        """
        Delete the tripleObject associated with objID.

        Arguments
        ---------
            objID : str
        The tripleObject ID associated with the resource to delete

        Returns
        -------
            msg: `The resource was deleted successfully`

        Raises
        ------
            CoronadoError
        A CoronadoError dependent on the specific error condition.  The full list of
        possible errors, causes, and semantics is available in the
        **`coronado.exceptions`** module.
        """
        endpoint = '/'.join([klass._serviceURL, '%s/%s' % (klass._servicePath, objID)])
        response = requests.request('DELETE', endpoint, headers = klass.headers)

        if response.status_code == 204:
            result = 'The resource was deleted successfully.'
        elif response.status_code == 404:
            result = 'The resource could not be found.'
        else:
            raise errorFor(response.status_code, info = response.text)

        return result

