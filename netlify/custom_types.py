from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


class Context(Enum):
    """The deploy context in which this value will be used. `dev` refers to local development
    when running `netlify dev`. `branch` must be provided with a value in
    `context_parameter`.
    
    The deploy context in which this value will be used. `dev` refers to local development
    when running `netlify dev`.
    """
    ALL = "all"
    BRANCH = "branch"
    BRANCH_DEPLOY = "branch-deploy"
    DEPLOY_PREVIEW = "deploy-preview"
    DEV = "dev"
    PRODUCTION = "production"


class PatchAccountsAccountIDEnvKeyBody:
    """The deploy context in which this value will be used. `dev` refers to local development
    when running `netlify dev`. `branch` must be provided with a value in `context_parameter`.
    """
    context: Optional[Context]
    """An additional parameter for custom branches. Currently, this is used for providing a
    branch name when `context=branch`.
    """
    context_parameter: Optional[str]
    """The environment variable's unencrypted value"""
    value: Optional[str]

    def __init__(self, context: Optional[Context], context_parameter: Optional[str], value: Optional[str]) -> None:
        self.context = context
        self.context_parameter = context_parameter
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'PatchAccountsAccountIDEnvKeyBody':
        assert isinstance(obj, dict)
        context = from_union([Context, from_none], obj.get("context"))
        context_parameter = from_union([from_str, from_none], obj.get("context_parameter"))
        value = from_union([from_str, from_none], obj.get("value"))
        return PatchAccountsAccountIDEnvKeyBody(context, context_parameter, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.context is not None:
            result["context"] = from_union([lambda x: to_enum(Context, x), from_none], self.context)
        if self.context_parameter is not None:
            result["context_parameter"] = from_union([from_str, from_none], self.context_parameter)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


class Scope(Enum):
    BUILDS = "builds"
    FUNCTIONS = "functions"
    POST_PROCESSING = "post-processing"
    RUNTIME = "runtime"


class EnvVarValue:
    """Environment variable value model definition"""
    """The deploy context in which this value will be used. `dev` refers to local development
    when running `netlify dev`.
    """
    context: Optional[Context]
    """An additional parameter for custom branches. Currently, this is used for specifying a
    branch name when `context=branch`.
    """
    context_parameter: Optional[str]
    """The environment variable value's universally unique ID"""
    id: Optional[str]
    """The environment variable's unencrypted value"""
    value: Optional[str]

    def __init__(self, context: Optional[Context], context_parameter: Optional[str], id: Optional[str], value: Optional[str]) -> None:
        self.context = context
        self.context_parameter = context_parameter
        self.id = id
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'EnvVarValue':
        assert isinstance(obj, dict)
        context = from_union([Context, from_none], obj.get("context"))
        context_parameter = from_union([from_str, from_none], obj.get("context_parameter"))
        id = from_union([from_str, from_none], obj.get("id"))
        value = from_union([from_str, from_none], obj.get("value"))
        return EnvVarValue(context, context_parameter, id, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.context is not None:
            result["context"] = from_union([lambda x: to_enum(Context, x), from_none], self.context)
        if self.context_parameter is not None:
            result["context_parameter"] = from_union([from_str, from_none], self.context_parameter)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


class PostAccountsAccountIDEnvBodyItem:
    """Secret values are only readable by code running on Netlify’s systems.  With secrets, only
    the local development context values are readable from the UI, API, and CLI. By default,
    environment variable values are not secret. (Enterprise plans only)
    """
    is_secret: Optional[bool]
    """The existing or new name of the key, if you wish to rename it (case-sensitive)"""
    key: Optional[str]
    """The scopes that this environment variable is set to (Pro plans and above)"""
    scopes: Optional[List[Scope]]
    values: Optional[List[EnvVarValue]]

    def __init__(self, is_secret: Optional[bool], key: Optional[str], scopes: Optional[List[Scope]], values: Optional[List[EnvVarValue]]) -> None:
        self.is_secret = is_secret
        self.key = key
        self.scopes = scopes
        self.values = values

    @staticmethod
    def from_dict(obj: Any) -> 'PostAccountsAccountIDEnvBodyItem':
        assert isinstance(obj, dict)
        is_secret = from_union([from_bool, from_none], obj.get("is_secret"))
        key = from_union([from_str, from_none], obj.get("key"))
        scopes = from_union([lambda x: from_list(Scope, x), from_none], obj.get("scopes"))
        values = from_union([lambda x: from_list(EnvVarValue.from_dict, x), from_none], obj.get("values"))
        return PostAccountsAccountIDEnvBodyItem(is_secret, key, scopes, values)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.is_secret is not None:
            result["is_secret"] = from_union([from_bool, from_none], self.is_secret)
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.scopes is not None:
            result["scopes"] = from_union([lambda x: from_list(lambda x: to_enum(Scope, x), x), from_none], self.scopes)
        if self.values is not None:
            result["values"] = from_union([lambda x: from_list(lambda x: to_class(EnvVarValue, x), x), from_none], self.values)
        return result


class PutAccountsAccountIDEnvKeyBody:
    """Secret values are only readable by code running on Netlify’s systems.  With secrets, only
    the local development context values are readable from the UI, API, and CLI. By default,
    environment variable values are not secret. (Enterprise plans only)
    """
    is_secret: Optional[bool]
    """The existing or new name of the key, if you wish to rename it (case-sensitive)"""
    key: Optional[str]
    """The scopes that this environment variable is set to (Pro plans and above)"""
    scopes: Optional[List[Scope]]
    values: Optional[List[EnvVarValue]]

    def __init__(self, is_secret: Optional[bool], key: Optional[str], scopes: Optional[List[Scope]], values: Optional[List[EnvVarValue]]) -> None:
        self.is_secret = is_secret
        self.key = key
        self.scopes = scopes
        self.values = values

    @staticmethod
    def from_dict(obj: Any) -> 'PutAccountsAccountIDEnvKeyBody':
        assert isinstance(obj, dict)
        is_secret = from_union([from_bool, from_none], obj.get("is_secret"))
        key = from_union([from_str, from_none], obj.get("key"))
        scopes = from_union([lambda x: from_list(Scope, x), from_none], obj.get("scopes"))
        values = from_union([lambda x: from_list(EnvVarValue.from_dict, x), from_none], obj.get("values"))
        return PutAccountsAccountIDEnvKeyBody(is_secret, key, scopes, values)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.is_secret is not None:
            result["is_secret"] = from_union([from_bool, from_none], self.is_secret)
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.scopes is not None:
            result["scopes"] = from_union([lambda x: from_list(lambda x: to_enum(Scope, x), x), from_none], self.scopes)
        if self.values is not None:
            result["values"] = from_union([lambda x: from_list(lambda x: to_class(EnvVarValue, x), x), from_none], self.values)
        return result


class AccessToken:
    access_token: Optional[str]
    created_at: Optional[str]
    id: Optional[str]
    user_email: Optional[str]
    user_id: Optional[str]

    def __init__(self, access_token: Optional[str], created_at: Optional[str], id: Optional[str], user_email: Optional[str], user_id: Optional[str]) -> None:
        self.access_token = access_token
        self.created_at = created_at
        self.id = id
        self.user_email = user_email
        self.user_id = user_id

    @staticmethod
    def from_dict(obj: Any) -> 'AccessToken':
        assert isinstance(obj, dict)
        access_token = from_union([from_str, from_none], obj.get("access_token"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        id = from_union([from_str, from_none], obj.get("id"))
        user_email = from_union([from_str, from_none], obj.get("user_email"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        return AccessToken(access_token, created_at, id, user_email, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.access_token is not None:
            result["access_token"] = from_union([from_str, from_none], self.access_token)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.user_email is not None:
            result["user_email"] = from_union([from_str, from_none], self.user_email)
        if self.user_id is not None:
            result["user_id"] = from_union([from_str, from_none], self.user_id)
        return result


class Role(Enum):
    COLLABORATOR = "Collaborator"
    CONTROLLER = "Controller"
    OWNER = "Owner"


class AccountAddMemberSetup:
    email: Optional[str]
    role: Optional[Role]

    def __init__(self, email: Optional[str], role: Optional[Role]) -> None:
        self.email = email
        self.role = role

    @staticmethod
    def from_dict(obj: Any) -> 'AccountAddMemberSetup':
        assert isinstance(obj, dict)
        email = from_union([from_str, from_none], obj.get("email"))
        role = from_union([Role, from_none], obj.get("role"))
        return AccountAddMemberSetup(email, role)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.role is not None:
            result["role"] = from_union([lambda x: to_enum(Role, x), from_none], self.role)
        return result


class AccountUsageCapability:
    included: Optional[int]
    used: Optional[int]

    def __init__(self, included: Optional[int], used: Optional[int]) -> None:
        self.included = included
        self.used = used

    @staticmethod
    def from_dict(obj: Any) -> 'AccountUsageCapability':
        assert isinstance(obj, dict)
        included = from_union([from_int, from_none], obj.get("included"))
        used = from_union([from_int, from_none], obj.get("used"))
        return AccountUsageCapability(included, used)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.included is not None:
            result["included"] = from_union([from_int, from_none], self.included)
        if self.used is not None:
            result["used"] = from_union([from_int, from_none], self.used)
        return result


class AccountMembershipCapabilities:
    collaborators: Optional[AccountUsageCapability]
    sites: Optional[AccountUsageCapability]

    def __init__(self, collaborators: Optional[AccountUsageCapability], sites: Optional[AccountUsageCapability]) -> None:
        self.collaborators = collaborators
        self.sites = sites

    @staticmethod
    def from_dict(obj: Any) -> 'AccountMembershipCapabilities':
        assert isinstance(obj, dict)
        collaborators = from_union([AccountUsageCapability.from_dict, from_none], obj.get("collaborators"))
        sites = from_union([AccountUsageCapability.from_dict, from_none], obj.get("sites"))
        return AccountMembershipCapabilities(collaborators, sites)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.collaborators is not None:
            result["collaborators"] = from_union([lambda x: to_class(AccountUsageCapability, x), from_none], self.collaborators)
        if self.sites is not None:
            result["sites"] = from_union([lambda x: to_class(AccountUsageCapability, x), from_none], self.sites)
        return result


class AccountMembership:
    billing_details: Optional[str]
    billing_email: Optional[str]
    billing_name: Optional[str]
    billing_period: Optional[str]
    capabilities: Optional[AccountMembershipCapabilities]
    created_at: Optional[str]
    id: Optional[str]
    name: Optional[str]
    owner_ids: Optional[List[str]]
    payment_method_id: Optional[str]
    roles_allowed: Optional[List[str]]
    slug: Optional[str]
    type: Optional[str]
    type_id: Optional[str]
    type_name: Optional[str]
    updated_at: Optional[str]

    def __init__(self, billing_details: Optional[str], billing_email: Optional[str], billing_name: Optional[str], billing_period: Optional[str], capabilities: Optional[AccountMembershipCapabilities], created_at: Optional[str], id: Optional[str], name: Optional[str], owner_ids: Optional[List[str]], payment_method_id: Optional[str], roles_allowed: Optional[List[str]], slug: Optional[str], type: Optional[str], type_id: Optional[str], type_name: Optional[str], updated_at: Optional[str]) -> None:
        self.billing_details = billing_details
        self.billing_email = billing_email
        self.billing_name = billing_name
        self.billing_period = billing_period
        self.capabilities = capabilities
        self.created_at = created_at
        self.id = id
        self.name = name
        self.owner_ids = owner_ids
        self.payment_method_id = payment_method_id
        self.roles_allowed = roles_allowed
        self.slug = slug
        self.type = type
        self.type_id = type_id
        self.type_name = type_name
        self.updated_at = updated_at

    @staticmethod
    def from_dict(obj: Any) -> 'AccountMembership':
        assert isinstance(obj, dict)
        billing_details = from_union([from_str, from_none], obj.get("billing_details"))
        billing_email = from_union([from_str, from_none], obj.get("billing_email"))
        billing_name = from_union([from_str, from_none], obj.get("billing_name"))
        billing_period = from_union([from_str, from_none], obj.get("billing_period"))
        capabilities = from_union([AccountMembershipCapabilities.from_dict, from_none], obj.get("capabilities"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        owner_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("owner_ids"))
        payment_method_id = from_union([from_str, from_none], obj.get("payment_method_id"))
        roles_allowed = from_union([lambda x: from_list(from_str, x), from_none], obj.get("roles_allowed"))
        slug = from_union([from_str, from_none], obj.get("slug"))
        type = from_union([from_str, from_none], obj.get("type"))
        type_id = from_union([from_str, from_none], obj.get("type_id"))
        type_name = from_union([from_str, from_none], obj.get("type_name"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        return AccountMembership(billing_details, billing_email, billing_name, billing_period, capabilities, created_at, id, name, owner_ids, payment_method_id, roles_allowed, slug, type, type_id, type_name, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.billing_details is not None:
            result["billing_details"] = from_union([from_str, from_none], self.billing_details)
        if self.billing_email is not None:
            result["billing_email"] = from_union([from_str, from_none], self.billing_email)
        if self.billing_name is not None:
            result["billing_name"] = from_union([from_str, from_none], self.billing_name)
        if self.billing_period is not None:
            result["billing_period"] = from_union([from_str, from_none], self.billing_period)
        if self.capabilities is not None:
            result["capabilities"] = from_union([lambda x: to_class(AccountMembershipCapabilities, x), from_none], self.capabilities)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.owner_ids is not None:
            result["owner_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.owner_ids)
        if self.payment_method_id is not None:
            result["payment_method_id"] = from_union([from_str, from_none], self.payment_method_id)
        if self.roles_allowed is not None:
            result["roles_allowed"] = from_union([lambda x: from_list(from_str, x), from_none], self.roles_allowed)
        if self.slug is not None:
            result["slug"] = from_union([from_str, from_none], self.slug)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.type_id is not None:
            result["type_id"] = from_union([from_str, from_none], self.type_id)
        if self.type_name is not None:
            result["type_name"] = from_union([from_str, from_none], self.type_name)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        return result


class Period(Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"


class AccountSetup:
    extra_seats_block: Optional[int]
    name: str
    payment_method_id: Optional[str]
    period: Optional[Period]
    type_id: str

    def __init__(self, extra_seats_block: Optional[int], name: str, payment_method_id: Optional[str], period: Optional[Period], type_id: str) -> None:
        self.extra_seats_block = extra_seats_block
        self.name = name
        self.payment_method_id = payment_method_id
        self.period = period
        self.type_id = type_id

    @staticmethod
    def from_dict(obj: Any) -> 'AccountSetup':
        assert isinstance(obj, dict)
        extra_seats_block = from_union([from_int, from_none], obj.get("extra_seats_block"))
        name = from_str(obj.get("name"))
        payment_method_id = from_union([from_str, from_none], obj.get("payment_method_id"))
        period = from_union([Period, from_none], obj.get("period"))
        type_id = from_str(obj.get("type_id"))
        return AccountSetup(extra_seats_block, name, payment_method_id, period, type_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.extra_seats_block is not None:
            result["extra_seats_block"] = from_union([from_int, from_none], self.extra_seats_block)
        result["name"] = from_str(self.name)
        if self.payment_method_id is not None:
            result["payment_method_id"] = from_union([from_str, from_none], self.payment_method_id)
        if self.period is not None:
            result["period"] = from_union([lambda x: to_enum(Period, x), from_none], self.period)
        result["type_id"] = from_str(self.type_id)
        return result


class AccountType:
    capabilities: Any
    description: Optional[str]
    id: Optional[str]
    monthly_dollar_price: Optional[int]
    monthly_seats_addon_dollar_price: Optional[int]
    name: Optional[str]
    yearly_dollar_price: Optional[int]
    yearly_seats_addon_dollar_price: Optional[int]

    def __init__(self, capabilities: Any, description: Optional[str], id: Optional[str], monthly_dollar_price: Optional[int], monthly_seats_addon_dollar_price: Optional[int], name: Optional[str], yearly_dollar_price: Optional[int], yearly_seats_addon_dollar_price: Optional[int]) -> None:
        self.capabilities = capabilities
        self.description = description
        self.id = id
        self.monthly_dollar_price = monthly_dollar_price
        self.monthly_seats_addon_dollar_price = monthly_seats_addon_dollar_price
        self.name = name
        self.yearly_dollar_price = yearly_dollar_price
        self.yearly_seats_addon_dollar_price = yearly_seats_addon_dollar_price

    @staticmethod
    def from_dict(obj: Any) -> 'AccountType':
        assert isinstance(obj, dict)
        capabilities = obj.get("capabilities")
        description = from_union([from_str, from_none], obj.get("description"))
        id = from_union([from_str, from_none], obj.get("id"))
        monthly_dollar_price = from_union([from_int, from_none], obj.get("monthly_dollar_price"))
        monthly_seats_addon_dollar_price = from_union([from_int, from_none], obj.get("monthly_seats_addon_dollar_price"))
        name = from_union([from_str, from_none], obj.get("name"))
        yearly_dollar_price = from_union([from_int, from_none], obj.get("yearly_dollar_price"))
        yearly_seats_addon_dollar_price = from_union([from_int, from_none], obj.get("yearly_seats_addon_dollar_price"))
        return AccountType(capabilities, description, id, monthly_dollar_price, monthly_seats_addon_dollar_price, name, yearly_dollar_price, yearly_seats_addon_dollar_price)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.capabilities is not None:
            result["capabilities"] = self.capabilities
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.monthly_dollar_price is not None:
            result["monthly_dollar_price"] = from_union([from_int, from_none], self.monthly_dollar_price)
        if self.monthly_seats_addon_dollar_price is not None:
            result["monthly_seats_addon_dollar_price"] = from_union([from_int, from_none], self.monthly_seats_addon_dollar_price)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.yearly_dollar_price is not None:
            result["yearly_dollar_price"] = from_union([from_int, from_none], self.yearly_dollar_price)
        if self.yearly_seats_addon_dollar_price is not None:
            result["yearly_seats_addon_dollar_price"] = from_union([from_int, from_none], self.yearly_seats_addon_dollar_price)
        return result


class SiteAccess(Enum):
    ALL = "all"
    NONE = "none"
    SELECTED = "selected"


class AccountUpdateMemberSetup:
    role: Optional[Role]
    site_access: Optional[SiteAccess]
    site_ids: Optional[List[str]]

    def __init__(self, role: Optional[Role], site_access: Optional[SiteAccess], site_ids: Optional[List[str]]) -> None:
        self.role = role
        self.site_access = site_access
        self.site_ids = site_ids

    @staticmethod
    def from_dict(obj: Any) -> 'AccountUpdateMemberSetup':
        assert isinstance(obj, dict)
        role = from_union([Role, from_none], obj.get("role"))
        site_access = from_union([SiteAccess, from_none], obj.get("site_access"))
        site_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("site_ids"))
        return AccountUpdateMemberSetup(role, site_access, site_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.role is not None:
            result["role"] = from_union([lambda x: to_enum(Role, x), from_none], self.role)
        if self.site_access is not None:
            result["site_access"] = from_union([lambda x: to_enum(SiteAccess, x), from_none], self.site_access)
        if self.site_ids is not None:
            result["site_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.site_ids)
        return result


class AccountUpdateSetup:
    billing_details: Optional[str]
    billing_email: Optional[str]
    billing_name: Optional[str]
    extra_seats_block: Optional[int]
    name: Optional[str]
    slug: Optional[str]
    type_id: Optional[str]

    def __init__(self, billing_details: Optional[str], billing_email: Optional[str], billing_name: Optional[str], extra_seats_block: Optional[int], name: Optional[str], slug: Optional[str], type_id: Optional[str]) -> None:
        self.billing_details = billing_details
        self.billing_email = billing_email
        self.billing_name = billing_name
        self.extra_seats_block = extra_seats_block
        self.name = name
        self.slug = slug
        self.type_id = type_id

    @staticmethod
    def from_dict(obj: Any) -> 'AccountUpdateSetup':
        assert isinstance(obj, dict)
        billing_details = from_union([from_str, from_none], obj.get("billing_details"))
        billing_email = from_union([from_str, from_none], obj.get("billing_email"))
        billing_name = from_union([from_str, from_none], obj.get("billing_name"))
        extra_seats_block = from_union([from_int, from_none], obj.get("extra_seats_block"))
        name = from_union([from_str, from_none], obj.get("name"))
        slug = from_union([from_str, from_none], obj.get("slug"))
        type_id = from_union([from_str, from_none], obj.get("type_id"))
        return AccountUpdateSetup(billing_details, billing_email, billing_name, extra_seats_block, name, slug, type_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.billing_details is not None:
            result["billing_details"] = from_union([from_str, from_none], self.billing_details)
        if self.billing_email is not None:
            result["billing_email"] = from_union([from_str, from_none], self.billing_email)
        if self.billing_name is not None:
            result["billing_name"] = from_union([from_str, from_none], self.billing_name)
        if self.extra_seats_block is not None:
            result["extra_seats_block"] = from_union([from_int, from_none], self.extra_seats_block)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.slug is not None:
            result["slug"] = from_union([from_str, from_none], self.slug)
        if self.type_id is not None:
            result["type_id"] = from_union([from_str, from_none], self.type_id)
        return result


class AssetPublicSignature:
    url: Optional[str]

    def __init__(self, url: Optional[str]) -> None:
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'AssetPublicSignature':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        return AssetPublicSignature(url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class Asset:
    content_type: Optional[str]
    created_at: Optional[str]
    creator_id: Optional[str]
    id: Optional[str]
    key: Optional[str]
    name: Optional[str]
    site_id: Optional[str]
    size: Optional[int]
    state: Optional[str]
    updated_at: Optional[str]
    url: Optional[str]
    visibility: Optional[str]

    def __init__(self, content_type: Optional[str], created_at: Optional[str], creator_id: Optional[str], id: Optional[str], key: Optional[str], name: Optional[str], site_id: Optional[str], size: Optional[int], state: Optional[str], updated_at: Optional[str], url: Optional[str], visibility: Optional[str]) -> None:
        self.content_type = content_type
        self.created_at = created_at
        self.creator_id = creator_id
        self.id = id
        self.key = key
        self.name = name
        self.site_id = site_id
        self.size = size
        self.state = state
        self.updated_at = updated_at
        self.url = url
        self.visibility = visibility

    @staticmethod
    def from_dict(obj: Any) -> 'Asset':
        assert isinstance(obj, dict)
        content_type = from_union([from_str, from_none], obj.get("content_type"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        creator_id = from_union([from_str, from_none], obj.get("creator_id"))
        id = from_union([from_str, from_none], obj.get("id"))
        key = from_union([from_str, from_none], obj.get("key"))
        name = from_union([from_str, from_none], obj.get("name"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        size = from_union([from_int, from_none], obj.get("size"))
        state = from_union([from_str, from_none], obj.get("state"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        url = from_union([from_str, from_none], obj.get("url"))
        visibility = from_union([from_str, from_none], obj.get("visibility"))
        return Asset(content_type, created_at, creator_id, id, key, name, site_id, size, state, updated_at, url, visibility)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.content_type is not None:
            result["content_type"] = from_union([from_str, from_none], self.content_type)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.creator_id is not None:
            result["creator_id"] = from_union([from_str, from_none], self.creator_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.size is not None:
            result["size"] = from_union([from_int, from_none], self.size)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.visibility is not None:
            result["visibility"] = from_union([from_str, from_none], self.visibility)
        return result


class AssetForm:
    fields: Any
    url: Optional[str]

    def __init__(self, fields: Any, url: Optional[str]) -> None:
        self.fields = fields
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'AssetForm':
        assert isinstance(obj, dict)
        fields = obj.get("fields")
        url = from_union([from_str, from_none], obj.get("url"))
        return AssetForm(fields, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.fields is not None:
            result["fields"] = self.fields
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class AssetSignature:
    asset: Optional[Asset]
    form: Optional[AssetForm]

    def __init__(self, asset: Optional[Asset], form: Optional[AssetForm]) -> None:
        self.asset = asset
        self.form = form

    @staticmethod
    def from_dict(obj: Any) -> 'AssetSignature':
        assert isinstance(obj, dict)
        asset = from_union([Asset.from_dict, from_none], obj.get("asset"))
        form = from_union([AssetForm.from_dict, from_none], obj.get("form"))
        return AssetSignature(asset, form)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.asset is not None:
            result["asset"] = from_union([lambda x: to_class(Asset, x), from_none], self.asset)
        if self.form is not None:
            result["form"] = from_union([lambda x: to_class(AssetForm, x), from_none], self.form)
        return result


class AuditLogPayload:
    action: Optional[str]
    actor_email: Optional[str]
    actor_id: Optional[str]
    actor_name: Optional[str]
    log_type: Optional[str]
    timestamp: Optional[str]

    def __init__(self, action: Optional[str], actor_email: Optional[str], actor_id: Optional[str], actor_name: Optional[str], log_type: Optional[str], timestamp: Optional[str]) -> None:
        self.action = action
        self.actor_email = actor_email
        self.actor_id = actor_id
        self.actor_name = actor_name
        self.log_type = log_type
        self.timestamp = timestamp

    @staticmethod
    def from_dict(obj: Any) -> 'AuditLogPayload':
        assert isinstance(obj, dict)
        action = from_union([from_str, from_none], obj.get("action"))
        actor_email = from_union([from_str, from_none], obj.get("actor_email"))
        actor_id = from_union([from_str, from_none], obj.get("actor_id"))
        actor_name = from_union([from_str, from_none], obj.get("actor_name"))
        log_type = from_union([from_str, from_none], obj.get("log_type"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        return AuditLogPayload(action, actor_email, actor_id, actor_name, log_type, timestamp)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.action is not None:
            result["action"] = from_union([from_str, from_none], self.action)
        if self.actor_email is not None:
            result["actor_email"] = from_union([from_str, from_none], self.actor_email)
        if self.actor_id is not None:
            result["actor_id"] = from_union([from_str, from_none], self.actor_id)
        if self.actor_name is not None:
            result["actor_name"] = from_union([from_str, from_none], self.actor_name)
        if self.log_type is not None:
            result["log_type"] = from_union([from_str, from_none], self.log_type)
        if self.timestamp is not None:
            result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        return result


class AuditLog:
    account_id: Optional[str]
    id: Optional[str]
    payload: Optional[AuditLogPayload]

    def __init__(self, account_id: Optional[str], id: Optional[str], payload: Optional[AuditLogPayload]) -> None:
        self.account_id = account_id
        self.id = id
        self.payload = payload

    @staticmethod
    def from_dict(obj: Any) -> 'AuditLog':
        assert isinstance(obj, dict)
        account_id = from_union([from_str, from_none], obj.get("account_id"))
        id = from_union([from_str, from_none], obj.get("id"))
        payload = from_union([AuditLogPayload.from_dict, from_none], obj.get("payload"))
        return AuditLog(account_id, id, payload)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account_id is not None:
            result["account_id"] = from_union([from_str, from_none], self.account_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.payload is not None:
            result["payload"] = from_union([lambda x: to_class(AuditLogPayload, x), from_none], self.payload)
        return result


class Build:
    created_at: Optional[str]
    deploy_id: Optional[str]
    done: Optional[bool]
    error: Optional[str]
    id: Optional[str]
    sha: Optional[str]

    def __init__(self, created_at: Optional[str], deploy_id: Optional[str], done: Optional[bool], error: Optional[str], id: Optional[str], sha: Optional[str]) -> None:
        self.created_at = created_at
        self.deploy_id = deploy_id
        self.done = done
        self.error = error
        self.id = id
        self.sha = sha

    @staticmethod
    def from_dict(obj: Any) -> 'Build':
        assert isinstance(obj, dict)
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        deploy_id = from_union([from_str, from_none], obj.get("deploy_id"))
        done = from_union([from_bool, from_none], obj.get("done"))
        error = from_union([from_str, from_none], obj.get("error"))
        id = from_union([from_str, from_none], obj.get("id"))
        sha = from_union([from_str, from_none], obj.get("sha"))
        return Build(created_at, deploy_id, done, error, id, sha)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.deploy_id is not None:
            result["deploy_id"] = from_union([from_str, from_none], self.deploy_id)
        if self.done is not None:
            result["done"] = from_union([from_bool, from_none], self.done)
        if self.error is not None:
            result["error"] = from_union([from_str, from_none], self.error)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.sha is not None:
            result["sha"] = from_union([from_str, from_none], self.sha)
        return result


class BuildHook:
    branch: Optional[str]
    created_at: Optional[str]
    id: Optional[str]
    site_id: Optional[str]
    title: Optional[str]
    url: Optional[str]

    def __init__(self, branch: Optional[str], created_at: Optional[str], id: Optional[str], site_id: Optional[str], title: Optional[str], url: Optional[str]) -> None:
        self.branch = branch
        self.created_at = created_at
        self.id = id
        self.site_id = site_id
        self.title = title
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'BuildHook':
        assert isinstance(obj, dict)
        branch = from_union([from_str, from_none], obj.get("branch"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        id = from_union([from_str, from_none], obj.get("id"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        url = from_union([from_str, from_none], obj.get("url"))
        return BuildHook(branch, created_at, id, site_id, title, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.branch is not None:
            result["branch"] = from_union([from_str, from_none], self.branch)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class BuildHookSetup:
    branch: Optional[str]
    title: Optional[str]

    def __init__(self, branch: Optional[str], title: Optional[str]) -> None:
        self.branch = branch
        self.title = title

    @staticmethod
    def from_dict(obj: Any) -> 'BuildHookSetup':
        assert isinstance(obj, dict)
        branch = from_union([from_str, from_none], obj.get("branch"))
        title = from_union([from_str, from_none], obj.get("title"))
        return BuildHookSetup(branch, title)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.branch is not None:
            result["branch"] = from_union([from_str, from_none], self.branch)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        return result


class Section(Enum):
    BUILDING = "building"
    CLEANUP = "cleanup"
    DEPLOYING = "deploying"
    INITIALIZING = "initializing"
    POSTPROCESSING = "postprocessing"


class BuildLogMsg:
    error: Optional[bool]
    message: Optional[str]
    section: Optional[Section]

    def __init__(self, error: Optional[bool], message: Optional[str], section: Optional[Section]) -> None:
        self.error = error
        self.message = message
        self.section = section

    @staticmethod
    def from_dict(obj: Any) -> 'BuildLogMsg':
        assert isinstance(obj, dict)
        error = from_union([from_bool, from_none], obj.get("error"))
        message = from_union([from_str, from_none], obj.get("message"))
        section = from_union([Section, from_none], obj.get("section"))
        return BuildLogMsg(error, message, section)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.error is not None:
            result["error"] = from_union([from_bool, from_none], self.error)
        if self.message is not None:
            result["message"] = from_union([from_str, from_none], self.message)
        if self.section is not None:
            result["section"] = from_union([lambda x: to_enum(Section, x), from_none], self.section)
        return result


class BuildSetup:
    clear_cache: Optional[bool]
    image: Optional[str]

    def __init__(self, clear_cache: Optional[bool], image: Optional[str]) -> None:
        self.clear_cache = clear_cache
        self.image = image

    @staticmethod
    def from_dict(obj: Any) -> 'BuildSetup':
        assert isinstance(obj, dict)
        clear_cache = from_union([from_bool, from_none], obj.get("clear_cache"))
        image = from_union([from_str, from_none], obj.get("image"))
        return BuildSetup(clear_cache, image)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.clear_cache is not None:
            result["clear_cache"] = from_union([from_bool, from_none], self.clear_cache)
        if self.image is not None:
            result["image"] = from_union([from_str, from_none], self.image)
        return result


class BuildStatusMinutes:
    current: Optional[int]
    current_average_sec: Optional[int]
    included_minutes: Optional[str]
    included_minutes_with_packs: Optional[str]
    last_updated_at: Optional[str]
    period_end_date: Optional[str]
    period_start_date: Optional[str]
    previous: Optional[int]

    def __init__(self, current: Optional[int], current_average_sec: Optional[int], included_minutes: Optional[str], included_minutes_with_packs: Optional[str], last_updated_at: Optional[str], period_end_date: Optional[str], period_start_date: Optional[str], previous: Optional[int]) -> None:
        self.current = current
        self.current_average_sec = current_average_sec
        self.included_minutes = included_minutes
        self.included_minutes_with_packs = included_minutes_with_packs
        self.last_updated_at = last_updated_at
        self.period_end_date = period_end_date
        self.period_start_date = period_start_date
        self.previous = previous

    @staticmethod
    def from_dict(obj: Any) -> 'BuildStatusMinutes':
        assert isinstance(obj, dict)
        current = from_union([from_int, from_none], obj.get("current"))
        current_average_sec = from_union([from_int, from_none], obj.get("current_average_sec"))
        included_minutes = from_union([from_str, from_none], obj.get("included_minutes"))
        included_minutes_with_packs = from_union([from_str, from_none], obj.get("included_minutes_with_packs"))
        last_updated_at = from_union([from_str, from_none], obj.get("last_updated_at"))
        period_end_date = from_union([from_str, from_none], obj.get("period_end_date"))
        period_start_date = from_union([from_str, from_none], obj.get("period_start_date"))
        previous = from_union([from_int, from_none], obj.get("previous"))
        return BuildStatusMinutes(current, current_average_sec, included_minutes, included_minutes_with_packs, last_updated_at, period_end_date, period_start_date, previous)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.current is not None:
            result["current"] = from_union([from_int, from_none], self.current)
        if self.current_average_sec is not None:
            result["current_average_sec"] = from_union([from_int, from_none], self.current_average_sec)
        if self.included_minutes is not None:
            result["included_minutes"] = from_union([from_str, from_none], self.included_minutes)
        if self.included_minutes_with_packs is not None:
            result["included_minutes_with_packs"] = from_union([from_str, from_none], self.included_minutes_with_packs)
        if self.last_updated_at is not None:
            result["last_updated_at"] = from_union([from_str, from_none], self.last_updated_at)
        if self.period_end_date is not None:
            result["period_end_date"] = from_union([from_str, from_none], self.period_end_date)
        if self.period_start_date is not None:
            result["period_start_date"] = from_union([from_str, from_none], self.period_start_date)
        if self.previous is not None:
            result["previous"] = from_union([from_int, from_none], self.previous)
        return result


class BuildStatus:
    active: Optional[int]
    build_count: Optional[int]
    enqueued: Optional[int]
    minutes: Optional[BuildStatusMinutes]
    pending_concurrency: Optional[int]

    def __init__(self, active: Optional[int], build_count: Optional[int], enqueued: Optional[int], minutes: Optional[BuildStatusMinutes], pending_concurrency: Optional[int]) -> None:
        self.active = active
        self.build_count = build_count
        self.enqueued = enqueued
        self.minutes = minutes
        self.pending_concurrency = pending_concurrency

    @staticmethod
    def from_dict(obj: Any) -> 'BuildStatus':
        assert isinstance(obj, dict)
        active = from_union([from_int, from_none], obj.get("active"))
        build_count = from_union([from_int, from_none], obj.get("build_count"))
        enqueued = from_union([from_int, from_none], obj.get("enqueued"))
        minutes = from_union([BuildStatusMinutes.from_dict, from_none], obj.get("minutes"))
        pending_concurrency = from_union([from_int, from_none], obj.get("pending_concurrency"))
        return BuildStatus(active, build_count, enqueued, minutes, pending_concurrency)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.active is not None:
            result["active"] = from_union([from_int, from_none], self.active)
        if self.build_count is not None:
            result["build_count"] = from_union([from_int, from_none], self.build_count)
        if self.enqueued is not None:
            result["enqueued"] = from_union([from_int, from_none], self.enqueued)
        if self.minutes is not None:
            result["minutes"] = from_union([lambda x: to_class(BuildStatusMinutes, x), from_none], self.minutes)
        if self.pending_concurrency is not None:
            result["pending_concurrency"] = from_union([from_int, from_none], self.pending_concurrency)
        return result


class FunctionSchedule:
    cron: Optional[str]
    name: Optional[str]

    def __init__(self, cron: Optional[str], name: Optional[str]) -> None:
        self.cron = cron
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'FunctionSchedule':
        assert isinstance(obj, dict)
        cron = from_union([from_str, from_none], obj.get("cron"))
        name = from_union([from_str, from_none], obj.get("name"))
        return FunctionSchedule(cron, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.cron is not None:
            result["cron"] = from_union([from_str, from_none], self.cron)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


class DeployFiles:
    deploy_files_async: Optional[bool]
    branch: Optional[str]
    draft: Optional[bool]
    files: Any
    framework: Optional[str]
    function_schedules: Optional[List[FunctionSchedule]]
    functions: Any
    functions_config: Any

    def __init__(self, deploy_files_async: Optional[bool], branch: Optional[str], draft: Optional[bool], files: Any, framework: Optional[str], function_schedules: Optional[List[FunctionSchedule]], functions: Any, functions_config: Any) -> None:
        self.deploy_files_async = deploy_files_async
        self.branch = branch
        self.draft = draft
        self.files = files
        self.framework = framework
        self.function_schedules = function_schedules
        self.functions = functions
        self.functions_config = functions_config

    @staticmethod
    def from_dict(obj: Any) -> 'DeployFiles':
        assert isinstance(obj, dict)
        deploy_files_async = from_union([from_bool, from_none], obj.get("async"))
        branch = from_union([from_str, from_none], obj.get("branch"))
        draft = from_union([from_bool, from_none], obj.get("draft"))
        files = obj.get("files")
        framework = from_union([from_str, from_none], obj.get("framework"))
        function_schedules = from_union([lambda x: from_list(FunctionSchedule.from_dict, x), from_none], obj.get("function_schedules"))
        functions = obj.get("functions")
        functions_config = obj.get("functions_config")
        return DeployFiles(deploy_files_async, branch, draft, files, framework, function_schedules, functions, functions_config)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.deploy_files_async is not None:
            result["async"] = from_union([from_bool, from_none], self.deploy_files_async)
        if self.branch is not None:
            result["branch"] = from_union([from_str, from_none], self.branch)
        if self.draft is not None:
            result["draft"] = from_union([from_bool, from_none], self.draft)
        if self.files is not None:
            result["files"] = self.files
        if self.framework is not None:
            result["framework"] = from_union([from_str, from_none], self.framework)
        if self.function_schedules is not None:
            result["function_schedules"] = from_union([lambda x: from_list(lambda x: to_class(FunctionSchedule, x), x), from_none], self.function_schedules)
        if self.functions is not None:
            result["functions"] = self.functions
        if self.functions_config is not None:
            result["functions_config"] = self.functions_config
        return result


class DeployKey:
    created_at: Optional[str]
    id: Optional[str]
    public_key: Optional[str]

    def __init__(self, created_at: Optional[str], id: Optional[str], public_key: Optional[str]) -> None:
        self.created_at = created_at
        self.id = id
        self.public_key = public_key

    @staticmethod
    def from_dict(obj: Any) -> 'DeployKey':
        assert isinstance(obj, dict)
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        id = from_union([from_str, from_none], obj.get("id"))
        public_key = from_union([from_str, from_none], obj.get("public_key"))
        return DeployKey(created_at, id, public_key)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.public_key is not None:
            result["public_key"] = from_union([from_str, from_none], self.public_key)
        return result


class DeployedBranch:
    deploy_id: Optional[str]
    id: Optional[str]
    name: Optional[str]
    slug: Optional[str]
    ssl_url: Optional[str]
    url: Optional[str]

    def __init__(self, deploy_id: Optional[str], id: Optional[str], name: Optional[str], slug: Optional[str], ssl_url: Optional[str], url: Optional[str]) -> None:
        self.deploy_id = deploy_id
        self.id = id
        self.name = name
        self.slug = slug
        self.ssl_url = ssl_url
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'DeployedBranch':
        assert isinstance(obj, dict)
        deploy_id = from_union([from_str, from_none], obj.get("deploy_id"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        slug = from_union([from_str, from_none], obj.get("slug"))
        ssl_url = from_union([from_str, from_none], obj.get("ssl_url"))
        url = from_union([from_str, from_none], obj.get("url"))
        return DeployedBranch(deploy_id, id, name, slug, ssl_url, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.deploy_id is not None:
            result["deploy_id"] = from_union([from_str, from_none], self.deploy_id)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.slug is not None:
            result["slug"] = from_union([from_str, from_none], self.slug)
        if self.ssl_url is not None:
            result["ssl_url"] = from_union([from_str, from_none], self.ssl_url)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class DNSRecordCreate:
    flag: Optional[int]
    hostname: Optional[str]
    port: Optional[int]
    priority: Optional[int]
    tag: Optional[str]
    ttl: Optional[int]
    type: Optional[str]
    value: Optional[str]
    weight: Optional[int]

    def __init__(self, flag: Optional[int], hostname: Optional[str], port: Optional[int], priority: Optional[int], tag: Optional[str], ttl: Optional[int], type: Optional[str], value: Optional[str], weight: Optional[int]) -> None:
        self.flag = flag
        self.hostname = hostname
        self.port = port
        self.priority = priority
        self.tag = tag
        self.ttl = ttl
        self.type = type
        self.value = value
        self.weight = weight

    @staticmethod
    def from_dict(obj: Any) -> 'DNSRecordCreate':
        assert isinstance(obj, dict)
        flag = from_union([from_int, from_none], obj.get("flag"))
        hostname = from_union([from_str, from_none], obj.get("hostname"))
        port = from_union([from_int, from_none], obj.get("port"))
        priority = from_union([from_int, from_none], obj.get("priority"))
        tag = from_union([from_str, from_none], obj.get("tag"))
        ttl = from_union([from_int, from_none], obj.get("ttl"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        weight = from_union([from_int, from_none], obj.get("weight"))
        return DNSRecordCreate(flag, hostname, port, priority, tag, ttl, type, value, weight)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.flag is not None:
            result["flag"] = from_union([from_int, from_none], self.flag)
        if self.hostname is not None:
            result["hostname"] = from_union([from_str, from_none], self.hostname)
        if self.port is not None:
            result["port"] = from_union([from_int, from_none], self.port)
        if self.priority is not None:
            result["priority"] = from_union([from_int, from_none], self.priority)
        if self.tag is not None:
            result["tag"] = from_union([from_str, from_none], self.tag)
        if self.ttl is not None:
            result["ttl"] = from_union([from_int, from_none], self.ttl)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        if self.weight is not None:
            result["weight"] = from_union([from_int, from_none], self.weight)
        return result


class DNSRecord:
    dns_zone_id: Optional[str]
    flag: Optional[int]
    hostname: Optional[str]
    id: Optional[str]
    managed: Optional[bool]
    priority: Optional[int]
    site_id: Optional[str]
    tag: Optional[str]
    ttl: Optional[int]
    type: Optional[str]
    value: Optional[str]

    def __init__(self, dns_zone_id: Optional[str], flag: Optional[int], hostname: Optional[str], id: Optional[str], managed: Optional[bool], priority: Optional[int], site_id: Optional[str], tag: Optional[str], ttl: Optional[int], type: Optional[str], value: Optional[str]) -> None:
        self.dns_zone_id = dns_zone_id
        self.flag = flag
        self.hostname = hostname
        self.id = id
        self.managed = managed
        self.priority = priority
        self.site_id = site_id
        self.tag = tag
        self.ttl = ttl
        self.type = type
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'DNSRecord':
        assert isinstance(obj, dict)
        dns_zone_id = from_union([from_str, from_none], obj.get("dns_zone_id"))
        flag = from_union([from_int, from_none], obj.get("flag"))
        hostname = from_union([from_str, from_none], obj.get("hostname"))
        id = from_union([from_str, from_none], obj.get("id"))
        managed = from_union([from_bool, from_none], obj.get("managed"))
        priority = from_union([from_int, from_none], obj.get("priority"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        tag = from_union([from_str, from_none], obj.get("tag"))
        ttl = from_union([from_int, from_none], obj.get("ttl"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        return DNSRecord(dns_zone_id, flag, hostname, id, managed, priority, site_id, tag, ttl, type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.dns_zone_id is not None:
            result["dns_zone_id"] = from_union([from_str, from_none], self.dns_zone_id)
        if self.flag is not None:
            result["flag"] = from_union([from_int, from_none], self.flag)
        if self.hostname is not None:
            result["hostname"] = from_union([from_str, from_none], self.hostname)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.managed is not None:
            result["managed"] = from_union([from_bool, from_none], self.managed)
        if self.priority is not None:
            result["priority"] = from_union([from_int, from_none], self.priority)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.tag is not None:
            result["tag"] = from_union([from_str, from_none], self.tag)
        if self.ttl is not None:
            result["ttl"] = from_union([from_int, from_none], self.ttl)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


class DNSZone:
    account_id: Optional[str]
    account_name: Optional[str]
    account_slug: Optional[str]
    created_at: Optional[str]
    dedicated: Optional[bool]
    dns_servers: Optional[List[str]]
    domain: Optional[str]
    errors: Optional[List[str]]
    id: Optional[str]
    ipv6_enabled: Optional[bool]
    name: Optional[str]
    records: Optional[List[DNSRecord]]
    site_id: Optional[str]
    supported_record_types: Optional[List[str]]
    updated_at: Optional[str]
    user_id: Optional[str]

    def __init__(self, account_id: Optional[str], account_name: Optional[str], account_slug: Optional[str], created_at: Optional[str], dedicated: Optional[bool], dns_servers: Optional[List[str]], domain: Optional[str], errors: Optional[List[str]], id: Optional[str], ipv6_enabled: Optional[bool], name: Optional[str], records: Optional[List[DNSRecord]], site_id: Optional[str], supported_record_types: Optional[List[str]], updated_at: Optional[str], user_id: Optional[str]) -> None:
        self.account_id = account_id
        self.account_name = account_name
        self.account_slug = account_slug
        self.created_at = created_at
        self.dedicated = dedicated
        self.dns_servers = dns_servers
        self.domain = domain
        self.errors = errors
        self.id = id
        self.ipv6_enabled = ipv6_enabled
        self.name = name
        self.records = records
        self.site_id = site_id
        self.supported_record_types = supported_record_types
        self.updated_at = updated_at
        self.user_id = user_id

    @staticmethod
    def from_dict(obj: Any) -> 'DNSZone':
        assert isinstance(obj, dict)
        account_id = from_union([from_str, from_none], obj.get("account_id"))
        account_name = from_union([from_str, from_none], obj.get("account_name"))
        account_slug = from_union([from_str, from_none], obj.get("account_slug"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        dedicated = from_union([from_bool, from_none], obj.get("dedicated"))
        dns_servers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("dns_servers"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        errors = from_union([lambda x: from_list(from_str, x), from_none], obj.get("errors"))
        id = from_union([from_str, from_none], obj.get("id"))
        ipv6_enabled = from_union([from_bool, from_none], obj.get("ipv6_enabled"))
        name = from_union([from_str, from_none], obj.get("name"))
        records = from_union([lambda x: from_list(DNSRecord.from_dict, x), from_none], obj.get("records"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        supported_record_types = from_union([lambda x: from_list(from_str, x), from_none], obj.get("supported_record_types"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        return DNSZone(account_id, account_name, account_slug, created_at, dedicated, dns_servers, domain, errors, id, ipv6_enabled, name, records, site_id, supported_record_types, updated_at, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account_id is not None:
            result["account_id"] = from_union([from_str, from_none], self.account_id)
        if self.account_name is not None:
            result["account_name"] = from_union([from_str, from_none], self.account_name)
        if self.account_slug is not None:
            result["account_slug"] = from_union([from_str, from_none], self.account_slug)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.dedicated is not None:
            result["dedicated"] = from_union([from_bool, from_none], self.dedicated)
        if self.dns_servers is not None:
            result["dns_servers"] = from_union([lambda x: from_list(from_str, x), from_none], self.dns_servers)
        if self.domain is not None:
            result["domain"] = from_union([from_str, from_none], self.domain)
        if self.errors is not None:
            result["errors"] = from_union([lambda x: from_list(from_str, x), from_none], self.errors)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.ipv6_enabled is not None:
            result["ipv6_enabled"] = from_union([from_bool, from_none], self.ipv6_enabled)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.records is not None:
            result["records"] = from_union([lambda x: from_list(lambda x: to_class(DNSRecord, x), x), from_none], self.records)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.supported_record_types is not None:
            result["supported_record_types"] = from_union([lambda x: from_list(from_str, x), from_none], self.supported_record_types)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        if self.user_id is not None:
            result["user_id"] = from_union([from_str, from_none], self.user_id)
        return result


class DNSZoneSetup:
    account_slug: Optional[str]
    name: Optional[str]
    site_id: Optional[str]

    def __init__(self, account_slug: Optional[str], name: Optional[str], site_id: Optional[str]) -> None:
        self.account_slug = account_slug
        self.name = name
        self.site_id = site_id

    @staticmethod
    def from_dict(obj: Any) -> 'DNSZoneSetup':
        assert isinstance(obj, dict)
        account_slug = from_union([from_str, from_none], obj.get("account_slug"))
        name = from_union([from_str, from_none], obj.get("name"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        return DNSZoneSetup(account_slug, name, site_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account_slug is not None:
            result["account_slug"] = from_union([from_str, from_none], self.account_slug)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        return result


class EnvVarUser:
    """A URL pointing to the user's avatar"""
    avatar_url: Optional[str]
    """The user's email address"""
    email: Optional[str]
    """The user's full name (first and last)"""
    full_name: Optional[str]
    """The user's unique identifier"""
    id: Optional[str]

    def __init__(self, avatar_url: Optional[str], email: Optional[str], full_name: Optional[str], id: Optional[str]) -> None:
        self.avatar_url = avatar_url
        self.email = email
        self.full_name = full_name
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'EnvVarUser':
        assert isinstance(obj, dict)
        avatar_url = from_union([from_str, from_none], obj.get("avatar_url"))
        email = from_union([from_str, from_none], obj.get("email"))
        full_name = from_union([from_str, from_none], obj.get("full_name"))
        id = from_union([from_str, from_none], obj.get("id"))
        return EnvVarUser(avatar_url, email, full_name, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.avatar_url is not None:
            result["avatar_url"] = from_union([from_str, from_none], self.avatar_url)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.full_name is not None:
            result["full_name"] = from_union([from_str, from_none], self.full_name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


class EnvVar:
    """Environment variable model definition"""
    """Secret values are only readable by code running on Netlify’s systems.  With secrets, only
    the local development context values are readable from the UI, API, and CLI. By default,
    environment variable values are not secret. (Enterprise plans only)
    """
    is_secret: Optional[bool]
    """The environment variable key, like ALGOLIA_ID (case-sensitive)"""
    key: Optional[str]
    """The scopes that this environment variable is set to"""
    scopes: Optional[List[Scope]]
    """The timestamp of when the value was last updated"""
    updated_at: Optional[str]
    updated_by: Optional[EnvVarUser]
    """An array of Value objects containing values and metadata"""
    values: Optional[List[EnvVarValue]]

    def __init__(self, is_secret: Optional[bool], key: Optional[str], scopes: Optional[List[Scope]], updated_at: Optional[str], updated_by: Optional[EnvVarUser], values: Optional[List[EnvVarValue]]) -> None:
        self.is_secret = is_secret
        self.key = key
        self.scopes = scopes
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.values = values

    @staticmethod
    def from_dict(obj: Any) -> 'EnvVar':
        assert isinstance(obj, dict)
        is_secret = from_union([from_bool, from_none], obj.get("is_secret"))
        key = from_union([from_str, from_none], obj.get("key"))
        scopes = from_union([lambda x: from_list(Scope, x), from_none], obj.get("scopes"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        updated_by = from_union([EnvVarUser.from_dict, from_none], obj.get("updated_by"))
        values = from_union([lambda x: from_list(EnvVarValue.from_dict, x), from_none], obj.get("values"))
        return EnvVar(is_secret, key, scopes, updated_at, updated_by, values)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.is_secret is not None:
            result["is_secret"] = from_union([from_bool, from_none], self.is_secret)
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.scopes is not None:
            result["scopes"] = from_union([lambda x: from_list(lambda x: to_enum(Scope, x), x), from_none], self.scopes)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        if self.updated_by is not None:
            result["updated_by"] = from_union([lambda x: to_class(EnvVarUser, x), from_none], self.updated_by)
        if self.values is not None:
            result["values"] = from_union([lambda x: from_list(lambda x: to_class(EnvVarValue, x), x), from_none], self.values)
        return result


class Error:
    code: Optional[int]
    message: str

    def __init__(self, code: Optional[int], message: str) -> None:
        self.code = code
        self.message = message

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        message = from_str(obj.get("message"))
        return Error(code, message)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.code is not None:
            result["code"] = from_union([from_int, from_none], self.code)
        result["message"] = from_str(self.message)
        return result


class File:
    id: Optional[str]
    mime_type: Optional[str]
    path: Optional[str]
    sha: Optional[str]
    size: Optional[int]

    def __init__(self, id: Optional[str], mime_type: Optional[str], path: Optional[str], sha: Optional[str], size: Optional[int]) -> None:
        self.id = id
        self.mime_type = mime_type
        self.path = path
        self.sha = sha
        self.size = size

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        mime_type = from_union([from_str, from_none], obj.get("mime_type"))
        path = from_union([from_str, from_none], obj.get("path"))
        sha = from_union([from_str, from_none], obj.get("sha"))
        size = from_union([from_int, from_none], obj.get("size"))
        return File(id, mime_type, path, sha, size)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.mime_type is not None:
            result["mime_type"] = from_union([from_str, from_none], self.mime_type)
        if self.path is not None:
            result["path"] = from_union([from_str, from_none], self.path)
        if self.sha is not None:
            result["sha"] = from_union([from_str, from_none], self.sha)
        if self.size is not None:
            result["size"] = from_union([from_int, from_none], self.size)
        return result


class Form:
    created_at: Optional[str]
    fields: Optional[List[Any]]
    id: Optional[str]
    name: Optional[str]
    paths: Optional[List[str]]
    site_id: Optional[str]
    submission_count: Optional[int]

    def __init__(self, created_at: Optional[str], fields: Optional[List[Any]], id: Optional[str], name: Optional[str], paths: Optional[List[str]], site_id: Optional[str], submission_count: Optional[int]) -> None:
        self.created_at = created_at
        self.fields = fields
        self.id = id
        self.name = name
        self.paths = paths
        self.site_id = site_id
        self.submission_count = submission_count

    @staticmethod
    def from_dict(obj: Any) -> 'Form':
        assert isinstance(obj, dict)
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        fields = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("fields"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        paths = from_union([lambda x: from_list(from_str, x), from_none], obj.get("paths"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        submission_count = from_union([from_int, from_none], obj.get("submission_count"))
        return Form(created_at, fields, id, name, paths, site_id, submission_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.fields is not None:
            result["fields"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.fields)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.paths is not None:
            result["paths"] = from_union([lambda x: from_list(from_str, x), from_none], self.paths)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.submission_count is not None:
            result["submission_count"] = from_union([from_int, from_none], self.submission_count)
        return result


class Function:
    id: Optional[str]
    name: Optional[str]
    sha: Optional[str]

    def __init__(self, id: Optional[str], name: Optional[str], sha: Optional[str]) -> None:
        self.id = id
        self.name = name
        self.sha = sha

    @staticmethod
    def from_dict(obj: Any) -> 'Function':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        sha = from_union([from_str, from_none], obj.get("sha"))
        return Function(id, name, sha)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.sha is not None:
            result["sha"] = from_union([from_str, from_none], self.sha)
        return result


class FunctionRoute:
    expression: Optional[str]
    literal: Optional[str]
    pattern: Optional[str]

    def __init__(self, expression: Optional[str], literal: Optional[str], pattern: Optional[str]) -> None:
        self.expression = expression
        self.literal = literal
        self.pattern = pattern

    @staticmethod
    def from_dict(obj: Any) -> 'FunctionRoute':
        assert isinstance(obj, dict)
        expression = from_union([from_str, from_none], obj.get("expression"))
        literal = from_union([from_str, from_none], obj.get("literal"))
        pattern = from_union([from_str, from_none], obj.get("pattern"))
        return FunctionRoute(expression, literal, pattern)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.expression is not None:
            result["expression"] = from_union([from_str, from_none], self.expression)
        if self.literal is not None:
            result["literal"] = from_union([from_str, from_none], self.literal)
        if self.pattern is not None:
            result["pattern"] = from_union([from_str, from_none], self.pattern)
        return result


class FunctionConfig:
    display_name: Optional[str]
    generator: Optional[str]
    routes: Optional[List[FunctionRoute]]

    def __init__(self, display_name: Optional[str], generator: Optional[str], routes: Optional[List[FunctionRoute]]) -> None:
        self.display_name = display_name
        self.generator = generator
        self.routes = routes

    @staticmethod
    def from_dict(obj: Any) -> 'FunctionConfig':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        generator = from_union([from_str, from_none], obj.get("generator"))
        routes = from_union([lambda x: from_list(FunctionRoute.from_dict, x), from_none], obj.get("routes"))
        return FunctionConfig(display_name, generator, routes)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.display_name is not None:
            result["display_name"] = from_union([from_str, from_none], self.display_name)
        if self.generator is not None:
            result["generator"] = from_union([from_str, from_none], self.generator)
        if self.routes is not None:
            result["routes"] = from_union([lambda x: from_list(lambda x: to_class(FunctionRoute, x), x), from_none], self.routes)
        return result


class Hook:
    created_at: Optional[str]
    data: Any
    disabled: Optional[bool]
    event: Optional[str]
    id: Optional[str]
    site_id: Optional[str]
    type: Optional[str]
    updated_at: Optional[str]

    def __init__(self, created_at: Optional[str], data: Any, disabled: Optional[bool], event: Optional[str], id: Optional[str], site_id: Optional[str], type: Optional[str], updated_at: Optional[str]) -> None:
        self.created_at = created_at
        self.data = data
        self.disabled = disabled
        self.event = event
        self.id = id
        self.site_id = site_id
        self.type = type
        self.updated_at = updated_at

    @staticmethod
    def from_dict(obj: Any) -> 'Hook':
        assert isinstance(obj, dict)
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        data = obj.get("data")
        disabled = from_union([from_bool, from_none], obj.get("disabled"))
        event = from_union([from_str, from_none], obj.get("event"))
        id = from_union([from_str, from_none], obj.get("id"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        return Hook(created_at, data, disabled, event, id, site_id, type, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.data is not None:
            result["data"] = self.data
        if self.disabled is not None:
            result["disabled"] = from_union([from_bool, from_none], self.disabled)
        if self.event is not None:
            result["event"] = from_union([from_str, from_none], self.event)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        return result


class HookType:
    events: Optional[List[str]]
    fields: Optional[List[Any]]
    name: Optional[str]

    def __init__(self, events: Optional[List[str]], fields: Optional[List[Any]], name: Optional[str]) -> None:
        self.events = events
        self.fields = fields
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'HookType':
        assert isinstance(obj, dict)
        events = from_union([lambda x: from_list(from_str, x), from_none], obj.get("events"))
        fields = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("fields"))
        name = from_union([from_str, from_none], obj.get("name"))
        return HookType(events, fields, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.events is not None:
            result["events"] = from_union([lambda x: from_list(from_str, x), from_none], self.events)
        if self.fields is not None:
            result["fields"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.fields)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


class Member:
    avatar: Optional[str]
    email: Optional[str]
    full_name: Optional[str]
    id: Optional[str]
    role: Optional[str]

    def __init__(self, avatar: Optional[str], email: Optional[str], full_name: Optional[str], id: Optional[str], role: Optional[str]) -> None:
        self.avatar = avatar
        self.email = email
        self.full_name = full_name
        self.id = id
        self.role = role

    @staticmethod
    def from_dict(obj: Any) -> 'Member':
        assert isinstance(obj, dict)
        avatar = from_union([from_str, from_none], obj.get("avatar"))
        email = from_union([from_str, from_none], obj.get("email"))
        full_name = from_union([from_str, from_none], obj.get("full_name"))
        id = from_union([from_str, from_none], obj.get("id"))
        role = from_union([from_str, from_none], obj.get("role"))
        return Member(avatar, email, full_name, id, role)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.avatar is not None:
            result["avatar"] = from_union([from_str, from_none], self.avatar)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.full_name is not None:
            result["full_name"] = from_union([from_str, from_none], self.full_name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.role is not None:
            result["role"] = from_union([from_str, from_none], self.role)
        return result


class PaymentMethodData:
    card_type: Optional[str]
    email: Optional[str]
    last4: Optional[str]

    def __init__(self, card_type: Optional[str], email: Optional[str], last4: Optional[str]) -> None:
        self.card_type = card_type
        self.email = email
        self.last4 = last4

    @staticmethod
    def from_dict(obj: Any) -> 'PaymentMethodData':
        assert isinstance(obj, dict)
        card_type = from_union([from_str, from_none], obj.get("card_type"))
        email = from_union([from_str, from_none], obj.get("email"))
        last4 = from_union([from_str, from_none], obj.get("last4"))
        return PaymentMethodData(card_type, email, last4)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.card_type is not None:
            result["card_type"] = from_union([from_str, from_none], self.card_type)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.last4 is not None:
            result["last4"] = from_union([from_str, from_none], self.last4)
        return result


class PaymentMethod:
    created_at: Optional[str]
    data: Optional[PaymentMethodData]
    id: Optional[str]
    method_name: Optional[str]
    state: Optional[str]
    type: Optional[str]
    updated_at: Optional[str]

    def __init__(self, created_at: Optional[str], data: Optional[PaymentMethodData], id: Optional[str], method_name: Optional[str], state: Optional[str], type: Optional[str], updated_at: Optional[str]) -> None:
        self.created_at = created_at
        self.data = data
        self.id = id
        self.method_name = method_name
        self.state = state
        self.type = type
        self.updated_at = updated_at

    @staticmethod
    def from_dict(obj: Any) -> 'PaymentMethod':
        assert isinstance(obj, dict)
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        data = from_union([PaymentMethodData.from_dict, from_none], obj.get("data"))
        id = from_union([from_str, from_none], obj.get("id"))
        method_name = from_union([from_str, from_none], obj.get("method_name"))
        state = from_union([from_str, from_none], obj.get("state"))
        type = from_union([from_str, from_none], obj.get("type"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        return PaymentMethod(created_at, data, id, method_name, state, type, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.data is not None:
            result["data"] = from_union([lambda x: to_class(PaymentMethodData, x), from_none], self.data)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.method_name is not None:
            result["method_name"] = from_union([from_str, from_none], self.method_name)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        return result


class Plugin:
    package: Optional[str]
    pinned_version: Optional[str]

    def __init__(self, package: Optional[str], pinned_version: Optional[str]) -> None:
        self.package = package
        self.pinned_version = pinned_version

    @staticmethod
    def from_dict(obj: Any) -> 'Plugin':
        assert isinstance(obj, dict)
        package = from_union([from_str, from_none], obj.get("package"))
        pinned_version = from_union([from_str, from_none], obj.get("pinned_version"))
        return Plugin(package, pinned_version)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.package is not None:
            result["package"] = from_union([from_str, from_none], self.package)
        if self.pinned_version is not None:
            result["pinned_version"] = from_union([from_str, from_none], self.pinned_version)
        return result


class PluginParams:
    pinned_version: Optional[str]

    def __init__(self, pinned_version: Optional[str]) -> None:
        self.pinned_version = pinned_version

    @staticmethod
    def from_dict(obj: Any) -> 'PluginParams':
        assert isinstance(obj, dict)
        pinned_version = from_union([from_str, from_none], obj.get("pinned_version"))
        return PluginParams(pinned_version)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.pinned_version is not None:
            result["pinned_version"] = from_union([from_str, from_none], self.pinned_version)
        return result


class PluginRunData:
    package: Optional[str]
    reporting_event: Optional[str]
    state: Optional[str]
    summary: Optional[str]
    text: Optional[str]
    title: Optional[str]
    version: Optional[str]

    def __init__(self, package: Optional[str], reporting_event: Optional[str], state: Optional[str], summary: Optional[str], text: Optional[str], title: Optional[str], version: Optional[str]) -> None:
        self.package = package
        self.reporting_event = reporting_event
        self.state = state
        self.summary = summary
        self.text = text
        self.title = title
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'PluginRunData':
        assert isinstance(obj, dict)
        package = from_union([from_str, from_none], obj.get("package"))
        reporting_event = from_union([from_str, from_none], obj.get("reporting_event"))
        state = from_union([from_str, from_none], obj.get("state"))
        summary = from_union([from_str, from_none], obj.get("summary"))
        text = from_union([from_str, from_none], obj.get("text"))
        title = from_union([from_str, from_none], obj.get("title"))
        version = from_union([from_str, from_none], obj.get("version"))
        return PluginRunData(package, reporting_event, state, summary, text, title, version)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.package is not None:
            result["package"] = from_union([from_str, from_none], self.package)
        if self.reporting_event is not None:
            result["reporting_event"] = from_union([from_str, from_none], self.reporting_event)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.summary is not None:
            result["summary"] = from_union([from_str, from_none], self.summary)
        if self.text is not None:
            result["text"] = from_union([from_str, from_none], self.text)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.version is not None:
            result["version"] = from_union([from_str, from_none], self.version)
        return result


class Service:
    created_at: Optional[str]
    description: Optional[str]
    environments: Optional[List[str]]
    events: Optional[List[Any]]
    icon: Optional[str]
    id: Optional[str]
    long_description: Optional[str]
    manifest_url: Optional[str]
    name: Optional[str]
    service_path: Optional[str]
    slug: Optional[str]
    tags: Optional[List[str]]
    updated_at: Optional[str]

    def __init__(self, created_at: Optional[str], description: Optional[str], environments: Optional[List[str]], events: Optional[List[Any]], icon: Optional[str], id: Optional[str], long_description: Optional[str], manifest_url: Optional[str], name: Optional[str], service_path: Optional[str], slug: Optional[str], tags: Optional[List[str]], updated_at: Optional[str]) -> None:
        self.created_at = created_at
        self.description = description
        self.environments = environments
        self.events = events
        self.icon = icon
        self.id = id
        self.long_description = long_description
        self.manifest_url = manifest_url
        self.name = name
        self.service_path = service_path
        self.slug = slug
        self.tags = tags
        self.updated_at = updated_at

    @staticmethod
    def from_dict(obj: Any) -> 'Service':
        assert isinstance(obj, dict)
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        description = from_union([from_str, from_none], obj.get("description"))
        environments = from_union([lambda x: from_list(from_str, x), from_none], obj.get("environments"))
        events = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("events"))
        icon = from_union([from_str, from_none], obj.get("icon"))
        id = from_union([from_str, from_none], obj.get("id"))
        long_description = from_union([from_str, from_none], obj.get("long_description"))
        manifest_url = from_union([from_str, from_none], obj.get("manifest_url"))
        name = from_union([from_str, from_none], obj.get("name"))
        service_path = from_union([from_str, from_none], obj.get("service_path"))
        slug = from_union([from_str, from_none], obj.get("slug"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tags"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        return Service(created_at, description, environments, events, icon, id, long_description, manifest_url, name, service_path, slug, tags, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.environments is not None:
            result["environments"] = from_union([lambda x: from_list(from_str, x), from_none], self.environments)
        if self.events is not None:
            result["events"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.events)
        if self.icon is not None:
            result["icon"] = from_union([from_str, from_none], self.icon)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.long_description is not None:
            result["long_description"] = from_union([from_str, from_none], self.long_description)
        if self.manifest_url is not None:
            result["manifest_url"] = from_union([from_str, from_none], self.manifest_url)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.service_path is not None:
            result["service_path"] = from_union([from_str, from_none], self.service_path)
        if self.slug is not None:
            result["slug"] = from_union([from_str, from_none], self.slug)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        return result


class ServiceInstance:
    auth_url: Optional[str]
    config: Any
    created_at: Optional[str]
    env: Any
    external_attributes: Any
    id: Optional[str]
    service_name: Optional[str]
    service_path: Optional[str]
    service_slug: Optional[str]
    snippets: Optional[List[Any]]
    updated_at: Optional[str]
    url: Optional[str]

    def __init__(self, auth_url: Optional[str], config: Any, created_at: Optional[str], env: Any, external_attributes: Any, id: Optional[str], service_name: Optional[str], service_path: Optional[str], service_slug: Optional[str], snippets: Optional[List[Any]], updated_at: Optional[str], url: Optional[str]) -> None:
        self.auth_url = auth_url
        self.config = config
        self.created_at = created_at
        self.env = env
        self.external_attributes = external_attributes
        self.id = id
        self.service_name = service_name
        self.service_path = service_path
        self.service_slug = service_slug
        self.snippets = snippets
        self.updated_at = updated_at
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceInstance':
        assert isinstance(obj, dict)
        auth_url = from_union([from_str, from_none], obj.get("auth_url"))
        config = obj.get("config")
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        env = obj.get("env")
        external_attributes = obj.get("external_attributes")
        id = from_union([from_str, from_none], obj.get("id"))
        service_name = from_union([from_str, from_none], obj.get("service_name"))
        service_path = from_union([from_str, from_none], obj.get("service_path"))
        service_slug = from_union([from_str, from_none], obj.get("service_slug"))
        snippets = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("snippets"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        url = from_union([from_str, from_none], obj.get("url"))
        return ServiceInstance(auth_url, config, created_at, env, external_attributes, id, service_name, service_path, service_slug, snippets, updated_at, url)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.auth_url is not None:
            result["auth_url"] = from_union([from_str, from_none], self.auth_url)
        if self.config is not None:
            result["config"] = self.config
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.env is not None:
            result["env"] = self.env
        if self.external_attributes is not None:
            result["external_attributes"] = self.external_attributes
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.service_name is not None:
            result["service_name"] = from_union([from_str, from_none], self.service_name)
        if self.service_path is not None:
            result["service_path"] = from_union([from_str, from_none], self.service_path)
        if self.service_slug is not None:
            result["service_slug"] = from_union([from_str, from_none], self.service_slug)
        if self.snippets is not None:
            result["snippets"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.snippets)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        return result


class RepoInfo:
    allowed_branches: Optional[List[str]]
    cmd: Optional[str]
    deploy_key_id: Optional[str]
    dir: Optional[str]
    env: Any
    functions_dir: Optional[str]
    id: Optional[int]
    installation_id: Optional[int]
    private_logs: Optional[bool]
    provider: Optional[str]
    public_repo: Optional[bool]
    repo_branch: Optional[str]
    repo_path: Optional[str]
    repo_url: Optional[str]
    stop_builds: Optional[bool]

    def __init__(self, allowed_branches: Optional[List[str]], cmd: Optional[str], deploy_key_id: Optional[str], dir: Optional[str], env: Any, functions_dir: Optional[str], id: Optional[int], installation_id: Optional[int], private_logs: Optional[bool], provider: Optional[str], public_repo: Optional[bool], repo_branch: Optional[str], repo_path: Optional[str], repo_url: Optional[str], stop_builds: Optional[bool]) -> None:
        self.allowed_branches = allowed_branches
        self.cmd = cmd
        self.deploy_key_id = deploy_key_id
        self.dir = dir
        self.env = env
        self.functions_dir = functions_dir
        self.id = id
        self.installation_id = installation_id
        self.private_logs = private_logs
        self.provider = provider
        self.public_repo = public_repo
        self.repo_branch = repo_branch
        self.repo_path = repo_path
        self.repo_url = repo_url
        self.stop_builds = stop_builds

    @staticmethod
    def from_dict(obj: Any) -> 'RepoInfo':
        assert isinstance(obj, dict)
        allowed_branches = from_union([lambda x: from_list(from_str, x), from_none], obj.get("allowed_branches"))
        cmd = from_union([from_str, from_none], obj.get("cmd"))
        deploy_key_id = from_union([from_str, from_none], obj.get("deploy_key_id"))
        dir = from_union([from_str, from_none], obj.get("dir"))
        env = obj.get("env")
        functions_dir = from_union([from_str, from_none], obj.get("functions_dir"))
        id = from_union([from_int, from_none], obj.get("id"))
        installation_id = from_union([from_int, from_none], obj.get("installation_id"))
        private_logs = from_union([from_bool, from_none], obj.get("private_logs"))
        provider = from_union([from_str, from_none], obj.get("provider"))
        public_repo = from_union([from_bool, from_none], obj.get("public_repo"))
        repo_branch = from_union([from_str, from_none], obj.get("repo_branch"))
        repo_path = from_union([from_str, from_none], obj.get("repo_path"))
        repo_url = from_union([from_str, from_none], obj.get("repo_url"))
        stop_builds = from_union([from_bool, from_none], obj.get("stop_builds"))
        return RepoInfo(allowed_branches, cmd, deploy_key_id, dir, env, functions_dir, id, installation_id, private_logs, provider, public_repo, repo_branch, repo_path, repo_url, stop_builds)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.allowed_branches is not None:
            result["allowed_branches"] = from_union([lambda x: from_list(from_str, x), from_none], self.allowed_branches)
        if self.cmd is not None:
            result["cmd"] = from_union([from_str, from_none], self.cmd)
        if self.deploy_key_id is not None:
            result["deploy_key_id"] = from_union([from_str, from_none], self.deploy_key_id)
        if self.dir is not None:
            result["dir"] = from_union([from_str, from_none], self.dir)
        if self.env is not None:
            result["env"] = self.env
        if self.functions_dir is not None:
            result["functions_dir"] = from_union([from_str, from_none], self.functions_dir)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.installation_id is not None:
            result["installation_id"] = from_union([from_int, from_none], self.installation_id)
        if self.private_logs is not None:
            result["private_logs"] = from_union([from_bool, from_none], self.private_logs)
        if self.provider is not None:
            result["provider"] = from_union([from_str, from_none], self.provider)
        if self.public_repo is not None:
            result["public_repo"] = from_union([from_bool, from_none], self.public_repo)
        if self.repo_branch is not None:
            result["repo_branch"] = from_union([from_str, from_none], self.repo_branch)
        if self.repo_path is not None:
            result["repo_path"] = from_union([from_str, from_none], self.repo_path)
        if self.repo_url is not None:
            result["repo_url"] = from_union([from_str, from_none], self.repo_url)
        if self.stop_builds is not None:
            result["stop_builds"] = from_union([from_bool, from_none], self.stop_builds)
        return result


class SiteDefaultHooksData:
    access_token: Optional[str]

    def __init__(self, access_token: Optional[str]) -> None:
        self.access_token = access_token

    @staticmethod
    def from_dict(obj: Any) -> 'SiteDefaultHooksData':
        assert isinstance(obj, dict)
        access_token = from_union([from_str, from_none], obj.get("access_token"))
        return SiteDefaultHooksData(access_token)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.access_token is not None:
            result["access_token"] = from_union([from_str, from_none], self.access_token)
        return result


class MinifyOptions:
    bundle: Optional[bool]
    minify: Optional[bool]

    def __init__(self, bundle: Optional[bool], minify: Optional[bool]) -> None:
        self.bundle = bundle
        self.minify = minify

    @staticmethod
    def from_dict(obj: Any) -> 'MinifyOptions':
        assert isinstance(obj, dict)
        bundle = from_union([from_bool, from_none], obj.get("bundle"))
        minify = from_union([from_bool, from_none], obj.get("minify"))
        return MinifyOptions(bundle, minify)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.bundle is not None:
            result["bundle"] = from_union([from_bool, from_none], self.bundle)
        if self.minify is not None:
            result["minify"] = from_union([from_bool, from_none], self.minify)
        return result


class SiteProcessingSettingsHTML:
    pretty_urls: Optional[bool]

    def __init__(self, pretty_urls: Optional[bool]) -> None:
        self.pretty_urls = pretty_urls

    @staticmethod
    def from_dict(obj: Any) -> 'SiteProcessingSettingsHTML':
        assert isinstance(obj, dict)
        pretty_urls = from_union([from_bool, from_none], obj.get("pretty_urls"))
        return SiteProcessingSettingsHTML(pretty_urls)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.pretty_urls is not None:
            result["pretty_urls"] = from_union([from_bool, from_none], self.pretty_urls)
        return result


class SiteProcessingSettingsImages:
    optimize: Optional[bool]

    def __init__(self, optimize: Optional[bool]) -> None:
        self.optimize = optimize

    @staticmethod
    def from_dict(obj: Any) -> 'SiteProcessingSettingsImages':
        assert isinstance(obj, dict)
        optimize = from_union([from_bool, from_none], obj.get("optimize"))
        return SiteProcessingSettingsImages(optimize)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.optimize is not None:
            result["optimize"] = from_union([from_bool, from_none], self.optimize)
        return result


class SiteProcessingSettings:
    css: Optional[MinifyOptions]
    html: Optional[SiteProcessingSettingsHTML]
    images: Optional[SiteProcessingSettingsImages]
    js: Optional[MinifyOptions]
    skip: Optional[bool]

    def __init__(self, css: Optional[MinifyOptions], html: Optional[SiteProcessingSettingsHTML], images: Optional[SiteProcessingSettingsImages], js: Optional[MinifyOptions], skip: Optional[bool]) -> None:
        self.css = css
        self.html = html
        self.images = images
        self.js = js
        self.skip = skip

    @staticmethod
    def from_dict(obj: Any) -> 'SiteProcessingSettings':
        assert isinstance(obj, dict)
        css = from_union([MinifyOptions.from_dict, from_none], obj.get("css"))
        html = from_union([SiteProcessingSettingsHTML.from_dict, from_none], obj.get("html"))
        images = from_union([SiteProcessingSettingsImages.from_dict, from_none], obj.get("images"))
        js = from_union([MinifyOptions.from_dict, from_none], obj.get("js"))
        skip = from_union([from_bool, from_none], obj.get("skip"))
        return SiteProcessingSettings(css, html, images, js, skip)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.css is not None:
            result["css"] = from_union([lambda x: to_class(MinifyOptions, x), from_none], self.css)
        if self.html is not None:
            result["html"] = from_union([lambda x: to_class(SiteProcessingSettingsHTML, x), from_none], self.html)
        if self.images is not None:
            result["images"] = from_union([lambda x: to_class(SiteProcessingSettingsImages, x), from_none], self.images)
        if self.js is not None:
            result["js"] = from_union([lambda x: to_class(MinifyOptions, x), from_none], self.js)
        if self.skip is not None:
            result["skip"] = from_union([from_bool, from_none], self.skip)
        return result


class DeploySiteCapabilities:
    large_media_enabled: Optional[bool]

    def __init__(self, large_media_enabled: Optional[bool]) -> None:
        self.large_media_enabled = large_media_enabled

    @staticmethod
    def from_dict(obj: Any) -> 'DeploySiteCapabilities':
        assert isinstance(obj, dict)
        large_media_enabled = from_union([from_bool, from_none], obj.get("large_media_enabled"))
        return DeploySiteCapabilities(large_media_enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.large_media_enabled is not None:
            result["large_media_enabled"] = from_union([from_bool, from_none], self.large_media_enabled)
        return result


class Deploy:
    admin_url: Optional[str]
    branch: Optional[str]
    build_id: Optional[str]
    commit_ref: Optional[str]
    commit_url: Optional[str]
    context: Optional[str]
    created_at: Optional[str]
    deploy_ssl_url: Optional[str]
    deploy_url: Optional[str]
    draft: Optional[bool]
    error_message: Optional[str]
    framework: Optional[str]
    function_schedules: Optional[List[FunctionSchedule]]
    id: Optional[str]
    locked: Optional[bool]
    name: Optional[str]
    published_at: Optional[str]
    required: Optional[List[str]]
    required_functions: Optional[List[str]]
    review_id: Optional[float]
    review_url: Optional[str]
    screenshot_url: Optional[str]
    site_capabilities: Optional[DeploySiteCapabilities]
    site_id: Optional[str]
    skipped: Optional[bool]
    ssl_url: Optional[str]
    state: Optional[str]
    title: Optional[str]
    updated_at: Optional[str]
    url: Optional[str]
    user_id: Optional[str]

    def __init__(self, admin_url: Optional[str], branch: Optional[str], build_id: Optional[str], commit_ref: Optional[str], commit_url: Optional[str], context: Optional[str], created_at: Optional[str], deploy_ssl_url: Optional[str], deploy_url: Optional[str], draft: Optional[bool], error_message: Optional[str], framework: Optional[str], function_schedules: Optional[List[FunctionSchedule]], id: Optional[str], locked: Optional[bool], name: Optional[str], published_at: Optional[str], required: Optional[List[str]], required_functions: Optional[List[str]], review_id: Optional[float], review_url: Optional[str], screenshot_url: Optional[str], site_capabilities: Optional[DeploySiteCapabilities], site_id: Optional[str], skipped: Optional[bool], ssl_url: Optional[str], state: Optional[str], title: Optional[str], updated_at: Optional[str], url: Optional[str], user_id: Optional[str]) -> None:
        self.admin_url = admin_url
        self.branch = branch
        self.build_id = build_id
        self.commit_ref = commit_ref
        self.commit_url = commit_url
        self.context = context
        self.created_at = created_at
        self.deploy_ssl_url = deploy_ssl_url
        self.deploy_url = deploy_url
        self.draft = draft
        self.error_message = error_message
        self.framework = framework
        self.function_schedules = function_schedules
        self.id = id
        self.locked = locked
        self.name = name
        self.published_at = published_at
        self.required = required
        self.required_functions = required_functions
        self.review_id = review_id
        self.review_url = review_url
        self.screenshot_url = screenshot_url
        self.site_capabilities = site_capabilities
        self.site_id = site_id
        self.skipped = skipped
        self.ssl_url = ssl_url
        self.state = state
        self.title = title
        self.updated_at = updated_at
        self.url = url
        self.user_id = user_id

    @staticmethod
    def from_dict(obj: Any) -> 'Deploy':
        assert isinstance(obj, dict)
        admin_url = from_union([from_str, from_none], obj.get("admin_url"))
        branch = from_union([from_str, from_none], obj.get("branch"))
        build_id = from_union([from_str, from_none], obj.get("build_id"))
        commit_ref = from_union([from_str, from_none], obj.get("commit_ref"))
        commit_url = from_union([from_str, from_none], obj.get("commit_url"))
        context = from_union([from_str, from_none], obj.get("context"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        deploy_ssl_url = from_union([from_str, from_none], obj.get("deploy_ssl_url"))
        deploy_url = from_union([from_str, from_none], obj.get("deploy_url"))
        draft = from_union([from_bool, from_none], obj.get("draft"))
        error_message = from_union([from_str, from_none], obj.get("error_message"))
        framework = from_union([from_str, from_none], obj.get("framework"))
        function_schedules = from_union([lambda x: from_list(FunctionSchedule.from_dict, x), from_none], obj.get("function_schedules"))
        id = from_union([from_str, from_none], obj.get("id"))
        locked = from_union([from_bool, from_none], obj.get("locked"))
        name = from_union([from_str, from_none], obj.get("name"))
        published_at = from_union([from_str, from_none], obj.get("published_at"))
        required = from_union([lambda x: from_list(from_str, x), from_none], obj.get("required"))
        required_functions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("required_functions"))
        review_id = from_union([from_float, from_none], obj.get("review_id"))
        review_url = from_union([from_str, from_none], obj.get("review_url"))
        screenshot_url = from_union([from_str, from_none], obj.get("screenshot_url"))
        site_capabilities = from_union([DeploySiteCapabilities.from_dict, from_none], obj.get("site_capabilities"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        skipped = from_union([from_bool, from_none], obj.get("skipped"))
        ssl_url = from_union([from_str, from_none], obj.get("ssl_url"))
        state = from_union([from_str, from_none], obj.get("state"))
        title = from_union([from_str, from_none], obj.get("title"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        url = from_union([from_str, from_none], obj.get("url"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        return Deploy(admin_url, branch, build_id, commit_ref, commit_url, context, created_at, deploy_ssl_url, deploy_url, draft, error_message, framework, function_schedules, id, locked, name, published_at, required, required_functions, review_id, review_url, screenshot_url, site_capabilities, site_id, skipped, ssl_url, state, title, updated_at, url, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.admin_url is not None:
            result["admin_url"] = from_union([from_str, from_none], self.admin_url)
        if self.branch is not None:
            result["branch"] = from_union([from_str, from_none], self.branch)
        if self.build_id is not None:
            result["build_id"] = from_union([from_str, from_none], self.build_id)
        if self.commit_ref is not None:
            result["commit_ref"] = from_union([from_str, from_none], self.commit_ref)
        if self.commit_url is not None:
            result["commit_url"] = from_union([from_str, from_none], self.commit_url)
        if self.context is not None:
            result["context"] = from_union([from_str, from_none], self.context)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.deploy_ssl_url is not None:
            result["deploy_ssl_url"] = from_union([from_str, from_none], self.deploy_ssl_url)
        if self.deploy_url is not None:
            result["deploy_url"] = from_union([from_str, from_none], self.deploy_url)
        if self.draft is not None:
            result["draft"] = from_union([from_bool, from_none], self.draft)
        if self.error_message is not None:
            result["error_message"] = from_union([from_str, from_none], self.error_message)
        if self.framework is not None:
            result["framework"] = from_union([from_str, from_none], self.framework)
        if self.function_schedules is not None:
            result["function_schedules"] = from_union([lambda x: from_list(lambda x: to_class(FunctionSchedule, x), x), from_none], self.function_schedules)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.locked is not None:
            result["locked"] = from_union([from_bool, from_none], self.locked)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.published_at is not None:
            result["published_at"] = from_union([from_str, from_none], self.published_at)
        if self.required is not None:
            result["required"] = from_union([lambda x: from_list(from_str, x), from_none], self.required)
        if self.required_functions is not None:
            result["required_functions"] = from_union([lambda x: from_list(from_str, x), from_none], self.required_functions)
        if self.review_id is not None:
            result["review_id"] = from_union([to_float, from_none], self.review_id)
        if self.review_url is not None:
            result["review_url"] = from_union([from_str, from_none], self.review_url)
        if self.screenshot_url is not None:
            result["screenshot_url"] = from_union([from_str, from_none], self.screenshot_url)
        if self.site_capabilities is not None:
            result["site_capabilities"] = from_union([lambda x: to_class(DeploySiteCapabilities, x), from_none], self.site_capabilities)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.skipped is not None:
            result["skipped"] = from_union([from_bool, from_none], self.skipped)
        if self.ssl_url is not None:
            result["ssl_url"] = from_union([from_str, from_none], self.ssl_url)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.user_id is not None:
            result["user_id"] = from_union([from_str, from_none], self.user_id)
        return result


class Site:
    account_name: Optional[str]
    account_slug: Optional[str]
    admin_url: Optional[str]
    branch_deploy_custom_domain: Optional[str]
    build_image: Optional[str]
    build_settings: Optional[RepoInfo]
    capabilities: Any
    created_at: Optional[str]
    custom_domain: Optional[str]
    default_hooks_data: Optional[SiteDefaultHooksData]
    deploy_hook: Optional[str]
    deploy_preview_custom_domain: Optional[str]
    deploy_url: Optional[str]
    domain_aliases: Optional[List[str]]
    force_ssl: Optional[bool]
    git_provider: Optional[str]
    id: Optional[str]
    id_domain: Optional[str]
    managed_dns: Optional[bool]
    name: Optional[str]
    notification_email: Optional[str]
    password: Optional[str]
    plan: Optional[str]
    prerender: Optional[str]
    processing_settings: Optional[SiteProcessingSettings]
    published_deploy: Optional[Deploy]
    screenshot_url: Optional[str]
    session_id: Optional[str]
    ssl: Optional[bool]
    ssl_url: Optional[str]
    state: Optional[str]
    updated_at: Optional[str]
    url: Optional[str]
    user_id: Optional[str]

    def __init__(self, account_name: Optional[str], account_slug: Optional[str], admin_url: Optional[str], branch_deploy_custom_domain: Optional[str], build_image: Optional[str], build_settings: Optional[RepoInfo], capabilities: Any, created_at: Optional[str], custom_domain: Optional[str], default_hooks_data: Optional[SiteDefaultHooksData], deploy_hook: Optional[str], deploy_preview_custom_domain: Optional[str], deploy_url: Optional[str], domain_aliases: Optional[List[str]], force_ssl: Optional[bool], git_provider: Optional[str], id: Optional[str], id_domain: Optional[str], managed_dns: Optional[bool], name: Optional[str], notification_email: Optional[str], password: Optional[str], plan: Optional[str], prerender: Optional[str], processing_settings: Optional[SiteProcessingSettings], published_deploy: Optional[Deploy], screenshot_url: Optional[str], session_id: Optional[str], ssl: Optional[bool], ssl_url: Optional[str], state: Optional[str], updated_at: Optional[str], url: Optional[str], user_id: Optional[str]) -> None:
        self.account_name = account_name
        self.account_slug = account_slug
        self.admin_url = admin_url
        self.branch_deploy_custom_domain = branch_deploy_custom_domain
        self.build_image = build_image
        self.build_settings = build_settings
        self.capabilities = capabilities
        self.created_at = created_at
        self.custom_domain = custom_domain
        self.default_hooks_data = default_hooks_data
        self.deploy_hook = deploy_hook
        self.deploy_preview_custom_domain = deploy_preview_custom_domain
        self.deploy_url = deploy_url
        self.domain_aliases = domain_aliases
        self.force_ssl = force_ssl
        self.git_provider = git_provider
        self.id = id
        self.id_domain = id_domain
        self.managed_dns = managed_dns
        self.name = name
        self.notification_email = notification_email
        self.password = password
        self.plan = plan
        self.prerender = prerender
        self.processing_settings = processing_settings
        self.published_deploy = published_deploy
        self.screenshot_url = screenshot_url
        self.session_id = session_id
        self.ssl = ssl
        self.ssl_url = ssl_url
        self.state = state
        self.updated_at = updated_at
        self.url = url
        self.user_id = user_id

    @staticmethod
    def from_dict(obj: Any) -> 'Site':
        assert isinstance(obj, dict)
        account_name = from_union([from_str, from_none], obj.get("account_name"))
        account_slug = from_union([from_str, from_none], obj.get("account_slug"))
        admin_url = from_union([from_str, from_none], obj.get("admin_url"))
        branch_deploy_custom_domain = from_union([from_str, from_none], obj.get("branch_deploy_custom_domain"))
        build_image = from_union([from_str, from_none], obj.get("build_image"))
        build_settings = from_union([RepoInfo.from_dict, from_none], obj.get("build_settings"))
        capabilities = obj.get("capabilities")
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        custom_domain = from_union([from_str, from_none], obj.get("custom_domain"))
        default_hooks_data = from_union([SiteDefaultHooksData.from_dict, from_none], obj.get("default_hooks_data"))
        deploy_hook = from_union([from_str, from_none], obj.get("deploy_hook"))
        deploy_preview_custom_domain = from_union([from_str, from_none], obj.get("deploy_preview_custom_domain"))
        deploy_url = from_union([from_str, from_none], obj.get("deploy_url"))
        domain_aliases = from_union([lambda x: from_list(from_str, x), from_none], obj.get("domain_aliases"))
        force_ssl = from_union([from_bool, from_none], obj.get("force_ssl"))
        git_provider = from_union([from_str, from_none], obj.get("git_provider"))
        id = from_union([from_str, from_none], obj.get("id"))
        id_domain = from_union([from_str, from_none], obj.get("id_domain"))
        managed_dns = from_union([from_bool, from_none], obj.get("managed_dns"))
        name = from_union([from_str, from_none], obj.get("name"))
        notification_email = from_union([from_str, from_none], obj.get("notification_email"))
        password = from_union([from_str, from_none], obj.get("password"))
        plan = from_union([from_str, from_none], obj.get("plan"))
        prerender = from_union([from_str, from_none], obj.get("prerender"))
        processing_settings = from_union([SiteProcessingSettings.from_dict, from_none], obj.get("processing_settings"))
        published_deploy = from_union([Deploy.from_dict, from_none], obj.get("published_deploy"))
        screenshot_url = from_union([from_str, from_none], obj.get("screenshot_url"))
        session_id = from_union([from_str, from_none], obj.get("session_id"))
        ssl = from_union([from_bool, from_none], obj.get("ssl"))
        ssl_url = from_union([from_str, from_none], obj.get("ssl_url"))
        state = from_union([from_str, from_none], obj.get("state"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        url = from_union([from_str, from_none], obj.get("url"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        return Site(account_name, account_slug, admin_url, branch_deploy_custom_domain, build_image, build_settings, capabilities, created_at, custom_domain, default_hooks_data, deploy_hook, deploy_preview_custom_domain, deploy_url, domain_aliases, force_ssl, git_provider, id, id_domain, managed_dns, name, notification_email, password, plan, prerender, processing_settings, published_deploy, screenshot_url, session_id, ssl, ssl_url, state, updated_at, url, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.account_name is not None:
            result["account_name"] = from_union([from_str, from_none], self.account_name)
        if self.account_slug is not None:
            result["account_slug"] = from_union([from_str, from_none], self.account_slug)
        if self.admin_url is not None:
            result["admin_url"] = from_union([from_str, from_none], self.admin_url)
        if self.branch_deploy_custom_domain is not None:
            result["branch_deploy_custom_domain"] = from_union([from_str, from_none], self.branch_deploy_custom_domain)
        if self.build_image is not None:
            result["build_image"] = from_union([from_str, from_none], self.build_image)
        if self.build_settings is not None:
            result["build_settings"] = from_union([lambda x: to_class(RepoInfo, x), from_none], self.build_settings)
        if self.capabilities is not None:
            result["capabilities"] = self.capabilities
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.custom_domain is not None:
            result["custom_domain"] = from_union([from_str, from_none], self.custom_domain)
        if self.default_hooks_data is not None:
            result["default_hooks_data"] = from_union([lambda x: to_class(SiteDefaultHooksData, x), from_none], self.default_hooks_data)
        if self.deploy_hook is not None:
            result["deploy_hook"] = from_union([from_str, from_none], self.deploy_hook)
        if self.deploy_preview_custom_domain is not None:
            result["deploy_preview_custom_domain"] = from_union([from_str, from_none], self.deploy_preview_custom_domain)
        if self.deploy_url is not None:
            result["deploy_url"] = from_union([from_str, from_none], self.deploy_url)
        if self.domain_aliases is not None:
            result["domain_aliases"] = from_union([lambda x: from_list(from_str, x), from_none], self.domain_aliases)
        if self.force_ssl is not None:
            result["force_ssl"] = from_union([from_bool, from_none], self.force_ssl)
        if self.git_provider is not None:
            result["git_provider"] = from_union([from_str, from_none], self.git_provider)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.id_domain is not None:
            result["id_domain"] = from_union([from_str, from_none], self.id_domain)
        if self.managed_dns is not None:
            result["managed_dns"] = from_union([from_bool, from_none], self.managed_dns)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.notification_email is not None:
            result["notification_email"] = from_union([from_str, from_none], self.notification_email)
        if self.password is not None:
            result["password"] = from_union([from_str, from_none], self.password)
        if self.plan is not None:
            result["plan"] = from_union([from_str, from_none], self.plan)
        if self.prerender is not None:
            result["prerender"] = from_union([from_str, from_none], self.prerender)
        if self.processing_settings is not None:
            result["processing_settings"] = from_union([lambda x: to_class(SiteProcessingSettings, x), from_none], self.processing_settings)
        if self.published_deploy is not None:
            result["published_deploy"] = from_union([lambda x: to_class(Deploy, x), from_none], self.published_deploy)
        if self.screenshot_url is not None:
            result["screenshot_url"] = from_union([from_str, from_none], self.screenshot_url)
        if self.session_id is not None:
            result["session_id"] = from_union([from_str, from_none], self.session_id)
        if self.ssl is not None:
            result["ssl"] = from_union([from_bool, from_none], self.ssl)
        if self.ssl_url is not None:
            result["ssl_url"] = from_union([from_str, from_none], self.ssl_url)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.user_id is not None:
            result["user_id"] = from_union([from_str, from_none], self.user_id)
        return result


class SniCertificate:
    created_at: Optional[str]
    domains: Optional[List[str]]
    expires_at: Optional[str]
    state: Optional[str]
    updated_at: Optional[str]

    def __init__(self, created_at: Optional[str], domains: Optional[List[str]], expires_at: Optional[str], state: Optional[str], updated_at: Optional[str]) -> None:
        self.created_at = created_at
        self.domains = domains
        self.expires_at = expires_at
        self.state = state
        self.updated_at = updated_at

    @staticmethod
    def from_dict(obj: Any) -> 'SniCertificate':
        assert isinstance(obj, dict)
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        domains = from_union([lambda x: from_list(from_str, x), from_none], obj.get("domains"))
        expires_at = from_union([from_str, from_none], obj.get("expires_at"))
        state = from_union([from_str, from_none], obj.get("state"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        return SniCertificate(created_at, domains, expires_at, state, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.domains is not None:
            result["domains"] = from_union([lambda x: from_list(from_str, x), from_none], self.domains)
        if self.expires_at is not None:
            result["expires_at"] = from_union([from_str, from_none], self.expires_at)
        if self.state is not None:
            result["state"] = from_union([from_str, from_none], self.state)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        return result


class Snippet:
    general: Optional[str]
    general_position: Optional[str]
    goal: Optional[str]
    goal_position: Optional[str]
    id: Optional[int]
    site_id: Optional[str]
    title: Optional[str]

    def __init__(self, general: Optional[str], general_position: Optional[str], goal: Optional[str], goal_position: Optional[str], id: Optional[int], site_id: Optional[str], title: Optional[str]) -> None:
        self.general = general
        self.general_position = general_position
        self.goal = goal
        self.goal_position = goal_position
        self.id = id
        self.site_id = site_id
        self.title = title

    @staticmethod
    def from_dict(obj: Any) -> 'Snippet':
        assert isinstance(obj, dict)
        general = from_union([from_str, from_none], obj.get("general"))
        general_position = from_union([from_str, from_none], obj.get("general_position"))
        goal = from_union([from_str, from_none], obj.get("goal"))
        goal_position = from_union([from_str, from_none], obj.get("goal_position"))
        id = from_union([from_int, from_none], obj.get("id"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        return Snippet(general, general_position, goal, goal_position, id, site_id, title)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.general is not None:
            result["general"] = from_union([from_str, from_none], self.general)
        if self.general_position is not None:
            result["general_position"] = from_union([from_str, from_none], self.general_position)
        if self.goal is not None:
            result["goal"] = from_union([from_str, from_none], self.goal)
        if self.goal_position is not None:
            result["goal_position"] = from_union([from_str, from_none], self.goal_position)
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        return result


class SplitTest:
    active: Optional[bool]
    branches: Optional[List[Any]]
    created_at: Optional[str]
    id: Optional[str]
    name: Optional[str]
    path: Optional[str]
    site_id: Optional[str]
    unpublished_at: Optional[str]
    updated_at: Optional[str]

    def __init__(self, active: Optional[bool], branches: Optional[List[Any]], created_at: Optional[str], id: Optional[str], name: Optional[str], path: Optional[str], site_id: Optional[str], unpublished_at: Optional[str], updated_at: Optional[str]) -> None:
        self.active = active
        self.branches = branches
        self.created_at = created_at
        self.id = id
        self.name = name
        self.path = path
        self.site_id = site_id
        self.unpublished_at = unpublished_at
        self.updated_at = updated_at

    @staticmethod
    def from_dict(obj: Any) -> 'SplitTest':
        assert isinstance(obj, dict)
        active = from_union([from_bool, from_none], obj.get("active"))
        branches = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("branches"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        path = from_union([from_str, from_none], obj.get("path"))
        site_id = from_union([from_str, from_none], obj.get("site_id"))
        unpublished_at = from_union([from_str, from_none], obj.get("unpublished_at"))
        updated_at = from_union([from_str, from_none], obj.get("updated_at"))
        return SplitTest(active, branches, created_at, id, name, path, site_id, unpublished_at, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.active is not None:
            result["active"] = from_union([from_bool, from_none], self.active)
        if self.branches is not None:
            result["branches"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.branches)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.path is not None:
            result["path"] = from_union([from_str, from_none], self.path)
        if self.site_id is not None:
            result["site_id"] = from_union([from_str, from_none], self.site_id)
        if self.unpublished_at is not None:
            result["unpublished_at"] = from_union([from_str, from_none], self.unpublished_at)
        if self.updated_at is not None:
            result["updated_at"] = from_union([from_str, from_none], self.updated_at)
        return result


class SplitTestSetup:
    branch_tests: Any

    def __init__(self, branch_tests: Any) -> None:
        self.branch_tests = branch_tests

    @staticmethod
    def from_dict(obj: Any) -> 'SplitTestSetup':
        assert isinstance(obj, dict)
        branch_tests = obj.get("branch_tests")
        return SplitTestSetup(branch_tests)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.branch_tests is not None:
            result["branch_tests"] = self.branch_tests
        return result


class Submission:
    body: Optional[str]
    company: Optional[str]
    created_at: Optional[str]
    data: Any
    email: Optional[str]
    first_name: Optional[str]
    id: Optional[str]
    last_name: Optional[str]
    name: Optional[str]
    number: Optional[int]
    site_url: Optional[str]
    summary: Optional[str]

    def __init__(self, body: Optional[str], company: Optional[str], created_at: Optional[str], data: Any, email: Optional[str], first_name: Optional[str], id: Optional[str], last_name: Optional[str], name: Optional[str], number: Optional[int], site_url: Optional[str], summary: Optional[str]) -> None:
        self.body = body
        self.company = company
        self.created_at = created_at
        self.data = data
        self.email = email
        self.first_name = first_name
        self.id = id
        self.last_name = last_name
        self.name = name
        self.number = number
        self.site_url = site_url
        self.summary = summary

    @staticmethod
    def from_dict(obj: Any) -> 'Submission':
        assert isinstance(obj, dict)
        body = from_union([from_str, from_none], obj.get("body"))
        company = from_union([from_str, from_none], obj.get("company"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        data = obj.get("data")
        email = from_union([from_str, from_none], obj.get("email"))
        first_name = from_union([from_str, from_none], obj.get("first_name"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_name = from_union([from_str, from_none], obj.get("last_name"))
        name = from_union([from_str, from_none], obj.get("name"))
        number = from_union([from_int, from_none], obj.get("number"))
        site_url = from_union([from_str, from_none], obj.get("site_url"))
        summary = from_union([from_str, from_none], obj.get("summary"))
        return Submission(body, company, created_at, data, email, first_name, id, last_name, name, number, site_url, summary)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.body is not None:
            result["body"] = from_union([from_str, from_none], self.body)
        if self.company is not None:
            result["company"] = from_union([from_str, from_none], self.company)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.data is not None:
            result["data"] = self.data
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.first_name is not None:
            result["first_name"] = from_union([from_str, from_none], self.first_name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_name is not None:
            result["last_name"] = from_union([from_str, from_none], self.last_name)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.number is not None:
            result["number"] = from_union([from_int, from_none], self.number)
        if self.site_url is not None:
            result["site_url"] = from_union([from_str, from_none], self.site_url)
        if self.summary is not None:
            result["summary"] = from_union([from_str, from_none], self.summary)
        return result


class Ticket:
    authorized: Optional[bool]
    client_id: Optional[str]
    created_at: Optional[str]
    id: Optional[str]

    def __init__(self, authorized: Optional[bool], client_id: Optional[str], created_at: Optional[str], id: Optional[str]) -> None:
        self.authorized = authorized
        self.client_id = client_id
        self.created_at = created_at
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'Ticket':
        assert isinstance(obj, dict)
        authorized = from_union([from_bool, from_none], obj.get("authorized"))
        client_id = from_union([from_str, from_none], obj.get("client_id"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        id = from_union([from_str, from_none], obj.get("id"))
        return Ticket(authorized, client_id, created_at, id)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.authorized is not None:
            result["authorized"] = from_union([from_bool, from_none], self.authorized)
        if self.client_id is not None:
            result["client_id"] = from_union([from_str, from_none], self.client_id)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        return result


class UserOnboardingProgress:
    slides: Optional[str]

    def __init__(self, slides: Optional[str]) -> None:
        self.slides = slides

    @staticmethod
    def from_dict(obj: Any) -> 'UserOnboardingProgress':
        assert isinstance(obj, dict)
        slides = from_union([from_str, from_none], obj.get("slides"))
        return UserOnboardingProgress(slides)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.slides is not None:
            result["slides"] = from_union([from_str, from_none], self.slides)
        return result


class User:
    affiliate_id: Optional[str]
    avatar_url: Optional[str]
    created_at: Optional[str]
    email: Optional[str]
    full_name: Optional[str]
    id: Optional[str]
    last_login: Optional[str]
    login_providers: Optional[List[str]]
    onboarding_progress: Optional[UserOnboardingProgress]
    site_count: Optional[int]
    uid: Optional[str]

    def __init__(self, affiliate_id: Optional[str], avatar_url: Optional[str], created_at: Optional[str], email: Optional[str], full_name: Optional[str], id: Optional[str], last_login: Optional[str], login_providers: Optional[List[str]], onboarding_progress: Optional[UserOnboardingProgress], site_count: Optional[int], uid: Optional[str]) -> None:
        self.affiliate_id = affiliate_id
        self.avatar_url = avatar_url
        self.created_at = created_at
        self.email = email
        self.full_name = full_name
        self.id = id
        self.last_login = last_login
        self.login_providers = login_providers
        self.onboarding_progress = onboarding_progress
        self.site_count = site_count
        self.uid = uid

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        affiliate_id = from_union([from_str, from_none], obj.get("affiliate_id"))
        avatar_url = from_union([from_str, from_none], obj.get("avatar_url"))
        created_at = from_union([from_str, from_none], obj.get("created_at"))
        email = from_union([from_str, from_none], obj.get("email"))
        full_name = from_union([from_str, from_none], obj.get("full_name"))
        id = from_union([from_str, from_none], obj.get("id"))
        last_login = from_union([from_str, from_none], obj.get("last_login"))
        login_providers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("login_providers"))
        onboarding_progress = from_union([UserOnboardingProgress.from_dict, from_none], obj.get("onboarding_progress"))
        site_count = from_union([from_int, from_none], obj.get("site_count"))
        uid = from_union([from_str, from_none], obj.get("uid"))
        return User(affiliate_id, avatar_url, created_at, email, full_name, id, last_login, login_providers, onboarding_progress, site_count, uid)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.affiliate_id is not None:
            result["affiliate_id"] = from_union([from_str, from_none], self.affiliate_id)
        if self.avatar_url is not None:
            result["avatar_url"] = from_union([from_str, from_none], self.avatar_url)
        if self.created_at is not None:
            result["created_at"] = from_union([from_str, from_none], self.created_at)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.full_name is not None:
            result["full_name"] = from_union([from_str, from_none], self.full_name)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.last_login is not None:
            result["last_login"] = from_union([from_str, from_none], self.last_login)
        if self.login_providers is not None:
            result["login_providers"] = from_union([lambda x: from_list(from_str, x), from_none], self.login_providers)
        if self.onboarding_progress is not None:
            result["onboarding_progress"] = from_union([lambda x: to_class(UserOnboardingProgress, x), from_none], self.onboarding_progress)
        if self.site_count is not None:
            result["site_count"] = from_union([from_int, from_none], self.site_count)
        if self.uid is not None:
            result["uid"] = from_union([from_str, from_none], self.uid)
        return result


def patch_accounts_account_id_env_key_body_from_dict(s: Any) -> PatchAccountsAccountIDEnvKeyBody:
    return PatchAccountsAccountIDEnvKeyBody.from_dict(s)


def patch_accounts_account_id_env_key_body_to_dict(x: PatchAccountsAccountIDEnvKeyBody) -> Any:
    return to_class(PatchAccountsAccountIDEnvKeyBody, x)


def post_accounts_account_id_env_body_item_from_dict(s: Any) -> PostAccountsAccountIDEnvBodyItem:
    return PostAccountsAccountIDEnvBodyItem.from_dict(s)


def post_accounts_account_id_env_body_item_to_dict(x: PostAccountsAccountIDEnvBodyItem) -> Any:
    return to_class(PostAccountsAccountIDEnvBodyItem, x)


def put_accounts_account_id_env_key_body_from_dict(s: Any) -> PutAccountsAccountIDEnvKeyBody:
    return PutAccountsAccountIDEnvKeyBody.from_dict(s)


def put_accounts_account_id_env_key_body_to_dict(x: PutAccountsAccountIDEnvKeyBody) -> Any:
    return to_class(PutAccountsAccountIDEnvKeyBody, x)


def access_token_from_dict(s: Any) -> AccessToken:
    return AccessToken.from_dict(s)


def access_token_to_dict(x: AccessToken) -> Any:
    return to_class(AccessToken, x)


def account_add_member_setup_from_dict(s: Any) -> AccountAddMemberSetup:
    return AccountAddMemberSetup.from_dict(s)


def account_add_member_setup_to_dict(x: AccountAddMemberSetup) -> Any:
    return to_class(AccountAddMemberSetup, x)


def account_membership_from_dict(s: Any) -> AccountMembership:
    return AccountMembership.from_dict(s)


def account_membership_to_dict(x: AccountMembership) -> Any:
    return to_class(AccountMembership, x)


def account_setup_from_dict(s: Any) -> AccountSetup:
    return AccountSetup.from_dict(s)


def account_setup_to_dict(x: AccountSetup) -> Any:
    return to_class(AccountSetup, x)


def account_type_from_dict(s: Any) -> AccountType:
    return AccountType.from_dict(s)


def account_type_to_dict(x: AccountType) -> Any:
    return to_class(AccountType, x)


def account_update_member_setup_from_dict(s: Any) -> AccountUpdateMemberSetup:
    return AccountUpdateMemberSetup.from_dict(s)


def account_update_member_setup_to_dict(x: AccountUpdateMemberSetup) -> Any:
    return to_class(AccountUpdateMemberSetup, x)


def account_update_setup_from_dict(s: Any) -> AccountUpdateSetup:
    return AccountUpdateSetup.from_dict(s)


def account_update_setup_to_dict(x: AccountUpdateSetup) -> Any:
    return to_class(AccountUpdateSetup, x)


def account_usage_capability_from_dict(s: Any) -> AccountUsageCapability:
    return AccountUsageCapability.from_dict(s)


def account_usage_capability_to_dict(x: AccountUsageCapability) -> Any:
    return to_class(AccountUsageCapability, x)


def asset_from_dict(s: Any) -> Asset:
    return Asset.from_dict(s)


def asset_to_dict(x: Asset) -> Any:
    return to_class(Asset, x)


def asset_form_from_dict(s: Any) -> AssetForm:
    return AssetForm.from_dict(s)


def asset_form_to_dict(x: AssetForm) -> Any:
    return to_class(AssetForm, x)


def asset_public_signature_from_dict(s: Any) -> AssetPublicSignature:
    return AssetPublicSignature.from_dict(s)


def asset_public_signature_to_dict(x: AssetPublicSignature) -> Any:
    return to_class(AssetPublicSignature, x)


def asset_signature_from_dict(s: Any) -> AssetSignature:
    return AssetSignature.from_dict(s)


def asset_signature_to_dict(x: AssetSignature) -> Any:
    return to_class(AssetSignature, x)


def audit_log_from_dict(s: Any) -> AuditLog:
    return AuditLog.from_dict(s)


def audit_log_to_dict(x: AuditLog) -> Any:
    return to_class(AuditLog, x)


def build_from_dict(s: Any) -> Build:
    return Build.from_dict(s)


def build_to_dict(x: Build) -> Any:
    return to_class(Build, x)


def build_hook_from_dict(s: Any) -> BuildHook:
    return BuildHook.from_dict(s)


def build_hook_to_dict(x: BuildHook) -> Any:
    return to_class(BuildHook, x)


def build_hook_setup_from_dict(s: Any) -> BuildHookSetup:
    return BuildHookSetup.from_dict(s)


def build_hook_setup_to_dict(x: BuildHookSetup) -> Any:
    return to_class(BuildHookSetup, x)


def build_log_msg_from_dict(s: Any) -> BuildLogMsg:
    return BuildLogMsg.from_dict(s)


def build_log_msg_to_dict(x: BuildLogMsg) -> Any:
    return to_class(BuildLogMsg, x)


def build_setup_from_dict(s: Any) -> BuildSetup:
    return BuildSetup.from_dict(s)


def build_setup_to_dict(x: BuildSetup) -> Any:
    return to_class(BuildSetup, x)


def build_status_from_dict(s: Any) -> BuildStatus:
    return BuildStatus.from_dict(s)


def build_status_to_dict(x: BuildStatus) -> Any:
    return to_class(BuildStatus, x)


def deploy_from_dict(s: Any) -> Deploy:
    return Deploy.from_dict(s)


def deploy_to_dict(x: Deploy) -> Any:
    return to_class(Deploy, x)


def deploy_files_from_dict(s: Any) -> DeployFiles:
    return DeployFiles.from_dict(s)


def deploy_files_to_dict(x: DeployFiles) -> Any:
    return to_class(DeployFiles, x)


def deploy_key_from_dict(s: Any) -> DeployKey:
    return DeployKey.from_dict(s)


def deploy_key_to_dict(x: DeployKey) -> Any:
    return to_class(DeployKey, x)


def deployed_branch_from_dict(s: Any) -> DeployedBranch:
    return DeployedBranch.from_dict(s)


def deployed_branch_to_dict(x: DeployedBranch) -> Any:
    return to_class(DeployedBranch, x)


def dns_record_from_dict(s: Any) -> DNSRecord:
    return DNSRecord.from_dict(s)


def dns_record_to_dict(x: DNSRecord) -> Any:
    return to_class(DNSRecord, x)


def dns_record_create_from_dict(s: Any) -> DNSRecordCreate:
    return DNSRecordCreate.from_dict(s)


def dns_record_create_to_dict(x: DNSRecordCreate) -> Any:
    return to_class(DNSRecordCreate, x)


def dns_zone_from_dict(s: Any) -> DNSZone:
    return DNSZone.from_dict(s)


def dns_zone_to_dict(x: DNSZone) -> Any:
    return to_class(DNSZone, x)


def dns_zone_setup_from_dict(s: Any) -> DNSZoneSetup:
    return DNSZoneSetup.from_dict(s)


def dns_zone_setup_to_dict(x: DNSZoneSetup) -> Any:
    return to_class(DNSZoneSetup, x)


def env_var_from_dict(s: Any) -> EnvVar:
    return EnvVar.from_dict(s)


def env_var_to_dict(x: EnvVar) -> Any:
    return to_class(EnvVar, x)


def env_var_user_from_dict(s: Any) -> EnvVarUser:
    return EnvVarUser.from_dict(s)


def env_var_user_to_dict(x: EnvVarUser) -> Any:
    return to_class(EnvVarUser, x)


def env_var_value_from_dict(s: Any) -> EnvVarValue:
    return EnvVarValue.from_dict(s)


def env_var_value_to_dict(x: EnvVarValue) -> Any:
    return to_class(EnvVarValue, x)


def error_from_dict(s: Any) -> Error:
    return Error.from_dict(s)


def error_to_dict(x: Error) -> Any:
    return to_class(Error, x)


def file_from_dict(s: Any) -> File:
    return File.from_dict(s)


def file_to_dict(x: File) -> Any:
    return to_class(File, x)


def form_from_dict(s: Any) -> Form:
    return Form.from_dict(s)


def form_to_dict(x: Form) -> Any:
    return to_class(Form, x)


def function_from_dict(s: Any) -> Function:
    return Function.from_dict(s)


def function_to_dict(x: Function) -> Any:
    return to_class(Function, x)


def function_config_from_dict(s: Any) -> FunctionConfig:
    return FunctionConfig.from_dict(s)


def function_config_to_dict(x: FunctionConfig) -> Any:
    return to_class(FunctionConfig, x)


def function_route_from_dict(s: Any) -> FunctionRoute:
    return FunctionRoute.from_dict(s)


def function_route_to_dict(x: FunctionRoute) -> Any:
    return to_class(FunctionRoute, x)


def function_schedule_from_dict(s: Any) -> FunctionSchedule:
    return FunctionSchedule.from_dict(s)


def function_schedule_to_dict(x: FunctionSchedule) -> Any:
    return to_class(FunctionSchedule, x)


def hook_from_dict(s: Any) -> Hook:
    return Hook.from_dict(s)


def hook_to_dict(x: Hook) -> Any:
    return to_class(Hook, x)


def hook_type_from_dict(s: Any) -> HookType:
    return HookType.from_dict(s)


def hook_type_to_dict(x: HookType) -> Any:
    return to_class(HookType, x)


def member_from_dict(s: Any) -> Member:
    return Member.from_dict(s)


def member_to_dict(x: Member) -> Any:
    return to_class(Member, x)


def minify_options_from_dict(s: Any) -> MinifyOptions:
    return MinifyOptions.from_dict(s)


def minify_options_to_dict(x: MinifyOptions) -> Any:
    return to_class(MinifyOptions, x)


def payment_method_from_dict(s: Any) -> PaymentMethod:
    return PaymentMethod.from_dict(s)


def payment_method_to_dict(x: PaymentMethod) -> Any:
    return to_class(PaymentMethod, x)


def plugin_from_dict(s: Any) -> Plugin:
    return Plugin.from_dict(s)


def plugin_to_dict(x: Plugin) -> Any:
    return to_class(Plugin, x)


def plugin_params_from_dict(s: Any) -> PluginParams:
    return PluginParams.from_dict(s)


def plugin_params_to_dict(x: PluginParams) -> Any:
    return to_class(PluginParams, x)


def plugin_run_data_from_dict(s: Any) -> PluginRunData:
    return PluginRunData.from_dict(s)


def plugin_run_data_to_dict(x: PluginRunData) -> Any:
    return to_class(PluginRunData, x)


def repo_info_from_dict(s: Any) -> RepoInfo:
    return RepoInfo.from_dict(s)


def repo_info_to_dict(x: RepoInfo) -> Any:
    return to_class(RepoInfo, x)


def service_from_dict(s: Any) -> Service:
    return Service.from_dict(s)


def service_to_dict(x: Service) -> Any:
    return to_class(Service, x)


def service_instance_from_dict(s: Any) -> ServiceInstance:
    return ServiceInstance.from_dict(s)


def service_instance_to_dict(x: ServiceInstance) -> Any:
    return to_class(ServiceInstance, x)


def site_from_dict(s: Any) -> Site:
    return Site.from_dict(s)


def site_to_dict(x: Site) -> Any:
    return to_class(Site, x)


def sni_certificate_from_dict(s: Any) -> SniCertificate:
    return SniCertificate.from_dict(s)


def sni_certificate_to_dict(x: SniCertificate) -> Any:
    return to_class(SniCertificate, x)


def snippet_from_dict(s: Any) -> Snippet:
    return Snippet.from_dict(s)


def snippet_to_dict(x: Snippet) -> Any:
    return to_class(Snippet, x)


def split_test_from_dict(s: Any) -> SplitTest:
    return SplitTest.from_dict(s)


def split_test_to_dict(x: SplitTest) -> Any:
    return to_class(SplitTest, x)


def split_test_setup_from_dict(s: Any) -> SplitTestSetup:
    return SplitTestSetup.from_dict(s)


def split_test_setup_to_dict(x: SplitTestSetup) -> Any:
    return to_class(SplitTestSetup, x)


def submission_from_dict(s: Any) -> Submission:
    return Submission.from_dict(s)


def submission_to_dict(x: Submission) -> Any:
    return to_class(Submission, x)


def ticket_from_dict(s: Any) -> Ticket:
    return Ticket.from_dict(s)


def ticket_to_dict(x: Ticket) -> Any:
    return to_class(Ticket, x)


def user_from_dict(s: Any) -> User:
    return User.from_dict(s)


def user_to_dict(x: User) -> Any:
    return to_class(User, x)
