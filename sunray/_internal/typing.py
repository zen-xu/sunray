from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import types

    from typing import Any
    from typing import Union

    from ray import runtime_env
    from ray.util import scheduling_strategies
    from typing_extensions import Literal
    from typing_extensions import NotRequired
    from typing_extensions import Required
    from typing_extensions import TypedDict

    SchedulingStrategy = Union[
        Literal["DEFAULT", "SPREAD"],
        scheduling_strategies.PlacementGroupSchedulingStrategy,
        scheduling_strategies.NodeAffinitySchedulingStrategy,
        scheduling_strategies.NodeLabelSchedulingStrategy,
        None,
    ]

    class ActorRemoteOptions(TypedDict, total=False):
        num_cpus: float
        num_gpus: float
        resources: dict[str, float]
        accelerator_type: str
        memory: float
        object_store_memory: float
        max_restarts: int
        max_task_retries: int
        max_pending_calls: int
        max_concurrency: int
        name: str
        namespace: str
        lifetime: Literal["detached"] | None
        runtime_env: RuntimeEnv | dict[str, Any]
        concurrency_groups: dict[str, int]
        scheduling_strategy: SchedulingStrategy

    class FunctionRemoteOptions(TypedDict, total=False):
        num_cpus: float
        num_gpus: float
        resources: dict[str, float]
        accelerator_type: str
        memory: float
        object_store_memory: float
        max_calls: int
        max_retries: int
        runtime_env: RuntimeEnv | dict[str, Any]
        retry_exceptions: list[type[Exception]]
        scheduling_strategy: SchedulingStrategy

    class RayInitOpts(TypedDict, total=False):
        labels: dict[str, str]
        namespace: str
        runtime_env: RuntimeEnv | dict[str, Any]

    class RuntimeEnv(TypedDict, total=False):
        working_dir: str
        """
        Specifies the working directory for the Ray workers. This must either be (1) an local existing directory with total size at most 100 MiB, (2) a local existing zipped file with total unzipped size at most 100 MiB (Note: ``excludes`` has no effect), or (3) a URI to a remotely-stored zip file containing the working directory for your job (no file size limit is enforced by Ray). See :ref:`remote-uris` for details.
        The specified directory will be downloaded to each node on the cluster, and Ray workers will be started in their node's copy of this directory.

        - Examples

            - ``"."  # cwd``

            - ``"/src/my_project"``

            - ``"/src/my_project.zip"``

            - ``"s3://path/to/my_dir.zip"``

        Note: Setting a local directory per-task or per-actor is currently unsupported; it can only be set per-job (i.e., in ``ray.init()``).

        Note: If the local directory contains a ``.gitignore`` file, the files and paths specified there are not uploaded to the cluster.  You can disable this by setting the environment variable `RAY_RUNTIME_ENV_IGNORE_GITIGNORE=1` on the machine doing the uploading.
        """

        py_modules: list[str | types.ModuleType]
        """
        Specifies Python modules to be available for import in the Ray workers.  (For more ways to specify packages, see also the ``pip`` and ``conda`` fields below.)
        Each entry must be either (1) a path to a local directory, (2) a URI to a remote zip or wheel file (see :ref:`remote-uris` for details), (3) a Python module object, or (4) a path to a local `.whl` file.

        - Examples of entries in the list:

            - ``"."``

            - ``"/local_dependency/my_module"``

            - ``"s3://bucket/my_module.zip"``

            - ``my_module # Assumes my_module has already been imported, e.g. via 'import my_module'``

            - ``my_module.whl``

            - ``"s3://bucket/my_module.whl"``

        The modules will be downloaded to each node on the cluster.

        Note: Setting options (1), (3) and (4) per-task or per-actor is currently unsupported, it can only be set per-job (i.e., in ``ray.init()``).

        Note: For option (1), if the local directory contains a ``.gitignore`` file, the files and paths specified there are not uploaded to the cluster.  You can disable this by setting the environment variable `RAY_RUNTIME_ENV_IGNORE_GITIGNORE=1` on the machine doing the uploading.

        Note: This feature is currently limited to modules that are packages with a single directory containing an ``__init__.py`` file.  For single-file modules, you may use ``working_dir``.
        """

        excludes: list[str]
        """
        When used with ``working_dir`` or ``py_modules``, specifies a list of files or paths to exclude from being uploaded to the cluster.

        This field uses the pattern-matching syntax used by ``.gitignore`` files: see `<https://git-scm.com/docs/gitignore>`_ for details.

        Note: In accordance with ``.gitignore`` syntax, if there is a separator (``/``) at the beginning or middle (or both) of the pattern, then the pattern is interpreted relative to the level of the ``working_dir``.

        In particular, you shouldn't use absolute paths (e.g. `/Users/my_working_dir/subdir/`) with `excludes`; rather, you should use the relative path `/subdir/` (written here with a leading `/` to match only the top-level `subdir` directory, rather than all directories named `subdir` at all levels.)

        - Example: ``{"working_dir": "/Users/my_working_dir/", "excludes": ["my_file.txt", "/subdir/, "path/to/dir", "*.log"]}``
        """

        pip: list[str] | str | PipConf
        """
        Either (1) a list of pip `requirements specifiers <https://pip.pypa.io/en/stable/cli/pip_install/#requirement-specifiers>`_, (2) a string containing the path to a local pip
        `“requirements.txt” <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`_ file, or (3) a python dictionary that has three fields: (a) ``packages`` (required, List[str]): a list of pip packages,
        (b) ``pip_check`` (optional, bool): whether to enable `pip check <https://pip.pypa.io/en/stable/cli/pip_check/>`_ at the end of pip install, defaults to ``False``.
        (c) ``pip_version`` (optional, str): the version of pip; Ray will spell the package name "pip" in front of the ``pip_version`` to form the final requirement string.
        The syntax of a requirement specifier is defined in full in `PEP 508 <https://www.python.org/dev/peps/pep-0508/>`_.
        This will be installed in the Ray workers at runtime.  Packages in the preinstalled cluster environment will still be available.
        To use a library like Ray Serve or Ray Tune, you will need to include ``"ray[serve]"`` or ``"ray[tune]"`` here.
        The Ray version must match that of the cluster.

        - Example: ``["requests==1.0.0", "aiohttp", "ray[serve]"]``

        - Example: ``"./requirements.txt"``

        - Example: ``{"packages":["tensorflow", "requests"], "pip_check": False, "pip_version": "==22.0.2;python_version=='3.8.11'"}``

        When specifying a path to a ``requirements.txt`` file, the file must be present on your local machine and it must be a valid absolute path or relative filepath relative to your local current working directory, *not* relative to the `working_dir` specified in the `runtime_env`.
        Furthermore, referencing local files `within` a `requirements.txt` file is not supported (e.g., ``-r ./my-laptop/more-requirements.txt``, ``./my-pkg.whl``).
        """

        conda: str | dict
        """
        Either (1) a dict representing the conda environment YAML, (2) a string containing the path to a local
        `conda “environment.yml” <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually>`_ file,
        or (3) the name of a local conda environment already installed on each node in your cluster (e.g., ``"pytorch_p36"``).
        In the first two cases, the Ray and Python dependencies will be automatically injected into the environment to ensure compatibility, so there is no need to manually include them.
        The Python and Ray version must match that of the cluster, so you likely should not specify them manually.
        Note that the ``conda`` and ``pip`` keys of ``runtime_env`` cannot both be specified at the same time---to use them together, please use ``conda`` and add your pip dependencies in the ``"pip"`` field in your conda ``environment.yaml``.

        - Example: ``{"dependencies": ["pytorch", "torchvision", "pip", {"pip": ["pendulum"]}]}``

        - Example: ``"./environment.yml"``

        - Example: ``"pytorch_p36"``

        When specifying a path to a ``environment.yml`` file, the file must be present on your local machine and it must be a valid absolute path or a relative filepath relative to your local current working directory, *not* relative to the `working_dir` specified in the `runtime_env`.
        Furthermore, referencing local files `within` a `environment.yml` file is not supported.
        """

        env_vars: dict[str, str]
        """
        Environment variables to set.  Environment variables already set on the cluster will still be visible to the Ray workers; so there is
        no need to include ``os.environ`` or similar in the ``env_vars`` field.
        By default, these environment variables override the same name environment variables on the cluster.
        You can also reference existing environment variables using ${ENV_VAR} to achieve the appending behavior.
        If the environment variable doesn't exist, it becomes an empty string `""`.

        - Example: ``{"OMP_NUM_THREADS": "32", "TF_WARNINGS": "none"}``

        - Example: ``{"LD_LIBRARY_PATH": "${LD_LIBRARY_PATH}:/home/admin/my_lib"}``

        - Non-existent variable example: ``{"ENV_VAR_NOT_EXIST": "${ENV_VAR_NOT_EXIST}:/home/admin/my_lib"}`` -> ``ENV_VAR_NOT_EXIST=":/home/admin/my_lib"``.
        """

        config: RuntimeEnvConfig | runtime_env.RuntimeEnvConfig
        """
        - ``config`` (dict | :class:`ray.runtime_env.RuntimeEnvConfig <ray.runtime_env.RuntimeEnvConfig>`): config for runtime environment. Either a dict or a RuntimeEnvConfig.
        Fields:
        (1) setup_timeout_seconds, the timeout of runtime environment creation, timeout is in seconds.

        - Example: ``{"setup_timeout_seconds": 10}``

        - Example: ``RuntimeEnvConfig(setup_timeout_seconds=10)``

        (2) ``eager_install`` (bool): Indicates whether to install the runtime environment on the cluster at ``ray.init()`` time, before the workers are leased. This flag is set to ``True`` by default.
        If set to ``False``, the runtime environment will be only installed when the first task is invoked or when the first actor is created.
        Currently, specifying this option per-actor or per-task is not supported.

        - Example: ``{"eager_install": False}``

        - Example: ``RuntimeEnvConfig(eager_install=False)``
        """

    class PipConf(TypedDict):
        packages: Required[list[str]]
        pip_check: NotRequired[bool]
        pip_version: NotRequired[str]

    class RuntimeEnvConfig(TypedDict, total=False):
        setup_timeout_seconds: int
        eager_install: bool
