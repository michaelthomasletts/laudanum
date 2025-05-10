.. image:: laudanum.png
   :align: center

|

.. toctree::
   :maxdepth: 1
   :hidden:

   CLI <cli>
   Modules <modules>

.. currentmodule:: laudanum

**Version:** |release|

**Helpful Links:**
:ref:`CLI Reference <cli>` |
:ref:`Module Reference <modules>`

**Author:** `Mike Letts <https://michaelthomasletts.github.io/>`_

**Description:** A simple Python package and CLI tool for easily creating logos with `ASCII art <https://www.ascii-art.site/FontList.html>`_.

Installation
------------

.. code-block:: bash

   pip install laudanum

Usage
-----

To mimic laudanum's logo.

.. code-block:: python

   from laudanum import Logo

   logo = Logo(
      text="laudanum",
      font="colossal",
      font_size=13,
      font_color=(245, 40, 145, 255),
   )
   logo.create()

To keep things simple.

.. code-block:: python

   logo = Logo("laudanum")
   logo.create()

Prefer the termianl? No problem.

.. code-block:: bash

   laudanum --text laudanum --font colossal --fontsize 13 --fontcolor 245 40 145 255


Good to Know
------------

Only PNG images can be created with laudanum. Transparent backgrounds FTW.

The size of the resultant logo is relative to the size of the rendered ASCII art. Resizing cannot be accomplished with laudanum for right now. 
Resize yourself in the meantime with another tool.

Every font in the `art font gallery <https://www.ascii-art.site/FontList.html>`_ is available through laudanum.

The default character font file can be found in the fonts/ submodule of this package. Use the ``font_path`` parameter for :class:`laudanum.logo.Logo` if you prefer something else.