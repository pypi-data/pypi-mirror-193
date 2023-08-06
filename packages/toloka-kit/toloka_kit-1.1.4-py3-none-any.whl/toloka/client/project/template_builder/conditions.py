__all__ = [
    'BaseConditionV1',

    'AllConditionV1',
    'AnyConditionV1',
    'DistanceConditionV1',
    'EmptyConditionV1',
    'EqualsConditionV1',
    'LinkOpenedConditionV1',
    'NotConditionV1',
    'PlayedConditionV1',
    'PlayedFullyConditionV1',
    'RequiredConditionV1',
    'SameDomainConditionV1',
    'SchemaConditionV1',
    'SubArrayConditionV1',
]
from typing import List, Any, Dict

from ....util._codegen import attribute

from .base import BaseComponent, ComponentType, VersionedBaseComponentMetaclass, base_component_or
from ....util._docstrings import inherit_docstrings


class BaseConditionV1Metaclass(VersionedBaseComponentMetaclass):
    def __new__(mcs, name, bases, namespace, **kwargs):
        if 'hint' not in namespace:
            namespace['hint'] = attribute(kw_only=True)
            namespace.setdefault('__annotations__', {})['hint'] = base_component_or(Any)
        return super().__new__(mcs, name, bases, namespace, **kwargs)


class BaseConditionV1(BaseComponent, metaclass=BaseConditionV1Metaclass):
    """Check an expression against a condition.

    For example, you can check that a text field is filled in.

    Attributes:
        hint: Validation error message that a Toloker will see.
    """

    pass


@inherit_docstrings
class AllConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_ALL):
    """Checks that all child conditions are met.

    If any of the conditions is not met, the component returns 'false'.

    If you only need one out of several conditions to be met, use the condition.any component. You can also combine
    these components.
    Attributes:
        conditions: A set of conditions that must be met.

    Example:
        How to check several conditions.

        >>> coordinates_validation = tb.conditions.AllConditionV1(
        >>>     [
        >>>         tb.conditions.RequiredConditionV1(
        >>>             tb.data.OutputData('performer_coordinates'),
        >>>             hint="Couldn't get your coordinates. Please enable geolocation.",
        >>>         ),
        >>>         tb.conditions.DistanceConditionV1(
        >>>             tb.data.LocationData(),
        >>>             tb.data.InputData('coordinates'),
        >>>             500,
        >>>             hint='You are too far from the destination coordinates.',
        >>>         ),
        >>>     ],
        >>> )
        ...
    """

    conditions: base_component_or(List[BaseComponent], 'ListBaseComponent')  # noqa: F821


@inherit_docstrings
class AnyConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_ANY):
    """Checks that at least one of the child conditions is met.

    If none of the conditions is met, the component returns false.

    If you need all conditions to be met, use the condition.all component. You can also combine these components.
    Attributes:
        conditions: A set of conditions, at least one of which must be met.
    """

    conditions: base_component_or(List[BaseComponent], 'ListBaseComponent')  # noqa: F821


@inherit_docstrings
class DistanceConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_YANDEX_DISTANCE):
    """This component checks whether the sent coordinates match the ones that you specified

    For example, you want a Toloker to take a photo of a specific place. The condition.distance component checks whether
    the photo was taken at the location that you specified.

    Attributes:
        from_: First point.
        to_: Second point.
        max: The distance in meters by which the X and Y coordinates may differ.

    Example:
        How to check that a Toloker is in the right place.

        >>> distance_condition = tb.conditions.DistanceConditionV1(
        >>>     tb.data.LocationData(),
        >>>     tb.data.InputData('coordinates'),
        >>>     500,
        >>>     hint='You are too far from the destination coordinates.',
        >>> ),
        ...
    """

    from_: base_component_or(str) = attribute(origin='from')
    to_: base_component_or(str) = attribute(origin='to')
    max: base_component_or(float)


@inherit_docstrings
class EmptyConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_EMPTY):
    """Checks that the data is empty (undefined).

    Returns false if the data received a value.

    You can check:
        Template data (data.*).
        Data for the input field (field.*) that contains condition.empty.
    Attributes:
        data: Data to check. If not specified, data is checked in the component that contains condition.empty.
    """

    data: base_component_or(Any)


