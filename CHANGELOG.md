# CHANGELOG


## v0.25.7 (2024-11-20)

### Bug Fixes

- **deps**: Update dependency pydantic to v2.10.0
  ([#776](https://github.com/MartinBernstorff/Memium/pull/776),
  [`4dcce97`](https://github.com/MartinBernstorff/Memium/commit/4dcce9792d82df32a763aa2068f3cce21910d665))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pydantic](https://redirect.github.com/pydantic/pydantic)
  ([changelog](https://docs.pydantic.dev/latest/changelog/)) | `==2.9.2` -> `==2.10.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pydantic/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pydantic/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pydantic/2.9.2/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pydantic/2.9.2/2.10.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pydantic/pydantic (pydantic)</summary>

### [`v2.10.0`](https://redirect.github.com/pydantic/pydantic/blob/HEAD/HISTORY.md#v2100-2024-11-20)

[Compare Source](https://redirect.github.com/pydantic/pydantic/compare/v2.9.2...v2.10.0)

The code released in v2.10.0 is practically identical to that of v2.10.0b2.

[GitHub release](https://redirect.github.com/pydantic/pydantic/releases/tag/v2.10.0)

See the [v2.10 release blog post](https://pydantic.dev/articles/pydantic-v2-10-release) for the
  highlights!

##### What's Changed

##### Packaging

- Bump `pydantic-core` to `v2.27.0` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10825](https://redirect.github.com/pydantic/pydantic/pull/10825) - Replaced pdm with uv
  by [@&#8203;frfahim](https://redirect.github.com/frfahim) in
  [#&#8203;10727](https://redirect.github.com/pydantic/pydantic/pull/10727)

##### New Features

- Support `fractions.Fraction` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [#&#8203;10318](https://redirect.github.com/pydantic/pydantic/pull/10318) - Support `Hashable`
  for json validation by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10324](https://redirect.github.com/pydantic/pydantic/pull/10324) - Add a `SocketPath`
  type for `linux` systems by [@&#8203;theunkn0wn1](https://redirect.github.com/theunkn0wn1) in
  [#&#8203;10378](https://redirect.github.com/pydantic/pydantic/pull/10378) - Allow arbitrary refs
  in JSON schema `examples` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10417](https://redirect.github.com/pydantic/pydantic/pull/10417) - Support `defer_build`
  for Pydantic dataclasses by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10313](https://redirect.github.com/pydantic/pydantic/pull/10313) - Adding v1 / v2
  incompatibility warning for nested v1 model by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10431](https://redirect.github.com/pydantic/pydantic/pull/10431) - Add support for
  unpacked `TypedDict` to type hint variadic keyword arguments with `@validate_call` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10416](https://redirect.github.com/pydantic/pydantic/pull/10416) - Support compiled
  patterns in `protected_namespaces` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10522](https://redirect.github.com/pydantic/pydantic/pull/10522) - Add support for
  `propertyNames` in JSON schema by [@&#8203;FlorianSW](https://redirect.github.com/FlorianSW) in
  [#&#8203;10478](https://redirect.github.com/pydantic/pydantic/pull/10478) - Adding `__replace__`
  protocol for Python 3.13+ support by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10596](https://redirect.github.com/pydantic/pydantic/pull/10596) - Expose public `sort`
  method for JSON schema generation by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10595](https://redirect.github.com/pydantic/pydantic/pull/10595) - Add runtime validation
  of `@validate_call` callable argument by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10627](https://redirect.github.com/pydantic/pydantic/pull/10627) - Add
  `experimental_allow_partial` support by
  [@&#8203;samuelcolvin](https://redirect.github.com/samuelcolvin) in
  [#&#8203;10748](https://redirect.github.com/pydantic/pydantic/pull/10748) - Support default
  factories taking validated data as an argument by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10678](https://redirect.github.com/pydantic/pydantic/pull/10678) - Allow subclassing
  `ValidationError` and `PydanticCustomError` by
  [@&#8203;Youssefares](https://redirect.github.com/Youssefares) in
  [pydantic/pydantic-core#1413](https://redirect.github.com/pydantic/pydantic-core/pull/1413) - Add
  `trailing-strings` support to `experimental_allow_partial` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10825](https://redirect.github.com/pydantic/pydantic/pull/10825) - Add `rebuild()` method
  for `TypeAdapter` and simplify `defer_build` patterns by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10537](https://redirect.github.com/pydantic/pydantic/pull/10537) - Improve `TypeAdapter`
  instance repr by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10872](https://redirect.github.com/pydantic/pydantic/pull/10872)

##### Changes

- Don't allow customization of `SchemaGenerator` until interface is more stable by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10303](https://redirect.github.com/pydantic/pydantic/pull/10303) - Cleanly `defer_build`
  on `TypeAdapters`, removing experimental flag by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10329](https://redirect.github.com/pydantic/pydantic/pull/10329) - Fix `mro` of generic
  subclass by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10100](https://redirect.github.com/pydantic/pydantic/pull/10100) - Strip whitespaces on
  JSON Schema title generation by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [#&#8203;10404](https://redirect.github.com/pydantic/pydantic/pull/10404) - Use `b64decode` and
  `b64encode` for `Base64Bytes` type by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10486](https://redirect.github.com/pydantic/pydantic/pull/10486) - Relax protected
  namespace config default by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10441](https://redirect.github.com/pydantic/pydantic/pull/10441) - Revalidate
  parametrized generics if instance's origin is subclass of OG class by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10666](https://redirect.github.com/pydantic/pydantic/pull/10666) - Warn if configuration
  is specified on the `@dataclass` decorator and with the `__pydantic_config__` attribute by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10406](https://redirect.github.com/pydantic/pydantic/pull/10406) - Recommend against
  using `Ellipsis` (...) with `Field` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10661](https://redirect.github.com/pydantic/pydantic/pull/10661) - Migrate to subclassing
  instead of annotated approach for pydantic url types by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10662](https://redirect.github.com/pydantic/pydantic/pull/10662) - Change JSON schema
  generation of `Literal`s and `Enums` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10692](https://redirect.github.com/pydantic/pydantic/pull/10692) - Simplify unions
  involving `Any` or `Never` when replacing type variables by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10338](https://redirect.github.com/pydantic/pydantic/pull/10338) - Do not require padding
  when decoding `base64` bytes by
  [@&#8203;bschoenmaeckers](https://redirect.github.com/bschoenmaeckers) in
  [pydantic/pydantic-core#1448](https://redirect.github.com/pydantic/pydantic-core/pull/1448) -
  Support dates all the way to 1BC by [@&#8203;changhc](https://redirect.github.com/changhc) in
  [pydantic/speedate#77](https://redirect.github.com/pydantic/speedate/pull/77)

##### Performance

- Schema cleaning: skip unnecessary copies during schema walking by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10286](https://redirect.github.com/pydantic/pydantic/pull/10286) - Refactor namespace
  logic for annotations evaluation by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10530](https://redirect.github.com/pydantic/pydantic/pull/10530) - Improve email regexp
  on edge cases by [@&#8203;AlekseyLobanov](https://redirect.github.com/AlekseyLobanov) in
  [#&#8203;10601](https://redirect.github.com/pydantic/pydantic/pull/10601) - `CoreMetadata`
  refactor with an emphasis on documentation, schema build time performance, and reducing complexity
  by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10675](https://redirect.github.com/pydantic/pydantic/pull/10675)

##### Fixes

- Remove guarding check on `computed_field` with `field_serializer` by
  [@&#8203;nix010](https://redirect.github.com/nix010) in
  [#&#8203;10390](https://redirect.github.com/pydantic/pydantic/pull/10390) - Fix `Predicate` issue
  in `v2.9.0` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10321](https://redirect.github.com/pydantic/pydantic/pull/10321) - Fixing
  `annotated-types` bound by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10327](https://redirect.github.com/pydantic/pydantic/pull/10327) - Turn `tzdata` install
  requirement into optional `timezone` dependency by
  [@&#8203;jakob-keller](https://redirect.github.com/jakob-keller) in
  [#&#8203;10331](https://redirect.github.com/pydantic/pydantic/pull/10331) - Use correct types
  namespace when building `namedtuple` core schemas by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10337](https://redirect.github.com/pydantic/pydantic/pull/10337) - Fix evaluation of
  stringified annotations during namespace inspection by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10347](https://redirect.github.com/pydantic/pydantic/pull/10347) - Fix `IncEx` type alias
  definition by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10339](https://redirect.github.com/pydantic/pydantic/pull/10339) - Do not error when
  trying to evaluate annotations of private attributes by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10358](https://redirect.github.com/pydantic/pydantic/pull/10358) - Fix nested type
  statement by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10369](https://redirect.github.com/pydantic/pydantic/pull/10369) - Improve typing of
  `ModelMetaclass.mro` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10372](https://redirect.github.com/pydantic/pydantic/pull/10372) - Fix class access of
  deprecated `computed_field`s by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10391](https://redirect.github.com/pydantic/pydantic/pull/10391) - Make sure
  `inspect.iscoroutinefunction` works on coroutines decorated with `@validate_call` by
  [@&#8203;MovisLi](https://redirect.github.com/MovisLi) in
  [#&#8203;10374](https://redirect.github.com/pydantic/pydantic/pull/10374) - Fix `NameError` when
  using `validate_call` with PEP 695 on a class by
  [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10380](https://redirect.github.com/pydantic/pydantic/pull/10380) - Fix `ZoneInfo` with
  various invalid types by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10408](https://redirect.github.com/pydantic/pydantic/pull/10408) - Fix
  `PydanticUserError` on empty `model_config` with annotations by
  [@&#8203;cdwilson](https://redirect.github.com/cdwilson) in
  [#&#8203;10412](https://redirect.github.com/pydantic/pydantic/pull/10412) - Fix variance issue in
  `_IncEx` type alias, only allow `True` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10414](https://redirect.github.com/pydantic/pydantic/pull/10414) - Fix serialization
  schema generation when using `PlainValidator` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10427](https://redirect.github.com/pydantic/pydantic/pull/10427) - Fix schema generation
  error when serialization schema holds references by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10444](https://redirect.github.com/pydantic/pydantic/pull/10444) - Inline references if
  possible when generating schema for `json_schema_input_type` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10439](https://redirect.github.com/pydantic/pydantic/pull/10439) - Fix recursive
  arguments in `Representation` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10480](https://redirect.github.com/pydantic/pydantic/pull/10480) - Fix representation for
  builtin function types by [@&#8203;kschwab](https://redirect.github.com/kschwab) in
  [#&#8203;10479](https://redirect.github.com/pydantic/pydantic/pull/10479) - Add python validators
  for decimal constraints (`max_digits` and `decimal_places`) by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10506](https://redirect.github.com/pydantic/pydantic/pull/10506) - Only fetch
  `__pydantic_core_schema__` from the current class during schema generation by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10518](https://redirect.github.com/pydantic/pydantic/pull/10518) - Fix `stacklevel` on
  deprecation warnings for `BaseModel` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10520](https://redirect.github.com/pydantic/pydantic/pull/10520) - Fix warning
  `stacklevel` in `BaseModel.__init__` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10526](https://redirect.github.com/pydantic/pydantic/pull/10526) - Improve error handling
  for in-evaluable refs for discriminator application by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10440](https://redirect.github.com/pydantic/pydantic/pull/10440) - Change the signature
  of `ConfigWrapper.core_config` to take the title directly by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10562](https://redirect.github.com/pydantic/pydantic/pull/10562) - Do not use the
  previous config from the stack for dataclasses without config by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10576](https://redirect.github.com/pydantic/pydantic/pull/10576) - Fix serialization for
  IP types with `mode='python'` by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10594](https://redirect.github.com/pydantic/pydantic/pull/10594) - Support constraint
  application for `Base64Etc` types by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10584](https://redirect.github.com/pydantic/pydantic/pull/10584) - Fix `validate_call`
  ignoring `Field` in `Annotated` by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10610](https://redirect.github.com/pydantic/pydantic/pull/10610) - Raise an error when
  `Self` is invalid by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10609](https://redirect.github.com/pydantic/pydantic/pull/10609) - Using
  `core_schema.InvalidSchema` instead of metadata injection + checks by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10523](https://redirect.github.com/pydantic/pydantic/pull/10523) - Tweak type alias logic
  by [@&#8203;kc0506](https://redirect.github.com/kc0506) in
  [#&#8203;10643](https://redirect.github.com/pydantic/pydantic/pull/10643) - Support usage of
  `type` with `typing.Self` and type aliases by [@&#8203;kc0506](https://redirect.github.com/kc0506)
  in [#&#8203;10621](https://redirect.github.com/pydantic/pydantic/pull/10621) - Use overloads for
  `Field` and `PrivateAttr` functions by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10651](https://redirect.github.com/pydantic/pydantic/pull/10651) - Clean up the `mypy`
  plugin implementation by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10669](https://redirect.github.com/pydantic/pydantic/pull/10669) - Properly check for
  `typing_extensions` variant of `TypeAliasType` by
  [@&#8203;Daraan](https://redirect.github.com/Daraan) in
  [#&#8203;10713](https://redirect.github.com/pydantic/pydantic/pull/10713) - Allow any mapping in
  `BaseModel.model_copy()` by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10751](https://redirect.github.com/pydantic/pydantic/pull/10751) - Fix `isinstance`
  behavior for urls by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10766](https://redirect.github.com/pydantic/pydantic/pull/10766) - Ensure
  `cached_property` can be set on Pydantic models by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10774](https://redirect.github.com/pydantic/pydantic/pull/10774) - Fix equality checks
  for primitives in literals by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle)
  in [pydantic/pydantic-core#1459](https://redirect.github.com/pydantic/pydantic-core/pull/1459) -
  Properly enforce `host_required` for URLs by [@&#8203;Viicos](https://redirect.github.com/Viicos)
  in [pydantic/pydantic-core#1488](https://redirect.github.com/pydantic/pydantic-core/pull/1488) -
  Fix when `coerce_numbers_to_str` enabled and string has invalid Unicode character by
  [@&#8203;andrey-berenda](https://redirect.github.com/andrey-berenda) in
  [pydantic/pydantic-core#1515](https://redirect.github.com/pydantic/pydantic-core/pull/1515) - Fix
  serializing `complex` values in `Enum`s by [@&#8203;changhc](https://redirect.github.com/changhc)
  in [pydantic/pydantic-core#1524](https://redirect.github.com/pydantic/pydantic-core/pull/1524) -
  Refactor `_typing_extra` module by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10725](https://redirect.github.com/pydantic/pydantic/pull/10725) - Support intuitive
  equality for urls by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10798](https://redirect.github.com/pydantic/pydantic/pull/10798) - Add `bytearray` to
  `TypeAdapter.validate_json` signature by
  [@&#8203;samuelcolvin](https://redirect.github.com/samuelcolvin) in
  [#&#8203;10802](https://redirect.github.com/pydantic/pydantic/pull/10802) - Ensure class access of
  method descriptors is performed when used as a default with `Field` by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10816](https://redirect.github.com/pydantic/pydantic/pull/10816) - Fix circular import
  with `validate_call` by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10807](https://redirect.github.com/pydantic/pydantic/pull/10807) - Fix error when using
  type aliases referencing other type aliases by
  [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10809](https://redirect.github.com/pydantic/pydantic/pull/10809) - Fix `IncEx` type alias
  to be compatible with mypy by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10813](https://redirect.github.com/pydantic/pydantic/pull/10813) - Make `__signature__` a
  lazy property, do not deepcopy defaults by [@&#8203;Viicos](https://redirect.github.com/Viicos) in
  [#&#8203;10818](https://redirect.github.com/pydantic/pydantic/pull/10818) - Make `__signature__`
  lazy for dataclasses, too by [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10832](https://redirect.github.com/pydantic/pydantic/pull/10832) - Subclass all single
  host url classes from `AnyUrl` to preserve behavior from v2.9 by
  [@&#8203;sydney-runkle](https://redirect.github.com/sydney-runkle) in
  [#&#8203;10856](https://redirect.github.com/pydantic/pydantic/pull/10856)

##### New Contributors

- [@&#8203;jakob-keller](https://redirect.github.com/jakob-keller) made their first contribution in
  [#&#8203;10331](https://redirect.github.com/pydantic/pydantic/pull/10331) -
  [@&#8203;MovisLi](https://redirect.github.com/MovisLi) made their first contribution in
  [#&#8203;10374](https://redirect.github.com/pydantic/pydantic/pull/10374) -
  [@&#8203;joaopalmeiro](https://redirect.github.com/joaopalmeiro) made their first contribution in
  [#&#8203;10405](https://redirect.github.com/pydantic/pydantic/pull/10405) -
  [@&#8203;theunkn0wn1](https://redirect.github.com/theunkn0wn1) made their first contribution in
  [#&#8203;10378](https://redirect.github.com/pydantic/pydantic/pull/10378) -
  [@&#8203;cdwilson](https://redirect.github.com/cdwilson) made their first contribution in
  [#&#8203;10412](https://redirect.github.com/pydantic/pydantic/pull/10412) -
  [@&#8203;dlax](https://redirect.github.com/dlax) made their first contribution in
  [#&#8203;10421](https://redirect.github.com/pydantic/pydantic/pull/10421) -
  [@&#8203;kschwab](https://redirect.github.com/kschwab) made their first contribution in
  [#&#8203;10479](https://redirect.github.com/pydantic/pydantic/pull/10479) -
  [@&#8203;santibreo](https://redirect.github.com/santibreo) made their first contribution in
  [#&#8203;10453](https://redirect.github.com/pydantic/pydantic/pull/10453) -
  [@&#8203;FlorianSW](https://redirect.github.com/FlorianSW) made their first contribution in
  [#&#8203;10478](https://redirect.github.com/pydantic/pydantic/pull/10478) -
  [@&#8203;tkasuz](https://redirect.github.com/tkasuz) made their first contribution in
  [#&#8203;10555](https://redirect.github.com/pydantic/pydantic/pull/10555) -
  [@&#8203;AlekseyLobanov](https://redirect.github.com/AlekseyLobanov) made their first contribution
  in [#&#8203;10601](https://redirect.github.com/pydantic/pydantic/pull/10601) -
  [@&#8203;NiclasvanEyk](https://redirect.github.com/NiclasvanEyk) made their first contribution in
  [#&#8203;10667](https://redirect.github.com/pydantic/pydantic/pull/10667) -
  [@&#8203;mschoettle](https://redirect.github.com/mschoettle) made their first contribution in
  [#&#8203;10677](https://redirect.github.com/pydantic/pydantic/pull/10677) -
  [@&#8203;Daraan](https://redirect.github.com/Daraan) made their first contribution in
  [#&#8203;10713](https://redirect.github.com/pydantic/pydantic/pull/10713) -
  [@&#8203;k4nar](https://redirect.github.com/k4nar) made their first contribution in
  [#&#8203;10736](https://redirect.github.com/pydantic/pydantic/pull/10736) -
  [@&#8203;UriyaHarpeness](https://redirect.github.com/UriyaHarpeness) made their first contribution
  in [#&#8203;10740](https://redirect.github.com/pydantic/pydantic/pull/10740) -
  [@&#8203;frfahim](https://redirect.github.com/frfahim) made their first contribution in
  [#&#8203;10727](https://redirect.github.com/pydantic/pydantic/pull/10727)

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency typer to v0.13.1
  ([#775](https://github.com/MartinBernstorff/Memium/pull/775),
  [`2f355ad`](https://github.com/MartinBernstorff/Memium/commit/2f355ad1b7622a5079959e81fd3af8cdc38ccfe7))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.13.0` -> `==0.13.1` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.13.0/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.13.0/0.13.1?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>fastapi/typer (typer)</summary>

### [`v0.13.1`](https://redirect.github.com/fastapi/typer/releases/tag/0.13.1)

[Compare Source](https://redirect.github.com/fastapi/typer/compare/0.13.0...0.13.1)

##### Features

- ✨ Remove Rich tags when showing completion text. PR
  [#&#8203;877](https://redirect.github.com/fastapi/typer/pull/877) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ✨ Render Rich markup as HTML in
  Markdown docs. PR [#&#8203;847](https://redirect.github.com/fastapi/typer/pull/847) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ✨ Support cp850 encoding for
  auto-completion in PowerShell. PR
  [#&#8203;808](https://redirect.github.com/fastapi/typer/pull/808) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ✨ Allow gettext translation of help
  message. PR [#&#8203;886](https://redirect.github.com/fastapi/typer/pull/886) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg).

##### Refactors

- 🐛 Fix printing HTML from Rich output. PR
  [#&#8203;1055](https://redirect.github.com/fastapi/typer/pull/1055) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo).

##### Docs

- 📝 Update markdown includes to use the new simpler format. PR
  [#&#8203;1054](https://redirect.github.com/fastapi/typer/pull/1054) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo).

##### Internal

- ⬆ Bump ruff from 0.7.3 to 0.7.4. PR
  [#&#8203;1051](https://redirect.github.com/fastapi/typer/pull/1051) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1047](https://redirect.github.com/fastapi/typer/pull/1047) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.7.2 to 0.7.3. PR [#&#8203;1046](https://redirect.github.com/fastapi/typer/pull/1046) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  tiangolo/latest-changes from 0.3.1 to 0.3.2. PR
  [#&#8203;1044](https://redirect.github.com/fastapi/typer/pull/1044) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Update pytest-cov
  requirement from <6.0.0,>=2.10.0 to >=2.10.0,<7.0.0. PR
  [#&#8203;1033](https://redirect.github.com/fastapi/typer/pull/1033) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot).

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xOS4wIiwidXBkYXRlZEluVmVyIjoiMzkuMTkuMCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.6 (2024-11-13)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.389
  ([#774](https://github.com/MartinBernstorff/Memium/pull/774),
  [`42e7e14`](https://github.com/MartinBernstorff/Memium/commit/42e7e14cfcf2ca454ccae03a61ac6173066b726a))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [pyright](https://redirect.github.com/RobertCraigie/pyright-python) | `==1.1.388` -> `==1.1.389` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/pyright/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/pyright/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/pyright/1.1.388/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/pyright/1.1.388/1.1.389?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>RobertCraigie/pyright-python (pyright)</summary>

###
  [`v1.1.389`](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.388...v1.1.389)

[Compare
  Source](https://redirect.github.com/RobertCraigie/pyright-python/compare/v1.1.388...v1.1.389)

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS4xMS41IiwidXBkYXRlZEluVmVyIjoiMzkuMTEuNSIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOltdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.14.0
  ([#773](https://github.com/MartinBernstorff/Memium/pull/773),
  [`1cd4ba2`](https://github.com/MartinBernstorff/Memium/commit/1cd4ba23acc1c16cf872d8cf00364c3caeb59d00))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.13.0` -> `v9.14.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.14.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9140-2024-11-11)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.13.0...v9.14.0)

##### Bug Fixes

- **release-notes**: Override default wordwrap to non-wrap for in default template

([`99ab99b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/99ab99bb0ba350ca1913a2bde9696f4242278972))

##### Documentation

- **changelog-templates**: Document new `mask_initial_release` changelog context variable

([`f294957`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/f2949577dfb2dbf9c2ac952c1bbcc4ab84da080b))

- **configuration**: Document new `mask_initial_release` option usage & effect

([`3cabcdc`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/3cabcdcd9473e008604e74cc2d304595317e921d))

- **homepage**: Fix reference to new ci workflow for test status badge

([`6760069`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/6760069e7489f50635beb5aedbbeb2cb82b7c584))

##### Features

- **context**: Add `mask_initial_release` setting to changelog context

([`6f2ee39`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/6f2ee39414b3cf75c0b67dee4db0146bbc1041bb))

- **configuration**: Add `changelog.default_templates.mask_initial_release` option

([`595a70b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/595a70bcbc8fea1f8ccf6c5069c41c35ec4efb8d))

- **release-notes**: Define first release w/o change descriptions in default template

([`83167a3`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/83167a3dcceb7db16b790e1b0efd5fc75fee8942))

- **changelog**: Define first release w/o change descriptions for default RST template

([`e30c94b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/e30c94bffe62b42e8dc6ed4fed6260e57b4d532b))

- **changelog**: Define first release w/o change descriptions for default MD template

([`fa89dec`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/fa89dec239efbae7544b187f624a998fa9ecc309))

- **changelog**: Add md to rst conversion for markdown inline links

([`cb2af1f`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/cb2af1f17cf6c8ae037c6cd8bb8b4d9c019bb47e))

- **changelog-md**: Add markdown inline link format macro

([`c6d8211`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/c6d8211c859442df17cb41d2ff19fdb7a81cdb76))

- **changelogs**: Prefix scopes on commit descriptions in default template

([#&#8203;1093](https://redirect.github.com/python-semantic-release/python-semantic-release/pull/1093),

[`560fd2c`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/560fd2c0d58c97318377cb83af899a336d24cfcc))

<!---->

- test(changelog): update default changelog unit tests to handle commit scope

- test(release-notes): update default release notes unit tests to handle commit scope

- test(fixtures): update changelog generator fixture to handle scope additions

- test(cmd-version): update implementation for test resiliency

- feat(changelog-md): prefix scopes on commit descriptions in Markdown changelog template

- feat(changelog-rst): prefix scopes on commit descriptions in ReStructuredText template

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43LjEiLCJ1cGRhdGVkSW5WZXIiOiIzOS43LjEiLCJ0YXJnZXRCcmFuY2giOiJtYWluIiwibGFiZWxzIjpbXX0=-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update python-semantic-release/python-semantic-release action to v9.13.0
  ([#772](https://github.com/MartinBernstorff/Memium/pull/772),
  [`947dead`](https://github.com/MartinBernstorff/Memium/commit/947dead0a0dcf7cdef5d5caedab73a3adfd42881))

This PR contains the following updates:

| Package | Type | Update | Change | |---|---|---|---| |
  [python-semantic-release/python-semantic-release](https://redirect.github.com/python-semantic-release/python-semantic-release)
  | action | minor | `v9.12.2` -> `v9.13.0` |

---

### Release Notes

<details> <summary>python-semantic-release/python-semantic-release
  (python-semantic-release/python-semantic-release)</summary>

###
  [`v9.13.0`](https://redirect.github.com/python-semantic-release/python-semantic-release/blob/HEAD/CHANGELOG.md#v9130-2024-11-10)

[Compare
  Source](https://redirect.github.com/python-semantic-release/python-semantic-release/compare/v9.12.2...v9.13.0)

##### Bug Fixes

- Ignore unknown parsed commit types in default RST changelog

([`77609b1`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/77609b1917a00b106ce254e6f6d5edcd1feebba7))

- Drop the `breaking` category but still maintain a major level bump

([`f1ffa54`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/f1ffa5411892de34cdc842fd55c460a24b6685c6))

- Improve reliability of text unwordwrap of descriptions

([`436374b`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/436374b04128d1550467ae97ba90253f1d1b3878))

##### Documentation

- Fix api class reference links

([`7a5bdf2`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/7a5bdf29b3df0f9a1346ea5301d2a7fee953667b))

- Add `linked_merge_request` field to examples

([`d4376bc`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/d4376bc2ae4d3708d501d91211ec3ee3a923e9b5))

- Add `linked_merge_request` field to Parsed Commit definition

([`ca61889`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/ca61889d4ac73e9864fbf637fb87ab2d5bc053ea))

##### Features

- Add PR/MR url linking to default reStructuredText template

([`5f018d6`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/5f018d630b4c625bdf6d329b27fd966eba75b017))

Resolves:
  [#&#8203;924](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/924),
  [#&#8203;953](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/953)

- Add PR/MR url linking to default Markdown changelog

([`cd8d131`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/cd8d1310a4000cc79b529fbbdc58933f4c6373c6))

Resolves:
  [#&#8203;924](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/924),
  [#&#8203;953](https://redirect.github.com/python-semantic-release/python-semantic-release/issues/953)

- Automatically parse PR/MR numbers from subject lines in commits

([`2b3f738`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2b3f73801f5760bac29acd93db3ffb2bc790cda0))

- Automatically parse PR/MR numbers from subject lines in commits

([`bca9909`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/bca9909c1b61fdb1f9ccf823fceb6951cd059820))

- Automatically parse PR/MR numbers from subject lines in commits

([`2ac798f`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2ac798f92e0c13c1db668747f7e35a65b99ae7ce))

- Add linked merge requests list to the `ParsedCommit` object

([`9a91062`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/9a9106212d6c240e9d3358e139b4c4694eaf9c4b))

##### Performance Improvements

- Increase speed & decrease complexity of commit parsing

([`2b661ed`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2b661ed122a6f0357a6b92233ac1351c54c7794e))

- Increase speed of commit parsing

([`2c9c468`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/2c9c4685a66feb35cd78571cf05f76344dd6d66a))

- Simplify commit parsing type pre-calculation

([`a86a28c`](https://redirect.github.com/python-semantic-release/python-semantic-release/commit/a86a28c5e26ed766cda71d26b9382c392e377c61))

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43LjEiLCJ1cGRhdGVkSW5WZXIiOiIzOS43LjEiLCJ0YXJnZXRCcmFuY2giOiJtYWluIiwibGFiZWxzIjpbXX0=-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.25.5 (2024-11-07)

### Bug Fixes

- **deps**: Update dependency typer to v0.13.0
  ([#771](https://github.com/MartinBernstorff/Memium/pull/771),
  [`0ffe1cf`](https://github.com/MartinBernstorff/Memium/commit/0ffe1cfe4f5569d06e49fee9bffb79e9eebc2e08))

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [typer](https://redirect.github.com/fastapi/typer)
  ([changelog](https://typer.tiangolo.com/release-notes/)) | `==0.12.5` -> `==0.13.0` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/typer/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/typer/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/typer/0.12.5/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/typer/0.12.5/0.13.0?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>fastapi/typer (typer)</summary>

### [`v0.13.0`](https://redirect.github.com/fastapi/typer/releases/tag/0.13.0)

[Compare Source](https://redirect.github.com/fastapi/typer/compare/0.12.5...0.13.0)

##### Features

- ✨ Handle `KeyboardInterrupt` separately from other exceptions. PR
  [#&#8203;1039](https://redirect.github.com/fastapi/typer/pull/1039) by
  [@&#8203;patrick91](https://redirect.github.com/patrick91). - ✨ Update `launch` to not print
  anything when opening urls. PR [#&#8203;1035](https://redirect.github.com/fastapi/typer/pull/1035)
  by [@&#8203;patrick91](https://redirect.github.com/patrick91). - ✨ Show help items in order of
  definition. PR [#&#8203;944](https://redirect.github.com/fastapi/typer/pull/944) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg).

##### Fixes

- 🐛 Fix equality check for custom classes. PR
  [#&#8203;979](https://redirect.github.com/fastapi/typer/pull/979) by
  [@&#8203;AryazE](https://redirect.github.com/AryazE). - 🐛 Allow colon in zsh autocomplete values
  and descriptions. PR [#&#8203;988](https://redirect.github.com/fastapi/typer/pull/988) by
  [@&#8203;snapbug](https://redirect.github.com/snapbug).

##### Refactors

- 🗑️ Deprecate support for `is_flag` and `flag_value` parameters. PR
  [#&#8203;987](https://redirect.github.com/fastapi/typer/pull/987) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - 🔥 Remove unused functionality from
  `_typing.py` file. PR [#&#8203;805](https://redirect.github.com/fastapi/typer/pull/805) by
  [@&#8203;ivantodorovich](https://redirect.github.com/ivantodorovich). - ✏️ Fix typo in function
  name `_make_rich_text`. PR [#&#8203;959](https://redirect.github.com/fastapi/typer/pull/959) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg).

##### Internal

- ✅ Only run completion installation tests when the env var `_TYPER_RUN_INSTALL_COMPLETION_TESTS` is
  set. PR [#&#8203;995](https://redirect.github.com/fastapi/typer/pull/995) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - 📝 Update the docstring of the
  `_make_rich_text` method. PR [#&#8203;972](https://redirect.github.com/fastapi/typer/pull/972) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ⬆ \[pre-commit.ci] pre-commit
  autoupdate. PR [#&#8203;1040](https://redirect.github.com/fastapi/typer/pull/1040) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump
  mkdocs-material from 9.5.42 to 9.5.44. PR
  [#&#8203;1042](https://redirect.github.com/fastapi/typer/pull/1042) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.7.1
  to 0.7.2. PR [#&#8203;1038](https://redirect.github.com/fastapi/typer/pull/1038) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  mkdocs-macros-plugin from 1.3.6 to 1.3.7. PR
  [#&#8203;1031](https://redirect.github.com/fastapi/typer/pull/1031) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1032](https://redirect.github.com/fastapi/typer/pull/1032) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.7.0 to 0.7.1. PR [#&#8203;1029](https://redirect.github.com/fastapi/typer/pull/1029) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump pillow from
  10.4.0 to 11.0.0. PR [#&#8203;1023](https://redirect.github.com/fastapi/typer/pull/1023) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.35 to 9.5.42. PR [#&#8203;1027](https://redirect.github.com/fastapi/typer/pull/1027) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.6.5
  to 0.7.0. PR [#&#8203;1026](https://redirect.github.com/fastapi/typer/pull/1026) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  mkdocs-macros-plugin from 1.2.0 to 1.3.6. PR
  [#&#8203;1025](https://redirect.github.com/fastapi/typer/pull/1025) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Update pre-commit
  requirement from <4.0.0,>=2.17.0 to >=2.17.0,<5.0.0. PR
  [#&#8203;1012](https://redirect.github.com/fastapi/typer/pull/1012) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  pypa/gh-action-pypi-publish from 1.10.1 to 1.10.3. PR
  [#&#8203;1009](https://redirect.github.com/fastapi/typer/pull/1009) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;1001](https://redirect.github.com/fastapi/typer/pull/1001) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - 👷 Update Deploy
  docs CI to use uv. PR [#&#8203;1021](https://redirect.github.com/fastapi/typer/pull/1021) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Fix smokeshow, checkout files on CI.
  PR [#&#8203;1020](https://redirect.github.com/fastapi/typer/pull/1020) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Use uv in CI. PR
  [#&#8203;1019](https://redirect.github.com/fastapi/typer/pull/1019) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Update `labeler.yml`. PR
  [#&#8203;1014](https://redirect.github.com/fastapi/typer/pull/1014) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Update worfkow deploy-docs-notify
  URL. PR [#&#8203;1011](https://redirect.github.com/fastapi/typer/pull/1011) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - 👷 Upgrade Cloudflare GitHub Action. PR
  [#&#8203;1010](https://redirect.github.com/fastapi/typer/pull/1010) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - ⬆ Bump mkdocs-macros-plugin from 1.0.5
  to 1.2.0. PR [#&#8203;992](https://redirect.github.com/fastapi/typer/pull/992) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump ruff from 0.6.4
  to 0.6.5. PR [#&#8203;991](https://redirect.github.com/fastapi/typer/pull/991) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.34 to 9.5.35. PR [#&#8203;996](https://redirect.github.com/fastapi/typer/pull/996) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;993](https://redirect.github.com/fastapi/typer/pull/993) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆
  \[pre-commit.ci] pre-commit autoupdate. PR
  [#&#8203;982](https://redirect.github.com/fastapi/typer/pull/982) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump
  tiangolo/issue-manager from 0.5.0 to 0.5.1. PR
  [#&#8203;980](https://redirect.github.com/fastapi/typer/pull/980) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - 👷 Update
  `issue-manager.yml`. PR [#&#8203;978](https://redirect.github.com/fastapi/typer/pull/978) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo). - ⬆ Bump ruff from 0.6.3 to 0.6.4. PR
  [#&#8203;975](https://redirect.github.com/fastapi/typer/pull/975) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump mkdocs-material
  from 9.5.33 to 9.5.34. PR [#&#8203;963](https://redirect.github.com/fastapi/typer/pull/963) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ Bump
  pypa/gh-action-pypi-publish from 1.9.0 to 1.10.1. PR
  [#&#8203;973](https://redirect.github.com/fastapi/typer/pull/973) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;966](https://redirect.github.com/fastapi/typer/pull/966) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - 💚 Set
  `include-hidden-files` to `True` when using the `upload-artifact` GH action. PR
  [#&#8203;967](https://redirect.github.com/fastapi/typer/pull/967) by
  [@&#8203;svlandeg](https://redirect.github.com/svlandeg). - ⬆ Bump ruff from 0.6.1 to 0.6.3. PR
  [#&#8203;961](https://redirect.github.com/fastapi/typer/pull/961) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - ⬆ \[pre-commit.ci]
  pre-commit autoupdate. PR [#&#8203;689](https://redirect.github.com/fastapi/typer/pull/689) by
  [@&#8203;pre-commit-ci\[bot\]](https://redirect.github.com/apps/pre-commit-ci). - ⬆ Bump ruff from
  0.2.0 to 0.6.1. PR [#&#8203;938](https://redirect.github.com/fastapi/typer/pull/938) by
  [@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot). - 👷 Update
  `latest-changes` GitHub Action. PR
  [#&#8203;955](https://redirect.github.com/fastapi/typer/pull/955) by
  [@&#8203;tiangolo](https://redirect.github.com/tiangolo).

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Enabled.

♻ **Rebasing**: Whenever PR is behind base branch, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job
  log](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzOS43LjEiLCJ1cGRhdGVkSW5WZXIiOiIzOS43LjEiLCJ0YXJnZXRCcmFuY2giOiJtYWluIiwibGFiZWxzIjpbXX0=-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.12.2
  ([`344ed9a`](https://github.com/MartinBernstorff/Memium/commit/344ed9afc3ce08094003692507c6f61ba3b045ad))


## v0.25.4 (2024-11-06)

### Bug Fixes

- **deps**: Update dependency tqdm to v4.67.0
  ([`ab27f1b`](https://github.com/MartinBernstorff/Memium/commit/ab27f1b9ce89f4d2dbe849f3397124f72e475925))


## v0.25.3 (2024-11-06)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.388
  ([`6763193`](https://github.com/MartinBernstorff/Memium/commit/6763193c733442854d88c375d85d45724e5d5709))

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.12.1
  ([`be2a1fb`](https://github.com/MartinBernstorff/Memium/commit/be2a1fbcd129ec35895ed1abdfee8276b020eb77))


## v0.25.2 (2024-11-05)

### Performance Improvements

- Check for anki before note sync ([#766](https://github.com/MartinBernstorff/Memium/pull/766),
  [`d4f33b9`](https://github.com/MartinBernstorff/Memium/commit/d4f33b958a8671e1bf69bb5f941d2d2a1894e423))


## v0.25.1 (2024-11-04)

### Bug Fixes

- **deps**: Update dependency sentry-sdk to v2.18.0
  ([`483feb4`](https://github.com/MartinBernstorff/Memium/commit/483feb4cf274a2e787e20f8292af2621f67d1a16))


## v0.25.0 (2024-11-01)

### Features

- Simplify code visualisation ([#764](https://github.com/MartinBernstorff/Memium/pull/764),
  [`315eb24`](https://github.com/MartinBernstorff/Memium/commit/315eb24381048ae0b56566a2e5a13bf50a3f4468))


## v0.24.10 (2024-10-30)

### Bug Fixes

- **deps**: Update dependency pyright to v1.1.387
  ([`5ac08cb`](https://github.com/MartinBernstorff/Memium/commit/5ac08cbe50223007916976cbdbbc83555147b122))


## v0.24.9 (2024-10-29)

### Bug Fixes

- **deps**: Update dependency pytest-cov to v6
  ([`f00e1ad`](https://github.com/MartinBernstorff/Memium/commit/f00e1ad36ab7169240fb62f8caa5dc9e3c14e6a4))


## v0.24.8 (2024-10-29)

### Bug Fixes

- **deps**: Update dependency pytest to v8
  ([`2004f7c`](https://github.com/MartinBernstorff/Memium/commit/2004f7c0cc9a8591a9e31790642b5a391bf504cd))

- **deps**: Update dependency pre-commit to v4
  ([`93053e7`](https://github.com/MartinBernstorff/Memium/commit/93053e7908ed767e447b4627234fecc43557fb90))


## v0.24.7 (2024-10-29)

### Bug Fixes

- **deps**: Update dependency syrupy to v4.7.2
  ([`90ac769`](https://github.com/MartinBernstorff/Memium/commit/90ac7695e893caa126899ef1a1f23f17b51b437c))

- **deps**: Update dependency pydantic to v2.9.2
  ([`279286b`](https://github.com/MartinBernstorff/Memium/commit/279286b31f76c0d5f98498f0341f586edc8f9c0b))


## v0.24.6 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency markdown to v3.7
  ([`c4bbd4f`](https://github.com/MartinBernstorff/Memium/commit/c4bbd4fbd93b8d888c1e75afbffb834ab927f57f))


## v0.24.5 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency pre-commit to v3.8.0
  ([`8233a4e`](https://github.com/MartinBernstorff/Memium/commit/8233a4e75e2453141c0d5d24c9b93143491f0882))


## v0.24.4 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency cffi to v1.17.1
  ([`77c8997`](https://github.com/MartinBernstorff/Memium/commit/77c89976ea4e126ab00607b95e60717759c59167))

- **deps**: Update dependency diff-cover to v9.2.0
  ([`df00d82`](https://github.com/MartinBernstorff/Memium/commit/df00d825e0d0adde3c4070fe234ea03f7fca3011))


## v0.24.3 (2024-10-28)

### Bug Fixes

- **deps**: Update dependency typer to v0.12.5
  ([`4c55218`](https://github.com/MartinBernstorff/Memium/commit/4c55218434fc0c196b0fda5eb2fc2e8d868625d1))

- **deps**: Update dependency bs4 to v0.0.2
  ([`44ca48d`](https://github.com/MartinBernstorff/Memium/commit/44ca48d7b05bace5a01ad60639a2540211c48d30))

### Chores

- **deps**: Update dependency tqdm to v4.66.6
  ([`40f0c52`](https://github.com/MartinBernstorff/Memium/commit/40f0c528c4694b6c4fdb40532529948394c0c09e))


## v0.24.2 (2024-10-27)

### Bug Fixes

- Typo ([#750](https://github.com/MartinBernstorff/Memium/pull/750),
  [`c6ff00e`](https://github.com/MartinBernstorff/Memium/commit/c6ff00eb3876a5789cff9f3a40fafec4d368efd4))


## v0.24.1 (2024-10-27)

### Bug Fixes

- Further improve duplicate loggig ([#749](https://github.com/MartinBernstorff/Memium/pull/749),
  [`2d6431b`](https://github.com/MartinBernstorff/Memium/commit/2d6431bc30a3fee1a53f147c27980bc7c23c058f))

### Refactoring

- Html parsing ([#748](https://github.com/MartinBernstorff/Memium/pull/748),
  [`a9578ce`](https://github.com/MartinBernstorff/Memium/commit/a9578cefe03d9336982af153bb7e966b46ab5d86))


## v0.24.0 (2024-10-27)

### Features

- Improve styling of code blocks ([#747](https://github.com/MartinBernstorff/Memium/pull/747),
  [`c513731`](https://github.com/MartinBernstorff/Memium/commit/c513731321eb822d2d2d4c9afba588783d7c4ff6))


## v0.23.0 (2024-10-27)

### Features

- Improve logging ([#746](https://github.com/MartinBernstorff/Memium/pull/746),
  [`a4647d3`](https://github.com/MartinBernstorff/Memium/commit/a4647d345db8a3dd04c63547ad30b5763b52fabe))


## v0.22.2 (2024-10-27)

### Bug Fixes

- Improve logging of parser errors ([#745](https://github.com/MartinBernstorff/Memium/pull/745),
  [`6a101d4`](https://github.com/MartinBernstorff/Memium/commit/6a101d40e35a0dd00da42ab77e419ecbabfdcbe4))


## v0.22.1 (2024-10-27)

### Bug Fixes

- Disable irrelevant genanki warnings ([#744](https://github.com/MartinBernstorff/Memium/pull/744),
  [`bbf5458`](https://github.com/MartinBernstorff/Memium/commit/bbf5458f768519f9ff27e0d9a81c309900431bb5))


## v0.22.0 (2024-10-27)

### Features

- Add codeblock parsing ([#742](https://github.com/MartinBernstorff/Memium/pull/742),
  [`cc48a3b`](https://github.com/MartinBernstorff/Memium/commit/cc48a3bda50b64808e6adceb818d9622737e3a5a))


## v0.21.6 (2024-10-27)

### Bug Fixes

- Empty rows in table parsing ([#741](https://github.com/MartinBernstorff/Memium/pull/741),
  [`03de23e`](https://github.com/MartinBernstorff/Memium/commit/03de23e7362f8a84a87a30b7d8d3513c2adf0b0e))


## v0.21.5 (2024-10-27)

### Bug Fixes

- Handle dashes in wikilinks ([#740](https://github.com/MartinBernstorff/Memium/pull/740),
  [`97d1cf0`](https://github.com/MartinBernstorff/Memium/commit/97d1cf0e92db1b9ab9e00de883d37b24870930c0))


## v0.21.4 (2024-10-27)

### Bug Fixes

- More generous parsing of italics ([#739](https://github.com/MartinBernstorff/Memium/pull/739),
  [`39298c1`](https://github.com/MartinBernstorff/Memium/commit/39298c1cdc75db95acbd02c3b7fc631e1456c444))

### Chores

- **deps**: Update dependency sentry-sdk to v2.17.0
  ([`c35c510`](https://github.com/MartinBernstorff/Memium/commit/c35c51091cedd9b68956e5ff26a904caf5691d2c))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.12.0
  ([`c2587b8`](https://github.com/MartinBernstorff/Memium/commit/c2587b81eede1cb71c560a0b0d778710167f44d6))

- **deps**: Update dependency pyright to v1.1.386
  ([`a7afc33`](https://github.com/MartinBernstorff/Memium/commit/a7afc33dafde6c45ad06aba5ab59c7b6b4dc3c40))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.6
  ([`dc51102`](https://github.com/MartinBernstorff/Memium/commit/dc51102619b15a82e7da4d2a44934ef218ccedce))

- **deps**: Update dependency sentry-sdk to v2.10.0
  ([`1625ea0`](https://github.com/MartinBernstorff/Memium/commit/1625ea072855013f4b6c96de28e4b0b0312cf2b3))

- **deps**: Update dependency sentry-sdk to v2.9.0
  ([`93f2d18`](https://github.com/MartinBernstorff/Memium/commit/93f2d1834095f19cbefc69f4fe2110ff257969da))

- **deps**: Update dependency dev/pyright to v1.1.371
  ([`b215832`](https://github.com/MartinBernstorff/Memium/commit/b2158322a0bef68e5eb7e15c66574a49ec7ff977))

- **deps**: Update dependency sentry-sdk to v2.8.0
  ([`23a5ce0`](https://github.com/MartinBernstorff/Memium/commit/23a5ce030b61a2f6a67c7cb90ee9ab66d3bd35fd))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.5
  ([`c306ac5`](https://github.com/MartinBernstorff/Memium/commit/c306ac5508d7d86195c7c73ed9b7cf2c4d8d9384))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.4
  ([`d0d62b6`](https://github.com/MartinBernstorff/Memium/commit/d0d62b65890aa70abd2852ec2e1049db4d74a45e))

- **deps**: Update dependency pydantic to v2.8.2
  ([`8b2c12e`](https://github.com/MartinBernstorff/Memium/commit/8b2c12e58cd395862ea4b10b57479ab2aa924472))

- **deps**: Update dependency pydantic to v2.8.1
  ([`2d711d9`](https://github.com/MartinBernstorff/Memium/commit/2d711d97ade8b64783de5e443ceddb1adbda2f62))

- **deps**: Update dependency dev/pyright to v1.1.370
  ([`595e89e`](https://github.com/MartinBernstorff/Memium/commit/595e89ec0f1a326cecb058fdee638119b6bdf9aa))

- **deps**: Update dependency pydantic to v2.8.0
  ([`c89414c`](https://github.com/MartinBernstorff/Memium/commit/c89414cd483aaf15071d6efdd95a6cd98567309b))

- **deps**: Update dependency sentry-sdk to v2.7.1
  ([`7f9163e`](https://github.com/MartinBernstorff/Memium/commit/7f9163e435af045c85182c61451efe55ea36f2d8))

- **deps**: Update dependency sentry-sdk to v2.7.0
  ([`525ad14`](https://github.com/MartinBernstorff/Memium/commit/525ad146d6763a62f4df549ec486c445c09441c9))

- **deps**: Update dependency tests/diff-cover to v9.1.0
  ([`a7d11e1`](https://github.com/MartinBernstorff/Memium/commit/a7d11e1cfe9557ee1a7fcbc92fe0171a9ed7d523))

- **deps**: Update dependency dev/pyright to v1.1.369
  ([`56a257e`](https://github.com/MartinBernstorff/Memium/commit/56a257ec62e10c496c538dc6a29000bbc0c9c3ca))

- Cleanup ([#696](https://github.com/MartinBernstorff/Memium/pull/696),
  [`035ea7c`](https://github.com/MartinBernstorff/Memium/commit/035ea7c3b076de669ef9cd2a8cc6a3e0a4366547))

- **deps**: Update dependency sentry-sdk to v2.6.0
  ([`da39d73`](https://github.com/MartinBernstorff/Memium/commit/da39d735c2b40ca6da41f85bbf9614f950a0f0d3))

- **deps**: Update dependency dev/pyright to v1.1.368
  ([`e807fc9`](https://github.com/MartinBernstorff/Memium/commit/e807fc943f2486eedfe402938e680889a92a2f00))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.3
  ([`368a2d0`](https://github.com/MartinBernstorff/Memium/commit/368a2d0816ae559c2d5f522243ea3eba0fe133c5))

- **deps**: Update docker/build-push-action action to v6
  ([`05d754c`](https://github.com/MartinBernstorff/Memium/commit/05d754c62e6c606f8eae7bfd1f49dce013549922))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.2
  ([`c27b50d`](https://github.com/MartinBernstorff/Memium/commit/c27b50d6c84ea4c36194fea34b95a29fcf666495))

- **deps**: Update dependency pydantic to v2.7.4
  ([`ef47449`](https://github.com/MartinBernstorff/Memium/commit/ef474490c539413fba3463945059aa59b5a1c047))

- **deps**: Update dependency dev/pyright to v1.1.367
  ([`7df6c4e`](https://github.com/MartinBernstorff/Memium/commit/7df6c4ecdaacec8cea27ec813040c6a311ebdaf9))

- **deps**: Update dependency sentry-sdk to v2.5.1
  ([`85d1211`](https://github.com/MartinBernstorff/Memium/commit/85d12110fb114120f9a4c1fb6ad93b073e5e3f45))

- **deps**: Update dependency sentry-sdk to v2.5.0
  ([`6141c7b`](https://github.com/MartinBernstorff/Memium/commit/6141c7b3b82195346c8981c59d01d26241c5ace9))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.1
  ([`243b1fe`](https://github.com/MartinBernstorff/Memium/commit/243b1fe2122cb7005aef5aab87e2867fe00584c9))

- **deps**: Update dependency sentry-sdk to v2.4.0
  ([`cb38267`](https://github.com/MartinBernstorff/Memium/commit/cb38267aad20cfdf25d4710ba1e17fdedf07036e))

- **deps**: Update dependency pydantic to v2.7.3
  ([`ade33b9`](https://github.com/MartinBernstorff/Memium/commit/ade33b9b8708c6c59a8d0db8f19fe4ebe838cc0f))

- **deps**: Update dependency wasabi to v1.1.3
  ([`a639a64`](https://github.com/MartinBernstorff/Memium/commit/a639a640fca2dd551cc22816603d79e3368054b5))

- **deps**: Update dependency dev/pyright to v1.1.365
  ([`788df39`](https://github.com/MartinBernstorff/Memium/commit/788df390436ba6f767b22b98aba56dfee5fd2852))

- **deps**: Update dependency pydantic to v2.7.2
  ([`469dd43`](https://github.com/MartinBernstorff/Memium/commit/469dd43e0039be7f7f976acce7e0413befd0fd33))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.8.0
  ([`40a7f7f`](https://github.com/MartinBernstorff/Memium/commit/40a7f7f039c8414b03914ce619af1ed73dab0b1b))

- **deps**: Update dependency sentry-sdk to v2.3.1
  ([`8973609`](https://github.com/MartinBernstorff/Memium/commit/897360944183d39de31ff5d2320b3add26a0673e))

- **deps**: Update dependency sentry-sdk to v2.3.0
  ([`68eba46`](https://github.com/MartinBernstorff/Memium/commit/68eba46fc5026e98d780f541e05767d046bd127c))

- **deps**: Update dependency dev/ruff to v0.4.5
  ([`7006e4f`](https://github.com/MartinBernstorff/Memium/commit/7006e4ff49cd64ff059a72fd05d99292624b3c7e))

- **deps**: Update dependency dev/pyright to v1.1.364
  ([`71f2f73`](https://github.com/MartinBernstorff/Memium/commit/71f2f739cb70320f8f9e57e1b3c0a1a2cc73aaf3))

- **deps**: Update dependency sentry-sdk to v2.2.1
  ([`58d33db`](https://github.com/MartinBernstorff/Memium/commit/58d33db77b94ec915f9aa9e436bf3805011f3adf))

- **deps**: Update dependency sentry-sdk to v2.2.0
  ([`3892955`](https://github.com/MartinBernstorff/Memium/commit/38929558ece763fda12b0b0b0ef770efa762b1ee))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.3
  ([`b6a0329`](https://github.com/MartinBernstorff/Memium/commit/b6a03293423ff8c9d105d49a9666e0ffa3bdf56b))

- **deps**: Update dependency dev/pyright to v1.1.363
  ([`f58bde5`](https://github.com/MartinBernstorff/Memium/commit/f58bde57b3ec756895157ca64e3d1a3dacb4c068))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.2
  ([`a8ce44c`](https://github.com/MartinBernstorff/Memium/commit/a8ce44c3412ff9fbae155f1feff3d334948c6ad7))

- **deps**: Update dependency dev/pre-commit to v3.7.1
  ([`3e41364`](https://github.com/MartinBernstorff/Memium/commit/3e41364c651315adcb2a743cc5f475e76f3fb11d))

- **deps**: Update dependency dev/ruff to v0.4.4
  ([`e0896bd`](https://github.com/MartinBernstorff/Memium/commit/e0896bd41b79cdd8dc324dd685fd066b640a2901))

- **deps**: Update dependency dev/pyright to v1.1.362
  ([`ed72e3f`](https://github.com/MartinBernstorff/Memium/commit/ed72e3fbebfa6f653ebe7b8ac975efa00f18a8b5))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.1
  ([`b36a693`](https://github.com/MartinBernstorff/Memium/commit/b36a693ea8c8c2656716504c8e5710bda2d54e10))


## v0.21.3 (2024-05-06)

### Bug Fixes

- Do not escape html ([#664](https://github.com/MartinBernstorff/Memium/pull/664),
  [`dcf5b28`](https://github.com/MartinBernstorff/Memium/commit/dcf5b28ac57a9df8996fc7abbd7ae05d676d215f))

- update anki_prompt_qa.py - test: update test_anki_prompt_qa.ambr

### Chores

- **deps**: Update dependency sentry-sdk to v2.1.1
  ([`94c4d3c`](https://github.com/MartinBernstorff/Memium/commit/94c4d3c80cf75f241470ef5211a68e7037be775c))

- **deps**: Update dependency sentry-sdk to v2.1.0
  ([`625b0bf`](https://github.com/MartinBernstorff/Memium/commit/625b0bfeb337895b6dc47fddae68836676cd3b1f))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.7.0
  ([`05181e1`](https://github.com/MartinBernstorff/Memium/commit/05181e1b3367c9231b1219728d2f54a7ddd769b9))

- **deps**: Update dependency dev/ruff to v0.4.3
  ([`e8f6541`](https://github.com/MartinBernstorff/Memium/commit/e8f6541bf1bbf49e738ec381ae5b609be2b52d4b))

- **deps**: Update dependency tqdm to v4.66.4
  ([`168a75e`](https://github.com/MartinBernstorff/Memium/commit/168a75e9afcae0b7cac8ce4d06a58427048467f2))

- **deps**: Update dependency dev/pyright to v1.1.361
  ([`9fdb56b`](https://github.com/MartinBernstorff/Memium/commit/9fdb56b8a2390e37a2e5cc8a85cb1d4a9488fa65))

- Delete test.py ([#656](https://github.com/MartinBernstorff/Memium/pull/656),
  [`1505b0f`](https://github.com/MartinBernstorff/Memium/commit/1505b0f8d8fbea4785f5935a79e717e38fece8c5))

- Delete test.py
  ([`f1854dc`](https://github.com/MartinBernstorff/Memium/commit/f1854dc65643c430df9db0ce62cafb94680abb03))

### Testing

- Update test_anki_prompt_qa.ambr
  ([`b08f56a`](https://github.com/MartinBernstorff/Memium/commit/b08f56ae8517f5b5a5c04ac58b79022fd9c29aaf))


## v0.21.2 (2024-04-30)

### Bug Fixes

- Only escape relevant sections ([#655](https://github.com/MartinBernstorff/Memium/pull/655),
  [`9f1cb01`](https://github.com/MartinBernstorff/Memium/commit/9f1cb01f86e83b82b7e92fd04bd05fab759a6458))

- Only escape relevant sections
  ([`5e6d403`](https://github.com/MartinBernstorff/Memium/commit/5e6d4034bfb35a02c224241ddfb32ba7c29b3be3))

### Chores

- **deps**: Update python-semantic-release/python-semantic-release action to v9.6.0
  ([`6acdc9c`](https://github.com/MartinBernstorff/Memium/commit/6acdc9cb1c02282ea392d2185ee26a6305628078))

- **deps**: Update dependency tests/pytest-xdist to v3.6.1
  ([`dcd0182`](https://github.com/MartinBernstorff/Memium/commit/dcd0182171c349ea94848c6289d71cc39d4b90c3))

### Refactoring

- Split cli and main ([#651](https://github.com/MartinBernstorff/Memium/pull/651),
  [`3e2fab4`](https://github.com/MartinBernstorff/Memium/commit/3e2fab401f0b397553746ba8c5b0fda3203ea1ce))

- Split cli and main
  ([`a316423`](https://github.com/MartinBernstorff/Memium/commit/a316423f5d4b4235848af9300f0b66919ee5bc90))

### Testing

- Update test_anki_prompt_qa.py
  ([`0dbd6c3`](https://github.com/MartinBernstorff/Memium/commit/0dbd6c37077c7acc56bef711f44f1944d0aad2d7))


## v0.21.1 (2024-04-27)

### Bug Fixes

- Html escaping ([#641](https://github.com/MartinBernstorff/Memium/pull/641),
  [`6f97f55`](https://github.com/MartinBernstorff/Memium/commit/6f97f55d85764265e4fbe6af58af832c6f3695a7))

### Testing

- Update test_anki_prompt_qa.py
  ([`e142041`](https://github.com/MartinBernstorff/Memium/commit/e1420419b3740c8a23281ff95254d107440e8ef2))


## v0.21.0 (2024-04-27)

### Features

- **#637**: Append log to output folder
  ([#649](https://github.com/MartinBernstorff/Memium/pull/649),
  [`f03969c`](https://github.com/MartinBernstorff/Memium/commit/f03969c17296c48ecd67f81df411435fe17384b9))

Fixes #637

- **#637**: Append log to output folder
  ([`178ff35`](https://github.com/MartinBernstorff/Memium/commit/178ff358501080b699f1173a3241d493e774e567))

Fixes #637


## v0.20.0 (2024-04-27)

### Chores

- **deps**: Update dependency sentry-sdk to v2.0.1
  ([`37dc0ed`](https://github.com/MartinBernstorff/Memium/commit/37dc0ed92635d1c82cfe60fa705c638fe3be2054))

- **deps**: Update dependency dev/ruff to v0.4.2
  ([`f7413f5`](https://github.com/MartinBernstorff/Memium/commit/f7413f5bdb96444623a0e447a390e04d9c256f94))

- **deps**: Update dependency sentry-sdk to v2
  ([`782b27b`](https://github.com/MartinBernstorff/Memium/commit/782b27b613d4cdb1bde0912b6e8e259204cbef7b))

- **deps**: Update dependency dev/pyright to v1.1.360
  ([`601e013`](https://github.com/MartinBernstorff/Memium/commit/601e0131a358c2a516701a7c3b6f523362342938))

- **deps**: Update dependency pydantic to v2.7.1
  ([`ea0ad67`](https://github.com/MartinBernstorff/Memium/commit/ea0ad67acfeb7dd53ef1833c4208597af3c12c1f))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.5.0
  ([`335798b`](https://github.com/MartinBernstorff/Memium/commit/335798bde44aee34346a9ecd5d0220a33e27cbd4))

### Features

- Move obsidian link to top of AnkiQA ([#648](https://github.com/MartinBernstorff/Memium/pull/648),
  [`f45cdf9`](https://github.com/MartinBernstorff/Memium/commit/f45cdf9bb65c06b4a9d470e866347db62a2bbfe9))

- Move obsidian link to top of AnkiQA
  ([`8802e01`](https://github.com/MartinBernstorff/Memium/commit/8802e015d449ab63d9c50601cca1ccea5b053299))


## v0.19.1 (2024-04-22)

### Bug Fixes

- Calling method instead of getting link contents
  ([#639](https://github.com/MartinBernstorff/Memium/pull/639),
  [`81e68b4`](https://github.com/MartinBernstorff/Memium/commit/81e68b4cbaab50984aaab17aa683c8ebefdf74b7))

- Calling method instead of getting link contents
  ([`121fa88`](https://github.com/MartinBernstorff/Memium/commit/121fa8821f76c33d911b0264023dfd637d6ed3ff))


## v0.19.0 (2024-04-20)

### Chores

- **deps**: Update dependency tests/pytest-xdist to v3.6.0
  ([`ab9face`](https://github.com/MartinBernstorff/Memium/commit/ab9face94242ce642b6801526cc7a2d666ea1605))

- **deps**: Update dependency dev/ruff to v0.4.1
  ([`5d56819`](https://github.com/MartinBernstorff/Memium/commit/5d5681946cacf21cfbd331f4baadee8aa960198d))

- **deps**: Update dependency dev/ruff to v0.4.0
  ([`122bf50`](https://github.com/MartinBernstorff/Memium/commit/122bf5073a9debc3467bcb77b56c4edce0ba974f))

- **deps**: Update dependency dev/pyright to v1.1.359
  ([`ad3ad6b`](https://github.com/MartinBernstorff/Memium/commit/ad3ad6b2ca2c736adbb7cfe91608db83107805bd))

- **deps**: Update dependency tests/diff-cover to v9
  ([`573571f`](https://github.com/MartinBernstorff/Memium/commit/573571f9380ef749552ee1f69c378d2ad00c47ef))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.4.2
  ([`c14629d`](https://github.com/MartinBernstorff/Memium/commit/c14629dfe91b787c09985d90719c2f8b43297164))

- **deps**: Update dependency dev/ruff to v0.3.7
  ([`ae3928c`](https://github.com/MartinBernstorff/Memium/commit/ae3928c0e8b8964d83733134119c28b779c9d332))

- **deps**: Update dependency dev/ruff to v0.3.6
  ([`9243d80`](https://github.com/MartinBernstorff/Memium/commit/9243d80a285d24d519cc12b86b2ab751e7d4236b))

- **deps**: Update dependency pydantic to v2.7.0
  ([`b3a32f0`](https://github.com/MartinBernstorff/Memium/commit/b3a32f0b862c8054cdaf255bb6ccb9e0582e1df3))

- **deps**: Update dependency sentry-sdk to v1.45.0
  ([`eae82e6`](https://github.com/MartinBernstorff/Memium/commit/eae82e68846c6dfe1cec45817aec0234bd448047))

- **deps**: Update dependency typer to v0.12.3
  ([`e2f44fc`](https://github.com/MartinBernstorff/Memium/commit/e2f44fc0b9c9cc89518bf3e597ada32964fdbcde))

- **deps**: Update dependency dev/pyright to v1.1.358
  ([`08ea850`](https://github.com/MartinBernstorff/Memium/commit/08ea850e29b3c374038367968fa8a3cde098a8ec))

### Features

- Add open in obsidian button ([#635](https://github.com/MartinBernstorff/Memium/pull/635),
  [`8843a65`](https://github.com/MartinBernstorff/Memium/commit/8843a65ffac535ce5aa1768f9ca35bfb24ddd620))

- Add obsidian URI
  ([`78cfbcd`](https://github.com/MartinBernstorff/Memium/commit/78cfbcd9420b122bb872d12c896ef1b57568fbf8))

### Testing

- Update test_extractor_table.py and test_prompt.py
  ([`a862723`](https://github.com/MartinBernstorff/Memium/commit/a86272353d500b47f1c56970e690b8d63a28f413))


## v0.18.0 (2024-04-09)

### Features

- Support slashes in wikilinks ([#622](https://github.com/MartinBernstorff/Memium/pull/622),
  [`8fc90ac`](https://github.com/MartinBernstorff/Memium/commit/8fc90acdff2dc77bdff564e8ad27eda668a57b46))

- Support slashes in wikilinks
  ([`7d207ff`](https://github.com/MartinBernstorff/Memium/commit/7d207ff8964b390881a9169ed236db3541eb58cc))


## v0.17.0 (2024-04-09)

### Features

- Sort terms before generating subdecks
  ([#621](https://github.com/MartinBernstorff/Memium/pull/621),
  [`fd7e703`](https://github.com/MartinBernstorff/Memium/commit/fd7e703ad17e5edfc2d4e07f15f974e48a7f65bf))

- Sort terms before generating subdecks
  ([`9564ff7`](https://github.com/MartinBernstorff/Memium/commit/9564ff740ebd8a32540dd514b0d0e1475289441c))


## v0.16.1 (2024-04-09)

### Bug Fixes

- Term extraction ([#620](https://github.com/MartinBernstorff/Memium/pull/620),
  [`8816e48`](https://github.com/MartinBernstorff/Memium/commit/8816e48b87dda53ad57e8e3db10406db2f2366ed))

### Testing

- Update test_anki_prompt_qa.py
  ([`ec2f0d2`](https://github.com/MartinBernstorff/Memium/commit/ec2f0d2b72107b7dd738c4bf3042894969c374b5))


## v0.16.0 (2024-04-09)

### Features

- Create model if it does not exist ([#619](https://github.com/MartinBernstorff/Memium/pull/619),
  [`380ed4e`](https://github.com/MartinBernstorff/Memium/commit/380ed4eb659e82704565299e798c2d0200c7c6ab))

- Create model if it does not exist
  ([`e979d45`](https://github.com/MartinBernstorff/Memium/commit/e979d4567139e8ef095146193672e4bde65c0f2b))


## v0.15.0 (2024-04-09)

### Chores

- **deps**: Update dependency typer to v0.12.2
  ([`92e40a1`](https://github.com/MartinBernstorff/Memium/commit/92e40a182c0dc5f7320e7a11a5090a19d8f5cc51))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.4.1
  ([`1f58fa3`](https://github.com/MartinBernstorff/Memium/commit/1f58fa3c6636a20e477ce2df699712948fed30aa))

- **deps**: Update dependency typer to v0.12.1
  ([`dc7edb0`](https://github.com/MartinBernstorff/Memium/commit/dc7edb0bc96cdbf67542dfdbcfd69b099ee8d951))

- **deps**: Update dependency dev/pyright to v1.1.357
  ([`d8c851d`](https://github.com/MartinBernstorff/Memium/commit/d8c851d4c24e8dde3143c982bad093e49ddc7195))

- **deps**: Update dependency sentry-sdk to v1.44.1
  ([`0607674`](https://github.com/MartinBernstorff/Memium/commit/0607674265c1b680faad4901be09486d7d4a5130))

- **deps**: Update dependency tests/pytest-cov to v5
  ([`874eaaa`](https://github.com/MartinBernstorff/Memium/commit/874eaaa7755585a8b8ac5d8a7e6a53e6088d475a))

- **deps**: Update dependency typer to v0.12.0
  ([`e6e049d`](https://github.com/MartinBernstorff/Memium/commit/e6e049d58e2a8ee9493ac586ca7494fa32dcd175))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.4.0
  ([`eed8164`](https://github.com/MartinBernstorff/Memium/commit/eed816481f2ca1f2ad603178183b997e61d88305))

- **deps**: Update dependency sentry-sdk to v1.44.0
  ([`0f4dade`](https://github.com/MartinBernstorff/Memium/commit/0f4dade1b0bdf962433e301bc42221d8383e6188))

- **deps**: Update dependency markdown to v3.6
  ([`1748178`](https://github.com/MartinBernstorff/Memium/commit/1748178470228ed879b02981d0d6ce6d2b3ba159))

- **deps**: Update dependency dev/pre-commit to v3.7.0
  ([`fa48661`](https://github.com/MartinBernstorff/Memium/commit/fa4866192533ce4a4bae393c59e64e2481b6b000))

- **deps**: Update dependency pydantic to v2.6.4
  ([`e734d3e`](https://github.com/MartinBernstorff/Memium/commit/e734d3e80212d1a55e1ba4dcf92c5dbe2bc06e52))

- **deps**: Update dependency dev/ruff to v0.3.5
  ([`a96013f`](https://github.com/MartinBernstorff/Memium/commit/a96013f9311e1b19b5d73c90ba9c3e77a89860fc))

- **deps**: Update dependency dev/pyright to v1.1.356
  ([`64b2cf1`](https://github.com/MartinBernstorff/Memium/commit/64b2cf1a17f4a22d0164011b82c406535ef432ca))

- **deps**: Update dependency iterpy to v1.9.0
  ([`906e640`](https://github.com/MartinBernstorff/Memium/commit/906e640fd54e2a63f9bf4c8a82792ab86fdad113))

- **deps**: Update dependency dev/ruff to v0.3.2
  ([`8525583`](https://github.com/MartinBernstorff/Memium/commit/8525583632ace4464590d0246760b1f0f73f7a91))

- **deps**: Update dependency dev/pyright to v1.1.353
  ([`80d8b97`](https://github.com/MartinBernstorff/Memium/commit/80d8b97e4797934bd01af7549f32abaadd93a4a6))

- **deps**: Update dependency iterpy to v1.8.1
  ([`68ece09`](https://github.com/MartinBernstorff/Memium/commit/68ece09d05296ff0494a9f7f190781385cf869e0))

- **deps**: Update dependency iterpy to v1.7.0
  ([`1153826`](https://github.com/MartinBernstorff/Memium/commit/1153826e756961ef24379300d1a808fdc402b794))

- **deps**: Update dependency sentry-sdk to v1.41.0
  ([`b422c1e`](https://github.com/MartinBernstorff/Memium/commit/b422c1ea25535acaa859e410b1f4f5f5f6d8f149))

- **deps**: Update dependency dev/ruff to v0.3.1
  ([`6095ed2`](https://github.com/MartinBernstorff/Memium/commit/6095ed24df306ef93c8eeb8d827a93d04f8c92ee))

- **deps**: Update dependency dev/ruff to v0.3.0
  ([`7a93e73`](https://github.com/MartinBernstorff/Memium/commit/7a93e73674faf1ec614bdacfc20699393d13a76e))

- **deps**: Update dependency dev/pyright to v1.1.352
  ([`4341487`](https://github.com/MartinBernstorff/Memium/commit/4341487e9fa78cdbbeed2162b75a1779c6c77933))

- **deps**: Update dependency pydantic to v2.6.3
  ([`69ef4fb`](https://github.com/MartinBernstorff/Memium/commit/69ef4fb8fa6789849f3441ddff6ac15e65846899))

- **deps**: Update dependency tests/pytest-testmon to v2.1.1
  ([`eda5e2c`](https://github.com/MartinBernstorff/Memium/commit/eda5e2c99d60a4a68f947a2f70a32f9fcbf34a51))

- **deps**: Update dependency sentry-sdk to v1.40.6
  ([`f4a8f0e`](https://github.com/MartinBernstorff/Memium/commit/f4a8f0e2cd02edd5faf27b2d2cad94b64744091a))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.1.1
  ([`9a91fbf`](https://github.com/MartinBernstorff/Memium/commit/9a91fbf50c673c75a6075f9c715ece08bdc5eb87))

- **deps**: Update dependency pydantic to v2.6.2
  ([`70d8084`](https://github.com/MartinBernstorff/Memium/commit/70d808475f854593e17de61cf482dc0b09b0620b))

- **deps**: Update dependency dev/pyright to v1.1.351
  ([`0d18783`](https://github.com/MartinBernstorff/Memium/commit/0d187834784d4fd1b57f6400424f81940d78f735))

- **deps**: Update dependency iterpy to v1.6.0
  ([`25ee384`](https://github.com/MartinBernstorff/Memium/commit/25ee384a10ce5e28b9fc7ef492d287650411371a))

- **deps**: Update dependency sentry-sdk to v1.40.5
  ([`737cb25`](https://github.com/MartinBernstorff/Memium/commit/737cb25023abd55df145ef77ddc17dcf458c8e45))

- **deps**: Update dependency dev/pre-commit to v3.6.2
  ([`4e52e8d`](https://github.com/MartinBernstorff/Memium/commit/4e52e8d5604a68eb9276afe9614298f38bf13370))

- **deps**: Update dependency dev/ruff to v0.2.2
  ([`81544f3`](https://github.com/MartinBernstorff/Memium/commit/81544f3cc9801c0fb72fb14d0db73e05e983b6c2))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.1.0
  ([`19ddce7`](https://github.com/MartinBernstorff/Memium/commit/19ddce77d14b1b4ebbc61ad23ebbb80af7367ed2))

- **deps**: Update dependency sentry-sdk to v1.40.4
  ([`3abd2d5`](https://github.com/MartinBernstorff/Memium/commit/3abd2d5432baa3c627fd05fcbc289f863ac85b1a))

- **deps**: Update dependency iterpy to v1.5.1
  ([`67c93bd`](https://github.com/MartinBernstorff/Memium/commit/67c93bd85639e7daf00a0027cd7f73ef393175bf))

- **deps**: Update dependency iterpy to v1.5.0
  ([`81cbf94`](https://github.com/MartinBernstorff/Memium/commit/81cbf940b25f088eaa4cce306bd5bcde1dcc0b60))

- **deps**: Update dependency tqdm to v4.66.2
  ([`4fa5a3d`](https://github.com/MartinBernstorff/Memium/commit/4fa5a3d6e34c384109864b0d6cb7de4aceef126b))

- **deps**: Update dependency dev/pre-commit to v3.6.1
  ([`c020f67`](https://github.com/MartinBernstorff/Memium/commit/c020f676cf9a46f9509f7f37b8adea1b5aefbb2e))

- **deps**: Update dependency iterpy to v1
  ([`455ff31`](https://github.com/MartinBernstorff/Memium/commit/455ff31a3389f809ed0055d49cd94512e349df67))

- **deps**: Update dependency sentry-sdk to v1.40.3
  ([`87a1e83`](https://github.com/MartinBernstorff/Memium/commit/87a1e8388147038211a3574e75a4f6721c5a386c))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.0.3
  ([`4d28b59`](https://github.com/MartinBernstorff/Memium/commit/4d28b5966a97102b5db802b5c609d06f5080014b))

- **deps**: Update python-semantic-release/python-semantic-release action to v9.0.2
  ([`ddeba70`](https://github.com/MartinBernstorff/Memium/commit/ddeba707e96634657053bac2b42199c86f6cc56e))

- **deps**: Update dependency sentry-sdk to v1.40.2
  ([`658a8c3`](https://github.com/MartinBernstorff/Memium/commit/658a8c30d8c24a2efdcf3aff174a093bd8aac446))

- **deps**: Update python-semantic-release/python-semantic-release action to v9
  ([`b4a4dd6`](https://github.com/MartinBernstorff/Memium/commit/b4a4dd654ba2ff09d70022089842565d82790565))

### Features

- Create decks based on wikilinks in qa question
  ([#618](https://github.com/MartinBernstorff/Memium/pull/618),
  [`bcd61e3`](https://github.com/MartinBernstorff/Memium/commit/bcd61e32384799e6791af0eb5acc5fca930a6a05))

feat: create decks based on wikilinks in qa question

update 8 files

- Create decks based on wikilinks in qa question
  ([`448976b`](https://github.com/MartinBernstorff/Memium/commit/448976ba82f92a0b3909861e746f28e5ceafb58f))


## v0.14.3 (2024-02-06)

### Bug Fixes

- Remove cloze extraction from default ([#571](https://github.com/MartinBernstorff/Memium/pull/571),
  [`48074a8`](https://github.com/MartinBernstorff/Memium/commit/48074a8194becd2bfc4c5391453d5df7726dde2c))

- Remove cloze extraction from default
  ([`3d4c889`](https://github.com/MartinBernstorff/Memium/commit/3d4c889c9ad56b51a4de4a9efbc2c163866909a0))

### Chores

- **deps**: Update dependency tests/pytest to v7.4.4
  ([#559](https://github.com/MartinBernstorff/Memium/pull/559),
  [`a481ede`](https://github.com/MartinBernstorff/Memium/commit/a481ede81df0bf67e6c67cf3dbacf18bcc8ce1b2))

[![Mend Renovate](https://app.renovatebot.com/images/banner.svg)](https://renovatebot.com)

This PR contains the following updates:

| Package | Change | Age | Adoption | Passing | Confidence | |---|---|---|---|---|---| |
  [tests/pytest](https://docs.pytest.org/en/latest/)
  ([source](https://togithub.com/pytest-dev/pytest),
  [changelog](https://docs.pytest.org/en/stable/changelog.html)) | `==7.4.0` -> `==7.4.4` |
  [![age](https://developer.mend.io/api/mc/badges/age/pypi/tests%2fpytest/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![adoption](https://developer.mend.io/api/mc/badges/adoption/pypi/tests%2fpytest/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![passing](https://developer.mend.io/api/mc/badges/compatibility/pypi/tests%2fpytest/7.4.0/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |
  [![confidence](https://developer.mend.io/api/mc/badges/confidence/pypi/tests%2fpytest/7.4.0/7.4.4?slim=true)](https://docs.renovatebot.com/merge-confidence/)
  |

---

### Release Notes

<details> <summary>pytest-dev/pytest (tests/pytest)</summary>

### [`v7.4.4`](https://togithub.com/pytest-dev/pytest/compare/7.4.3...7.4.4)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.3...7.4.4)

### [`v7.4.3`](https://togithub.com/pytest-dev/pytest/releases/tag/v7.4.3): pytest 7.4.3
  (2023-10-24)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.2...7.4.3)

## Bug Fixes

- [#&#8203;10447](https://togithub.com/pytest-dev/pytest/issues/10447): Markers are now considered
  in the reverse mro order to ensure base class markers are considered first -- this resolves a
  regression.

- [#&#8203;11239](https://togithub.com/pytest-dev/pytest/issues/11239): Fixed `:=` in asserts
  impacting unrelated test cases.

- [#&#8203;11439](https://togithub.com/pytest-dev/pytest/issues/11439): Handled an edge case where
  :data:`sys.stderr` might already be closed when :ref:`faulthandler` is tearing down.

### [`v7.4.2`](https://togithub.com/pytest-dev/pytest/releases/tag/7.4.2): pytest 7.4.2 (2023-09-07)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.1...7.4.2)

##### Bug Fixes

- [#&#8203;11237](https://togithub.com/pytest-dev/pytest/issues/11237): Fix doctest collection of
  `functools.cached_property` objects.

- [#&#8203;11306](https://togithub.com/pytest-dev/pytest/issues/11306): Fixed bug using
  `--importmode=importlib` which would cause package `__init__.py` files to be imported more than
  once in some cases.

- [#&#8203;11367](https://togithub.com/pytest-dev/pytest/issues/11367): Fixed bug where
  `user_properties` where not being saved in the JUnit XML file if a fixture failed during teardown.

- [#&#8203;11394](https://togithub.com/pytest-dev/pytest/issues/11394): Fixed crash when parsing
  long command line arguments that might be interpreted as files.

##### Improved Documentation

- [#&#8203;11391](https://togithub.com/pytest-dev/pytest/issues/11391): Improved disclaimer on
  pytest plugin reference page to better indicate this is an automated, non-curated listing.

### [`v7.4.1`](https://togithub.com/pytest-dev/pytest/releases/tag/7.4.1): pytest 7.4.1 (2023-09-02)

[Compare Source](https://togithub.com/pytest-dev/pytest/compare/7.4.0...7.4.1)

## Bug Fixes

- [#&#8203;10337](https://togithub.com/pytest-dev/pytest/issues/10337): Fixed bug where fake
  intermediate modules generated by `--import-mode=importlib` would not include the child modules as
  attributes of the parent modules.

- [#&#8203;10702](https://togithub.com/pytest-dev/pytest/issues/10702): Fixed error assertion
  handling in `pytest.approx` when `None` is an expected or received value when comparing
  dictionaries.

- [#&#8203;10811](https://togithub.com/pytest-dev/pytest/issues/10811): Fixed issue when using
  `--import-mode=importlib` together with `--doctest-modules` that caused modules to be imported
  more than once, causing problems with modules that have import side effects.

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no
  schedule defined).

🚦 **Automerge**: Disabled because a matching PR was automerged previously.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR has been generated by [Mend Renovate](https://www.mend.io/free-developer-tools/renovate/).
  View repository job log [here](https://developer.mend.io/github/MartinBernstorff/Memium).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiIzNy4xNzAuMCIsInVwZGF0ZWRJblZlciI6IjM3LjE3MC4wIiwidGFyZ2V0QnJhbmNoIjoibWFpbiJ9-->

- **deps**: Update dependency tests/pytest to v7.4.4
  ([`427d6a8`](https://github.com/MartinBernstorff/Memium/commit/427d6a813bae2ee3c799bc53e4df517c144015b5))


## v0.14.2 (2024-02-06)

### Bug Fixes

- Duplicate prompt detection ([#569](https://github.com/MartinBernstorff/Memium/pull/569),
  [`31b39c6`](https://github.com/MartinBernstorff/Memium/commit/31b39c657839e038fa65331099cd9fc620a6d280))

- Duplicate prompt detection
  ([`5e3e37e`](https://github.com/MartinBernstorff/Memium/commit/5e3e37ef2ebb6b420cd58e455641acf158f1977d))

### Continuous Integration

- Do not disable on concurrency ([#570](https://github.com/MartinBernstorff/Memium/pull/570),
  [`9e1fc1b`](https://github.com/MartinBernstorff/Memium/commit/9e1fc1b59b9446f60fbd350087c54ef97f55fae4))

- Do not disable on concurrency
  ([`05223f7`](https://github.com/MartinBernstorff/Memium/commit/05223f7ada7320dc494a28b1382a8063812bf9d1))


## v0.14.1 (2024-02-06)

### Bug Fixes

- Gracefully fail if block cannot be parsed
  ([#565](https://github.com/MartinBernstorff/Memium/pull/565),
  [`7a49b05`](https://github.com/MartinBernstorff/Memium/commit/7a49b0533e0e3b9cc076112141d9e179803bc369))

- Gracefully fail if block cannot be parsed
  ([`4691aa8`](https://github.com/MartinBernstorff/Memium/commit/4691aa85b88abd2b30b33130f3026f79e42c1a49))

### Chores

- **deps**: Update dependency sentry-sdk to v1.40.1
  ([`caf7852`](https://github.com/MartinBernstorff/Memium/commit/caf78528062e62d6a876605e7017db47db5a43d5))

- **deps**: Update dependency dev/ruff to v0.2.1
  ([`125e96d`](https://github.com/MartinBernstorff/Memium/commit/125e96d16d710401eee7b669f6fd23794c594f9c))

- **deps**: Update dependency dev/pyright to v1.1.350
  ([`7b4c9f7`](https://github.com/MartinBernstorff/Memium/commit/7b4c9f7ea9f1dcbce079f76e0c102c79a972f9c3))

- **deps**: Update dependency pydantic to v2.6.1
  ([`bdf76a5`](https://github.com/MartinBernstorff/Memium/commit/bdf76a51fa1ccb3e643ed9e06d18ece5bf60e2de))


## v0.14.0 (2024-02-05)

### Chores

- **deps**: Update dependency pydantic to v2.6.0
  ([`74776d2`](https://github.com/MartinBernstorff/Memium/commit/74776d26748fa3a902ea628d27bfca0bd7e8267b))

### Features

- **#534**: Allow both rowwise and row-wise when parsing tables
  ([#558](https://github.com/MartinBernstorff/Memium/pull/558),
  [`6a454bd`](https://github.com/MartinBernstorff/Memium/commit/6a454bd60fda1d7b1e7201a5f375fef09922d76d))

Fixes #534

- **#534**: Allow both rowwise and row-wise when parsing tables
  ([`5fdbac7`](https://github.com/MartinBernstorff/Memium/commit/5fdbac7d0868852c0024f5852120fb0dd58ed154))

Fixes #534


## v0.13.1 (2024-02-04)

### Bug Fixes

- Migrate to iterpy ([#555](https://github.com/MartinBernstorff/Memium/pull/555),
  [`752db8e`](https://github.com/MartinBernstorff/Memium/commit/752db8ec27587de1abbd9deb7557f14ff948335c))

fix: migrate to iterpy

update prompt_source.py

- Migrate to iterpy
  ([`bf8fba0`](https://github.com/MartinBernstorff/Memium/commit/bf8fba0882a08323e2f3819c85c72bf4330d3c6d))

### Chores

- **deps**: Update dependency tests/pytest to v8
  ([`cdb09b3`](https://github.com/MartinBernstorff/Memium/commit/cdb09b3b4d667ceaf320a1b074d7a0992cefbde0))

- **deps**: Update dependency dev/ruff to v0.2.0
  ([`9f7c810`](https://github.com/MartinBernstorff/Memium/commit/9f7c810213e4e0892d94a3f5ce25e0c370cb3d00))

- **deps**: Update dependency tests/pytest-sugar to v1
  ([`1a9d95b`](https://github.com/MartinBernstorff/Memium/commit/1a9d95ba72319bdbed17b69a4b9160fb77ca5ecf))

- **deps**: Update dependency sentry-sdk to v1.40.0
  ([`ce58593`](https://github.com/MartinBernstorff/Memium/commit/ce585936d688359bba1e9d1612986e0c8f31427b))

- **deps**: Update dependency dev/pyright to v1.1.349
  ([`0be7671`](https://github.com/MartinBernstorff/Memium/commit/0be76718ac5b2608128a4be04ab3b209c70975de))


## v0.13.0 (2024-01-15)

### Chores

- **deps**: Update dependency dev/pyright to v1.1.347
  ([`23224db`](https://github.com/MartinBernstorff/Memium/commit/23224dbeeaba28b81147c52cf94a678893d83738))

- **deps**: Update dependency dev/pyright to v1.1.346
  ([`f0f6cb5`](https://github.com/MartinBernstorff/Memium/commit/f0f6cb518c5d2e6380620da4b58eab1301defa70))

### Features

- Exclude sparse cells from TableExtractor
  ([#542](https://github.com/MartinBernstorff/Memium/pull/542),
  [`244dabc`](https://github.com/MartinBernstorff/Memium/commit/244dabce4ec3a855e2bbdb3d0d69406f0fdb48d1))

misc.

misc.


## v0.12.1 (2024-01-14)

### Bug Fixes

- Correct table extraction without trailing spaces
  ([#535](https://github.com/MartinBernstorff/Memium/pull/535),
  [`9a1e1ba`](https://github.com/MartinBernstorff/Memium/commit/9a1e1ba7f826d74249e1de6f2dccfcd5176df3a4))

- Correct table extraction without trailing spaces
  ([`8cb789c`](https://github.com/MartinBernstorff/Memium/commit/8cb789c3c756dcc6ea419bfac01995e271708e98))


## v0.12.0 (2024-01-13)

### Chores

- **deps**: Update dependency dev/ruff to v0.1.13
  ([`1a1d6e2`](https://github.com/MartinBernstorff/Memium/commit/1a1d6e260e9a82bae5daf0a7fcddb4ac06d9c688))

- **deps**: Update dependency dev/ruff to v0.1.12
  ([`0ce963f`](https://github.com/MartinBernstorff/Memium/commit/0ce963fd0ee95751ccfe419b8b2385f6750fe092))

- **deps**: Update dependency unidecode to v1.3.8
  ([`59b5add`](https://github.com/MartinBernstorff/Memium/commit/59b5addf89e500f59a5ab8a15ff416cb204a7440))

- **deps**: Update dependency markdown to v3.5.2
  ([`7c2c0c4`](https://github.com/MartinBernstorff/Memium/commit/7c2c0c45f2938701b377144b99127f461d89fe82))

- **deps**: Update dependency sentry-sdk to v1.39.2
  ([`9159fec`](https://github.com/MartinBernstorff/Memium/commit/9159fec58de91091e92dc7c2c58fb4aa6ffd16d0))

- **deps**: Update dependency dev/pyright to v1.1.345
  ([`9ead8ac`](https://github.com/MartinBernstorff/Memium/commit/9ead8ac6f1d0e6c7b3be7819235c42fcb623e467))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.7.2
  ([`66341e5`](https://github.com/MartinBernstorff/Memium/commit/66341e56aa17eb6793edbc331cfc3a5051c386c8))

### Features

- Table parser ([#531](https://github.com/MartinBernstorff/Memium/pull/531),
  [`8c0d109`](https://github.com/MartinBernstorff/Memium/commit/8c0d109fd745c995ca521f172c91395e03dccd3c))

- Add table parser
  ([`dc3fac7`](https://github.com/MartinBernstorff/Memium/commit/dc3fac74bee7c60e2560754c050b028a6a663993))


## v0.11.0 (2024-01-03)

### Documentation

- Recommend naming memium container ([#521](https://github.com/MartinBernstorff/Memium/pull/521),
  [`d71ab7f`](https://github.com/MartinBernstorff/Memium/commit/d71ab7f3969c21e6b408f5febb5c7179e9af621a))

### Features

- Add delays before erroring ([#523](https://github.com/MartinBernstorff/Memium/pull/523),
  [`610aad2`](https://github.com/MartinBernstorff/Memium/commit/610aad2bfeeadb347c6c7691b6b104afdda264e9))

feat: add delays before erroring

Fixes #522

feat: add delays before erroring

Fixes #522

- Add delays before erroring
  ([`9ef8e6c`](https://github.com/MartinBernstorff/Memium/commit/9ef8e6cb3544b6fa4c0723af22802f3efa408155))

Fixes #522

- Add delays before erroring
  ([`869d2a8`](https://github.com/MartinBernstorff/Memium/commit/869d2a86a27c233623cda3801bc3379cbbc2b5e5))

Fixes #522


## v0.10.3 (2024-01-03)

### Bug Fixes

- Improve content-extraction for scheduling uuid detection
  ([#520](https://github.com/MartinBernstorff/Memium/pull/520),
  [`b0ac0ce`](https://github.com/MartinBernstorff/Memium/commit/b0ac0cef0c047324cfa418ced7654f60006df670))

fix: improve content-extraction for scheduling uuid detection

Fixes #519

misc.

- Only remove list markup if at beginning of line
  ([`a112e11`](https://github.com/MartinBernstorff/Memium/commit/a112e1187f5898f8d55d86a279a27c770f3561fe))

- Improve content-extraction for scheduling uuid detection
  ([`4acfd59`](https://github.com/MartinBernstorff/Memium/commit/4acfd598ddf12df573f5151e6e3374209f91bf1c))

Fixes #519


## v0.10.2 (2024-01-03)

### Bug Fixes

- Unicode encoding for uuids ([#518](https://github.com/MartinBernstorff/Memium/pull/518),
  [`2415f6a`](https://github.com/MartinBernstorff/Memium/commit/2415f6a4707625b3d10e29b1a60c7932b8ceee3b))

fix: Å encoding

Fixes #517

fix: Å encoding

Fixes #517

fix: handle unicode encoding for uids

- Handle unicode encoding for uids
  ([`94b4c7f`](https://github.com/MartinBernstorff/Memium/commit/94b4c7fb389692b8267454fa72c4ba8ef92242c7))

- Å encoding
  ([`edba7e0`](https://github.com/MartinBernstorff/Memium/commit/edba7e04687902990b108d8d95d9c5e26d820bae))

Fixes #517


## v0.10.1 (2024-01-03)

### Bug Fixes

- Deduplicate prompts on extraction ([#516](https://github.com/MartinBernstorff/Memium/pull/516),
  [`cb1592b`](https://github.com/MartinBernstorff/Memium/commit/cb1592b4aa307946ad99ef432c368a7db15fb60d))

fix: handle duplicate prompts

Fixes #512

fix: deduplicate prompts on extraction

- Deduplicate prompts on extraction
  ([`8f6cd54`](https://github.com/MartinBernstorff/Memium/commit/8f6cd5495891cdabfb22a6b848e32282370c425b))

- Handle duplicate prompts
  ([`683955a`](https://github.com/MartinBernstorff/Memium/commit/683955aa9261f3cdf19c2d326e5854966cf1af7a))

Fixes #512

### Code Style

- Lint
  ([`9bb033d`](https://github.com/MartinBernstorff/Memium/commit/9bb033d2f686d2f13ad58972d1efc2b6a39a5fd5))

### Refactoring

- Easier hash debugging ([#514](https://github.com/MartinBernstorff/Memium/pull/514),
  [`5b03293`](https://github.com/MartinBernstorff/Memium/commit/5b03293d55d702eda97709750c410ca014477c9d))

refactor: easier hash debugging

Fixes #513

refactor: easier hash debugging

Fixes #513

misc.

- Easier hash debugging
  ([`ff2e8c7`](https://github.com/MartinBernstorff/Memium/commit/ff2e8c782a5abc9ce13afbc5ab3b7bb66abcec08))

Fixes #513

- Easier hash debugging
  ([`1b89c23`](https://github.com/MartinBernstorff/Memium/commit/1b89c2331e39cfde8a6626963a60a34df17b81be))

Fixes #513


## v0.10.0 (2024-01-03)

### Continuous Integration

- No need to manually specify latest tag
  ([`b71247c`](https://github.com/MartinBernstorff/Memium/commit/b71247cb91b10db88ce417cd0bf8ab4dc79d16a7))

- Fix docker tag
  ([`3abf5b4`](https://github.com/MartinBernstorff/Memium/commit/3abf5b47074335216bdddb01b303d8da2b11eac9))

### Features

- Update tag
  ([`84c845b`](https://github.com/MartinBernstorff/Memium/commit/84c845bf7964d329c872b767c7cc47ae098ef9bf))


## v0.9.0 (2024-01-03)

### Continuous Integration

- Push docker image with version tag ([#510](https://github.com/MartinBernstorff/Memium/pull/510),
  [`5b37eda`](https://github.com/MartinBernstorff/Memium/commit/5b37edabed3e0c4f045b9f4fa561fba5a6a1fd0d))

ci: push docker image with version tag

Fixes #509

- Push docker image with version tag
  ([`cab954e`](https://github.com/MartinBernstorff/Memium/commit/cab954e8a90370507eb73eb901991589cf89b7ff))

Fixes #509

- Push docker image with version tag
  ([`e77d102`](https://github.com/MartinBernstorff/Memium/commit/e77d10217bc58e350e82916ff1b9246b70e41430))

Fixes #509

### Features

- Update tag
  ([`ec0c75c`](https://github.com/MartinBernstorff/Memium/commit/ec0c75c9ee9dcad4c8676bc686174b7a84257925))


## v0.8.4 (2024-01-03)

### Bug Fixes

- Ankiconnect uuid handling ([#506](https://github.com/MartinBernstorff/Memium/pull/506),
  [`112a7f1`](https://github.com/MartinBernstorff/Memium/commit/112a7f126c7d2f3b05fdd941d4885e2d9d49fb91))

refactor: What is the AnkiPrompt UUID used for?

Fixes #504

refactor: clarify anki uuid usage

- Tests
  ([`4069335`](https://github.com/MartinBernstorff/Memium/commit/406933579f4d4746ae2d9bdd3603c2cbb87e9142))

### Refactoring

- Clarify anki uuid usage
  ([`146bd44`](https://github.com/MartinBernstorff/Memium/commit/146bd44baa5d026c716498181b8c9e1280105c0c))

- What is the AnkiPrompt UUID used for?
  ([`3d79f93`](https://github.com/MartinBernstorff/Memium/commit/3d79f93eba858f12495fa8212f9da93c017e019a))

Fixes #504


## v0.8.3 (2024-01-03)

### Bug Fixes

- Ankiconnect sync does not appear idempotent
  ([#505](https://github.com/MartinBernstorff/Memium/pull/505),
  [`afe06ba`](https://github.com/MartinBernstorff/Memium/commit/afe06baca3d1cd09a0e3487bd10a68420e7041c9))

fix: AnkiConnect sync does not appear idempotent

Fixes #503

refactor: pure-ish functions for ankiconverter

fix: apply the html cleaner

- Apply the html cleaner
  ([`9aa0aaa`](https://github.com/MartinBernstorff/Memium/commit/9aa0aaaf23f909225a87d33a05d53a1b07f10d6b))

- Ankiconnect sync does not appear idempotent
  ([`1cba106`](https://github.com/MartinBernstorff/Memium/commit/1cba106630f9f5fd2fde046296dc943254cdbc57))

Fixes #503

### Chores

- **deps**: Update dependency dev/ruff to v0.1.11
  ([`6fee03d`](https://github.com/MartinBernstorff/Memium/commit/6fee03d4fe2fc7f00aae79eec26eee5a70dd37e7))

- **deps**: Update dependency dev/ruff to v0.1.10
  ([`d491d3f`](https://github.com/MartinBernstorff/Memium/commit/d491d3f1ac75ec4aed2e7fc2e5c8fd0788fcf1a4))

- **deps**: Update dependency functionalpy to v0.15.0
  ([`937b6db`](https://github.com/MartinBernstorff/Memium/commit/937b6dbcb515237f660abc4879abe210c0d4b7f9))

- **deps**: Update dependency tests/pytest to v7.4.4
  ([`4f716ae`](https://github.com/MartinBernstorff/Memium/commit/4f716aec3dc662913c2a0e72503759e2409f2269))

- **deps**: Update dependency dev/pyright to v1.1.344
  ([`8519b4f`](https://github.com/MartinBernstorff/Memium/commit/8519b4fc8dd823608888c3f77501219b2119c0b1))

### Refactoring

- Pure-ish functions for ankiconverter
  ([`ac82416`](https://github.com/MartinBernstorff/Memium/commit/ac82416fa2d834314d069cd30db53d14b37e174e))


## v0.8.2 (2023-12-27)

### Bug Fixes

- False positives on brackets ([#496](https://github.com/MartinBernstorff/Memium/pull/496),
  [`5606322`](https://github.com/MartinBernstorff/Memium/commit/56063221e2d3e02bf915e460d345d250b93c77f2))

fix: false positives on brackets

Fixes #495

fix: remove entire code blocks

- Remove entire code blocks
  ([`780ec6f`](https://github.com/MartinBernstorff/Memium/commit/780ec6f8f825f93160524211c25ddd4a6870521c))

- False positives on brackets
  ([`b2b656b`](https://github.com/MartinBernstorff/Memium/commit/b2b656be603a1af31c78b3e7a399190116482d0f))

Fixes #495


## v0.8.1 (2023-12-27)

### Bug Fixes

- False positives on cloze for html comments
  ([#494](https://github.com/MartinBernstorff/Memium/pull/494),
  [`df5ff29`](https://github.com/MartinBernstorff/Memium/commit/df5ff2933f33e06c230253741ed267fb5fdf82cf))

Fixes #492

- False positives on cloze for html comments
  ([`2fe2136`](https://github.com/MartinBernstorff/Memium/commit/2fe2136765783749eedea6a4b82ff750b2cff390))

Fixes #492


## v0.8.0 (2023-12-27)

### Continuous Integration

- Fix smoketest permissions ([#482](https://github.com/MartinBernstorff/Memium/pull/482),
  [`056a6e0`](https://github.com/MartinBernstorff/Memium/commit/056a6e058b439e34f92e4bc2e55c1932b7ae7947))

ci: fix smoketest permissions

Fixes #481

ci: fix smoketest permissions

Fixes #481

- Smoketests don't need ghcr
  ([`927668c`](https://github.com/MartinBernstorff/Memium/commit/927668cc2dbfc8fd15be82e8d387f9a7113a013b))

- Fix smoketest permissions
  ([`a36bbd3`](https://github.com/MartinBernstorff/Memium/commit/a36bbd3b05addc03c9a6ae6a0baf866fade89cfe))

Fixes #481

- Fix smoketest permissions
  ([`9c6fc8e`](https://github.com/MartinBernstorff/Memium/commit/9c6fc8e6c03243242157665ea11307e2a744e4ec))

Fixes #481

### Features

- Handle wikilinks and aliases ([#487](https://github.com/MartinBernstorff/Memium/pull/487),
  [`1c5dff5`](https://github.com/MartinBernstorff/Memium/commit/1c5dff5065dc784539c5af0359e1aa167fa9b5b5))

feat: handle wikilinks

Fixes #485 and fixes #486.

- Handle wikilinks
  ([`18023f6`](https://github.com/MartinBernstorff/Memium/commit/18023f631ac3acba9745961d6aca1c5a6bf393bf))

Fixes #485

- Handle wikilinks
  ([`19355d8`](https://github.com/MartinBernstorff/Memium/commit/19355d89805d2fd50c3e13ec63e02a61c6610fec))

Fixes #485


## v0.7.1 (2023-12-27)

### Bug Fixes

- Cli entrypoint
  ([`c7edcb3`](https://github.com/MartinBernstorff/Memium/commit/c7edcb3c61ce29abcf24b98aca459e1050b1c25b))

- Type errors
  ([`725f3d3`](https://github.com/MartinBernstorff/Memium/commit/725f3d380f8767cc307a28e12355bff0987eb803))

### Refactoring

- Misc. ([#480](https://github.com/MartinBernstorff/Memium/pull/480),
  [`907ab9f`](https://github.com/MartinBernstorff/Memium/commit/907ab9f544c40e249ad5ce6ffe412a26aabceacc))


## v0.7.0 (2023-12-27)

### Bug Fixes

- Release to pypi ([#475](https://github.com/MartinBernstorff/Memium/pull/475),
  [`199ed12`](https://github.com/MartinBernstorff/Memium/commit/199ed125cc5cddff16a72665bfc36df871979152))

- Append \ to docker command
  ([`2778bbb`](https://github.com/MartinBernstorff/Memium/commit/2778bbbb2465a9f142e82857bca7087b6b3af3e3))

- Readme casing
  ([`35828d5`](https://github.com/MartinBernstorff/Memium/commit/35828d56a6bfae18f84cd1ae7fe8034643d8ed3a))

- Release flow ([#467](https://github.com/MartinBernstorff/Memium/pull/467),
  [`56f6422`](https://github.com/MartinBernstorff/Memium/commit/56f64223a10da8c0cf094b7d9a52de14798a0cb1))

fix: release flow

Fixes #465

major: release to pypi

- Release flow
  ([`e6def83`](https://github.com/MartinBernstorff/Memium/commit/e6def83a9d0d5b351895a4846b1ec937d5bc1de8))

Fixes #465

- Release flow
  ([`0db976e`](https://github.com/MartinBernstorff/Memium/commit/0db976e0183b36576a4457a81d23d0e3e65dfda4))

Fixes #465

- Smokestest
  ([`da1e4ad`](https://github.com/MartinBernstorff/Memium/commit/da1e4ad4ecd9393153709ed71e600a7427319fcd))

- Smokestest
  ([`b472748`](https://github.com/MartinBernstorff/Memium/commit/b4727483335fb44411790f80fb7bbf94b14d2bd8))

- Smokestest
  ([`fa7c5bb`](https://github.com/MartinBernstorff/Memium/commit/fa7c5bb53bd7cb6775349c07fa1fee61522e8964))

- Create a subdir, so it can never delete an existing dir
  ([`0978523`](https://github.com/MartinBernstorff/Memium/commit/0978523972239e54064be61c0c6e15fea9690bfa))

- Do not delete entire dir
  ([`9dc5bef`](https://github.com/MartinBernstorff/Memium/commit/9dc5beffc0a3501e5f6006da925ed0a577a1f278))

- Imports
  ([`3244f6e`](https://github.com/MartinBernstorff/Memium/commit/3244f6ee4a7c303b97672e2dc086a62223f5ef0f))

- Anki subdecks are not used ([#404](https://github.com/MartinBernstorff/Memium/pull/404),
  [`7ca3781`](https://github.com/MartinBernstorff/Memium/commit/7ca3781c10bdee78b4773cb610fcf3763f1a3b99))

fix: anki subdecks are not used

Fixes #396

tests: ensure ankiconnect gets correct subdecks

fix: extract all tags from markdown documents

fix: tag strings should not contain "#"

fix: import all decks

feat: support arbitrary subdeck nesting

- Import all decks
  ([`dda73bd`](https://github.com/MartinBernstorff/Memium/commit/dda73bd8e9b670a274e43b3d86ccefd75e71089b))

- Tag strings should not contain "#"
  ([`5a220ff`](https://github.com/MartinBernstorff/Memium/commit/5a220ff2543ed582c30f90418f67915b005ac4a7))

- Extract all tags from markdown documents
  ([`9ab65fa`](https://github.com/MartinBernstorff/Memium/commit/9ab65fa34217c6c99cbdcc9844f9c359c0a5d9f8))

- Anki subdecks are not used
  ([`4762a48`](https://github.com/MartinBernstorff/Memium/commit/4762a481695947508937e11cb7470779889acfb2))

- Anki subdecks are not used ([#400](https://github.com/MartinBernstorff/Memium/pull/400),
  [`0aa8473`](https://github.com/MartinBernstorff/Memium/commit/0aa84734c4f855ff17c03cbbe1afce4c27b2047b))

fix: anki subdecks are not used

fix: use anki subdecks

- Use anki subdecks
  ([`7fc378e`](https://github.com/MartinBernstorff/Memium/commit/7fc378eebd3539831b3c058a1549f0ae4f618eb9))

- Anki subdecks are not used
  ([`3c71336`](https://github.com/MartinBernstorff/Memium/commit/3c713366f3400d84766ef8589ba488d4e178ec5a))

- Use answer when generating hash for QA
  ([#399](https://github.com/MartinBernstorff/Memium/pull/399),
  [`3345bff`](https://github.com/MartinBernstorff/Memium/commit/3345bff7b27135ad903d7886108ba6a941e7fc78))

- Use answer when generating hash for QA
  ([`2919d77`](https://github.com/MartinBernstorff/Memium/commit/2919d7766005a00bc264ca654ef3bc6d13e6d48a))

- Anki tags are not added ([#398](https://github.com/MartinBernstorff/Memium/pull/398),
  [`5e05ab5`](https://github.com/MartinBernstorff/Memium/commit/5e05ab5ac31cad478d4674655e3dbb941649aac6))

fix: anki tags are not added

feat: implement

misc.

- Anki tags are not added
  ([`27432d1`](https://github.com/MartinBernstorff/Memium/commit/27432d194e52732a57237ba913e9a140b84d471a))

- Use localhost for ANKICONNECT_URL if not on docker
  ([`045eaa4`](https://github.com/MartinBernstorff/Memium/commit/045eaa414d4b8ef634a0f0cf331251bee41bcbff))

- Only update unique models
  ([`cfbae0e`](https://github.com/MartinBernstorff/Memium/commit/cfbae0e6364a6ef28af20f6a30c4df35591c0785))

- Submit entire stack
  ([`1b37e1b`](https://github.com/MartinBernstorff/Memium/commit/1b37e1bb6d7cb5c55b9c7c816798bc6370d0779e))

- Use invoke on devcontainer.json
  ([`3adb865`](https://github.com/MartinBernstorff/Memium/commit/3adb86501b98ab291abfa4c8d1fe3d106f5ded95))

- Qa uuid should include answer
  ([`9cc2991`](https://github.com/MartinBernstorff/Memium/commit/9cc29910f572b9663993483a384b7e0193e00a11))

Fixes #346

- Use remote id for sync ([#334](https://github.com/MartinBernstorff/Memium/pull/334),
  [`b3e98f5`](https://github.com/MartinBernstorff/Memium/commit/b3e98f5026313cf4290fcb78aae14d46db70d5b6))

- Use correct id for remote sync
  ([`526480b`](https://github.com/MartinBernstorff/Memium/commit/526480becd316737871ca871dcb8b2349f2eaef0))

- Promptid to NoteID mapping
  ([`2f981b1`](https://github.com/MartinBernstorff/Memium/commit/2f981b1313689201e7ed539ea1a1a3f5618f6514))

Fixes #284

- Inherit from protocol ([#287](https://github.com/MartinBernstorff/Memium/pull/287),
  [`6e2862f`](https://github.com/MartinBernstorff/Memium/commit/6e2862f8b1b1ab7ccc528c503479f01f2f8028f3))

### Chores

- Cleanup ([#476](https://github.com/MartinBernstorff/Memium/pull/476),
  [`c064b68`](https://github.com/MartinBernstorff/Memium/commit/c064b68c5a929ad3400665b67fe0e3dfcd840f45))

- **deps**: Update actions/setup-python action to v5
  ([`45a6637`](https://github.com/MartinBernstorff/Memium/commit/45a663750576c6885403a11cb7038f6bfa9a677e))

- **deps**: Update dependency dev/pyright to v1.1.343
  ([`a2dbeb6`](https://github.com/MartinBernstorff/Memium/commit/a2dbeb6137026e5e836040921321837570c262dd))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.7.0
  ([`3d4b538`](https://github.com/MartinBernstorff/Memium/commit/3d4b538212c079097878b5ab16e1623d3b6c6fae))

- **deps**: Update dependency pydantic to v2.5.3
  ([`11a85a9`](https://github.com/MartinBernstorff/Memium/commit/11a85a9b6bfbecf1bb5c2753dfcc4dfafaf5a54f))

- **deps**: Update dependency dev/ruff to v0.1.9
  ([`b69d658`](https://github.com/MartinBernstorff/Memium/commit/b69d6584163869ab9c63393d658d76863faf9180))

- **deps**: Update dependency dev/pyright to v1.1.342
  ([`cf5a8b1`](https://github.com/MartinBernstorff/Memium/commit/cf5a8b16e8a87727730cff04dc2678c6fcac4b73))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.5.2
  ([`6e6496b`](https://github.com/MartinBernstorff/Memium/commit/6e6496bc5cc14b83a54c2272352b8fa456a0306f))

- **deps**: Update dependency dev/pre-commit to v3
  ([`f506653`](https://github.com/MartinBernstorff/Memium/commit/f5066538bb066327be10e384718676836a5c6bb8))

- **deps**: Update docker/login-action action to v3
  ([`8e76a16`](https://github.com/MartinBernstorff/Memium/commit/8e76a16e3aee608294ac25269edf1850c409ed7b))

- **deps**: Update actions/stale action to v9
  ([`e5967b0`](https://github.com/MartinBernstorff/Memium/commit/e5967b06f4b7314e4ece77327bd3214af1f7b69b))

- **deps**: Update actions/checkout action to v4
  ([`b15c5d6`](https://github.com/MartinBernstorff/Memium/commit/b15c5d6c70d802504db4111dd519c587030acb82))

- **deps**: Update python docker tag to v3.12
  ([`e50a018`](https://github.com/MartinBernstorff/Memium/commit/e50a018da3525a0a812a6c5242e1813d4f66ee7d))

- **deps**: Update python-semantic-release/python-semantic-release action to v8.5.1
  ([`ff53391`](https://github.com/MartinBernstorff/Memium/commit/ff53391d9bfabc36a76fb9b46189730a5fc81ff9))

- **deps**: Update dependency tests/pytest-xdist to v3.5.0
  ([`2d97f73`](https://github.com/MartinBernstorff/Memium/commit/2d97f73a23dd91791d1efa58655ba89e7b0a0c7a))

- **deps**: Update dependency tests/pytest to v7.4.3
  ([`acf432a`](https://github.com/MartinBernstorff/Memium/commit/acf432a8ade8c61c6a1e3612d85e1f974135b606))

- **deps**: Update dependency sentry-sdk to v1.39.1
  ([`ff95683`](https://github.com/MartinBernstorff/Memium/commit/ff95683807d6e200b8a0dd11aa44b58b6b2c9760))

- **deps**: Update dependency dev/pre-commit to v2.21.0
  ([`02eb2cc`](https://github.com/MartinBernstorff/Memium/commit/02eb2cca0fef89e9fda62a16386f1e1a8fe78de9))

- **deps**: Update dependency tests/diff-cover to v8.0.2
  ([`a4512f8`](https://github.com/MartinBernstorff/Memium/commit/a4512f827d75570fac95ecfb11e2007dba45c59a))

- **deps**: Update dependency genanki to v0.13.1
  ([`abf835a`](https://github.com/MartinBernstorff/Memium/commit/abf835a61a0b2de54615c69528a73c774a3fd16b))

- **deps**: Update dependency dev/pyright to v1.1.341
  ([`8466592`](https://github.com/MartinBernstorff/Memium/commit/84665922ab7c8341c4239cec8e7f0b413f4c052a))

- **deps**: Update dependency dev/ruff to v0.1.8
  ([`e670f8e`](https://github.com/MartinBernstorff/Memium/commit/e670f8e07459afe2e02ad5a8d609557c7e5f78ba))

- Configure Renovate ([#368](https://github.com/MartinBernstorff/Memium/pull/368),
  [`d9fa9c0`](https://github.com/MartinBernstorff/Memium/commit/d9fa9c0f05fe9e17d1e0d7efe133f3ba925bf9ef))

Fixes #260.

### Code Style

- Linting
  ([`554fedc`](https://github.com/MartinBernstorff/Memium/commit/554fedc7e2c73761fcfaabc855bd67a604d60d01))

- Lint
  ([`e5f11a9`](https://github.com/MartinBernstorff/Memium/commit/e5f11a9d3706f378d1d8f95da0bb63797f08ddba))

### Continuous Integration

- Add manual trigger to release
  ([`32470a5`](https://github.com/MartinBernstorff/Memium/commit/32470a5f24ce24bfe6f37ead8b9aff7ae0141874))

- Typo in release.yml
  ([`72c7a08`](https://github.com/MartinBernstorff/Memium/commit/72c7a0896aea44d431dd4dfc8eb21364d885109c))

- Release override permissions ([#479](https://github.com/MartinBernstorff/Memium/pull/479),
  [`975630d`](https://github.com/MartinBernstorff/Memium/commit/975630d2bd7efd5b53d4397a70ebd8bd3c93475f))

- Update release token
  ([`b4f1f2e`](https://github.com/MartinBernstorff/Memium/commit/b4f1f2e6b8bc0ca76dedefeff587b981ffc3877b))

- Remove github release ([#477](https://github.com/MartinBernstorff/Memium/pull/477),
  [`941f587`](https://github.com/MartinBernstorff/Memium/commit/941f587455531f1e4f2d3eeb3cfcc9e946d582f8))

- Release to memium on pypi
  ([`b8fdb6b`](https://github.com/MartinBernstorff/Memium/commit/b8fdb6ba563aa2ba009fa41ad44f2c56bb4efb6b))

Fixes #455

- Update ref groups. ([#447](https://github.com/MartinBernstorff/Memium/pull/447),
  [`1387d00`](https://github.com/MartinBernstorff/Memium/commit/1387d00a319f04961a448e19d91acd09b9245453))

ci: update ref groups.

Fixes #446

implement

- Update ref groups.
  ([`a18ccaa`](https://github.com/MartinBernstorff/Memium/commit/a18ccaa5b8f76654aa8db9fd7a8ce02b6a4d2744))

Fixes #446

- Update
  ([`75b3f22`](https://github.com/MartinBernstorff/Memium/commit/75b3f22e5e4fa38c2fb86f80c8a34829b4d31116))

- Remove dependabot
  ([`e2e0721`](https://github.com/MartinBernstorff/Memium/commit/e2e07211b5c1a497aa3ac2253dc7dcf06ae22705))

- Add automerge
  ([`5f15b7d`](https://github.com/MartinBernstorff/Memium/commit/5f15b7d02404071218deb8917ea9017f8b037a80))

- Use invoke
  ([`ca61482`](https://github.com/MartinBernstorff/Memium/commit/ca614829284d0d9db7b410beb23191726025cd0b))

- Update
  ([`126f81a`](https://github.com/MartinBernstorff/Memium/commit/126f81a2f3b413e923413ccaa4717af5acaa3352))

- Correct path to docker smoketest
  ([`ee50f34`](https://github.com/MartinBernstorff/Memium/commit/ee50f34ccd2977c7af4a36a86c3a1eca629fa2e7))

Fixes #343

- Clean up
  ([`8ad85f1`](https://github.com/MartinBernstorff/Memium/commit/8ad85f101a4b7b04019bfb4ded226867d82e6e07))

- Remove codecov ([#283](https://github.com/MartinBernstorff/Memium/pull/283),
  [`b65cb11`](https://github.com/MartinBernstorff/Memium/commit/b65cb11e6681ef895548ee1727aa00754c5a3685))

- Remove codecov
  ([`8d7f9d7`](https://github.com/MartinBernstorff/Memium/commit/8d7f9d7a10ff88836fe05ccd9ae10ea5290727ba))

- Add codecov ([#199](https://github.com/MartinBernstorff/Memium/pull/199),
  [`4d546d4`](https://github.com/MartinBernstorff/Memium/commit/4d546d473228c7977b3843c028fb72092e1ce48e))

### Documentation

- Use ghcr in readme for docker image ([#471](https://github.com/MartinBernstorff/Memium/pull/471),
  [`52cbec6`](https://github.com/MartinBernstorff/Memium/commit/52cbec631a5760fb1f19dff6cd7bc78b54a648b2))

docs: use ghcr in readme for docker image

Fixes #470

misc.

- Use ghcr in readme for docker image
  ([`04229f1`](https://github.com/MartinBernstorff/Memium/commit/04229f16d4363f63e0e28cbd5c0355f9cc9cbd93))

Fixes #470

- Use ghcr in readme for docker image
  ([`0b3f810`](https://github.com/MartinBernstorff/Memium/commit/0b3f810d815c7f22a23fc1d2b3df1e78f2b9b578))

Fixes #470

- Update readme ([#466](https://github.com/MartinBernstorff/Memium/pull/466),
  [`01aa23d`](https://github.com/MartinBernstorff/Memium/commit/01aa23d51813436bf23b849c779484b29813a9e0))

docs: update readme

Fixes #462

misc.

- Update readme
  ([`adb5527`](https://github.com/MartinBernstorff/Memium/commit/adb552751f0198092f9ff1df41b2c7bc2b423069))

Fixes #462

### Features

- Raise error if input dir is not writeable
  ([#474](https://github.com/MartinBernstorff/Memium/pull/474),
  [`4f0ea80`](https://github.com/MartinBernstorff/Memium/commit/4f0ea807b017ce99d018dbcf9404411cdbbe672d))

feat: raise error if input dir is not writeable

Fixes #473

feat: raise error if input dir is not writeable

Fixes #473

- Raise error if input dir is not writeable
  ([`883f16e`](https://github.com/MartinBernstorff/Memium/commit/883f16eae653bd58d33445a3ba92b7636b6f9ed6))

Fixes #473

- Raise error if input dir is not writeable
  ([`f837faa`](https://github.com/MartinBernstorff/Memium/commit/f837faa25f6e2299b964c1211ef97683f23554cf))

Fixes #473

- Rename to memium ([#448](https://github.com/MartinBernstorff/Memium/pull/448),
  [`41fbe4a`](https://github.com/MartinBernstorff/Memium/commit/41fbe4aefc57bd677543c985f44994ac644371bc))

feat: rename to memium.

Fixes #419

implement

- Rename to memium.
  ([`fb02dc2`](https://github.com/MartinBernstorff/Memium/commit/fb02dc27c435369766b2db19c256b5f1bdfc5c53))

Fixes #419

- Make `pipx` installable. ([#441](https://github.com/MartinBernstorff/Memium/pull/441),
  [`61c397d`](https://github.com/MartinBernstorff/Memium/commit/61c397dcacfd567bd005f1e9d76fb3e786e6ab50))

Fixes #413

- Make `pipx` installable.
  ([`540588a`](https://github.com/MartinBernstorff/Memium/commit/540588a38ca7e7b735ca63b865fc1ad281b79bff))

Fixes #413

- Add `push_all` option to CLI ([#439](https://github.com/MartinBernstorff/Memium/pull/439),
  [`bfd76ba`](https://github.com/MartinBernstorff/Memium/commit/bfd76ba4bbb4ad8047c502be750dfdbc076b222d))

feat: update_all option.

Fixes #409

feat: update_all option.

Fixes #409

- Update_all option.
  ([`d6a184f`](https://github.com/MartinBernstorff/Memium/commit/d6a184f73c64e893fe84f5dbd11d5eb9d3d53e25))

Fixes #409

- Add sentry_dsn flag which enables/disables sentry.
  ([#437](https://github.com/MartinBernstorff/Memium/pull/437),
  [`7e001cf`](https://github.com/MartinBernstorff/Memium/commit/7e001cfc10b6a9d3a4a04ccf7f436d3204dbe91e))

feat: add sentry_dsn flag which enables/disables sentry.

Fixes #421

feat: add sentry_dsn flag which enables/disables sentry.

Fixes #421

- Add sentry_dsn flag which enables/disables sentry.
  ([`9c45c7b`](https://github.com/MartinBernstorff/Memium/commit/9c45c7b9192eff0fbb0ee9d8eb3491f20d04056e))

Fixes #421

- Add sentry_dsn flag which enables/disables sentry.
  ([`6db2467`](https://github.com/MartinBernstorff/Memium/commit/6db2467ce812ea6edae63ea0ab158c07e7ee293b))

Fixes #421

- Remove temp dir from cli interface. Fixes #374
  ([#428](https://github.com/MartinBernstorff/Memium/pull/428),
  [`cb6c95c`](https://github.com/MartinBernstorff/Memium/commit/cb6c95cc7f3a13d32da107f1d26b9fe599d79421))

feat: remove temp dir from cli interface. Fixes #374

misc.

misc.

- Remove temp dir from cli interface. Fixes #374
  ([`a07738a`](https://github.com/MartinBernstorff/Memium/commit/a07738acb86da80c94b5eba9bf8b73f4ba0b71e5))

- Use context manager to temp deck file deletion. Fixes #423
  ([#427](https://github.com/MartinBernstorff/Memium/pull/427),
  [`be4999d`](https://github.com/MartinBernstorff/Memium/commit/be4999dca85607781872b67b5014e8297d7c1550))

feat: use context manager to temp deck file deletion. Fixes #423

implement

- Use context manager to temp deck file deletion. Fixes #423
  ([`d1c7e3d`](https://github.com/MartinBernstorff/Memium/commit/d1c7e3d83bc6d4fd053114022578d3e869ea906a))

- Add optional arguments to cli ([#422](https://github.com/MartinBernstorff/Memium/pull/422),
  [`bec9363`](https://github.com/MartinBernstorff/Memium/commit/bec93639b68be0687fc027bb78ff0f813aab16fc))

feat: add optional arguments to cli

misc.

- Add optional arguments to cli
  ([`e20142a`](https://github.com/MartinBernstorff/Memium/commit/e20142a8bb38283fc073a08197ae7d1156f4a7ef))

- Fail with user friendly error if ankiconnect is not live
  ([`e489e2f`](https://github.com/MartinBernstorff/Memium/commit/e489e2ff2dd5d09c0b87692ef963dbe59997290b))

- Change document ingestion to best-effort
  ([#416](https://github.com/MartinBernstorff/Memium/pull/416),
  [`bbe1196`](https://github.com/MartinBernstorff/Memium/commit/bbe1196d1f0197d967e377f86cf17d367bf61fc1))

feat: change document ingestion to best-effort

feat: implement

- Implement
  ([`bb00c4c`](https://github.com/MartinBernstorff/Memium/commit/bb00c4c0ad55e58d06d1709fbf181c6e92d47cc4))

- Change document ingestion to best-effort
  ([`5b4401c`](https://github.com/MartinBernstorff/Memium/commit/5b4401c67251be967a81092c4f64cb09b4d48bf6))

- Update remote if tags have changed ([#410](https://github.com/MartinBernstorff/Memium/pull/410),
  [`908ed5e`](https://github.com/MartinBernstorff/Memium/commit/908ed5e4885bb2d4d111a2b550c1f1780012a327))

feat: update remote if tags have changed

misc.

tests: make tests more readable

- Update remote if tags have changed
  ([`e9b06f7`](https://github.com/MartinBernstorff/Memium/commit/e9b06f707b9cce3308471891709d15abaf9ccd87))

- Support arbitrary subdeck nesting
  ([`3ba0c90`](https://github.com/MartinBernstorff/Memium/commit/3ba0c9092fa06a61fbacbb50b7d6fccad438f499))

- Implement
  ([`10eecf4`](https://github.com/MartinBernstorff/Memium/commit/10eecf49e1d832ac8cea012250953328040cdbd3))

- First run on v2 ([#397](https://github.com/MartinBernstorff/Memium/pull/397),
  [`49d0501`](https://github.com/MartinBernstorff/Memium/commit/49d0501d2fca55c773c5ffb374d5a4aee982f5c5))

fix: only update unique models Fixes #315

dev: add run cli launch option

fix: use localhost for ANKICONNECT_URL if not on docker

misc: formatting

- Set max_wait_seconds for ankiconnect destination
  ([`da53a73`](https://github.com/MartinBernstorff/Memium/commit/da53a7313577d971055cef731f7d8c238e7a54de))

- Implement sleep for ankiconnectdestination
  ([`2204f4d`](https://github.com/MartinBernstorff/Memium/commit/2204f4dcd21608adb485b627a21d297a693bc0ce))

- Use v2 when running docker smoketest
  ([`510eb33`](https://github.com/MartinBernstorff/Memium/commit/510eb330886fcb0d4fa191e345f4206b06ef844b))

Fixes #331

- Add dry-run
  ([`ccde648`](https://github.com/MartinBernstorff/Memium/commit/ccde648621495d3b42f082559a62a31413fd3126))

Fixes #336

- Polish cli
  ([`bd11c10`](https://github.com/MartinBernstorff/Memium/commit/bd11c108c9114042958de7b313802891c127c9f7))

Fixes #338

- Use markdown promptsource
  ([`464d8fa`](https://github.com/MartinBernstorff/Memium/commit/464d8facd83191666f051bd372173447f3d44257))

Fixes #309

- Add remoteid and use for prompt deletion
  ([`3c47d7e`](https://github.com/MartinBernstorff/Memium/commit/3c47d7ee4cdff588a4f654d15c62bb2580ea74b2))

Fixes #321

- If n+ notes are scheduled for deletion, do not sync
  ([`0915e7f`](https://github.com/MartinBernstorff/Memium/commit/0915e7fa56f2de747f1f0ded1667203058ad2d6b))

Fixes #251

- Add diffdeterminer
  ([`9d708f2`](https://github.com/MartinBernstorff/Memium/commit/9d708f2928af270c53e06f3ca285c8ff588f899e))

- Implement diffdeterminer
  ([`174add1`](https://github.com/MartinBernstorff/Memium/commit/174add194efb4d57de0e0627a9bfc24e15a318fb))

Fixes #292 Add GeneralSyncer

- Implement ClozeExtractor
  ([`a9afe36`](https://github.com/MartinBernstorff/Memium/commit/a9afe36c9b6530dc8fd97f9d5577c5dee93c2c1c))

Fixes #297

- Implement QA extractor
  ([`aa7079c`](https://github.com/MartinBernstorff/Memium/commit/aa7079c815e892f3ba3c1b5adcd628b9b4dd07f0))

Fixes #294

- Add markdown ingester
  ([`728de65`](https://github.com/MartinBernstorff/Memium/commit/728de65c47bd722bfdeb247dd54f8520d652e1d2))

- Stub out promptsource
  ([`0e2e2f2`](https://github.com/MartinBernstorff/Memium/commit/0e2e2f235c1dad0a3c2112dfe754fe61bf209689))

Fixes #293

- Stub out `main` for cli in v2 ([#291](https://github.com/MartinBernstorff/Memium/pull/291),
  [`f2b4cf0`](https://github.com/MartinBernstorff/Memium/commit/f2b4cf05cc0595fa1837cc8e57d60671ae001fb4))

- Stub out main cli v2
  ([`24954c7`](https://github.com/MartinBernstorff/Memium/commit/24954c72dc1d7a720b2c6080da40aefa85145bd8))

- Stub out main cli v2
  ([`79f2d09`](https://github.com/MartinBernstorff/Memium/commit/79f2d098bce415ad0367618790f756aaf5052340))

- Finalise push on `AnkiConnectPromptDestination`
  ([#289](https://github.com/MartinBernstorff/Memium/pull/289),
  [`8edeee7`](https://github.com/MartinBernstorff/Memium/commit/8edeee7e1e400496c83224ac916f1b012f025e60))

- Anki `prompts_to_cards` ([#288](https://github.com/MartinBernstorff/Memium/pull/288),
  [`d9fd7aa`](https://github.com/MartinBernstorff/Memium/commit/d9fd7aa0549afeaade55cb3c873cfc5d2755f138))

- Ankiconnect destination `get_all_prompts`
  ([#286](https://github.com/MartinBernstorff/Memium/pull/286),
  [`3184006`](https://github.com/MartinBernstorff/Memium/commit/31840062f2f4612beca2db83109fcdad852f2972))

- Ankiconnect support delete notes ([#285](https://github.com/MartinBernstorff/Memium/pull/285),
  [`99b507a`](https://github.com/MartinBernstorff/Memium/commit/99b507a646ec4d6447aa236312b4c6ed8a6d77ec))

- Add ankiconnect destination get all
  ([`60f52d8`](https://github.com/MartinBernstorff/Memium/commit/60f52d8a3b2320bdce0ecfd28bb21e64ba8cda09))

- Stub out ankiconnect destination ([#282](https://github.com/MartinBernstorff/Memium/pull/282),
  [`7de7bec`](https://github.com/MartinBernstorff/Memium/commit/7de7beccec96a655c271b456e2340006bbd064ff))

### Refactoring

- Remove top level git
  ([`eff9e9e`](https://github.com/MartinBernstorff/Memium/commit/eff9e9e7f751e0aa8347bbaa2fdecd525a826f07))

- Remove top level git ([#472](https://github.com/MartinBernstorff/Memium/pull/472),
  [`3000b65`](https://github.com/MartinBernstorff/Memium/commit/3000b65fbed633f68ec77779acb92f8c02e64923))

- Remove top level git
  ([`a2913b7`](https://github.com/MartinBernstorff/Memium/commit/a2913b73e35af64d18a365dd0456b7bf62fa92de))

- Decrease file nesting ([#414](https://github.com/MartinBernstorff/Memium/pull/414),
  [`0acd631`](https://github.com/MartinBernstorff/Memium/commit/0acd631b47e69c31ff9f7fda92c62082a60412dd))

refactor: decrease file nesting

Fixes #350

phase 1

fix: imports

style: linting

misc.

- Decrease file nesting
  ([`15938e1`](https://github.com/MartinBernstorff/Memium/commit/15938e114034a7f7dd4e6a29e28f0d86664c1c0a))

- Misc
  ([`56fc926`](https://github.com/MartinBernstorff/Memium/commit/56fc9260921aaa1f5c1627f90353414bfd62e30a))

- Split tasks into multiple files
  ([`c533a9e`](https://github.com/MartinBernstorff/Memium/commit/c533a9e4911a4646b608b3ac4d4df501483d873d))

- Remove makefile
  ([`6c97f96`](https://github.com/MartinBernstorff/Memium/commit/6c97f96e5985957f7d03bd45124541aedeeebaa8))

- Remove v1 ([#344](https://github.com/MartinBernstorff/Memium/pull/344),
  [`f1be2d3`](https://github.com/MartinBernstorff/Memium/commit/f1be2d3d814832c581ed1b3358759ef30f408932))

- Move max wait duration to gateway
  ([`b237169`](https://github.com/MartinBernstorff/Memium/commit/b237169fc65eb76ef6350e6f81f22660c6eb52c4))

- Move cli to top-level
  ([`e14a694`](https://github.com/MartinBernstorff/Memium/commit/e14a694e23f9d3f0b8c94e3300f41154b78c9ef3))

- Move v2 to top level
  ([`8afcb5a`](https://github.com/MartinBernstorff/Memium/commit/8afcb5adfc62017c1f6bfc7ad6287b5eceae22ba))

- Remove v1
  ([`3df182b`](https://github.com/MartinBernstorff/Memium/commit/3df182bfee0e03987e4eaf2b07a69fea70d9d416))

Fixes #338

- Remove tmp_dirs from pushprompts and promptdiffdeterminer
  ([`8e80469`](https://github.com/MartinBernstorff/Memium/commit/8e804696b5ddd7832a27c9ebc19caa1b1c313b92))

- Remove tmp_dirs from PushPrompts and `PromptDiffDeterminer`
  ([`9fc4e3e`](https://github.com/MartinBernstorff/Memium/commit/9fc4e3efa9e89c26461795b535309ecfad85f3ac))

Fixes #323

- Renames
  ([`003b523`](https://github.com/MartinBernstorff/Memium/commit/003b5236ef126cb3732cfdf72908a54d24f06547))

- Get rid of tmp_read_dir and tmp_write_dir
  ([`93116a4`](https://github.com/MartinBernstorff/Memium/commit/93116a4b5cb6384b6e31601ee1c2258f02195575))

Fixes #308

- Simplify prompts ([#312](https://github.com/MartinBernstorff/Memium/pull/312),
  [`be6a5db`](https://github.com/MartinBernstorff/Memium/commit/be6a5dbeb787fd9c94ad8c87ec52352a25cdc7d2))

- Simplify prompts
  ([`1b4c802`](https://github.com/MartinBernstorff/Memium/commit/1b4c802d8eeaf094ad735ed9a9e663225303c1a9))

- `int_hash_str` location ([#303](https://github.com/MartinBernstorff/Memium/pull/303),
  [`02eea89`](https://github.com/MartinBernstorff/Memium/commit/02eea8903fba90803a7a7cf321357c8b68c56193))

- Minor cleanup ([#290](https://github.com/MartinBernstorff/Memium/pull/290),
  [`2564780`](https://github.com/MartinBernstorff/Memium/commit/2564780d30f2e2ae6dafe1417730948a15c05195))

- Abstract outline
  ([`6fb9675`](https://github.com/MartinBernstorff/Memium/commit/6fb9675533fee3882f2af15694c7cf678636c1f6))

- Sync decks into functional core imperative shell
  ([#270](https://github.com/MartinBernstorff/Memium/pull/270),
  [`80f956d`](https://github.com/MartinBernstorff/Memium/commit/80f956d3f45e5521219190f4a896c0938dddb03c))

- Sync decks into functional core, imperative shell
  ([`32a0e3a`](https://github.com/MartinBernstorff/Memium/commit/32a0e3a54e03c80d1aae9587a6d1f643b8fab52d))

Fixes #240

- Sync decks into functional core, imperative shell
  ([`9e709ff`](https://github.com/MartinBernstorff/Memium/commit/9e709ff93bface18fa2874c440c3dd9614c55ce6))

Fixes #240

- Sync decks into functional core, imperative shell
  ([`562d46f`](https://github.com/MartinBernstorff/Memium/commit/562d46f93d96c3cd0f88ca1d3d17d030317338a0))

Fixes #240

- Simplify tests and remove defaults from extractors
  ([`e259578`](https://github.com/MartinBernstorff/Memium/commit/e2595786ab7b752b1480b5b79307b36eea118817))

Fixes #245

- Minor cleanup of markdown ingester ([#246](https://github.com/MartinBernstorff/Memium/pull/246),
  [`c542d8e`](https://github.com/MartinBernstorff/Memium/commit/c542d8e3afeb78fd83e012856ca1236f85a3b092))

- Move things out of globals ([#224](https://github.com/MartinBernstorff/Memium/pull/224),
  [`05a83b6`](https://github.com/MartinBernstorff/Memium/commit/05a83b6cf07f00e35751c8a796e60af067845984))

Auto-created

- Decrease makefile verbosity ([#212](https://github.com/MartinBernstorff/Memium/pull/212),
  [`464453b`](https://github.com/MartinBernstorff/Memium/commit/464453b72b8f2a414fd2c75f928dd301b77fd8e5))

Auto-created

- Fix import errors after folder restructure
  ([#202](https://github.com/MartinBernstorff/Memium/pull/202),
  [`5680ad9`](https://github.com/MartinBernstorff/Memium/commit/5680ad9663075465f5454b1f34311b349ade30e6))

Auto-created

---------

Co-authored-by: github-actions <github-actions@github.com>

### Testing

- Tags
  ([`f493ed4`](https://github.com/MartinBernstorff/Memium/commit/f493ed492c55766d56c85dcbb633b0de3988032e))


## v0.6.0 (2023-11-18)

### Bug Fixes

- Do not mount input dir on remote ([#201](https://github.com/MartinBernstorff/Memium/pull/201),
  [`83cedae`](https://github.com/MartinBernstorff/Memium/commit/83cedaeb83c918248d52ad2f09233232761972b6))

Auto-created

- Add mounts points for devcontainer
  ([`c2497ee`](https://github.com/MartinBernstorff/Memium/commit/c2497eeb7a0cc76763d45db4694b1a0c9d6d55ac))

### Build System

- Update dockerfile for new dir structure
  ([`0f1e8c0`](https://github.com/MartinBernstorff/Memium/commit/0f1e8c0f3bfbc1610c159ea6e0f0c40cc86bd1b1))

### Continuous Integration

- Fix integration tests with new path ([#200](https://github.com/MartinBernstorff/Memium/pull/200),
  [`b734f9e`](https://github.com/MartinBernstorff/Memium/commit/b734f9ee8f103586cdf7718ae13a50bf9dc5eb12))

Auto-created

- Run docker publish independently of integration test
  ([`d1402c6`](https://github.com/MartinBernstorff/Memium/commit/d1402c6a29d5ef2878ed8342ca237edb5d3b5ae5))

- Run type checks on application script as well
  ([`849c0f5`](https://github.com/MartinBernstorff/Memium/commit/849c0f552ae9ae785bdb515d480dca811f0436ef))

- Setup multiplatform conditions ([#192](https://github.com/MartinBernstorff/Memium/pull/192),
  [`5120b18`](https://github.com/MartinBernstorff/Memium/commit/5120b18685cce3af0930473d8981d5f87e0016c0))

- Add arm64 to deploy
  ([`a6fb2c5`](https://github.com/MartinBernstorff/Memium/commit/a6fb2c58b1ef39ead800263a33b2e56210c8f9dc))

- Update docker build action
  ([`6724cd4`](https://github.com/MartinBernstorff/Memium/commit/6724cd4c6475924d5780420d6446e5d869c82cda))

### Features

- Move cli to separate file
  ([`f91216b`](https://github.com/MartinBernstorff/Memium/commit/f91216b9cf9fdd04eb7227de4b7d497472dc4ccd))

### Refactoring

- Rename pipeline to not hit test
  ([`1b5cbf2`](https://github.com/MartinBernstorff/Memium/commit/1b5cbf2ed84aa1459853cf143509f690ede4ea79))


## v0.5.1 (2023-10-28)

### Bug Fixes

- Docker deploy should be lowercase
  ([`56d0517`](https://github.com/MartinBernstorff/Memium/commit/56d0517da01ba25c950e5c01e13e190fd4bbeabe))


## v0.5.0 (2023-10-28)

### Continuous Integration

- Add docker deploy
  ([`a658f15`](https://github.com/MartinBernstorff/Memium/commit/a658f15e9818449262f123ddc63d6ae64e1b4bbe))

- Support multiline comment
  ([`273d2c9`](https://github.com/MartinBernstorff/Memium/commit/273d2c980b67e0b12a52246e1d98e1144cc5111a))

- Remove unused section
  ([`79bb2d2`](https://github.com/MartinBernstorff/Memium/commit/79bb2d21327e243398ffbe56a17055e9e44f4b10))

- Make integration test unique
  ([`85753df`](https://github.com/MartinBernstorff/Memium/commit/85753df8d6270f53fa85eaf8496e456e0efb5631))

- Build prod image as part of tests
  ([`b595956`](https://github.com/MartinBernstorff/Memium/commit/b59595611de1bc208501cdb09c630d20cfbc7728))

### Documentation

- Update contribution
  ([`a804fc7`](https://github.com/MartinBernstorff/Memium/commit/a804fc7627e330cfa21fc92c0a0c360d0da88175))

- Update readme
  ([`704ae21`](https://github.com/MartinBernstorff/Memium/commit/704ae21840118a826d0e8a4d3ce38e93e8a261fe))

### Features

- Add integration test
  ([`e0526b6`](https://github.com/MartinBernstorff/Memium/commit/e0526b60bfb06f2e0d75d0c52ebb8d1ed5d7966c))

- Add prod docker image
  ([`ed5f350`](https://github.com/MartinBernstorff/Memium/commit/ed5f35099d7d79295726967545b6bce87b0927d2))


## v0.4.0 (2023-10-27)

### Bug Fixes

- Duplicate version toml
  ([`8526eed`](https://github.com/MartinBernstorff/Memium/commit/8526eed202a59021c15b258fcdf422172f7972b7))

### Features

- Add build command
  ([`d6cb133`](https://github.com/MartinBernstorff/Memium/commit/d6cb1330cbc7b7fbc4babc2e9e480da6a37bb5b0))


## v0.3.0 (2023-10-27)

### Bug Fixes

- Correctly sync dirs in bind mounts
  ([`3e269ee`](https://github.com/MartinBernstorff/Memium/commit/3e269ee2dfceb005b7418336cf0f3a5d821c3027))

- Add field to attribute, not property
  ([`274370f`](https://github.com/MartinBernstorff/Memium/commit/274370f914078c8c8b00bd1cc42fe26bacce2f2f))

- Re-add required import
  ([`3d0d51d`](https://github.com/MartinBernstorff/Memium/commit/3d0d51d5354ce31ddbc18d3d3fa662635cc38933))

- Infinite loop
  ([`ce7470a`](https://github.com/MartinBernstorff/Memium/commit/ce7470a08570d14a5d6667a3b08f989d302936b6))

- Pin invoke to version 2.1.0
  ([`a5c56b9`](https://github.com/MartinBernstorff/Memium/commit/a5c56b946ae5083cf67aaed0dd51c0876ad61b7c))

- Incorrect type hints from misaka
  ([`6988e7a`](https://github.com/MartinBernstorff/Memium/commit/6988e7a63957a9f23c4b8296b44b64768e798ea2))

- Remove rej
  ([`152f124`](https://github.com/MartinBernstorff/Memium/commit/152f124d4bb608f041da4b53dcd34666803b84c5))

- Typo
  ([`e687c3e`](https://github.com/MartinBernstorff/Memium/commit/e687c3ed239ea8abdabf06143657c5a2a9a5f577))

- Overlapping commands
  ([`dd66cc1`](https://github.com/MartinBernstorff/Memium/commit/dd66cc11ceda6b1890b1c69a11e36578f515b2da))

- Do not point to non-existing license
  ([`5197292`](https://github.com/MartinBernstorff/Memium/commit/5197292ddd6b30e549cd46167a89495a29623a88))

- Shrink matching
  ([`5dc43d7`](https://github.com/MartinBernstorff/Memium/commit/5dc43d7b62752affc4a9d3ee73fc723084727472))

- Remove da references
  ([`1b32634`](https://github.com/MartinBernstorff/Memium/commit/1b326345dfa2ce65814a4412c91bd67e59354f85))

### Build System

- Auto-fix formatting by default
  ([`16806cf`](https://github.com/MartinBernstorff/Memium/commit/16806cfb1d5caa54f41626148dd6d779405fbf44))

- Update tasks.py
  ([`cef2666`](https://github.com/MartinBernstorff/Memium/commit/cef266634fecb9546ccd149b53d3116f81764bb5))

- Typo
  ([`c3b4ed0`](https://github.com/MartinBernstorff/Memium/commit/c3b4ed0e1bccc0f72abec5d60d8a13c2d1d5c983))

- More informative messaging when syncing
  ([`d351a16`](https://github.com/MartinBernstorff/Memium/commit/d351a169c723f524e96ebe8c6618c4881097ab24))

- Pull before push
  ([`027d426`](https://github.com/MartinBernstorff/Memium/commit/027d426159a89893249e698a8a00b38c60a7761c))

- Hide result from gh pr lsit
  ([`9c91fa1`](https://github.com/MartinBernstorff/Memium/commit/9c91fa19cf96d944d4c7ed8ace8f4fd42677e665))

- Only open browser if PR does not exist
  ([`883ddca`](https://github.com/MartinBernstorff/Memium/commit/883ddca4bdb160ce809e161d4d17345d7927e7d7))

- Prettier messages
  ([`4c5d961`](https://github.com/MartinBernstorff/Memium/commit/4c5d96153067b555571d05834cd1541ed1249b6a))

- Hide output of branch_exists_on_remote
  ([`9bef312`](https://github.com/MartinBernstorff/Memium/commit/9bef31295b03348c52649193d3fc6129cffedc08))

- Separate exist and does not exist flow
  ([`b044fe6`](https://github.com/MartinBernstorff/Memium/commit/b044fe67b9b523c0644a0bebf2ab710ee47ddc4d))

- Remove @task decorator from utils function
  ([`2e7a61d`](https://github.com/MartinBernstorff/Memium/commit/2e7a61d46d39b45dc0d7cf37c966733f2de5bdc6))

- Add timeout to pr list
  ([`d76f8d1`](https://github.com/MartinBernstorff/Memium/commit/d76f8d1f840385130fb4b8e89b325a8955371483))

- Fix quotation marks
  ([`d833bc5`](https://github.com/MartinBernstorff/Memium/commit/d833bc599dd3139d2d5539485a7e0c2599cbda65))

- Push branch to origin if doesn't exist
  ([`2b07dd9`](https://github.com/MartinBernstorff/Memium/commit/2b07dd9f3c63033fc6a9abe35f36017b9b900fdc))

- Push to PR if exists
  ([`137aa06`](https://github.com/MartinBernstorff/Memium/commit/137aa0616c0e2f6409becf47ab8c88c0bf6d9ab6))

- Ask for commit if uncommitted changes before PR
  ([`4b4f7d3`](https://github.com/MartinBernstorff/Memium/commit/4b4f7d39d316e7d920ea637279241f175a28f065))

- Complete migration to Invoke
  ([`4c77a87`](https://github.com/MartinBernstorff/Memium/commit/4c77a87fe1b1cc50581991b4c1698cc7953b8d89))

- Use all available cores
  ([`f9916e8`](https://github.com/MartinBernstorff/Memium/commit/f9916e8147819a47642a157900305bc56e4bf149))

- Add more emojis
  ([`bb858f9`](https://github.com/MartinBernstorff/Memium/commit/bb858f9bd191316997990219531f392b3e2f795d))

- Make tests only show minimal effect
  ([`65c3ddc`](https://github.com/MartinBernstorff/Memium/commit/65c3ddcf80afc187de6192e4c6d20f44329ac61d))

- Run failed tests first
  ([`af11fcb`](https://github.com/MartinBernstorff/Memium/commit/af11fcbadb72778574257f8163915cea13e159c3))

- Missing backslash
  ([`0fa130e`](https://github.com/MartinBernstorff/Memium/commit/0fa130e9fb611b3795f1dfeba8b306191a4c523d))

- Pre_commit before mypy
  ([`d2a5c40`](https://github.com/MartinBernstorff/Memium/commit/d2a5c4008945e3f8e532987d04be009b65de9bfb))

- Misc.
  ([`968cd47`](https://github.com/MartinBernstorff/Memium/commit/968cd4713f315ad77b0d1516cf18903fa5a9ecfe))

- Misc.
  ([`0d94a1d`](https://github.com/MartinBernstorff/Memium/commit/0d94a1df383e873ccc71cbf48494bc8931ceab8d))

- First makefile
  ([`e446e8b`](https://github.com/MartinBernstorff/Memium/commit/e446e8b61ec74ecf14308a685e9fea406339174a))

- Remove unused readme
  ([`7f00c19`](https://github.com/MartinBernstorff/Memium/commit/7f00c19a6635e0168ae16126b40d7db6db1611d7))

### Chores

- Cleanup repo
  ([`2f7c31f`](https://github.com/MartinBernstorff/Memium/commit/2f7c31f97139275964d034da616f7d8ca1ad5c79))

### Code Style

- Auto-fixes from pre-commit
  ([`45d16ee`](https://github.com/MartinBernstorff/Memium/commit/45d16eea207f5a337de8878f82dfd9a28657e402))

- Auto-fixes from pre-commit
  ([`8c79758`](https://github.com/MartinBernstorff/Memium/commit/8c7975885265bce9de1a9919fcb929e841e8862c))

- Lint
  ([`1998401`](https://github.com/MartinBernstorff/Memium/commit/19984014599e94f84ff46d128de126feb05e9818))

- Linting
  ([`2db1686`](https://github.com/MartinBernstorff/Memium/commit/2db1686bcf4a4e09b87cbdaf5605efc9f2ad879f))

- Linting
  ([`98f0a06`](https://github.com/MartinBernstorff/Memium/commit/98f0a0604de83de09d33922ebbd61986bdde6bf7))

- Linting
  ([`521cf42`](https://github.com/MartinBernstorff/Memium/commit/521cf42889a64bd8c3de873657643b03e0a0e483))

- Linting
  ([`1b59dcc`](https://github.com/MartinBernstorff/Memium/commit/1b59dccd5bfc4d59cfca8a05bb7f4144671460c7))

- Remove unused type: ignore
  ([`0fb4b28`](https://github.com/MartinBernstorff/Memium/commit/0fb4b28d598a16e91ea7db562eafaeff05ef01eb))

- Linting
  ([`6198058`](https://github.com/MartinBernstorff/Memium/commit/6198058164273d63d4de0dc597854915b5a90d75))

- Linting
  ([`17c3163`](https://github.com/MartinBernstorff/Memium/commit/17c31631ce35ed2c03dcf87247f0f69e5476980a))

### Continuous Integration

- Update cruft
  ([`28c6125`](https://github.com/MartinBernstorff/Memium/commit/28c61258104da50093e9762387c8e50269112c9f))

- Run release after tests
  ([`345abc3`](https://github.com/MartinBernstorff/Memium/commit/345abc37ad64191113de7b9afac81a001170059d))

- Create hosts before push
  ([`6d38c59`](https://github.com/MartinBernstorff/Memium/commit/6d38c59ba3b38d3a71c09d2ea08cecfc84dd4a64))

- Update cruft
  ([`357ac0a`](https://github.com/MartinBernstorff/Memium/commit/357ac0a10ad7409b5d725d8c03ed8669cec0032b))

- Reenable release
  ([`6a81185`](https://github.com/MartinBernstorff/Memium/commit/6a81185f68c81d5b0ac23369c480687015f4acb0))

- Reenable release
  ([`1d2d20a`](https://github.com/MartinBernstorff/Memium/commit/1d2d20affac9d21f9f376a37c3836c6c918fca0d))

- Re-enable caching in tests
  ([`dee7316`](https://github.com/MartinBernstorff/Memium/commit/dee7316908ab7d8ffbcf813500943af622f6a7c6))

- Move dependencies to correct subheading
  ([`fea7ee1`](https://github.com/MartinBernstorff/Memium/commit/fea7ee1f89829974fa8bee49f9724b5848fe093f))

- Invalidate cache
  ([`4eb6aae`](https://github.com/MartinBernstorff/Memium/commit/4eb6aaef43e2df931b56de953cb5f9b847a8ccd7))

- Run tests
  ([`26473be`](https://github.com/MartinBernstorff/Memium/commit/26473bef39f6acf0fd2fd7d7f2441544f8678954))

- Simplify
  ([`abae734`](https://github.com/MartinBernstorff/Memium/commit/abae734e498eedc95537e2579101f56e32d75a26))

- Remove pull-request template
  ([`bfbe55d`](https://github.com/MartinBernstorff/Memium/commit/bfbe55d2241c9ec260e0d2b9d762e30443f453bb))

- Use nimble-python
  ([`9da7e6c`](https://github.com/MartinBernstorff/Memium/commit/9da7e6cc0d4e45fd7abf1d2536ed59be76215fb6))

- Create pr on web
  ([`654349a`](https://github.com/MartinBernstorff/Memium/commit/654349a36bab5bd1ef9015a572dab176fcdecb09))

- Send alert if script fails
  ([`25f88c2`](https://github.com/MartinBernstorff/Memium/commit/25f88c2773a55b1a1fa8ac20cf4793f85cf116ae))

- Add dockerignore
  ([`35f6ecf`](https://github.com/MartinBernstorff/Memium/commit/35f6ecfc8cb47be58b75246fc16a8954c43b0acb))

- Align dockerfile devcontainer python with rest of project
  ([`fd0a59d`](https://github.com/MartinBernstorff/Memium/commit/fd0a59d97bc3e72c5ad1e22c1349e3168012eb04))

- Install pre-commit hooks on setup
  ([`61bfc12`](https://github.com/MartinBernstorff/Memium/commit/61bfc1257ec01476c331cf2d6e586268aed2b121))

- Optimise layers for deps
  ([`eea7e9b`](https://github.com/MartinBernstorff/Memium/commit/eea7e9b6412071dae6dc6b2f28af73cf93307047))

- Install test deps in dev container
  ([`0a03465`](https://github.com/MartinBernstorff/Memium/commit/0a034657ff9ed42a8a4727c37115d45b2c1a9e56))

- Do not automatically commit formatting changes
  ([`9073d12`](https://github.com/MartinBernstorff/Memium/commit/9073d12f21ba7cec2bc178c997005fa33598654b))

- Update tasks
  ([`2837861`](https://github.com/MartinBernstorff/Memium/commit/283786145c625efd9e942d090a06fa05b977c978))

- Print branch name
  ([`3e3dbf2`](https://github.com/MartinBernstorff/Memium/commit/3e3dbf247e79c196896239c1b6f3103d750f9831))

- Update cruft
  ([`4e5a414`](https://github.com/MartinBernstorff/Memium/commit/4e5a414bc3af76b690806c9acc47b343e3c5faa2))

- Update paths
  ([`29cc8ce`](https://github.com/MartinBernstorff/Memium/commit/29cc8cea1aaa789f69b48b89a34fe8e8b3c94f2c))

- Remove unused PR
  ([`949e2e3`](https://github.com/MartinBernstorff/Memium/commit/949e2e312b75ed38541e0354518bd8753e96d034))

- Simplify call
  ([`c072a29`](https://github.com/MartinBernstorff/Memium/commit/c072a294bd354f45b491a896e9fda18cf329e566))

- Update tasks
  ([`687cdb8`](https://github.com/MartinBernstorff/Memium/commit/687cdb8dec71d5a1a21a8f91cbbf412a5239393c))

- Broader ignore for venv
  ([`a5f534f`](https://github.com/MartinBernstorff/Memium/commit/a5f534f83c434da9c18e92495d3bf3c7e2e3c0cb))

- Minimal test interface
  ([`0059b80`](https://github.com/MartinBernstorff/Memium/commit/0059b803ead752006d1943b06b351d8591324fad))

- Update cruft
  ([`bda3461`](https://github.com/MartinBernstorff/Memium/commit/bda3461e914fcd421b2fcc9107f267a98734bff5))

- Update cruft
  ([`169171c`](https://github.com/MartinBernstorff/Memium/commit/169171ce0677d21e9559784f99deb811d2b536b4))

- Disable release
  ([`a73a8d3`](https://github.com/MartinBernstorff/Memium/commit/a73a8d3827e0d918c09e66852c54efa824fa31a3))

- Update cruft
  ([`382231d`](https://github.com/MartinBernstorff/Memium/commit/382231db184585973869738e581f9f2323e8fead))

- Remove poetry
  ([`a7c091d`](https://github.com/MartinBernstorff/Memium/commit/a7c091d668eab47f24fccfd708b02a115fa3a1e1))

- Update cruft
  ([`9a3c0fb`](https://github.com/MartinBernstorff/Memium/commit/9a3c0fb10b7d9e258aa6df00e0d621f101c8b380))

- Add mypy to pre-commit
  ([`9746c27`](https://github.com/MartinBernstorff/Memium/commit/9746c2722e862159844fe10c22cb8ac68e7f79c0))

### Documentation

- Improve readme
  ([`b5a4ccc`](https://github.com/MartinBernstorff/Memium/commit/b5a4ccc2684f1fc55ab02608fd9b8cf9f92fb607))

- Update docs
  ([`d0b646d`](https://github.com/MartinBernstorff/Memium/commit/d0b646df07910a25e357d24d6554ca2e1a7f2674))

- Clean up readme
  ([`bcf2480`](https://github.com/MartinBernstorff/Memium/commit/bcf2480cf1eb3a2532338d82e27f7ad6b02b1658))

### Features

- Bump
  ([`26ea9fb`](https://github.com/MartinBernstorff/Memium/commit/26ea9fb53ac4693a834b3c2fd65846e8850fb43d))

- Use functionalpy
  ([`b7352f1`](https://github.com/MartinBernstorff/Memium/commit/b7352f1961177661ce7de8b5f4c5a754564140dd))

- Use functionalpy
  ([`72d106a`](https://github.com/MartinBernstorff/Memium/commit/72d106a5e9597798f329d502401c4d4848a9721d))

- Add docker image
  ([`2c0b7c6`](https://github.com/MartinBernstorff/Memium/commit/2c0b7c6e3233f235c2b5fee1c8f0deeb6558a9f3))

- Pre-populate msic
  ([`73dcb46`](https://github.com/MartinBernstorff/Memium/commit/73dcb46273e88509ae4fb872c979d2ab1144635d))

- Add preferred extensions
  ([`388dce3`](https://github.com/MartinBernstorff/Memium/commit/388dce336c8fc8497da338729c6cb34727137dfc))

- Add dev_container
  ([`0e29b4d`](https://github.com/MartinBernstorff/Memium/commit/0e29b4dbe41a6df5728026db66e22fb1a56ed988))

- Dynamic user dir in debug main launch.json
  ([`0aa5d38`](https://github.com/MartinBernstorff/Memium/commit/0aa5d386d073a8e3d77c3a5957f6beb45fed6f31))

- Robustness to cards with errors
  ([`d340b50`](https://github.com/MartinBernstorff/Memium/commit/d340b50f1bf5bae9f49794e86dfd65d46d893a99))

- Add vscode setting sto tracking
  ([`147716e`](https://github.com/MartinBernstorff/Memium/commit/147716e164d13a1474001905ac24d4465446e974))

- Use obsidian uris
  ([`e107087`](https://github.com/MartinBernstorff/Memium/commit/e1070871474f9205fd905d0e33a6e5e374ae0143))

- Support dash in links
  ([`add5191`](https://github.com/MartinBernstorff/Memium/commit/add51919ccd246d84225b5989b3f04a6b110b858))

- Restrict polling time
  ([`00f163e`](https://github.com/MartinBernstorff/Memium/commit/00f163ea912b35278fa0f3fdf6ec18b88c632b13))

- Improve dir parsing speed
  ([`e17dea6`](https://github.com/MartinBernstorff/Memium/commit/e17dea693d268eeebeedbe83125a3b1e2f81aef2))

- Update guid for qa
  ([`f88d7ad`](https://github.com/MartinBernstorff/Memium/commit/f88d7ad44e9ddc3dbe181c9f8866257d9b308090))

- Add guid test for qa ankinotes
  ([`dfdf04c`](https://github.com/MartinBernstorff/Memium/commit/dfdf04cf962cdb906427f9339eeadb18256583bf))

- Add Obsidian URI to AnkiCards
  ([`b04f44b`](https://github.com/MartinBernstorff/Memium/commit/b04f44b89db5df81de2ba2a805899a48f88c0ee8))

- Sync deletions
  ([`14c24e2`](https://github.com/MartinBernstorff/Memium/commit/14c24e21cb09d34ecb7aefc95f535b815e02cda2))

- Delete cards on sync
  ([`cfd82c9`](https://github.com/MartinBernstorff/Memium/commit/cfd82c968a39c3ba82341d04c39d1f9fc3f90019))

- Add support for markdown link aliases
  ([`add7e2a`](https://github.com/MartinBernstorff/Memium/commit/add7e2ac3769ad99b0bb8841a93fa21af4718ba3))

- Add tts
  ([`5eaf984`](https://github.com/MartinBernstorff/Memium/commit/5eaf9848937678588b84213acbb81a663f6e1d5d))

- Attempt tts addition
  ([`3ccb493`](https://github.com/MartinBernstorff/Memium/commit/3ccb49365eec003ce98bb6ae1c3e0a7f491ff7b7))

- Decrease length of note id
  ([`6075894`](https://github.com/MartinBernstorff/Memium/commit/6075894de68d34b5a2db7277bf82d9aba604c798))

### Refactoring

- Major rewrite of input pipeline
  ([`88793cd`](https://github.com/MartinBernstorff/Memium/commit/88793cd886c444e4cbe2e3dd55d010ff33590b78))

- Split ankicard into AnkiQA and AnkiCloze
  ([`824660c`](https://github.com/MartinBernstorff/Memium/commit/824660c165e70be08d0d4992ac69f4a400b9cf28))

- Specify anki packagegenerator
  ([`8b52a42`](https://github.com/MartinBernstorff/Memium/commit/8b52a42c32e443188684fe825894d636dc3e4083))

- Extract url generation
  ([`b740700`](https://github.com/MartinBernstorff/Memium/commit/b7407001d357a5e814394effaa5bd45a4b9c130b))

- Modularise
  ([`5eba16c`](https://github.com/MartinBernstorff/Memium/commit/5eba16ceefb68fb8b6a5a0ec6f68897716fe2db2))

- Split cards_to_decks
  ([`fa183f0`](https://github.com/MartinBernstorff/Memium/commit/fa183f08bc883a81bf41fd94beb0d9765e04053b))

- Renaming
  ([`61baacc`](https://github.com/MartinBernstorff/Memium/commit/61baacc5d6374dff99f4707887afce02d040a1d0))

- Split git sync and github pr handling
  ([`981d105`](https://github.com/MartinBernstorff/Memium/commit/981d105a222b2f90c61adbb1a6d71a2ead1dee8a))

- Remove unused arguments from config
  ([`c27068b`](https://github.com/MartinBernstorff/Memium/commit/c27068bb735cae85c8d85b1353ab3181e76b6b75))

- Remove support for QA DK card
  ([`125c725`](https://github.com/MartinBernstorff/Memium/commit/125c725a23cdf68f6a5edd317ec6a863665500a7))


## v0.2.0 (2023-03-12)

### Continuous Integration

- Update cruft
  ([`89b9e86`](https://github.com/MartinBernstorff/Memium/commit/89b9e8697ea20a53e44f4e511d91061e951b7013))

- Ignore bearimages
  ([`32bf9e4`](https://github.com/MartinBernstorff/Memium/commit/32bf9e4069a575dda3ac45cd62e4b00608368525))

### Features

- Exclude q. and a. fields from cloze prompts
  ([`5b2d6cd`](https://github.com/MartinBernstorff/Memium/commit/5b2d6cda3825582381444b36c6ef1dbc8779d4af))


## v0.1.0 (2023-03-11)

### Bug Fixes

- Cruft typography
  ([`99b7a25`](https://github.com/MartinBernstorff/Memium/commit/99b7a25ec613b8017309662354ed3def767975f3))

- Hash anki cards on markdown
  ([`b5a35b9`](https://github.com/MartinBernstorff/Memium/commit/b5a35b91f58c3d43e237f495a30940e3ea780a00))

- Don't fail on missing media references
  ([`5274e3f`](https://github.com/MartinBernstorff/Memium/commit/5274e3fb3f494c56c99624ec76cbbd307de548a4))

- Do not use tts for now
  ([`7e3bab5`](https://github.com/MartinBernstorff/Memium/commit/7e3bab580adf7d50d556024db29dd343db6a8cb3))

- Typo in toml
  ([`be9499e`](https://github.com/MartinBernstorff/Memium/commit/be9499e60f9e872112cedd6454ff6fa16af1eabe))

- Ensure guids match cloze
  ([`694f701`](https://github.com/MartinBernstorff/Memium/commit/694f701aa44a1962168cb3256062f70371aef1cd))

- Match guide for first test case
  ([`ee41799`](https://github.com/MartinBernstorff/Memium/commit/ee41799941a027792588821f22003fc2a4c99171))

- Better support for TTS
  ([`78032e7`](https://github.com/MartinBernstorff/Memium/commit/78032e761e7661e1974d5595f39eaf43b8965264))

### Chores

- Remove unused type ignore
  ([`4cbd2b8`](https://github.com/MartinBernstorff/Memium/commit/4cbd2b88cc86c2d8ecc0716d15b64ef5596fa7de))

- More typing
  ([`dcb04d0`](https://github.com/MartinBernstorff/Memium/commit/dcb04d043ae173b02c6b86f707d4d24008d95241))

- Type everything
  ([`884deea`](https://github.com/MartinBernstorff/Memium/commit/884deeaa9c5e58f5d82ade7cdad4575900b8f793))

- Housekeeping
  ([`3c93bd7`](https://github.com/MartinBernstorff/Memium/commit/3c93bd738fbb122ba5d9f4babebeaa8ef9a9a391))

### Code Style

- Linting
  ([`057d034`](https://github.com/MartinBernstorff/Memium/commit/057d0348763f1c3b11dba4bd83877cbb65ac0831))

- Linting
  ([`ba808b6`](https://github.com/MartinBernstorff/Memium/commit/ba808b66ab4d83f919512cfce5d853d19714bdaa))

- Final linting
  ([`8e59770`](https://github.com/MartinBernstorff/Memium/commit/8e597700e268a2f26cc5dc940dfe1fb13789d0ab))

- Linting
  ([`186208c`](https://github.com/MartinBernstorff/Memium/commit/186208c9b009c211c66f57c1ce2efadf7ef2b909))

- Linting
  ([`9f0d580`](https://github.com/MartinBernstorff/Memium/commit/9f0d5802cc6155f2774faeeb293f72d72112a58d))

- Linting
  ([`66e30e1`](https://github.com/MartinBernstorff/Memium/commit/66e30e1b97e7ebed29b1552a0a48c659f09ffe9a))

### Continuous Integration

- Update find comment
  ([`3de3a91`](https://github.com/MartinBernstorff/Memium/commit/3de3a91015f316e5c651ef3f3de0e38704cf12fd))

- Update cruft logic
  ([`9d2109a`](https://github.com/MartinBernstorff/Memium/commit/9d2109ac5d29195bb103a84e5cb8ebb08f7d07b0))

- Update cruft
  ([`aea9b87`](https://github.com/MartinBernstorff/Memium/commit/aea9b870cd52a2d4784e98d11710971d19c6006b))

- Update cruft message
  ([`2343489`](https://github.com/MartinBernstorff/Memium/commit/234348919d8f39546aadf1ff14de0873e30e9100))

- Update cruft failed template
  ([`2d793c5`](https://github.com/MartinBernstorff/Memium/commit/2d793c53579cb2665039a35c11f13168b4f5b52c))

- Cruft
  ([`55b6232`](https://github.com/MartinBernstorff/Memium/commit/55b62321376b3fee21252f4b2878f6e8bdaf2d4e))

- Cruft check
  ([`c3b5353`](https://github.com/MartinBernstorff/Memium/commit/c3b5353b7febd1337acd3addc1a1711e47472bc5))

- Cruft
  ([`eca6564`](https://github.com/MartinBernstorff/Memium/commit/eca65640591eeac6bd7edcb4aa6e3bdb3f450b80))

- Test new cruft procedure
  ([`e41862c`](https://github.com/MartinBernstorff/Memium/commit/e41862c0433c7838282cd7e880dc6a3847c32f54))

- Test
  ([`62ea30c`](https://github.com/MartinBernstorff/Memium/commit/62ea30c0e8d504409bd91fbdcd01540b99752268))

- Test
  ([`babf357`](https://github.com/MartinBernstorff/Memium/commit/babf357b30cecd73e8c202a80d881cfd2c2399fa))

- Fix error in cruft
  ([`c3114e5`](https://github.com/MartinBernstorff/Memium/commit/c3114e5809a7135ad7dabf088abc99cec35a0968))

- Try new cruft ci
  ([`6412ae8`](https://github.com/MartinBernstorff/Memium/commit/6412ae8eaf9626de016abbef28e4c291e093c088))

- Update cruft
  ([`12bd8a9`](https://github.com/MartinBernstorff/Memium/commit/12bd8a9736da761c405af7e42f0747073a1364bf))

- Permissions for setup_for_dev
  ([`8f23875`](https://github.com/MartinBernstorff/Memium/commit/8f23875ad5e970bdb64503dc2a72a909e6c22e74))

### Features

- Ignore cloze-likes in code blocks
  ([`80b0888`](https://github.com/MartinBernstorff/Memium/commit/80b0888839ea8206fc1697674be4ac2e42e0627f))

- Compile fields to html
  ([`13f8c07`](https://github.com/MartinBernstorff/Memium/commit/13f8c079a2db56c0b80161488d2831cc9d9eadf2))

- Better sh file
  ([`fc0b2e6`](https://github.com/MartinBernstorff/Memium/commit/fc0b2e6197940906061e22f069c361d3f379685c))

- Working version
  ([`a8438c7`](https://github.com/MartinBernstorff/Memium/commit/a8438c7b3cb42f4cb2718008b8e2ed4f2514c7ab))

- Don't update bear
  ([`59fef60`](https://github.com/MartinBernstorff/Memium/commit/59fef60eb4d22fc9e3e5443b7456a1687689d4e3))

- Migrate main to use new pipeline
  ([`fa71108`](https://github.com/MartinBernstorff/Memium/commit/fa7110896aa326cf44646cb0fe7353c0d8ffa337))

- Create a unified pipeline
  ([`a703fcc`](https://github.com/MartinBernstorff/Memium/commit/a703fcc8158d2412170dda333d24cc87bf4c3daf))

- Fit uuid generation to qa prompt extractor
  ([`4e33b0d`](https://github.com/MartinBernstorff/Memium/commit/4e33b0d37075d897aba0a932316d10284572e1e4))

- Remove filepath requirement
  ([`65c97a5`](https://github.com/MartinBernstorff/Memium/commit/65c97a5262965cd0776bfb36bc7108a27e83fd6d))

- First working rewrite
  ([`9a16d98`](https://github.com/MartinBernstorff/Memium/commit/9a16d983054fa03c005922778f1e4bc33222496d))

- First stab at main package
  ([`069accd`](https://github.com/MartinBernstorff/Memium/commit/069accdfff488ed285dabebdbb847fb1ba064c3b))

- Add markdown to card logic
  ([`f1a204f`](https://github.com/MartinBernstorff/Memium/commit/f1a204ff74c898374f8399f34aba8577830391a0))

- Add cloze extractor
  ([`8fda355`](https://github.com/MartinBernstorff/Memium/commit/8fda355e9ab7b9e945c61c7b2853a3418cfa4458))

- Add source notes to QAPrompts
  ([`08bae17`](https://github.com/MartinBernstorff/Memium/commit/08bae173fcd0ce96aa54319cbe529a918e0b3229))

- Add qa_prompt_extractor
  ([`377b426`](https://github.com/MartinBernstorff/Memium/commit/377b426d97ab985832cb577cfbfa4e4c01d73fd6))

- Disable automatic tts (replaced by AwesomeTTS)
  ([`5f37882`](https://github.com/MartinBernstorff/Memium/commit/5f37882a9ce24ba84e36b7d2d1939cc035144dbe))

### Refactoring

- Add guards
  ([`c92eeb7`](https://github.com/MartinBernstorff/Memium/commit/c92eeb7c101f7a3c30e57827b8d5e696c7c82b49))

- Stylise pipeline
  ([`34ba2a3`](https://github.com/MartinBernstorff/Memium/commit/34ba2a317f61f1ff0771ac4388ac634b99e67773))

- Disambiguate note and prompt uuids
  ([`db5c457`](https://github.com/MartinBernstorff/Memium/commit/db5c4570378fd7f50265b8ca3991cfb4dab7bbb5))

- Clean up subdeck
  ([`7f03b42`](https://github.com/MartinBernstorff/Memium/commit/7f03b42bdb46733683459d5b8e21df39e44bc427))

- Misc.
  ([`8a366b3`](https://github.com/MartinBernstorff/Memium/commit/8a366b3fc2dce6788ae93a5f80c0a57e40fc75b7))

- Rename factory classes
  ([`af592f4`](https://github.com/MartinBernstorff/Memium/commit/af592f4f51c4ed531582be5b7d538a27fd4680fb))
