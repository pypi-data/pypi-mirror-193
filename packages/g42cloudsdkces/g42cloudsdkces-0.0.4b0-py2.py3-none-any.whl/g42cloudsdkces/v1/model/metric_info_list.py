# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimensions': 'list[MetricsDimension]',
        'metric_name': 'str',
        'namespace': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'metric_name': 'metric_name',
        'namespace': 'namespace',
        'unit': 'unit'
    }

    def __init__(self, dimensions=None, metric_name=None, namespace=None, unit=None):
        """MetricInfoList

        The model defined in g42cloud sdk

        :param dimensions: The param of the MetricInfoList
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        :param metric_name: The param of the MetricInfoList
        :type metric_name: str
        :param namespace: The param of the MetricInfoList
        :type namespace: str
        :param unit: The param of the MetricInfoList
        :type unit: str
        """
        
        

        self._dimensions = None
        self._metric_name = None
        self._namespace = None
        self._unit = None
        self.discriminator = None

        self.dimensions = dimensions
        self.metric_name = metric_name
        self.namespace = namespace
        self.unit = unit

    @property
    def dimensions(self):
        """Gets the dimensions of this MetricInfoList.

        :return: The dimensions of this MetricInfoList.
        :rtype: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this MetricInfoList.

        :param dimensions: The dimensions of this MetricInfoList.
        :type dimensions: list[:class:`g42cloudsdkces.v1.MetricsDimension`]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricInfoList.

        :return: The metric_name of this MetricInfoList.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricInfoList.

        :param metric_name: The metric_name of this MetricInfoList.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this MetricInfoList.

        :return: The namespace of this MetricInfoList.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MetricInfoList.

        :param namespace: The namespace of this MetricInfoList.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def unit(self):
        """Gets the unit of this MetricInfoList.

        :return: The unit of this MetricInfoList.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricInfoList.

        :param unit: The unit of this MetricInfoList.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, MetricInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
