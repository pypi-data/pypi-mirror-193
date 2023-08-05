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
class Camera(Object3D):
    """Camera

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/cameras/Camera
    """

    def __init__(self, **kwargs):
        super(Camera, self).__init__(**kwargs)

    _model_name = Unicode('CameraModel').tag(sync=True)

    matrixWorldInverse = Matrix4(default_value=[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]).tag(sync=True)

    projectionMatrix = Matrix4(default_value=[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]).tag(sync=True)

    type = Unicode("Camera", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
Camera.__signature__ = inspect.signature(Camera.__init__)
