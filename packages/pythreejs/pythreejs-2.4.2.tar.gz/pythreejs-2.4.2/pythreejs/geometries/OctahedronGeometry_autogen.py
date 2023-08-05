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
class OctahedronGeometry(BaseGeometry):
    """OctahedronGeometry

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/geometries/OctahedronGeometry
    """

    def __init__(self, radius=1, detail=0, **kwargs):
        kwargs['radius'] = radius
        kwargs['detail'] = detail
        super(OctahedronGeometry, self).__init__(**kwargs)

    _model_name = Unicode('OctahedronGeometryModel').tag(sync=True)

    radius = IEEEFloat(1, allow_none=False).tag(sync=True)

    detail = CInt(0, allow_none=False).tag(sync=True)

    type = Unicode("OctahedronGeometry", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
OctahedronGeometry.__signature__ = inspect.signature(OctahedronGeometry.__init__)
