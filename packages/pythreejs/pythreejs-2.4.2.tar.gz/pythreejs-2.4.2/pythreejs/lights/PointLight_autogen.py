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

from .Light_autogen import Light

from .LightShadow_autogen import LightShadow

@register
class PointLight(Light):
    """PointLight

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/lights/PointLight
    """

    def __init__(self, color="#ffffff", intensity=1, distance=0, decay=1, **kwargs):
        kwargs['color'] = color
        kwargs['intensity'] = intensity
        kwargs['distance'] = distance
        kwargs['decay'] = decay
        super(PointLight, self).__init__(**kwargs)

    _model_name = Unicode('PointLightModel').tag(sync=True)

    power = IEEEFloat(12.566370614359172, allow_none=False).tag(sync=True)

    distance = IEEEFloat(0, allow_none=False).tag(sync=True)

    decay = IEEEFloat(1, allow_none=False).tag(sync=True)

    shadow = Union([
        Instance(Uninitialized),
        Instance(LightShadow),
        ], default_value=UninitializedSentinel, allow_none=False).tag(sync=True, **unitialized_serialization)

    type = Unicode("PointLight", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
PointLight.__signature__ = inspect.signature(PointLight.__init__)
