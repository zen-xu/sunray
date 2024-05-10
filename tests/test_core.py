from __future__ import annotations

import ray.actor

from ray.util.state import get_actor

from sunray import Actor
from sunray import ActorMixin
from sunray import remote
from sunray import remote_method
from sunray._internal import core


def test_get(init_ray):
    @remote(num_cpus=0)
    def f(v: int):
        return v

    ref1, ref2 = f.remote(1), f.remote(2)
    assert core.get(ref1) == 1
    assert core.get((ref1, ref2)) == (1, 2)
    assert core.get([ref1, ref2]) == (1, 2)


def test_get_actor(init_ray):
    class MyActor(ActorMixin, num_cpus=0.1, name="my-actor"): ...

    _actor = MyActor.new_actor().remote()

    actor_handle = core.get_actor("my-actor")
    actor = core.get_actor[MyActor]("my-actor")
    assert isinstance(actor_handle, ray.actor.ActorHandle)
    assert isinstance(actor, Actor)


def test_kill(init_ray):
    class MyActor(ActorMixin, num_cpus=0):
        @remote_method
        def ready(self):
            return True

    actor = MyActor.new_actor().options(name="demo1").remote()
    ray.get(actor.methods.ready.remote())
    core.kill(actor)
    actor_info = get_actor(actor._actor_handle._actor_id.hex())
    assert actor_info.state == "DEAD"

    actor2 = MyActor.new_actor().options(name="demo2").remote()
    ray.get(actor2.methods.ready.remote())
    core.kill(actor2._actor_handle)
    assert get_actor(actor2._actor_handle._actor_id.hex()).state == "DEAD"
