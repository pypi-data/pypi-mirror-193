from ipywidgets import (
    Widget, DOMWidget, widget_serialization, register
)
from ipywidgets.widgets.trait_types import TypedTuple
from traitlets import (
    Unicode, Int, CInt, Instance, ForwardDeclaredInstance, This, Enum,
    Tuple, List, Dict, Float, CFloat, Bool, Union, Any,
)

from ..._base.Three import ThreeWidget
from ..._base.uniforms import uniforms_serialization
from ...enums import *
from ...traits import *

from ..._base.Three import ThreeWidget


@register
class WebGLState(ThreeWidget):
    """WebGLState

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/renderers/webgl/WebGLState
    """

    def __init__(self, **kwargs):
        raise NotImplementedError('WebGLState is not yet implemented!')

    _model_name = Unicode('WebGLStateModel').tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
WebGLState.__signature__ = inspect.signature(WebGLState.__init__)
