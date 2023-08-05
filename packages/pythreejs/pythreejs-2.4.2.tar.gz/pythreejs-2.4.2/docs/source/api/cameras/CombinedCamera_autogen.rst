
.. py:currentmodule:: pythreejs

CombinedCamera
====================================================

.. Use autoclass to fill any memebers not manually specified.
   This ensures it picks up any members in overridden classes.

.. autohastraits:: CombinedCamera(width=0, height=0, fov=50, near=0.1, far=2000, orthoNear=0.1, orthoFar=2000, )
    :members:
    :undoc-members:


    Inherits :py:class:`~pythreejs.Camera`.

    Three.js docs: https://threejs.org/docs/#api/cameras/CombinedCamera


    .. py:attribute:: fov


        .. sourcecode:: python

            IEEEFloat(50, allow_none=False).tag(sync=True)

    .. py:attribute:: zoom


        .. sourcecode:: python

            IEEEFloat(1, allow_none=False).tag(sync=True)

    .. py:attribute:: near


        .. sourcecode:: python

            IEEEFloat(0.1, allow_none=False).tag(sync=True)

    .. py:attribute:: far


        .. sourcecode:: python

            IEEEFloat(2000, allow_none=False).tag(sync=True)

    .. py:attribute:: orthoNear


        .. sourcecode:: python

            IEEEFloat(0.1, allow_none=False).tag(sync=True)

    .. py:attribute:: orthoFar


        .. sourcecode:: python

            IEEEFloat(2000, allow_none=False).tag(sync=True)

    .. py:attribute:: width


        .. sourcecode:: python

            IEEEFloat(0, allow_none=False).tag(sync=True)

    .. py:attribute:: height


        .. sourcecode:: python

            IEEEFloat(0, allow_none=False).tag(sync=True)

    .. py:attribute:: mode


        .. sourcecode:: python

            Enum(['perspective', 'orthographic'], "perspective", allow_none=False).tag(sync=True)

    .. py:attribute:: impersonate


        .. sourcecode:: python

            Bool(True, allow_none=False).tag(sync=True)

    .. py:attribute:: type


        .. sourcecode:: python

            Unicode("CombinedCamera", allow_none=False).tag(sync=True)

