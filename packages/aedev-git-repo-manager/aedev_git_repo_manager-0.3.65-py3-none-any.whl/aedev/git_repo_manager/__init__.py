"""
create and maintain local/remote git repositories of Python projects
====================================================================

this module provides the ``grm`` tool. this document explains how to change/extend the code base of this tool.

detailed information on the installation and usage of this tool are available `in a separate user manual document
<https://aedev.readthedocs.io/en/latest/man/git_repo_manager.html>`__.


define a new action
-------------------

to add a new action you only need to declare a new method or function decorated with the :func:`_action` decorator. the
decorator will automatically register and integrate the new action into the ``grm`` tool.


file patching helper functions
------------------------------

this portion is also providing some helper functions to patch code and documentation files.

the functions :func:`~aedev.git_repo_manager.bump_file_version`, :func:`~aedev.git_repo_manager.increment_version`,
:func:`~aedev.git_repo_manager.next_package_version` and :func:`~aedev.git_repo_manager.replace_file_version`
are incrementing any part of a version number of a module, portion, app or package.

templates are patched with the help of the functions :func:`~aedev.git_repo_manager.deploy_template`,
:func:`~aedev.git_repo_manager.patch_string` and :func:`~aedev.git_repo_manager.refresh_templates`.

in conjunction with the template projects of the `aedev` namespace (like e.g. :mod:`aedev.tpl_project`) any common
portions file (even the ``setup.py`` file) can be created/maintained as a template in a single place, and then requested
and updated individually for each portion project.
"""


__version__ = '0.3.65'
