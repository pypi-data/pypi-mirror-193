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

from ..core.BaseGeometry_autogen import BaseGeometry

from ..extras.core.Curve_autogen import Curve

@register
class TubeGeometry(BaseGeometry):
    """TubeGeometry

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/geometries/TubeGeometry
    """

    def __init__(self, path=None, segments=64, radius=1, radialSegments=8, close=False, **kwargs):
        kwargs['path'] = path
        kwargs['segments'] = segments
        kwargs['radius'] = radius
        kwargs['radialSegments'] = radialSegments
        kwargs['close'] = close
        super(TubeGeometry, self).__init__(**kwargs)

    _model_name = Unicode('TubeGeometryModel').tag(sync=True)

    path = Instance(Curve, allow_none=True).tag(sync=True, **widget_serialization)

    segments = CInt(64, allow_none=False).tag(sync=True)

    radius = IEEEFloat(1, allow_none=False).tag(sync=True)

    radialSegments = CInt(8, allow_none=False).tag(sync=True)

    close = Bool(False, allow_none=False).tag(sync=True)

    type = Unicode("TubeGeometry", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
TubeGeometry.__signature__ = inspect.signature(TubeGeometry.__init__)
