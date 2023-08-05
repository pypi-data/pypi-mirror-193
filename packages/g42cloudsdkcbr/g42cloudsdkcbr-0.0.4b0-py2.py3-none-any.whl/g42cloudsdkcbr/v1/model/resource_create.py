# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extra_info': 'ResourceExtraInfo',
        'id': 'str',
        'type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'extra_info': 'extra_info',
        'id': 'id',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, extra_info=None, id=None, type=None, name=None):
        """ResourceCreate

        The model defined in g42cloud sdk

        :param extra_info: The param of the ResourceCreate
        :type extra_info: :class:`g42cloudsdkcbr.v1.ResourceExtraInfo`
        :param id: The param of the ResourceCreate
        :type id: str
        :param type: The param of the ResourceCreate
        :type type: str
        :param name: The param of the ResourceCreate
        :type name: str
        """
        
        

        self._extra_info = None
        self._id = None
        self._type = None
        self._name = None
        self.discriminator = None

        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        self.type = type
        if name is not None:
            self.name = name

    @property
    def extra_info(self):
        """Gets the extra_info of this ResourceCreate.

        :return: The extra_info of this ResourceCreate.
        :rtype: :class:`g42cloudsdkcbr.v1.ResourceExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this ResourceCreate.

        :param extra_info: The extra_info of this ResourceCreate.
        :type extra_info: :class:`g42cloudsdkcbr.v1.ResourceExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this ResourceCreate.

        :return: The id of this ResourceCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceCreate.

        :param id: The id of this ResourceCreate.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this ResourceCreate.

        :return: The type of this ResourceCreate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceCreate.

        :param type: The type of this ResourceCreate.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ResourceCreate.

        :return: The name of this ResourceCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceCreate.

        :param name: The name of this ResourceCreate.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ResourceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
