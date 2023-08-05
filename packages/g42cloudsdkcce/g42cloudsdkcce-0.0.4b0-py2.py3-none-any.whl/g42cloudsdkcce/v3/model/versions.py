# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Versions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'input': 'object',
        'stable': 'bool',
        'translate': 'object',
        'support_versions': 'list[SupportVersions]',
        'creation_timestamp': 'date',
        'update_timestamp': 'date'
    }

    attribute_map = {
        'version': 'version',
        'input': 'input',
        'stable': 'stable',
        'translate': 'translate',
        'support_versions': 'supportVersions',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, version=None, input=None, stable=None, translate=None, support_versions=None, creation_timestamp=None, update_timestamp=None):
        """Versions

        The model defined in g42cloud sdk

        :param version: The param of the Versions
        :type version: str
        :param input: The param of the Versions
        :type input: object
        :param stable: The param of the Versions
        :type stable: bool
        :param translate: The param of the Versions
        :type translate: object
        :param support_versions: The param of the Versions
        :type support_versions: list[:class:`g42cloudsdkcce.v3.SupportVersions`]
        :param creation_timestamp: The param of the Versions
        :type creation_timestamp: date
        :param update_timestamp: The param of the Versions
        :type update_timestamp: date
        """
        
        

        self._version = None
        self._input = None
        self._stable = None
        self._translate = None
        self._support_versions = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self.discriminator = None

        self.version = version
        self.input = input
        self.stable = stable
        self.translate = translate
        self.support_versions = support_versions
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        self.update_timestamp = update_timestamp

    @property
    def version(self):
        """Gets the version of this Versions.

        :return: The version of this Versions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Versions.

        :param version: The version of this Versions.
        :type version: str
        """
        self._version = version

    @property
    def input(self):
        """Gets the input of this Versions.

        :return: The input of this Versions.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this Versions.

        :param input: The input of this Versions.
        :type input: object
        """
        self._input = input

    @property
    def stable(self):
        """Gets the stable of this Versions.

        :return: The stable of this Versions.
        :rtype: bool
        """
        return self._stable

    @stable.setter
    def stable(self, stable):
        """Sets the stable of this Versions.

        :param stable: The stable of this Versions.
        :type stable: bool
        """
        self._stable = stable

    @property
    def translate(self):
        """Gets the translate of this Versions.

        :return: The translate of this Versions.
        :rtype: object
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        """Sets the translate of this Versions.

        :param translate: The translate of this Versions.
        :type translate: object
        """
        self._translate = translate

    @property
    def support_versions(self):
        """Gets the support_versions of this Versions.

        :return: The support_versions of this Versions.
        :rtype: list[:class:`g42cloudsdkcce.v3.SupportVersions`]
        """
        return self._support_versions

    @support_versions.setter
    def support_versions(self, support_versions):
        """Sets the support_versions of this Versions.

        :param support_versions: The support_versions of this Versions.
        :type support_versions: list[:class:`g42cloudsdkcce.v3.SupportVersions`]
        """
        self._support_versions = support_versions

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Versions.

        :return: The creation_timestamp of this Versions.
        :rtype: date
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Versions.

        :param creation_timestamp: The creation_timestamp of this Versions.
        :type creation_timestamp: date
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this Versions.

        :return: The update_timestamp of this Versions.
        :rtype: date
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this Versions.

        :param update_timestamp: The update_timestamp of this Versions.
        :type update_timestamp: date
        """
        self._update_timestamp = update_timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Versions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
