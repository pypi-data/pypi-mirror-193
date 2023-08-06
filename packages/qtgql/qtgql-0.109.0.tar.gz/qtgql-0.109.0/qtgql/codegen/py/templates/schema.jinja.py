from __future__ import annotations
from PySide6.QtCore import Signal, QObject, QEnum

from PySide6.QtQuick import QQuickItem
from typing import Optional, Union
from enum import Enum, auto
from PySide6.QtQml import QmlElement, QmlSingleton

from qtgql.tools import qproperty
from qtgql.codegen.py.runtime.bases import QGraphQListModel






{% for dep in context.dependencies %}
{{dep}}{% endfor %}


QML_IMPORT_NAME = "generated.{{context.config.env_name}}.types"
QML_IMPORT_MAJOR_VERSION = 1



{% for enum in context.enums %}
class {{enum.name}}(Enum):
    {% for member in enum.members %}
    {{member.name}} = auto()
    """{{member.description}}"""{% endfor %}

{% endfor %}

{% if context.enums %}
@QmlElement
class Enums(QObject):
    {% for enum in context.enums %}
    QEnum({{enum.name}})
    {% endfor %}
{% endif %}


class SCALARS:
    {% for scalar in context.custom_scalars %}
    {{scalar}} = {{scalar}}{% endfor %}

{% for type in context.types %}
class {{ type.name }}({{context.base_object_name}}):
    """{{  type.docstring  }}"""

    DEFAULT_INIT_DICT = dict({% for f in type.fields %}
        {{f.name}}=None,{% endfor %}
    )
    def __init__(self, parent: QObject = None, {% for f in type.fields %} {{f.name}}: {{f.annotation}} = None, {% endfor %}):
        super().__init__(parent){% for f in type.fields %}
        self.{{  f.private_name  }} = {{f.name}} if {{f.name}} else {{f.default_value}}{% endfor %}

    def update(self, data: dict):
        parent = self.parent()
        {% for f in type.fields %}
        if {{f.name}} := data.get('{{f.name}}', None):
            deserialized = {{f.deserializer}}
            if self.{{f.name}} != deserialized:
                self.{{f.setter_name}}(deserialized)
        return self{% endfor %}

    @classmethod
    def from_dict(cls, parent,  data: dict) -> {{type.name}}:
        if instance := cls.__store__.get_node(data['id']):
            return instance.update(data)
        else:
            init_dict = cls.DEFAULT_INIT_DICT.copy()
            {% for f in type.fields %}
            if {{f.name}} := data.get('{{f.name}}', None):
                init_dict['{{f.name}}'] = {{f.deserializer}}{% endfor %}
            return cls(
                parent=parent,
                **init_dict
            )

    {% for f in type.fields %}
    {{ f.signal_name }} = Signal()

    def {{ f.setter_name }}(self, v: {{  f.annotation  }}) -> None:
        self.{{  f.private_name  }} = v
        self.{{  f.name  }}Changed.emit()

    @qproperty(type={{f.property_type}}, fset={{ f.setter_name }}, notify={{f.signal_name}})
    def {{ f.name }}(self) -> {{ f.fget_annotation }}:
        {{f.fget}}
    {% endfor %}

{% endfor %}



