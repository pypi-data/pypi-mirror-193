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


@register
class Quaternion(ThreeWidget):
    """Quaternion

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/math/Quaternion
    """

    def __init__(self, x=0, y=0, z=0, w=1, **kwargs):
        kwargs['x'] = x
        kwargs['y'] = y
        kwargs['z'] = z
        kwargs['w'] = w
        super(Quaternion, self).__init__(**kwargs)

    _model_name = Unicode('QuaternionModel').tag(sync=True)

    x = IEEEFloat(0, allow_none=False).tag(sync=True)

    y = IEEEFloat(0, allow_none=False).tag(sync=True)

    z = IEEEFloat(0, allow_none=False).tag(sync=True)

    w = IEEEFloat(1, allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
Quaternion.__signature__ = inspect.signature(Quaternion.__init__)
