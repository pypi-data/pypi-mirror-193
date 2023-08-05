# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class Condition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comparison_operator': 'str',
        'count': 'int',
        'filter': 'str',
        'period': 'int',
        'unit': 'str',
        'value': 'float',
        'suppress_duration': 'int'
    }

    attribute_map = {
        'comparison_operator': 'comparison_operator',
        'count': 'count',
        'filter': 'filter',
        'period': 'period',
        'unit': 'unit',
        'value': 'value',
        'suppress_duration': 'suppress_duration'
    }

    def __init__(self, comparison_operator=None, count=None, filter=None, period=None, unit=None, value=None, suppress_duration=None):
        """Condition

        The model defined in g42cloud sdk

        :param comparison_operator: The param of the Condition
        :type comparison_operator: str
        :param count: The param of the Condition
        :type count: int
        :param filter: The param of the Condition
        :type filter: str
        :param period: The param of the Condition
        :type period: int
        :param unit: The param of the Condition
        :type unit: str
        :param value: The param of the Condition
        :type value: float
        :param suppress_duration: The param of the Condition
        :type suppress_duration: int
        """
        
        

        self._comparison_operator = None
        self._count = None
        self._filter = None
        self._period = None
        self._unit = None
        self._value = None
        self._suppress_duration = None
        self.discriminator = None

        self.comparison_operator = comparison_operator
        self.count = count
        self.filter = filter
        self.period = period
        if unit is not None:
            self.unit = unit
        self.value = value
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this Condition.

        :return: The comparison_operator of this Condition.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this Condition.

        :param comparison_operator: The comparison_operator of this Condition.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def count(self):
        """Gets the count of this Condition.

        :return: The count of this Condition.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Condition.

        :param count: The count of this Condition.
        :type count: int
        """
        self._count = count

    @property
    def filter(self):
        """Gets the filter of this Condition.

        :return: The filter of this Condition.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Condition.

        :param filter: The filter of this Condition.
        :type filter: str
        """
        self._filter = filter

    @property
    def period(self):
        """Gets the period of this Condition.

        :return: The period of this Condition.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Condition.

        :param period: The period of this Condition.
        :type period: int
        """
        self._period = period

    @property
    def unit(self):
        """Gets the unit of this Condition.

        :return: The unit of this Condition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Condition.

        :param unit: The unit of this Condition.
        :type unit: str
        """
        self._unit = unit

    @property
    def value(self):
        """Gets the value of this Condition.

        :return: The value of this Condition.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Condition.

        :param value: The value of this Condition.
        :type value: float
        """
        self._value = value

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this Condition.

        :return: The suppress_duration of this Condition.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this Condition.

        :param suppress_duration: The suppress_duration of this Condition.
        :type suppress_duration: int
        """
        self._suppress_duration = suppress_duration

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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
