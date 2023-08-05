import logging as log
from typing import Dict, List, Any

from fameio.source.logs import log_error_and_raise
from fameio.source.schema.exception import SchemaException
from fameio.source.schema.attribute import AttributeSpecs
from fameio.source.tools import keys_to_lower


class AgentType:
    """Schema definitions for an Agent type"""

    _ERR_PRODUCTS_NO_STRING_LIST = "Product definition of AgentType '{}' contains item(s) other than string: '{}'"
    _ERR_PRODUCTS_UNKNOWN_STRUCTURE = "Product definition of AgentType '{}' is neither list nor dictionary: '{}'"

    _NO_ATTRIBUTES = "Agent '{}' has no specified 'Attributes'."
    _NO_PRODUCTS = "Agent '{}' has no specified 'Products'."

    _KEY_ATTRIBUTES = "Attributes".lower()
    _KEY_PRODUCTS = "Products".lower()

    def __init__(self, name: str):
        self._name = name
        self._attributes = {}
        self._products = []

    @classmethod
    def from_dict(cls, name: str, definitions: dict) -> "AgentType":
        """Loads an agent type `definition` from the given input dict"""
        definition = keys_to_lower(definitions)

        result = cls(name)
        if AgentType._KEY_ATTRIBUTES in definition:
            for attribute_name, attribute_details in definition[AgentType._KEY_ATTRIBUTES].items():
                full_name = name + "." + attribute_name
                result._attributes[attribute_name] = AttributeSpecs(full_name, attribute_details)
        else:
            log.info(AgentType._NO_ATTRIBUTES.format(name))

        if AgentType._KEY_PRODUCTS in definition:
            products_to_add = definition[AgentType._KEY_PRODUCTS]
            if products_to_add:
                result._products.extend(AgentType.read_products(products_to_add, name))

        if not result._products:
            log.info(AgentType._NO_PRODUCTS.format(name))
        return result

    @staticmethod
    def read_products(products: Any, agent_type: str) -> List[str]:
        """Returns a list of product names obtained from given `products` defined for `agent_type`"""
        product_names = None
        if isinstance(products, dict):
            product_names = [key for key in products.keys()]
        elif isinstance(products, list):
            product_names = products
        else:
            log_error_and_raise(SchemaException(AgentType._ERR_PRODUCTS_UNKNOWN_STRUCTURE.format(agent_type, products)))

        if all([isinstance(item, str) for item in product_names]):
            return product_names
        else:
            log_error_and_raise(
                SchemaException(AgentType._ERR_PRODUCTS_NO_STRING_LIST.format(agent_type, product_names))
            )

    @property
    def name(self) -> str:
        """Returns the agent type name"""
        return self._name

    @property
    def products(self) -> list:
        """Returns list of products or an empty list if no products are defined"""
        return self._products

    @property
    def attributes(self) -> Dict[str, AttributeSpecs]:
        """Returns list of Attributes of this agent or an empty list if no attributes are defined"""
        return self._attributes
