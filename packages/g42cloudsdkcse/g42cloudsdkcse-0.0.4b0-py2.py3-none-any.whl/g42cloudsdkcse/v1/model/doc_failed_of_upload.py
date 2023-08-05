# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocFailedOfUpload:

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
        'labels': 'object',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'key': 'key',
        'labels': 'labels',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, key=None, labels=None, error_code=None, error_message=None):
        """DocFailedOfUpload

        The model defined in g42cloud sdk

        :param key: The param of the DocFailedOfUpload
        :type key: str
        :param labels: The param of the DocFailedOfUpload
        :type labels: object
        :param error_code: The param of the DocFailedOfUpload
        :type error_code: str
        :param error_message: The param of the DocFailedOfUpload
        :type error_message: str
        """
        
        

        self._key = None
        self._labels = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if labels is not None:
            self.labels = labels
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def key(self):
        """Gets the key of this DocFailedOfUpload.

        :return: The key of this DocFailedOfUpload.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DocFailedOfUpload.

        :param key: The key of this DocFailedOfUpload.
        :type key: str
        """
        self._key = key

    @property
    def labels(self):
        """Gets the labels of this DocFailedOfUpload.

        :return: The labels of this DocFailedOfUpload.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DocFailedOfUpload.

        :param labels: The labels of this DocFailedOfUpload.
        :type labels: object
        """
        self._labels = labels

    @property
    def error_code(self):
        """Gets the error_code of this DocFailedOfUpload.

        :return: The error_code of this DocFailedOfUpload.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this DocFailedOfUpload.

        :param error_code: The error_code of this DocFailedOfUpload.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this DocFailedOfUpload.

        :return: The error_message of this DocFailedOfUpload.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DocFailedOfUpload.

        :param error_message: The error_message of this DocFailedOfUpload.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, DocFailedOfUpload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
