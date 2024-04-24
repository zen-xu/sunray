# ruff: noqa: E402, F401
# mypy: disable-error-code="no-overload-impl"

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Generic
from typing import TypeVar
from typing import overload

import ray
import ray.runtime_context


if TYPE_CHECKING:
    import asyncio
    import concurrent.futures
    import enum

    from pathlib import Path
    from typing import Any
    from typing import Callable
    from typing import Generator
    from typing import Self
    from typing import TypedDict

    import ray.actor

    from ray._private.worker import BaseContext
    from ray.job_config import JobConfig
    from typing_extensions import deprecated

    from . import actor_mixin
    from .typing import RuntimeEnv


_T = TypeVar("_T")

_R = TypeVar("_R")
_R0 = TypeVar("_R0")
_R1 = TypeVar("_R1")
_R2 = TypeVar("_R2")
_R3 = TypeVar("_R3")
_R4 = TypeVar("_R4")
_R5 = TypeVar("_R5")
_R6 = TypeVar("_R6")
_R7 = TypeVar("_R7")
_R8 = TypeVar("_R8")
_R9 = TypeVar("_R9")


if TYPE_CHECKING:

    class _BaseID:
        def binary(self) -> bytes: ...
        def hex(self) -> str: ...
        def is_nill(self) -> bool: ...
        def redis_shard_hash(self) -> int: ...
        @classmethod
        def size(cls) -> int: ...

    class ActorID(_BaseID):
        @classmethod
        def of(
            cls, job_id: JobID, parent_task_id: TaskID, parent_task_counter: int
        ) -> Self: ...
        @classmethod
        def nil(cls) -> Self: ...
        @classmethod
        def from_random(cls) -> Self: ...
        @property
        def job_id(self) -> JobID: ...
        def _set_id(self, id: bytes): ...

    class UniqueID(_BaseID): ...

    class TaskID(_BaseID):
        def actor_id(self) -> ActorID: ...
        def job_id(self) -> JobID: ...
        @classmethod
        def for_actor_creation_task(cls, actor_id: ActorID) -> Self: ...
        @classmethod
        def for_actor_task(
            cls,
            job_id: JobID,
            parent_task_id: TaskID,
            parent_task_counter: int,
            actor_id: ActorID,
        ) -> Self: ...
        @classmethod
        def for_driver_task(cls, job_id: JobID) -> Self: ...
        @classmethod
        def for_fake_task(cls, job_id: JobID) -> Self: ...
        @classmethod
        def for_normal_task(
            cls, job_id: JobID, parent_task_id: TaskID, parent_task_counter: int
        ) -> Self: ...

    class JobID(_BaseID):
        @classmethod
        def from_int(cls, value: int): ...
        def int(self) -> int: ...

    class PlacementGroupID(_BaseID):
        @classmethod
        def of(cls, job_id: JobID) -> Self: ...
        @classmethod
        def from_random(cls) -> Self: ...
        @classmethod
        def nil(cls) -> Self: ...

    class ActorClassID(UniqueID): ...

    class NodeID(UniqueID): ...

    class WorkerID(UniqueID): ...

    class FunctionID(UniqueID): ...

    class ObjectRef(_BaseID, ray.ObjectRef[_R]):
        def as_future(self, _internal: bool = False) -> asyncio.Future[_R]: ...
        def future(self) -> concurrent.futures.Future[_R]: ...
        def job_id(self) -> JobID: ...
        def task_id(self) -> TaskID: ...
        def owner_address(self) -> bytes: ...
        def call_site(self) -> str: ...
        @classmethod
        def from_random(cls) -> Self: ...
        @classmethod
        def nil(cls) -> Self: ...
        def __await__(self) -> Generator[None, None, _R]: ...

    class ObjectRefGenerator(Generator[ObjectRef[_R], None, None]):
        def __aiter__(self) -> Self: ...

        async def __anext__(self) -> ObjectRef[_R]: ...

        def completed(self) -> ObjectRef[_R]: ...

        def next_ready(self) -> bool: ...

        def is_finished(self) -> bool: ...

    def method(
        *,
        num_returns: int = ...,
        concurrency_group: str = ...,
        max_task_retries: int = ...,
        retry_exceptions: bool | list[type[Exception]] = ...,
        enable_task_events: bool = ...,
        _generator_backpressure_num_objects=...,
    ) -> Callable[[_T], _T]: ...

    @overload
    def get(
        __object_refs: ObjectRef[_R0],
        *,
        timeout: float = ...,
    ) -> _R0: ...
    @overload
    def get(
        __object_refs: tuple[ObjectRef[_R0], ObjectRef[_R1]],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1]: ...
    @overload
    def get(
        __object_refs: tuple[ObjectRef[_R0], ObjectRef[_R1], ObjectRef[_R2]],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2]: ...
    @overload
    def get(
        __object_refs: tuple[
            ObjectRef[_R0],
            ObjectRef[_R1],
            ObjectRef[_R2],
            ObjectRef[_R3],
        ],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2, _R3]: ...
    @overload
    def get(
        __object_refs: tuple[
            ObjectRef[_R0],
            ObjectRef[_R1],
            ObjectRef[_R2],
            ObjectRef[_R3],
            ObjectRef[_R4],
        ],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2, _R3, _R4]: ...
    @overload
    def get(
        __object_refs: tuple[
            ObjectRef[_R0],
            ObjectRef[_R1],
            ObjectRef[_R2],
            ObjectRef[_R3],
            ObjectRef[_R4],
            ObjectRef[_R5],
        ],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2, _R3, _R4, _R5]: ...
    @overload
    def get(
        __object_refs: tuple[
            ObjectRef[_R0],
            ObjectRef[_R1],
            ObjectRef[_R2],
            ObjectRef[_R3],
            ObjectRef[_R4],
            ObjectRef[_R5],
            ObjectRef[_R6],
        ],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6]: ...
    @overload
    def get(
        __object_refs: tuple[
            ObjectRef[_R0],
            ObjectRef[_R1],
            ObjectRef[_R2],
            ObjectRef[_R3],
            ObjectRef[_R4],
            ObjectRef[_R5],
            ObjectRef[_R6],
            ObjectRef[_R7],
        ],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7]: ...
    @overload
    def get(
        __object_refs: tuple[
            ObjectRef[_R0],
            ObjectRef[_R1],
            ObjectRef[_R2],
            ObjectRef[_R3],
            ObjectRef[_R4],
            ObjectRef[_R5],
            ObjectRef[_R6],
            ObjectRef[_R7],
            ObjectRef[_R8],
        ],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8]: ...
    @overload
    def get(
        __object_refs: tuple[
            ObjectRef[_R0],
            ObjectRef[_R1],
            ObjectRef[_R2],
            ObjectRef[_R3],
            ObjectRef[_R4],
            ObjectRef[_R5],
            ObjectRef[_R6],
            ObjectRef[_R7],
            ObjectRef[_R8],
            ObjectRef[_R9],
        ],
        *,
        timeout: float = ...,
    ) -> tuple[_R0, _R1, _R2, _R3, _R4, _R5, _R6, _R7, _R8, _R9]: ...
    @overload
    def get(
        __object_refs: list[ObjectRef[_R0]],
        *,
        timeout: float | None = ...,
    ) -> tuple[_R0, ...]: ...
    @overload
    def get(
        __object_refs: list[ObjectRef],
        *,
        timeout: float | None = ...,
    ) -> tuple: ...

    def put(value: _T, *, _owner: ray.actor.ActorHandle = ...) -> ObjectRef[_T]: ...

    @overload
    def wait(
        object_refs: list[ObjectRef[_T]],
        *,
        num_returns: int = ...,
        timeout: float | None = ...,
        fetch_local: bool = ...,
    ) -> tuple[list[ObjectRef[_T]], list[ObjectRef[_T]]]: ...
    @overload
    def wait(
        object_refs: list[ObjectRef],
        *,
        num_returns: int = ...,
        timeout: float | None = ...,
        fetch_local: bool = ...,
    ) -> tuple[list[ObjectRef], list[ObjectRef]]: ...

    class Language(enum.IntEnum):
        JAVA = 1
        CPP = 2
        PYTHON = 3

    class RuntimeContext(ray.runtime_context.RuntimeContext):
        @deprecated("Use get_xxx_id() methods to get relevant ids instead.")
        def get(self) -> dict[str, Any]: ...

        @property
        @deprecated("Use get_job_id() instead.")
        def job_id(self) -> JobID: ...

        @property
        @deprecated("Use get_node_id() instead.")
        def node_id(self) -> NodeID: ...

        @property
        @deprecated("Use get_task_id() instead.")
        def task_id(self) -> TaskID | None: ...

        @property
        @deprecated("Use get_actor_id() instead")
        def actor_id(self) -> ActorID | None: ...

        @property
        def namespace(self) -> str: ...

        @property
        def was_current_actor_reconstructed(self) -> bool: ...

        @property
        @deprecated("Use get_placement_group_id() instead.")
        def current_placement_group_id(self) -> PlacementGroupID | None: ...

        @property
        def should_capture_child_tasks_in_placement_group(self) -> bool: ...

        def get_assigned_resources(self) -> dict[str, float]: ...

        def get_runtime_env_string(self) -> RuntimeEnv: ...

        @property
        def runtime_env(self) -> RuntimeEnv: ...

        @property
        def current_actor(self) -> ray.actor.ActorHandle: ...

        @property
        def gcs_address(self) -> str: ...

        @property
        @deprecated("Use get_accelerator_ids() instead.")
        def get_resource_ids(self) -> dict[str, list[str]]:
            return super().get_resource_ids()

    def get_runtime_context() -> RuntimeContext: ...

    @deprecated("Use ray.init instead")
    class ClientBuilder(ray.ClientBuilder): ...

    def available_resources() -> dict[str, float]: ...

    def cluster_resources() -> dict[str, float]: ...

    class NodeInfo(TypedDict):
        NodeID: str
        Alive: bool
        NodeManagerAddress: str
        NodeManagerHostname: str
        NodeManagerPort: int
        ObjectManagerPort: int
        ObjectStoreSocketName: str
        RayletSocketName: str
        MetricsExportPort: int
        NodeName: str
        RuntimeEnvAgentPort: int
        alive: bool
        Resources: dict[str, float]
        Labels: dict[str, str]

    def nodes() -> list[NodeInfo]: ...

    class ProfileEvent(TypedDict):
        cat: str
        "The category of the event."

        name: str
        "The string displayed on the event"

        pid: str
        "The identifier for the group of rows that the event appears in"

        tid: int
        "The identifier for the row that the event appears in."

        ts: float
        "The start time in microseconds."

        dur: float
        "The duration in microseconds."

        ph: str
        "What is this?"

        cname: str
        "This is the name of the color to display the box in."

        args: dict[str, Any]
        "The extra user-defined data."

    @overload
    def timeline(filename: str | Path) -> None: ...

    @overload
    def timeline(filename: None = None) -> list[ProfileEvent]: ...

    def cancel(
        ray_waitable: ObjectRef[_R] | ObjectRefGenerator[_R],
        *,
        force: bool = False,
        recursive: bool = True,
    ) -> None: ...

    def get_gpu_ids() -> list[int] | list[str]: ...

    def init(
        address: str | None = None,
        *,
        num_cpus: int | None = None,
        num_gpus: int | None = None,
        resources: dict[str, float] | None = None,
        labels: dict[str, str] | None = None,
        object_store_memory: int | None = None,
        local_mode: bool = False,
        ignore_reinit_error: bool = False,
        include_dashboard: bool | None = None,
        dashboard_host: str = ...,
        dashboard_port: int | None = None,
        job_config: JobConfig | None = None,
        configure_logging: bool = True,
        logging_level: int = ...,
        logging_format: str | None = None,
        log_to_driver: bool = True,
        namespace: str | None = None,
        runtime_env: RuntimeEnv | None = None,
        storage: str | None = None,
        **kwargs,
    ) -> BaseContext: ...

    def is_initialized() -> bool: ...

    def shutdown(_exiting_interpreter: bool = False) -> None: ...
