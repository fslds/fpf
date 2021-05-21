*******************
File Path Filtering
*******************

Filter Paths in Python the easy way.

This library aims to provide simple means to filter file paths.


The base function: `filter_file_paths`
######################################


`filter_file_paths` takes in three arguments:

* `root_dir`:  the directory to start searching in
* `path_filter`: a function (`callable`) that should return true for any path/filename encountered that should be kept.
* `relative_paths`: default set to `True`, resulting in relative paths of matched files (with base `root_dir`).
    If set to `False`, absolute paths will be returned.

``filename_filter``
--------------------

``file_path_filter`` can be a simple function:


.. code-block:: python

   def filter(filepath):
      return filepath.lower().endswith('.py'):

   # Or, for those that like to use lambda:
   lambda x: x.lower().endswith('.py)


Applying a filter like like this on a directory should return only python file filepaths.
Easy enough.

But there are advanced usecases.
Consider our (simplified) project directory:


.. code-block:: console

   .
   ├── build
   │   └── lib
   │       └── fpf
   │           ├── filters.py
   │           ├── __init__.py
   │           ├── logger.py
   │           └── mixins.py
   ├── fpf
   │   ├── filters.py
   │   ├── __init__.py
   │   ├── logger.py
   │   └── mixins.py
   ├── LICENSE
   ├── README.md
   ├── setup.cfg
   ├── setup.py
   ├── tests
   │  ├── __init__.py
   │  └── test_fpf.py
   ├── .gitignore
   └── .travis.yml

Applying the filter, would give us the following result:

.. code-block:: python

   from fpf import file_path_filter

   for path in file_path_filter(root_dir='.', path_filter=filter ):
      print(path)


.. code-block:: console

   build/lib/fpf/__init__.py
   build/lib/fpf/filters.py
   ...
   fpf/__init__.py
   fpf/filters.py
   ...
   tests/__init__.py
   setup.py

* Q: But what if I am not interested in build artifacts or tests?
* A: You can add more conditions to ``filter(filepath)``
* Q: Does that scale?
* A: No
* Q: Is a list of exceptions easy to maintain?
* A: No
* Q: Is creating a library to deal with these usecases overkill?
* A: Maybe. But is too late now.


Introducing ignore files
-------------------------

The Git project and their users had the same issue. They solved this with the `.gitignore(pathspec)  file <https://git-scm.com/docs/gitignore>`_.

This library offers some helper classes and functions to apply this to your project.

