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

from .Material import Material

from ..textures.Texture_autogen import Texture

@register
class MeshDepthMaterial(Material):
    """MeshDepthMaterial

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/materials/MeshDepthMaterial
    """

    _model_name = Unicode('MeshDepthMaterialModel').tag(sync=True)

    alphaMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)

    displacementMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)

    displacementScale = IEEEFloat(1, allow_none=False).tag(sync=True)

    displacementBias = IEEEFloat(0, allow_none=False).tag(sync=True)

    fog = Bool(False, allow_none=False).tag(sync=True)

    lights = Bool(False, allow_none=False).tag(sync=True)

    map = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)

    morphTargets = Bool(False, allow_none=False).tag(sync=True)

    skinning = Bool(False, allow_none=False).tag(sync=True)

    wireframe = Bool(False, allow_none=False).tag(sync=True)

    wireframeLinewidth = IEEEFloat(1, allow_none=False).tag(sync=True)

    type = Unicode("MeshDepthMaterial", allow_none=False).tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
MeshDepthMaterial.__signature__ = inspect.signature(MeshDepthMaterial.__init__)
