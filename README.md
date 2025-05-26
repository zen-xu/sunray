# Sunray

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Tests](https://github.com/zen-xu/sunray/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/zen-xu/sunray/actions/workflows/test.yaml)
[![Mypy](https://github.com/zen-xu/sunray/actions/workflows/test-mypy.yaml/badge.svg?branch=main)](https://github.com/zen-xu/sunray/actions/workflows/test-mypy.yaml)
[![codecov](https://codecov.io/gh/zen-xu/sunray/graph/badge.svg?token=NkaEIVRqk6)](https://codecov.io/gh/zen-xu/sunray)
![GitHub License](https://img.shields.io/github/license/zen-xu/sunray)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sunray)
![PyPI - Version](https://img.shields.io/pypi/v/sunray)
![Static Badge](https://img.shields.io/badge/RMV-2.20.0-blue)

[Ray](https://github.com/ray-project/ray) is a unified framework for scaling AI and Python applications. However, it falls short in offering friendly type hints, particularly when it comes to working with the `Actor`.

To address this shortfall, sunray provides enhanced and more robust type hints.

## install

```shell
pip install sunray
```

## Let's vs.

### Round 1: Build an actor

|                                   sunray                                    |                                   ray                                    |
| :-------------------------------------------------------------------------: | :----------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_actor.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_actor.jpg) |

- sunray returns `Actor[Demo]`, but ray returns `ObjectRef[Demo]`
- ray mypy raise error `Type[Demo] has no attribute "remote"`

### Round 2: Get actor remote methods
|                                       sunray                                        |                                       ray                                        |
| :---------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_actor_methods.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_actor_methods.jpg) |

- sunray list all remote methods
- ray list nothing

### Round 3: Actor remote method call
|                                          sunray                                          |                                          ray                                          |
| :--------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_method_remote_call.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_method_remote_call.jpg) |

- sunray correctly provided parameter hints.
- ray ...

### Round 4: Annotate with Actor
|                                         sunray                                         |                                         ray                                         |
| :------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_actor_annotation.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_actor_annotation.jpg) |

- with sunray, just annotate it with `Actor[Demo]`.
- with ray, I don't known.

### Round 5: Stream
|                                    sunray                                    |                                    ray                                    |
| :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_stream.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_stream.jpg) |

- sunray correctly identified that `stream` returns a generator.
- ray still returns ObjectRef.

### Round 6: Unpack result
|                                    sunray                                    |                                    ray                                    |
| :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_unpack.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_unpack.jpg) |

- sunray will auto unpack tuple result if options specify `unpack=True`.
- ray need to specify how many return numbers, so you need to count it.
- ray mypy raise error 'RemoteFunctionNoArgs has no attribute "options"'.

### Round 7: Get actor
|                                     sunray                                      |                                     ray                                      |
| :-----------------------------------------------------------------------------: | :--------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_get_actor.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_get_actor.jpg) |

- sunray get_actor will return `ActorHandle`, and return `Actor[Demo]` if you specify with generic type.
- ray just return `Any`.

### Round 8: Call self remote method
|                                            sunray                                             |                                            ray                                             |
| :-------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_call_self_remote_method.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_call_self_remote_method.jpg) |

- sunray maintains a consistent calling convention, whether it's from internal or external functions.
- ray, you need to first obtain the current actor from the running context, and then call through the actor.

### Round 9: Lazy Computation
|                                   sunray                                   |                                   ray                                   |
| :------------------------------------------------------------------------: | :---------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_bind.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_bind.jpg) |

- sunray can successfully track the input parameter types and output types.
- ray does not have this capability.

## API

`sunray` re-export all apis from `ray.core` with friendly type hints. In addition, `sunray` provides `ActorMixin` which is used to help creating more robust actors.

### ActorMixin

`ActorMixin` is a mixin, and provides a classmethod `new_actor`

```python
import sunray


class Demo(
                       # Here to specify default actor options
    sunray.ActorMixin, name="DemoActor", num_cpus=1, concurrency_groups={"g1": 1}
):
    def __init__(self, init_v: int):
        self.init_v = init_v

    # annotate `add` is a remote_method
    @sunray.remote_method
    def add(self, v: int) -> int:
        return self.init_v + v

    # support directly call remote_method
    @sunray.remote_method
    def calculate(self, v: int) -> int:
        return self.add(v)

    # support specify remote method options
    @sunray.remote_method(concurrency_group="g1")
    async def sleep(self): ...


# construct the actor
actor = Demo.new_actor().remote(1)

# call remote method
ref = actor.methods.add.remote(1)
print(sunray.get(ref))
```
