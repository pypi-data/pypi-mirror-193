"""


bpy.utils submodule (bpy.utils.previews)
****************************************

This module contains utility functions to handle custom previews.

It behaves as a high-level 'cached' previews manager.

This allows scripts to generate their own previews, and use them as icons in UI widgets
('icon_value' for UILayout functions).


Custom Icon Example
===================

:func:`new`

:func:`remove`

:class:`ImagePreviewCollection`

"""

import typing

import bpy

def new() -> ImagePreviewCollection:

  ...

def remove(pcoll: ImagePreviewCollection) -> None:

  """

  Remove the specified previews collection.

  """

  ...

class ImagePreviewCollection:

  """

  Dictionary-like class of previews.

  This is a subclass of Python's built-in dict type,
used to store multiple image previews.

  Note: * instance with :mod:`bpy.utils.previews.new`

    * keys must be ``str`` type.

    * values will be :class:`bpy.types.ImagePreview`

  """

  def clear(self) -> None:

    """

    Clear all previews.

    """

    ...

  def close(self) -> None:

    """

    Close the collection and clear all previews.

    """

    ...

  def load(self, name: str, filepath: str, filetype: str, force_reload: bool = False) -> bpy.types.ImagePreview:

    """

    Generate a new preview from given file path.

    """

    ...

  def new(self, name: str) -> bpy.types.ImagePreview:

    """

    Generate a new empty preview.

    """

    ...
