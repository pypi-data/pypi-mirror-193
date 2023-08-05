from ipywidgets import (
    Widget, DOMWidget, widget_serialization, register
)
from ipywidgets.widgets.trait_types import TypedTuple
from traitlets import (
    Unicode, Int, CInt, Instance, ForwardDeclaredInstance, This, Enum,
    Tuple, List, Dict, Float, CFloat, Bool, Union, Any,
)

from .._base.Three import ThreeWidget
from .._base.uniforms import uniforms_serialization
from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget

from ..core.Object3D import Object3D

@register
class Controls(ThreeWidget):
    """Controls

    Autogenerated by generate-wrappers.js
    This class is a custom class for pythreejs, with no
    direct corresponding class in three.js.
    """

    def __init__(self, **kwargs):
        super(Controls, self).__init__(**kwargs)

    _model_name = Unicode('ControlsModel').tag(sync=True)

    controlling = Instance(Object3D, allow_none=False).tag(sync=True, **widget_serialization)


import inspect
# Include explicit signature since the metaclass screws it up
Controls.__signature__ = inspect.signature(Controls.__init__)