else:
    import ray

    ActorID = ray.ActorID
    UniqueID = ray.UniqueID
    TaskID = ray.TaskID
    JobID = ray.JobID
    PlacementGroupID = ray.PlacementGroupID
    ActorClassID = ray.ActorClassID
    NodeID = ray.NodeID
    WorkerID = ray.WorkerID
    FunctionID = ray.FunctionID
    ObjectRefGenerator = ray.ObjectRefGenerator
    ObjectRef = ray.ObjectRef

    method = ray.method

    def get(
        __object_refs,
        *,
        timeout: float | None = None,
    ):
        if isinstance(__object_refs, ObjectRef):
            return ray.get(__object_refs, timeout=timeout)
        return tuple(ray.get(list(__object_refs), timeout=timeout))

    put = ray.put
    wait = ray.wait
    Language = ray.Language
    get_runtime_context = ray.get_runtime_context
    ClientBuilder = ray.ClientBuilder
    available_resources = ray.available_resources
    cluster_resources = ray.cluster_resources
    nodes = ray.nodes
    timeline = ray.timeline
    cancel = ray.cancel
    get_gpu_ids = ray.get_gpu_ids
    init = ray.init
    is_initialized = ray.is_initialized
    shutdown = ray.shutdown


ObjectID = ObjectRef

