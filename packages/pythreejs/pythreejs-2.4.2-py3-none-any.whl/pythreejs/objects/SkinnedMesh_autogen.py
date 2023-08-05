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

from .Mesh_autogen import Mesh

from .Skeleton_autogen import Skeleton

@register
class SkinnedMesh(Mesh):
    """SkinnedMesh

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/objects/SkinnedMesh
    """

    def __init__(self, geometry=None, material=[], **kwargs):
        kwargs['geometry'] = geometry
        kwargs['material'] = material
        super(SkinnedMesh, self).__init__(**kwargs)

    _model_name = Unicode('SkinnedMeshModel').tag(sync=True)

    bindMode = Unicode("attached", allow_none=False).tag(sync=True)

    bindMatrix = Matrix4(default_value=[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]).tag(sync=True)

    skeleton = Instance(Skeleton, allow_none=True).tag(sync=True, **widget_serialization)

    type = Unicode("SkinnedMesh", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
SkinnedMesh.__signature__ = inspect.signature(SkinnedMesh.__init__)