@inherit_docstrings
class EqualsConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_EQUALS):
    """Checks whether the original value is equal to the specified value.

    If it matches, it returns true, otherwise it returns false.

    When substituting values, you can refer to data.* or another element using $ref. You can also use helpers and
    conditions to get the value.
    Attributes:
        to: The value to compare with the original.
            How to pass a value:
            * Specify the value itself, like the number 42 or a string.
            * Get the value from your data.
            * Refer to another element using $ref.
            * Use helpers and conditions to get the value.
        data: Original value. If not specified, it uses the value returned by the parent component (the component that
            contains condition.equals).
            How to pass a value:
                * Specify the value itself, like the number 42 or a string.
                * Get the value from your data.
                * Refer to another element using $ref.
                * Use helpers and conditions to get the value.
    """

    to: base_component_or(Any)
    data: base_component_or(Any)


@inherit_docstrings
class LinkOpenedConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_LINK_OPENED):
    """Checks that the Toloker clicked the link.

    Important: To trigger the condition, the Toloker must follow the link from the Toloka interface — you must give Tolokers
    this option. The condition will not work if the Toloker opens the link from the browser address bar.

    This condition can be used in the view.link component and also anywhere you can use (conditions).
    Attributes:
        url: The link that must be clicked.
    """

    url: base_component_or(Any)


@inherit_docstrings
class NotConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_NOT):
    """Returns the inverse of the specified condition.

    For example, if the specified condition is met (returns true), then condition.not will return false.
    Attributes:
        condition: The condition for which the inverse is returned.
    """

    condition: BaseComponent


@inherit_docstrings
class PlayedConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_PLAYED):
    """Checks the start of playback.

    Validation will be passed if playback is started. To play media with the condition.played check, you can use
    view.audio and view.video. The condition.played check only works in the player's validation property.
    """

    pass


@inherit_docstrings
class PlayedFullyConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_PLAYED_FULLY):
    """This component checks for the end of playback.

    Validation is passed if playback is finished. To play media with the condition.played-fully check, you can use
    view.audio and view.video. The condition.played-fully check only works in the player's validation property.
    """

    pass


@inherit_docstrings
class RequiredConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_REQUIRED):
    """Checks that the data is filled in. This way you can get the Toloker to answer all the required questions.

    If used inside the validation property, you can omit the data property and the same property will be used from the
    parent component field (the one that contains the condition.required component).
    Attributes:
        data: Data to be filled in. If the property is not specified, the data of the parent component (the one that
            contains condition.required) is used.

    Example:
        How to check that image is uploaded.

        >>> image = tb.fields.MediaFileFieldV1(
        >>>     tb.data.OutputData('image'),
        >>>     tb.fields.MediaFileFieldV1.Accept(photo=True, gallery=True),
        >>>     validation=tb.conditions.RequiredConditionV1(hint='Your must upload photo.'),
        >>> )
        ...
    """

    data: base_component_or(Any)


@inherit_docstrings
class SameDomainConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_SAME_DOMAIN):
    """Checks if the link that you entered belongs to a specific site. If it does, returns true, otherwise, false.

    Links must be specified in full, including the protocol (http, https, ftp).

    The `www.` subdomain is ignored when checking, meaning that links to `www.example.com`
    and `example.com` are considered to be the same.

    How to pass a link address:

    * Specify it explicitly as a string.
    * [Get the value](https://toloka.ai/en/docs/template-builder/operations/work-with-data) from your data.
    * Refer to another element using `$ref`.
    * Use [helpers](https://toloka.ai/en/docs/template-builder/reference/helpers) and
      [conditions](https://toloka.ai/en/docs/template-builder/reference/conditions) to get the value.

    Attributes:
        data: The link address to be checked. If you don't specify it, the value returned by the parent component
            (the one that contains condition.same-domain) is used.
        original: The link address that your link is compared to.
    """

    data: base_component_or(Any)
    original: base_component_or(Any)


@inherit_docstrings
class SchemaConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_SCHEMA):
    """Allows validating data using JSON Schema. This is a special format for describing data in JSON format.

    For example, you can describe the data type, the minimum and maximum values, and specify that all values must be
    unique.

    This component is useful in the following cases:
        * If available components don't provide everything you need to configure validation.
        * If you already have a prepared JSON Schema configuration for the check and you want to use it.
    Attributes:
        data: Data that should be checked.
        schema: The schema for validating data.
    """

    data: base_component_or(Any)
    schema: Dict  # TODO: support base_component_or(Dict)


@inherit_docstrings
class SubArrayConditionV1(BaseConditionV1, spec_value=ComponentType.CONDITION_SUB_ARRAY):
    """Checks that the array in data is a subarray for parent.

    Attributes:
        data: Subarray that is checked for in parent.
        parent: The array where data is searched for.
    """

    data: base_component_or(Any)
    parent: base_component_or(Any)
