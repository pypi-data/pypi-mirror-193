# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Taint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'effect': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'effect': 'effect'
    }

    def __init__(self, key=None, value=None, effect=None):
        """Taint

        The model defined in g42cloud sdk

        :param key: The param of the Taint
        :type key: str
        :param value: The param of the Taint
        :type value: str
        :param effect: The param of the Taint
        :type effect: str
        """
        
        

        self._key = None
        self._value = None
        self._effect = None
        self.discriminator = None

        self.key = key
        if value is not None:
            self.value = value
        self.effect = effect

    @property
    def key(self):
        """Gets the key of this Taint.

        :return: The key of this Taint.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Taint.

        :param key: The key of this Taint.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this Taint.

        :return: The value of this Taint.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Taint.

        :param value: The value of this Taint.
        :type value: str
        """
        self._value = value

    @property
    def effect(self):
        """Gets the effect of this Taint.

        :return: The effect of this Taint.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this Taint.

        :param effect: The effect of this Taint.
        :type effect: str
        """
        self._effect = effect

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
        if not isinstance(other, Taint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
