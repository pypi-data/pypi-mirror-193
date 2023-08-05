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

from ..KeyframeTrack_autogen import KeyframeTrack


@register
class StringKeyframeTrack(KeyframeTrack):
    """StringKeyframeTrack

    Autogenerated by generate-wrappers.js
    See https://threejs.org/docs/#api/animation/tracks/StringKeyframeTrack
    """

    def __init__(self, name="", times=None, values=None, interpolation="InterpolateLinear", **kwargs):
        kwargs['name'] = name
        kwargs['times'] = times
        kwargs['values'] = values
        kwargs['interpolation'] = interpolation
        super(StringKeyframeTrack, self).__init__(**kwargs)

    _model_name = Unicode('StringKeyframeTrackModel').tag(sync=True)


import inspect
# Include explicit signature since the metaclass screws it up
StringKeyframeTrack.__signature__ = inspect.signature(StringKeyframeTrack.__init__)
