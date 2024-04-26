# Sunray

[Ray](https://github.com/ray-project/ray) is a unified framework for scaling AI and Python applications. However, it falls short in offering friendly type hints, particularly when it comes to working with the `Actor`.

To address this shortfall, sunray provides enhanced and more robust type hints.

# Lets't vs.

## Round 1: Build an actor

|                                   sunray                                    |                                   ray                                    |
| :-------------------------------------------------------------------------: | :----------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_actor.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_actor.jpg) |

- sunray returns `Actor[Demo]`, but ray returns `ObjectRef[Demo]`
- ray mypy raise error `Type[Demo] has no attribute "remote"`

## Round 2: Get actor remote methods
|                                       sunray                                        |                                       ray                                        |
| :---------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_actor_methods.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_actor_methods.jpg) |

- sunray list all remote methods
- ray list nothing

## Round 3: Actor remote method call
|                                          sunray                                          |                                          ray                                          |
| :--------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_method_remote_call.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_method_remote_call.jpg) |

- sunray correctly provided parameter hints.
- ray ...

## Round 4: Annotate with Actor
|                                         sunray                                         |                                         ray                                         |
| :------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_actor_annotation.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_actor_annotation.jpg) |

- with sunray, just annotate it with `Actor[Demo]`.
- with ray, I don't known.

## Round 5: Stream
|                                    sunray                                    |                                    ray                                    |
| :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_stream.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_stream.jpg) |

- sunray correctly identified that `stream` returns a generator.
- ray still returns ObjectRef.

# Round 6: Unpack result
|                                    sunray                                    |                                    ray                                    |
| :--------------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
| ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/sunray_unpack.jpg) | ![](https://zenxu-github-asset.s3.us-east-2.amazonaws.com/ray_unpack.jpg) |

- sunray will auto unpack tuple result if options specify `unpack=True`.
- ray need to specify how many return numbers, so you need to count it.
- ray mypy raise error 'RemoteFunctionNoArgs has no attribute "options"'.
