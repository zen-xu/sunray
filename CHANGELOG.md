# Changelog

All notable changes to this project will be documented in this file.

## [0.4.1](https://github.com/zen-xu/sunray/compare/0.4.0..0.4.1) - 2024-05-31

### 🐛 Bug Fixes

- Make ObjectRef type var as covariant ([#48](https://github.com/zen-xu/sunray/issues/48)) - ([dc2f4df](https://github.com/zen-xu/sunray/commit/dc2f4dff09effdbe9c3da22ec36b6f7eb9c9462f))

### 🚜 Refactor

- *(typing.py)* Move classes out of TYPE_CHECKING block ([#49](https://github.com/zen-xu/sunray/issues/49)) - ([77f342c](https://github.com/zen-xu/sunray/commit/77f342c10ffc16eb59a1798a2ae6dfc648991455))

## [0.4.0](https://github.com/zen-xu/sunray/compare/0.3.1..0.4.0) - 2024-05-21

### 🚀  Features

- Support `put` owner with Actor ([#45](https://github.com/zen-xu/sunray/issues/45)) - ([9058ef6](https://github.com/zen-xu/sunray/commit/9058ef6c9ead13922f47fa52c8d0b286cf6eccde))

### ⚙️ Miscellaneous Tasks

- *(taplo)* Disable reorder_keys ([#43](https://github.com/zen-xu/sunray/issues/43)) - ([79ca218](https://github.com/zen-xu/sunray/commit/79ca218e151fbbc45a534d35880982cffc6e442e))

## [0.3.1](https://github.com/zen-xu/sunray/compare/0.3.0..0.3.1) - 2024-05-20

### 🐛 Bug Fixes

- *(typing)* Fix `runtime_env` does not support extra options ([#41](https://github.com/zen-xu/sunray/issues/41)) - ([0be3cb3](https://github.com/zen-xu/sunray/commit/0be3cb37a1e76f9ea655b98f3efb87fcc5e70876))

### ⚙️ Miscellaneous Tasks

- Update pyproject metadata ([#42](https://github.com/zen-xu/sunray/issues/42)) - ([98fda59](https://github.com/zen-xu/sunray/commit/98fda59fb9ace0523af47329777d3fac3ad030c5))

## [0.3.0](https://github.com/zen-xu/sunray/compare/0.2.0..0.3.0) - 2024-05-11

### 🚀  Features

- Support bind ([#39](https://github.com/zen-xu/sunray/issues/39)) - ([d707e6c](https://github.com/zen-xu/sunray/commit/d707e6c5491bef8ca98352d1ef3da388ee4ea975))

## [0.2.0](https://github.com/zen-xu/sunray/compare/0.1.0..0.2.0) - 2024-04-29

### 🚀  Features

- Support actor to call self remote method ([#31](https://github.com/zen-xu/sunray/issues/31)) - ([b04ebd9](https://github.com/zen-xu/sunray/commit/b04ebd93710b205bec8c1dbbc095ec4a0a2a732d))

### 🐛 Bug Fixes

- Fix __version__ ([#33](https://github.com/zen-xu/sunray/issues/33)) - ([1cda9a7](https://github.com/zen-xu/sunray/commit/1cda9a735cd5e18b59b775e5e7e361cda2bdd6fd))

### ⚙️ Miscellaneous Tasks

- *(cliff)* Add more skip cases ([#35](https://github.com/zen-xu/sunray/issues/35)) - ([5f78c30](https://github.com/zen-xu/sunray/commit/5f78c30fb364be2141a5d0ab7ce23a46acf481fc))
- Update release message ([#36](https://github.com/zen-xu/sunray/issues/36)) - ([69e7cfb](https://github.com/zen-xu/sunray/commit/69e7cfb6191c67234eeff0809aebf6b93b8cd792))
- Add commitizen config to support dump version ([#34](https://github.com/zen-xu/sunray/issues/34)) - ([a121aa9](https://github.com/zen-xu/sunray/commit/a121aa937b7b8fa80e71b04c8e7cd4d114cbf96b))

## [0.1.0] - 2024-04-26

### 🚀  Features

- Impl core apis ([#15](https://github.com/zen-xu/sunray/issues/15)) - ([3179efb](https://github.com/zen-xu/sunray/commit/3179efbaded1227720d0b9461f2d7a86ddd7d6c1))
- Impl enhanced version of `ray.remote` ([#14](https://github.com/zen-xu/sunray/issues/14)) - ([d3fa7cc](https://github.com/zen-xu/sunray/commit/d3fa7cc8dcf7a8a0db54027f035cc41013b6147a))
- Impl ActorMixin ([#12](https://github.com/zen-xu/sunray/issues/12)) - ([89058c5](https://github.com/zen-xu/sunray/commit/89058c59d101093112e4f6076270cc718bb20a8d))

### 🐛 Bug Fixes

- Fix `remote_method`  type annotations ([#22](https://github.com/zen-xu/sunray/issues/22)) - ([03f338d](https://github.com/zen-xu/sunray/commit/03f338dd3f3df484b734bf9906e624e4b238560b))
- Fix actor with empty options will raise exception ([#17](https://github.com/zen-xu/sunray/issues/17)) - ([2e480c5](https://github.com/zen-xu/sunray/commit/2e480c553a0b3a4871b61e8fe5e53b5a1a927514))

### 🚜 Refactor

- Move submodules into _internal/ ([#16](https://github.com/zen-xu/sunray/issues/16)) - ([fa6d70a](https://github.com/zen-xu/sunray/commit/fa6d70a3fac3ac9be8a0fc93f4b98b9db56996e9))

### 📚 Documentation

- Add cliff.toml and CHANGELOG.md ([#27](https://github.com/zen-xu/sunray/issues/27)) - ([c9d6592](https://github.com/zen-xu/sunray/commit/c9d65925ef264069daa2158bd5f3c172c7cce7be))
- Update README.md ([#26](https://github.com/zen-xu/sunray/issues/26)) - ([328a04b](https://github.com/zen-xu/sunray/commit/328a04bdb7701bbc97aa9d4b87ae1d668288857f))
- Add README.md ([#24](https://github.com/zen-xu/sunray/issues/24)) - ([afbc02a](https://github.com/zen-xu/sunray/commit/afbc02a9350c29c7488b0ccb01c9db6d003e67d5))

### 🧪 Testing

- Use pytest-mypy-plugins to test typing ([#21](https://github.com/zen-xu/sunray/issues/21)) - ([89f4554](https://github.com/zen-xu/sunray/commit/89f45546d5f06aafa85953dbf2964d8b19722370))

### ⚙️ Miscellaneous Tasks

- *(pre-commit)* Init pre-commit config ([#2](https://github.com/zen-xu/sunray/issues/2)) - ([feaea70](https://github.com/zen-xu/sunray/commit/feaea7083bd1d553d169fbeb66b388c7109a22e8))
- *(ruff)* Init ruff config ([#3](https://github.com/zen-xu/sunray/issues/3)) - ([6a0a74d](https://github.com/zen-xu/sunray/commit/6a0a74d7866269755154bd572aad72e5e20bff58))
- Enable release ([#28](https://github.com/zen-xu/sunray/issues/28)) - ([464cbf6](https://github.com/zen-xu/sunray/commit/464cbf6244fec337fea3821753e5b23d9cf0b6a6))
- Add test-mypy.yaml ([#25](https://github.com/zen-xu/sunray/issues/25)) - ([27e546e](https://github.com/zen-xu/sunray/commit/27e546e11ff56fe7301f973745a99462813c041a))
- Upgrade github action codecov from v3 -> v4 ([#23](https://github.com/zen-xu/sunray/issues/23)) - ([c371789](https://github.com/zen-xu/sunray/commit/c3717891d294cad7dfcfcba9cdccda87468fb76a))
- Add py.typed ([#20](https://github.com/zen-xu/sunray/issues/20)) - ([b15a552](https://github.com/zen-xu/sunray/commit/b15a552c2323fdec14dfdc8266a2112b5cdf8a5b))
- Remove unused import ([#18](https://github.com/zen-xu/sunray/issues/18)) - ([1f9a3f3](https://github.com/zen-xu/sunray/commit/1f9a3f3e8cac59164e7639bba0c53f1e944e8cf6))
- Add taplo lint ([#10](https://github.com/zen-xu/sunray/issues/10)) - ([62af700](https://github.com/zen-xu/sunray/commit/62af700394d83c96938afa4ab4efb469723659e5))
- Rm abc.xml ([#7](https://github.com/zen-xu/sunray/issues/7)) - ([0483cf3](https://github.com/zen-xu/sunray/commit/0483cf37c8d145293215cf8c41842fcf50a25970))
- Enable github test workflow ([#6](https://github.com/zen-xu/sunray/issues/6)) - ([09d921a](https://github.com/zen-xu/sunray/commit/09d921a9cb1dbd31a490dff0a2435e1393a80f25))
- Add project vars __version__ and __authors__ ([#5](https://github.com/zen-xu/sunray/issues/5)) - ([2a44a5a](https://github.com/zen-xu/sunray/commit/2a44a5a7318ea096895d0c58fbde3328e00f5a82))
- Use poetry to manage project - ([5dbffe1](https://github.com/zen-xu/sunray/commit/5dbffe1984f5226e9d481ef673819dbb8f9332c3))

### Build

- *(test-dep)* Add test dependencies ([#4](https://github.com/zen-xu/sunray/issues/4)) - ([22fa233](https://github.com/zen-xu/sunray/commit/22fa2335fcd99e006128cc4d2f8cde424634872f))
- Add dep typing-extensions ([#19](https://github.com/zen-xu/sunray/issues/19)) - ([0c7b3dd](https://github.com/zen-xu/sunray/commit/0c7b3ddbef270eaaeffed1bb82cd21d5e906edec))

<!-- generated by git-cliff -->