_ActorMixinT = TypeVar("_ActorMixinT", bound="actor_mixin.ActorMixin")


class _GetActorFunc:
    def __call__(
        self, name: str, namespace: str | None = None
    ) -> ray.actor.ActorHandle:
        """
        Default return a handle to a named actor. If specify a type, return a sunray actor.

        ```python
        from sunray import get_actor, ActorMixin


        class MyActor(ActorMixin, name="my-actor"): ...


        _actor = MyActor.new_actor().remote()

        actor_handle = get_actor("my-actor")
        actor = get_actor[MyActor]("my-actor")
        ```
        """
        return ray.get_actor(name, namespace)

    def __getitem__(
        self, actor_type: type[_ActorMixinT]
    ) -> _GetSunrayActorFunc[_ActorMixinT]:
        return _GetSunrayActorFunc(actor_type)


class _GetSunrayActorFunc(Generic[_ActorMixinT]):
    def __init__(self, actor_type: type[_ActorMixinT]) -> None:
        self._actor_type = actor_type

    def __call__(
        self, name: str, namespace: str | None = None
    ) -> actor_mixin.Actor[_ActorMixinT]:
        from .actor_mixin import Actor

        return Actor(ray.get_actor(name, namespace))


get_actor = _GetActorFunc()


def kill(
    actor: ray.actor.ActorHandle | actor_mixin.Actor, *, no_restart: bool = False
) -> None:
    """
    Kill an actor forcefully
    """
    from . import actor_mixin

    if isinstance(actor, actor_mixin.Actor):
        actor = actor._actor_handle
    ray.kill(actor, no_restart=no_restart)
