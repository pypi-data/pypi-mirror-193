# Jupyter XBlock

This is an [XBlock](https://edx.readthedocs.io/projects/xblock-tutorial/en/latest/overview/introduction.html) to integrate JupyterHub notebooks to your [Open edX](https://openedx.org) learning management system (LMS).

> ⚠️ THIS IS A WORK-IN_PROGRESS! We expect to release a first stable version sometime in March 2023.

Features:

* Integrate [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) notebooks to the Open edX courseware.
* Fully editable notebooks and student workspaces.
* Simple integration of notebooks from public git repositories.


## Usage

Install this xblock with [Tutor](https://docs.tutor.overhang.io/) (Olive release):

    echo "jupyter-xblock>=15.0.0,<16.0.0" >> "$(tutor config printroot)/env/build/openedx/requirements/private.txt"
    tutor images build openedx
    tutor local start -d

Note that you will have to launch your own JupyterHub cluster separately. It should support LTI authentication via [ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator/).


## License

This work is licensed under the terms of the [GNU Affero General Public License (AGPL)](https://github.com/overhangio/jupyter-xblock/blob/master/LICENSE.txt).
