
.. py:currentmodule:: pythreejs

PerspectiveCamera
====================================================

.. Use autoclass to fill any memebers not manually specified.
   This ensures it picks up any members in overridden classes.

.. autohastraits:: PerspectiveCamera(fov=50, aspect=1, near=0.1, far=2000, )
    :members:
    :undoc-members:


    Inherits :py:class:`~pythreejs.Camera`.

    Three.js docs: https://threejs.org/docs/#api/cameras/PerspectiveCamera


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

    .. py:attribute:: focus


        .. sourcecode:: python

            IEEEFloat(10, allow_none=False).tag(sync=True)

    .. py:attribute:: aspect


        .. sourcecode:: python

            IEEEFloat(1, allow_none=False).tag(sync=True)

    .. py:attribute:: type


        .. sourcecode:: python

            Unicode("PerspectiveCamera", allow_none=False).tag(sync=True)

