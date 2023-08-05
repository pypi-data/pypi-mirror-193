# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlarmRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_name': 'str',
        'alarm_description': 'str',
        'metric': 'MetricForAlarm',
        'condition': 'Condition',
        'alarm_enabled': 'bool',
        'alarm_action_enabled': 'bool',
        'alarm_level': 'int',
        'alarm_type': 'str',
        'alarm_actions': 'list[AlarmActions]',
        'insufficientdata_actions': 'list[AlarmActions]',
        'ok_actions': 'list[AlarmActions]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'alarm_name': 'alarm_name',
        'alarm_description': 'alarm_description',
        'metric': 'metric',
        'condition': 'condition',
        'alarm_enabled': 'alarm_enabled',
        'alarm_action_enabled': 'alarm_action_enabled',
        'alarm_level': 'alarm_level',
        'alarm_type': 'alarm_type',
        'alarm_actions': 'alarm_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'ok_actions': 'ok_actions',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, alarm_name=None, alarm_description=None, metric=None, condition=None, alarm_enabled=None, alarm_action_enabled=None, alarm_level=None, alarm_type=None, alarm_actions=None, insufficientdata_actions=None, ok_actions=None, enterprise_project_id=None):
        """CreateAlarmRequestBody

        The model defined in g42cloud sdk

        :param alarm_name: The param of the CreateAlarmRequestBody
        :type alarm_name: str
        :param alarm_description: The param of the CreateAlarmRequestBody
        :type alarm_description: str
        :param metric: The param of the CreateAlarmRequestBody
        :type metric: :class:`g42cloudsdkces.v1.MetricForAlarm`
        :param condition: The param of the CreateAlarmRequestBody
        :type condition: :class:`g42cloudsdkces.v1.Condition`
        :param alarm_enabled: The param of the CreateAlarmRequestBody
        :type alarm_enabled: bool
        :param alarm_action_enabled: The param of the CreateAlarmRequestBody
        :type alarm_action_enabled: bool
        :param alarm_level: The param of the CreateAlarmRequestBody
        :type alarm_level: int
        :param alarm_type: The param of the CreateAlarmRequestBody
        :type alarm_type: str
        :param alarm_actions: The param of the CreateAlarmRequestBody
        :type alarm_actions: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        :param insufficientdata_actions: The param of the CreateAlarmRequestBody
        :type insufficientdata_actions: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        :param ok_actions: The param of the CreateAlarmRequestBody
        :type ok_actions: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        :param enterprise_project_id: The param of the CreateAlarmRequestBody
        :type enterprise_project_id: str
        """
        
        

        self._alarm_name = None
        self._alarm_description = None
        self._metric = None
        self._condition = None
        self._alarm_enabled = None
        self._alarm_action_enabled = None
        self._alarm_level = None
        self._alarm_type = None
        self._alarm_actions = None
        self._insufficientdata_actions = None
        self._ok_actions = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.alarm_name = alarm_name
        if alarm_description is not None:
            self.alarm_description = alarm_description
        self.metric = metric
        self.condition = condition
        if alarm_enabled is not None:
            self.alarm_enabled = alarm_enabled
        if alarm_action_enabled is not None:
            self.alarm_action_enabled = alarm_action_enabled
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def alarm_name(self):
        """Gets the alarm_name of this CreateAlarmRequestBody.

        :return: The alarm_name of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this CreateAlarmRequestBody.

        :param alarm_name: The alarm_name of this CreateAlarmRequestBody.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_description(self):
        """Gets the alarm_description of this CreateAlarmRequestBody.

        :return: The alarm_description of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_description

    @alarm_description.setter
    def alarm_description(self, alarm_description):
        """Sets the alarm_description of this CreateAlarmRequestBody.

        :param alarm_description: The alarm_description of this CreateAlarmRequestBody.
        :type alarm_description: str
        """
        self._alarm_description = alarm_description

    @property
    def metric(self):
        """Gets the metric of this CreateAlarmRequestBody.

        :return: The metric of this CreateAlarmRequestBody.
        :rtype: :class:`g42cloudsdkces.v1.MetricForAlarm`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this CreateAlarmRequestBody.

        :param metric: The metric of this CreateAlarmRequestBody.
        :type metric: :class:`g42cloudsdkces.v1.MetricForAlarm`
        """
        self._metric = metric

    @property
    def condition(self):
        """Gets the condition of this CreateAlarmRequestBody.

        :return: The condition of this CreateAlarmRequestBody.
        :rtype: :class:`g42cloudsdkces.v1.Condition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this CreateAlarmRequestBody.

        :param condition: The condition of this CreateAlarmRequestBody.
        :type condition: :class:`g42cloudsdkces.v1.Condition`
        """
        self._condition = condition

    @property
    def alarm_enabled(self):
        """Gets the alarm_enabled of this CreateAlarmRequestBody.

        :return: The alarm_enabled of this CreateAlarmRequestBody.
        :rtype: bool
        """
        return self._alarm_enabled

    @alarm_enabled.setter
    def alarm_enabled(self, alarm_enabled):
        """Sets the alarm_enabled of this CreateAlarmRequestBody.

        :param alarm_enabled: The alarm_enabled of this CreateAlarmRequestBody.
        :type alarm_enabled: bool
        """
        self._alarm_enabled = alarm_enabled

    @property
    def alarm_action_enabled(self):
        """Gets the alarm_action_enabled of this CreateAlarmRequestBody.

        :return: The alarm_action_enabled of this CreateAlarmRequestBody.
        :rtype: bool
        """
        return self._alarm_action_enabled

    @alarm_action_enabled.setter
    def alarm_action_enabled(self, alarm_action_enabled):
        """Sets the alarm_action_enabled of this CreateAlarmRequestBody.

        :param alarm_action_enabled: The alarm_action_enabled of this CreateAlarmRequestBody.
        :type alarm_action_enabled: bool
        """
        self._alarm_action_enabled = alarm_action_enabled

    @property
    def alarm_level(self):
        """Gets the alarm_level of this CreateAlarmRequestBody.

        :return: The alarm_level of this CreateAlarmRequestBody.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this CreateAlarmRequestBody.

        :param alarm_level: The alarm_level of this CreateAlarmRequestBody.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_type(self):
        """Gets the alarm_type of this CreateAlarmRequestBody.

        :return: The alarm_type of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        """Sets the alarm_type of this CreateAlarmRequestBody.

        :param alarm_type: The alarm_type of this CreateAlarmRequestBody.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this CreateAlarmRequestBody.

        :return: The alarm_actions of this CreateAlarmRequestBody.
        :rtype: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this CreateAlarmRequestBody.

        :param alarm_actions: The alarm_actions of this CreateAlarmRequestBody.
        :type alarm_actions: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        """
        self._alarm_actions = alarm_actions

    @property
    def insufficientdata_actions(self):
        """Gets the insufficientdata_actions of this CreateAlarmRequestBody.

        :return: The insufficientdata_actions of this CreateAlarmRequestBody.
        :rtype: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        """Sets the insufficientdata_actions of this CreateAlarmRequestBody.

        :param insufficientdata_actions: The insufficientdata_actions of this CreateAlarmRequestBody.
        :type insufficientdata_actions: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this CreateAlarmRequestBody.

        :return: The ok_actions of this CreateAlarmRequestBody.
        :rtype: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this CreateAlarmRequestBody.

        :param ok_actions: The ok_actions of this CreateAlarmRequestBody.
        :type ok_actions: list[:class:`g42cloudsdkces.v1.AlarmActions`]
        """
        self._ok_actions = ok_actions

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateAlarmRequestBody.

        :return: The enterprise_project_id of this CreateAlarmRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateAlarmRequestBody.

        :param enterprise_project_id: The enterprise_project_id of this CreateAlarmRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateAlarmRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
