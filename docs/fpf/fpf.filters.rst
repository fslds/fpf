===============
``fpf.filters``
===============

.. automodule:: fpf.filters

   .. contents::
      :local:

.. currentmodule:: fpf.filters


Classes
=======

- :py:class:`ExtensionFileFilter`:
  Filter files based on a match of the file extensions.

- :py:class:`IgnoreFileFilter`:
  Filter files based on an ignore file like `.gitignore`.

- :py:class:`PathSpecWildcardFileFilter`:
  Filter files based on PathSpec WildMatch (`.gitignore`).

- :py:class:`YamlIgnoreFileFilter`:
  Filter YAML files(`.yml, .yaml`) based on pathspec wildcard file(gitignore style).

- :py:class:`YamlPathSpecFilter`:
  Filter YAML files (.yml, .yaml) based on pathspec wildcards (gitignore style).


.. autoclass:: ExtensionFileFilter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: ExtensionFileFilter
      :parts: 1

.. autoclass:: IgnoreFileFilter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: IgnoreFileFilter
      :parts: 1

.. autoclass:: PathSpecWildcardFileFilter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: PathSpecWildcardFileFilter
      :parts: 1

.. autoclass:: YamlIgnoreFileFilter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: YamlIgnoreFileFilter
      :parts: 1

.. autoclass:: YamlPathSpecFilter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: YamlPathSpecFilter
      :parts: 1
