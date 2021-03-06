# coding: utf-8

#
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.19.17-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class PhasePriceOverride(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'plan_name': 'Str',
        'phase_name': 'Str',
        'phase_type': 'Str',
        'fixed_price': 'Float',
        'recurring_price': 'Float',
        'usage_price_overrides': 'List[UsagePriceOverride]'
    }

    attribute_map = {
        'plan_name': 'planName',
        'phase_name': 'phaseName',
        'phase_type': 'phaseType',
        'fixed_price': 'fixedPrice',
        'recurring_price': 'recurringPrice',
        'usage_price_overrides': 'usagePriceOverrides'
    }

    def __init__(self, plan_name=None, phase_name=None, phase_type=None, fixed_price=None, recurring_price=None, usage_price_overrides=None):  # noqa: E501
        """PhasePriceOverride - a model defined in Swagger"""  # noqa: E501

        self._plan_name = None
        self._phase_name = None
        self._phase_type = None
        self._fixed_price = None
        self._recurring_price = None
        self._usage_price_overrides = None
        self.discriminator = None

        if plan_name is not None:
            self.plan_name = plan_name
        if phase_name is not None:
            self.phase_name = phase_name
        if phase_type is not None:
            self.phase_type = phase_type
        if fixed_price is not None:
            self.fixed_price = fixed_price
        if recurring_price is not None:
            self.recurring_price = recurring_price
        if usage_price_overrides is not None:
            self.usage_price_overrides = usage_price_overrides

    @property
    def plan_name(self):
        """Gets the plan_name of this PhasePriceOverride.  # noqa: E501


        :return: The plan_name of this PhasePriceOverride.  # noqa: E501
        :rtype: Str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this PhasePriceOverride.


        :param plan_name: The plan_name of this PhasePriceOverride.  # noqa: E501
        :type: Str
        """


        self._plan_name = plan_name

    @property
    def phase_name(self):
        """Gets the phase_name of this PhasePriceOverride.  # noqa: E501


        :return: The phase_name of this PhasePriceOverride.  # noqa: E501
        :rtype: Str
        """
        return self._phase_name

    @phase_name.setter
    def phase_name(self, phase_name):
        """Sets the phase_name of this PhasePriceOverride.


        :param phase_name: The phase_name of this PhasePriceOverride.  # noqa: E501
        :type: Str
        """


        self._phase_name = phase_name

    @property
    def phase_type(self):
        """Gets the phase_type of this PhasePriceOverride.  # noqa: E501


        :return: The phase_type of this PhasePriceOverride.  # noqa: E501
        :rtype: Str
        """
        return self._phase_type

    @phase_type.setter
    def phase_type(self, phase_type):
        """Sets the phase_type of this PhasePriceOverride.


        :param phase_type: The phase_type of this PhasePriceOverride.  # noqa: E501
        :type: Str
        """


        self._phase_type = phase_type

    @property
    def fixed_price(self):
        """Gets the fixed_price of this PhasePriceOverride.  # noqa: E501


        :return: The fixed_price of this PhasePriceOverride.  # noqa: E501
        :rtype: Float
        """
        return self._fixed_price

    @fixed_price.setter
    def fixed_price(self, fixed_price):
        """Sets the fixed_price of this PhasePriceOverride.


        :param fixed_price: The fixed_price of this PhasePriceOverride.  # noqa: E501
        :type: Float
        """


        self._fixed_price = fixed_price

    @property
    def recurring_price(self):
        """Gets the recurring_price of this PhasePriceOverride.  # noqa: E501


        :return: The recurring_price of this PhasePriceOverride.  # noqa: E501
        :rtype: Float
        """
        return self._recurring_price

    @recurring_price.setter
    def recurring_price(self, recurring_price):
        """Sets the recurring_price of this PhasePriceOverride.


        :param recurring_price: The recurring_price of this PhasePriceOverride.  # noqa: E501
        :type: Float
        """


        self._recurring_price = recurring_price

    @property
    def usage_price_overrides(self):
        """Gets the usage_price_overrides of this PhasePriceOverride.  # noqa: E501


        :return: The usage_price_overrides of this PhasePriceOverride.  # noqa: E501
        :rtype: List[UsagePriceOverride]
        """
        return self._usage_price_overrides

    @usage_price_overrides.setter
    def usage_price_overrides(self, usage_price_overrides):
        """Sets the usage_price_overrides of this PhasePriceOverride.


        :param usage_price_overrides: The usage_price_overrides of this PhasePriceOverride.  # noqa: E501
        :type: List[UsagePriceOverride]
        """


        self._usage_price_overrides = usage_price_overrides

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PhasePriceOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
