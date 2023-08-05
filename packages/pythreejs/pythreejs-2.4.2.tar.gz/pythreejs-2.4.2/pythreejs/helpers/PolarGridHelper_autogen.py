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

from ..core.Object3D import Object3D


@register
class PolarGridHelper(Object3D):
    """PolarGridHelper

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/helpers/PolarGridHelper
    """

    def __init__(self, radius=10, radials=16, circles=8, divisions=64, color1="#444444", color2="#888888", **kwargs):
        kwargs['radius'] = radius
        kwargs['radials'] = radials
        kwargs['circles'] = circles
        kwargs['divisions'] = divisions
        kwargs['color1'] = color1
        kwargs['color2'] = color2
        super(PolarGridHelper, self).__init__(**kwargs)

    _model_name = Unicode('PolarGridHelperModel').tag(sync=True)

    radius = CInt(10, allow_none=False).tag(sync=True)

    radials = CInt(16, allow_none=False).tag(sync=True)

    circles = CInt(8, allow_none=False).tag(sync=True)

    divisions = CInt(64, allow_none=False).tag(sync=True)

    color1 = Color("#444444", allow_none=False).tag(sync=True)

    color2 = Color("#888888", allow_none=False).tag(sync=True)

    type = Unicode("PolarGridHelper", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
PolarGridHelper.__signature__ = inspect.signature(PolarGridHelper.__init__)
