
.. py:currentmodule:: pythreejs

SpotLight
====================================================

.. Use autoclass to fill any memebers not manually specified.
   This ensures it picks up any members in overridden classes.

.. autohastraits:: SpotLight(color="#ffffff", intensity=1, distance=0, angle=1.0471975511965976, penumbra=0, decay=1, )
    :members:
    :undoc-members:


    Inherits :py:class:`~pythreejs.Light`.

    Three.js docs: https://threejs.org/docs/#api/lights/SpotLight


    .. py:attribute:: target


        .. sourcecode:: python

            Union([
                Instance(Uninitialized),
                Instance(Object3D),
                ], default_value=UninitializedSentinel, allow_none=False).tag(sync=True, **unitialized_serialization)

    .. py:attribute:: distance


        .. sourcecode:: python

            IEEEFloat(0, allow_none=False).tag(sync=True)

    .. py:attribute:: angle


        .. sourcecode:: python

            IEEEFloat(1.0471975511965976, allow_none=False).tag(sync=True)

    .. py:attribute:: penumbra


        .. sourcecode:: python

            IEEEFloat(0, allow_none=False).tag(sync=True)

    .. py:attribute:: decay


        .. sourcecode:: python

            IEEEFloat(1, allow_none=False).tag(sync=True)

    .. py:attribute:: shadow


        .. sourcecode:: python

            Union([
                Instance(Uninitialized),
                Instance(LightShadow),
                ], default_value=UninitializedSentinel, allow_none=False).tag(sync=True, **unitialized_serialization)

    .. py:attribute:: type


        .. sourcecode:: python

            Unicode("SpotLight", allow_none=False).tag(sync=True)

