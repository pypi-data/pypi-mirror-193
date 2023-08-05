# coding: utf-8

import re
import six



from g42cloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrackerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tracker_type': 'str',
        'tracker_name': 'str',
        'is_lts_enabled': 'bool',
        'obs_info': 'TrackerObsInfo',
        'is_support_trace_files_encryption': 'bool',
        'kms_id': 'str',
        'is_support_validate': 'bool',
        'data_bucket': 'DataBucket'
    }

    attribute_map = {
        'tracker_type': 'tracker_type',
        'tracker_name': 'tracker_name',
        'is_lts_enabled': 'is_lts_enabled',
        'obs_info': 'obs_info',
        'is_support_trace_files_encryption': 'is_support_trace_files_encryption',
        'kms_id': 'kms_id',
        'is_support_validate': 'is_support_validate',
        'data_bucket': 'data_bucket'
    }

    def __init__(self, tracker_type=None, tracker_name=None, is_lts_enabled=None, obs_info=None, is_support_trace_files_encryption=None, kms_id=None, is_support_validate=None, data_bucket=None):
        """CreateTrackerRequestBody

        The model defined in g42cloud sdk

        :param tracker_type: The param of the CreateTrackerRequestBody
        :type tracker_type: str
        :param tracker_name: The param of the CreateTrackerRequestBody
        :type tracker_name: str
        :param is_lts_enabled: The param of the CreateTrackerRequestBody
        :type is_lts_enabled: bool
        :param obs_info: The param of the CreateTrackerRequestBody
        :type obs_info: :class:`g42cloudsdkcts.v3.TrackerObsInfo`
        :param is_support_trace_files_encryption: The param of the CreateTrackerRequestBody
        :type is_support_trace_files_encryption: bool
        :param kms_id: The param of the CreateTrackerRequestBody
        :type kms_id: str
        :param is_support_validate: The param of the CreateTrackerRequestBody
        :type is_support_validate: bool
        :param data_bucket: The param of the CreateTrackerRequestBody
        :type data_bucket: :class:`g42cloudsdkcts.v3.DataBucket`
        """
        
        

        self._tracker_type = None
        self._tracker_name = None
        self._is_lts_enabled = None
        self._obs_info = None
        self._is_support_trace_files_encryption = None
        self._kms_id = None
        self._is_support_validate = None
        self._data_bucket = None
        self.discriminator = None

        self.tracker_type = tracker_type
        self.tracker_name = tracker_name
        if is_lts_enabled is not None:
            self.is_lts_enabled = is_lts_enabled
        if obs_info is not None:
            self.obs_info = obs_info
        if is_support_trace_files_encryption is not None:
            self.is_support_trace_files_encryption = is_support_trace_files_encryption
        if kms_id is not None:
            self.kms_id = kms_id
        if is_support_validate is not None:
            self.is_support_validate = is_support_validate
        if data_bucket is not None:
            self.data_bucket = data_bucket

    @property
    def tracker_type(self):
        """Gets the tracker_type of this CreateTrackerRequestBody.

        :return: The tracker_type of this CreateTrackerRequestBody.
        :rtype: str
        """
        return self._tracker_type

    @tracker_type.setter
    def tracker_type(self, tracker_type):
        """Sets the tracker_type of this CreateTrackerRequestBody.

        :param tracker_type: The tracker_type of this CreateTrackerRequestBody.
        :type tracker_type: str
        """
        self._tracker_type = tracker_type

    @property
    def tracker_name(self):
        """Gets the tracker_name of this CreateTrackerRequestBody.

        :return: The tracker_name of this CreateTrackerRequestBody.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        """Sets the tracker_name of this CreateTrackerRequestBody.

        :param tracker_name: The tracker_name of this CreateTrackerRequestBody.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

    @property
    def is_lts_enabled(self):
        """Gets the is_lts_enabled of this CreateTrackerRequestBody.

        :return: The is_lts_enabled of this CreateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_lts_enabled

    @is_lts_enabled.setter
    def is_lts_enabled(self, is_lts_enabled):
        """Sets the is_lts_enabled of this CreateTrackerRequestBody.

        :param is_lts_enabled: The is_lts_enabled of this CreateTrackerRequestBody.
        :type is_lts_enabled: bool
        """
        self._is_lts_enabled = is_lts_enabled

    @property
    def obs_info(self):
        """Gets the obs_info of this CreateTrackerRequestBody.

        :return: The obs_info of this CreateTrackerRequestBody.
        :rtype: :class:`g42cloudsdkcts.v3.TrackerObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        """Sets the obs_info of this CreateTrackerRequestBody.

        :param obs_info: The obs_info of this CreateTrackerRequestBody.
        :type obs_info: :class:`g42cloudsdkcts.v3.TrackerObsInfo`
        """
        self._obs_info = obs_info

    @property
    def is_support_trace_files_encryption(self):
        """Gets the is_support_trace_files_encryption of this CreateTrackerRequestBody.

        :return: The is_support_trace_files_encryption of this CreateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_support_trace_files_encryption

    @is_support_trace_files_encryption.setter
    def is_support_trace_files_encryption(self, is_support_trace_files_encryption):
        """Sets the is_support_trace_files_encryption of this CreateTrackerRequestBody.

        :param is_support_trace_files_encryption: The is_support_trace_files_encryption of this CreateTrackerRequestBody.
        :type is_support_trace_files_encryption: bool
        """
        self._is_support_trace_files_encryption = is_support_trace_files_encryption

    @property
    def kms_id(self):
        """Gets the kms_id of this CreateTrackerRequestBody.

        :return: The kms_id of this CreateTrackerRequestBody.
        :rtype: str
        """
        return self._kms_id

    @kms_id.setter
    def kms_id(self, kms_id):
        """Sets the kms_id of this CreateTrackerRequestBody.

        :param kms_id: The kms_id of this CreateTrackerRequestBody.
        :type kms_id: str
        """
        self._kms_id = kms_id

    @property
    def is_support_validate(self):
        """Gets the is_support_validate of this CreateTrackerRequestBody.

        :return: The is_support_validate of this CreateTrackerRequestBody.
        :rtype: bool
        """
        return self._is_support_validate

    @is_support_validate.setter
    def is_support_validate(self, is_support_validate):
        """Sets the is_support_validate of this CreateTrackerRequestBody.

        :param is_support_validate: The is_support_validate of this CreateTrackerRequestBody.
        :type is_support_validate: bool
        """
        self._is_support_validate = is_support_validate

    @property
    def data_bucket(self):
        """Gets the data_bucket of this CreateTrackerRequestBody.

        :return: The data_bucket of this CreateTrackerRequestBody.
        :rtype: :class:`g42cloudsdkcts.v3.DataBucket`
        """
        return self._data_bucket

    @data_bucket.setter
    def data_bucket(self, data_bucket):
        """Sets the data_bucket of this CreateTrackerRequestBody.

        :param data_bucket: The data_bucket of this CreateTrackerRequestBody.
        :type data_bucket: :class:`g42cloudsdkcts.v3.DataBucket`
        """
        self._data_bucket = data_bucket

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
        if not isinstance(other, CreateTrackerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
