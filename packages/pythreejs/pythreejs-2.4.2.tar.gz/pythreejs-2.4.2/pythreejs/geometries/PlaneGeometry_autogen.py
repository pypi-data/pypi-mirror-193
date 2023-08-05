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


@register
class PlaneGeometry(BaseGeometry):
    """PlaneGeometry

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/geometries/PlaneGeometry
    """

    def __init__(self, width=1, height=1, widthSegments=1, heightSegments=1, **kwargs):
        kwargs['width'] = width
        kwargs['height'] = height
        kwargs['widthSegments'] = widthSegments
        kwargs['heightSegments'] = heightSegments
        super(PlaneGeometry, self).__init__(**kwargs)

    _model_name = Unicode('PlaneGeometryModel').tag(sync=True)

    width = IEEEFloat(1, allow_none=False).tag(sync=True)

    height = IEEEFloat(1, allow_none=False).tag(sync=True)

    widthSegments = CInt(1, allow_none=False).tag(sync=True)

    heightSegments = CInt(1, allow_none=False).tag(sync=True)

    type = Unicode("PlaneGeometry", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
PlaneGeometry.__signature__ = inspect.signature(PlaneGeometry.__init__)
