import typing
import json
import requests
from urllib.parse import urljoin

from .custom_types import *

JSONType = typing.Union[str, int, float, bool, None, typing.Dict[str, typing.Any], typing.List[typing.Any]]

class RequestError(Exception):
    def __init__(self, status_code: int, method: str, url: str, message: str):
        super().__init__(f"received {status_code} from {method.upper()} {url}")
        self.status_code = status_code
        self.method = method
        self.url = url
        try:
            self.data = json.loads(message)
        except:
            self.data = message

class Netlify:
    def __init__(self, token: typing.Optional[str] = None, base_url: typing.Optional[str] = None):
        url = base_url or "https://api.netlify.com/api/v1"
        self.base_url = url        
        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _cast_list(self, input_list, target_class):
        casted = []
        for el in input_list:
            if isinstance(el, list):
                casted.append(self._cast_list(el, target_class))
            else:
                casted.append(target_class.from_dict(el))
        return casted

    def _raise_exception(self, response: requests.models.Response) -> typing.Any:
        method = response.request.method or "unknown"
        raise RequestError(response.status_code, method, response.url, response.text)

    def _to_json_encodable(self, target: typing.Any) -> JSONType:
        if isinstance(target, list):
            return [self._to_json_encodable(el) for el in target]

        to_dict_method = getattr(target, "to_dict", None)
        if callable(to_dict_method):
            return target.to_dict()

        return target

    def with_token(self, token: str) -> None:
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def cancel_account(self, account_id: str) -> typing.Any:
        """  """
        endpoint = f"/accounts/{account_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_env_var(self, account_id: str, key: str, site_id: typing.Optional[str] = None) -> typing.Any:
        """ Deletes an environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;&quot;https://docs.netlify.com/environment-variables/classic-experience/&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI. """
        endpoint = f"/accounts/{account_id}/env/{key}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        params["key"] = key
        if site_id is not None:
            params["site_id"] = site_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_env_var_value(self, account_id: str, key: str, id: str, site_id: typing.Optional[str] = None) -> typing.Any:
        """ Deletes a specific environment variable value. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;&quot;https://docs.netlify.com/environment-variables/classic-experience/&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI. """
        endpoint = f"/accounts/{account_id}/env/{key}/value/{id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        params["key"] = key
        params["id"] = id
        if site_id is not None:
            params["site_id"] = site_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_deploy_key(self, key_id: str) -> typing.Any:
        """  """
        endpoint = f"/deploy_keys/{key_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["key_id"] = key_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_deploy(self, deploy_id: str) -> typing.Any:
        """  """
        endpoint = f"/deploys/{deploy_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["deploy_id"] = deploy_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_dns_zone(self, zone_id: str) -> typing.Any:
        """  """
        endpoint = f"/dns_zones/{zone_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["zone_id"] = zone_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_dns_record(self, zone_id: str, dns_record_id: str) -> typing.Any:
        """  """
        endpoint = f"/dns_zones/{zone_id}/dns_records/{dns_record_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["zone_id"] = zone_id
        params["dns_record_id"] = dns_record_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_hook(self, hook_id: str) -> typing.Any:
        """  """
        endpoint = f"/hooks/{hook_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["hook_id"] = hook_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_site(self, site_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_site_asset(self, site_id: str, asset_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/assets/{asset_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["asset_id"] = asset_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_site_build_hook(self, site_id: str, id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/build_hooks/{id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["id"] = id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_site_deploy(self, site_id: str, deploy_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/deploys/{deploy_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["deploy_id"] = deploy_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_site_form(self, site_id: str, form_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/forms/{form_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["form_id"] = form_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_service_instance(self, site_id: str, addon: str, instance_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/services/{addon}/instances/{instance_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["addon"] = addon
        params["instance_id"] = instance_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_site_snippet(self, site_id: str, snippet_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/snippets/{snippet_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["snippet_id"] = snippet_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def delete_submission(self, submission_id: str) -> typing.Any:
        """  """
        endpoint = f"/submissions/{submission_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["submission_id"] = submission_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def remove_account_member(self, account_slug: str, member_id: str) -> typing.Any:
        """  """
        endpoint = f"/{account_slug}/members/{member_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_slug"] = account_slug
        params["member_id"] = member_id
        raw_response = self.session.delete(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def list_accounts_for_user(self) -> typing.List[AccountMembership]:
        """  """
        endpoint = f"/accounts"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, AccountMembership)
        return response

    def list_account_types_for_user(self) -> typing.List[AccountType]:
        """  """
        endpoint = f"/accounts/types"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, AccountType)
        return response

    def get_account(self, account_id: str) -> typing.List[AccountMembership]:
        """  """
        endpoint = f"/accounts/{account_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, AccountMembership)
        return response

    def list_account_audit_events(self, account_id: str, log_type: typing.Optional[str] = None, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None, query: typing.Optional[str] = None) -> typing.List[AuditLog]:
        """  """
        endpoint = f"/accounts/{account_id}/audit"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        if log_type is not None:
            params["log_type"] = log_type
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if query is not None:
            params["query"] = query
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, AuditLog)
        return response

    def get_env_vars(self, account_id: str, context_name: typing.Optional[str] = None, scope: typing.Optional[str] = None, site_id: typing.Optional[str] = None) -> typing.List[EnvVar]:
        """ Returns all environment variables for an account or site. An account corresponds to a team in the Netlify UI. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;&quot;https://docs.netlify.com/environment-variables/classic-experience/&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI. """
        endpoint = f"/accounts/{account_id}/env"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        if context_name is not None:
            params["context_name"] = context_name
        if scope is not None:
            params["scope"] = scope
        if site_id is not None:
            params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, EnvVar)
        return response

    def get_env_var(self, account_id: str, key: str, site_id: typing.Optional[str] = None) -> EnvVar:
        """ Returns an individual environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;&quot;https://docs.netlify.com/environment-variables/classic-experience/&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI. """
        endpoint = f"/accounts/{account_id}/env/{key}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        params["key"] = key
        if site_id is not None:
            params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = EnvVar.from_dict(response)
        return response

    def list_payment_methods_for_user(self) -> typing.List[PaymentMethod]:
        """  """
        endpoint = f"/billing/payment_methods"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, PaymentMethod)
        return response

    def get_site_build(self, build_id: str) -> Build:
        """  """
        endpoint = f"/builds/{build_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["build_id"] = build_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Build.from_dict(response)
        return response

    def list_deploy_keys(self) -> typing.List[DeployKey]:
        """  """
        endpoint = f"/deploy_keys"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, DeployKey)
        return response

    def get_deploy_key(self, key_id: str) -> DeployKey:
        """  """
        endpoint = f"/deploy_keys/{key_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["key_id"] = key_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = DeployKey.from_dict(response)
        return response

    def get_deploy(self, deploy_id: str) -> Deploy:
        """  """
        endpoint = f"/deploys/{deploy_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["deploy_id"] = deploy_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def get_dns_zones(self, account_slug: typing.Optional[str] = None) -> typing.List[DNSZone]:
        """  """
        endpoint = f"/dns_zones"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        if account_slug is not None:
            params["account_slug"] = account_slug
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, DNSZone)
        return response

    def get_dns_zone(self, zone_id: str) -> DNSZone:
        """  """
        endpoint = f"/dns_zones/{zone_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["zone_id"] = zone_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = DNSZone.from_dict(response)
        return response

    def get_dns_records(self, zone_id: str) -> typing.List[DNSRecord]:
        """  """
        endpoint = f"/dns_zones/{zone_id}/dns_records"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["zone_id"] = zone_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, DNSRecord)
        return response

    def get_individual_dns_record(self, zone_id: str, dns_record_id: str) -> DNSRecord:
        """  """
        endpoint = f"/dns_zones/{zone_id}/dns_records/{dns_record_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["zone_id"] = zone_id
        params["dns_record_id"] = dns_record_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = DNSRecord.from_dict(response)
        return response

    def list_form_submissions(self, form_id: str, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None) -> typing.List[Submission]:
        """  """
        endpoint = f"/forms/{form_id}/submissions"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["form_id"] = form_id
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Submission)
        return response

    def list_hooks_by_site_id(self, site_id: str) -> typing.List[Hook]:
        """  """
        endpoint = f"/hooks"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Hook)
        return response

    def list_hook_types(self) -> typing.List[HookType]:
        """  """
        endpoint = f"/hooks/types"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, HookType)
        return response

    def get_hook(self, hook_id: str) -> Hook:
        """  """
        endpoint = f"/hooks/{hook_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["hook_id"] = hook_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Hook.from_dict(response)
        return response

    def show_ticket(self, ticket_id: str) -> Ticket:
        """  """
        endpoint = f"/oauth/tickets/{ticket_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["ticket_id"] = ticket_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Ticket.from_dict(response)
        return response

    def get_services(self, search: typing.Optional[str] = None) -> typing.List[Service]:
        """  """
        endpoint = f"/services/"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        if search is not None:
            params["search"] = search
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Service)
        return response

    def show_service(self, addon_name: str) -> Service:
        """  """
        endpoint = f"/services/{addon_name}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["addon_name"] = addon_name
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Service.from_dict(response)
        return response

    def show_service_manifest(self, addon_name: str) -> typing.Any:
        """  """
        endpoint = f"/services/{addon_name}/manifest"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["addon_name"] = addon_name
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def list_sites(self, filter: typing.Optional[str] = None, name: typing.Optional[str] = None, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None) -> typing.List[Site]:
        """ **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables. """
        endpoint = f"/sites"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        if filter is not None:
            params["filter"] = filter
        if name is not None:
            params["name"] = name
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Site)
        return response

    def get_site(self, site_id: str) -> Site:
        """ **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables. """
        endpoint = f"/sites/{site_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Site.from_dict(response)
        return response

    def list_site_assets(self, site_id: str) -> typing.List[Asset]:
        """  """
        endpoint = f"/sites/{site_id}/assets"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Asset)
        return response

    def get_site_asset_info(self, site_id: str, asset_id: str) -> Asset:
        """  """
        endpoint = f"/sites/{site_id}/assets/{asset_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["asset_id"] = asset_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Asset.from_dict(response)
        return response

    def get_site_asset_public_signature(self, site_id: str, asset_id: str) -> AssetPublicSignature:
        """  """
        endpoint = f"/sites/{site_id}/assets/{asset_id}/public_signature"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["asset_id"] = asset_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = AssetPublicSignature.from_dict(response)
        return response

    def list_site_build_hooks(self, site_id: str) -> typing.List[BuildHook]:
        """  """
        endpoint = f"/sites/{site_id}/build_hooks"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, BuildHook)
        return response

    def get_site_build_hook(self, site_id: str, id: str) -> BuildHook:
        """  """
        endpoint = f"/sites/{site_id}/build_hooks/{id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["id"] = id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = BuildHook.from_dict(response)
        return response

    def list_site_builds(self, site_id: str, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None) -> typing.List[Build]:
        """  """
        endpoint = f"/sites/{site_id}/builds"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Build)
        return response

    def list_site_deployed_branches(self, site_id: str) -> typing.List[DeployedBranch]:
        """  """
        endpoint = f"/sites/{site_id}/deployed-branches"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, DeployedBranch)
        return response

    def list_site_deploys(self, site_id: str, branch: typing.Optional[str] = None, deploy_previews: typing.Optional[bool] = None, latest_published: typing.Optional[bool] = None, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None, production: typing.Optional[bool] = None, state: typing.Optional[str] = None) -> typing.List[Deploy]:
        """  """
        endpoint = f"/sites/{site_id}/deploys"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        if branch is not None:
            params["branch"] = branch
        if deploy_previews is not None:
            params["deploy_previews"] = deploy_previews
        if latest_published is not None:
            params["latest_published"] = latest_published
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if production is not None:
            params["production"] = production
        if state is not None:
            params["state"] = state
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Deploy)
        return response

    def get_site_deploy(self, site_id: str, deploy_id: str) -> Deploy:
        """  """
        endpoint = f"/sites/{site_id}/deploys/{deploy_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["deploy_id"] = deploy_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def get_dns_for_site(self, site_id: str) -> typing.List[DNSZone]:
        """  """
        endpoint = f"/sites/{site_id}/dns"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, DNSZone)
        return response

    def list_site_files(self, site_id: str) -> typing.List[File]:
        """  """
        endpoint = f"/sites/{site_id}/files"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, File)
        return response

    def get_site_file_by_path_name(self, site_id: str, file_path: str) -> File:
        """  """
        endpoint = f"/sites/{site_id}/files/{file_path}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["file_path"] = file_path
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = File.from_dict(response)
        return response

    def list_site_forms(self, site_id: str) -> typing.List[Form]:
        """  """
        endpoint = f"/sites/{site_id}/forms"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Form)
        return response

    def get_site_metadata(self, site_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/metadata"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def list_service_instances_for_site(self, site_id: str) -> typing.List[ServiceInstance]:
        """  """
        endpoint = f"/sites/{site_id}/service-instances"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, ServiceInstance)
        return response

    def show_service_instance(self, site_id: str, addon: str, instance_id: str) -> ServiceInstance:
        """  """
        endpoint = f"/sites/{site_id}/services/{addon}/instances/{instance_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["addon"] = addon
        params["instance_id"] = instance_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = ServiceInstance.from_dict(response)
        return response

    def list_site_snippets(self, site_id: str) -> typing.List[Snippet]:
        """  """
        endpoint = f"/sites/{site_id}/snippets"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Snippet)
        return response

    def get_site_snippet(self, site_id: str, snippet_id: str) -> Snippet:
        """  """
        endpoint = f"/sites/{site_id}/snippets/{snippet_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["snippet_id"] = snippet_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Snippet.from_dict(response)
        return response

    def show_site_tls_certificate(self, site_id: str) -> SniCertificate:
        """  """
        endpoint = f"/sites/{site_id}/ssl"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = SniCertificate.from_dict(response)
        return response

    def list_site_submissions(self, site_id: str, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None) -> typing.List[Submission]:
        """  """
        endpoint = f"/sites/{site_id}/submissions"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Submission)
        return response

    def get_split_tests(self, site_id: str) -> typing.List[SplitTest]:
        """  """
        endpoint = f"/sites/{site_id}/traffic_splits"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, SplitTest)
        return response

    def get_split_test(self, site_id: str, split_test_id: str) -> SplitTest:
        """  """
        endpoint = f"/sites/{site_id}/traffic_splits/{split_test_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["split_test_id"] = split_test_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = SplitTest.from_dict(response)
        return response

    def list_form_submission(self, submission_id: str, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None, query: typing.Optional[str] = None) -> typing.List[Submission]:
        """  """
        endpoint = f"/submissions/{submission_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["submission_id"] = submission_id
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if query is not None:
            params["query"] = query
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Submission)
        return response

    def get_current_user(self) -> typing.List[User]:
        """  """
        endpoint = f"/user"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, User)
        return response

    def get_account_build_status(self, account_id: str) -> typing.List[BuildStatus]:
        """  """
        endpoint = f"/{account_id}/builds/status"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, BuildStatus)
        return response

    def list_members_for_account(self, account_slug: str) -> typing.List[Member]:
        """  """
        endpoint = f"/{account_slug}/members"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_slug"] = account_slug
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Member)
        return response

    def get_account_member(self, account_slug: str, member_id: str) -> Member:
        """  """
        endpoint = f"/{account_slug}/members/{member_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_slug"] = account_slug
        params["member_id"] = member_id
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Member.from_dict(response)
        return response

    def list_sites_for_account(self, account_slug: str, name: typing.Optional[str] = None, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None) -> typing.List[Site]:
        """ **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables. """
        endpoint = f"/{account_slug}/sites"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_slug"] = account_slug
        if name is not None:
            params["name"] = name
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        raw_response = self.session.get(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Site)
        return response

    def set_env_var_value(self, request_body: PatchAccountsAccountIDEnvKeyBody, account_id: str, key: str, site_id: typing.Optional[str] = None) -> EnvVar:
        """ Updates or creates a new value for an existing environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;&quot;https://docs.netlify.com/environment-variables/classic-experience/&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI. """
        endpoint = f"/accounts/{account_id}/env/{key}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        params["key"] = key
        if site_id is not None:
            params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.patch(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = EnvVar.from_dict(response)
        return response

    def update_site(self, request_body: typing.Any, site_id: str) -> Site:
        """ **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [updateEnvVar](#tag/environmentVariables/operation/updateEnvVar) to update a site&#x27;s environment variables. """
        endpoint = f"/sites/{site_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.patch(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Site.from_dict(response)
        return response

    def create_account(self, request_body: AccountSetup) -> AccountMembership:
        """  """
        endpoint = f"/accounts"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = AccountMembership.from_dict(response)
        return response

    def create_env_vars(self, request_body: typing.List[PostAccountsAccountIDEnvBodyItem], account_id: str, site_id: typing.Optional[str] = None) -> typing.List[EnvVar]:
        """ Creates new environment variables. Granular scopes are available on Pro plans and above.  To use this endpoint, your site must no longer be using the &lt;a href&#x3D;&quot;https://docs.netlify.com/environment-variables/classic-experience/&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI. """
        endpoint = f"/accounts/{account_id}/env"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        if site_id is not None:
            params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, EnvVar)
        return response

    def update_site_build_log(self, build_id: str) -> typing.Any:
        """  """
        endpoint = f"/builds/{build_id}/log"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["build_id"] = build_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def notify_build_start(self, build_id: str) -> typing.Any:
        """  """
        endpoint = f"/builds/{build_id}/start"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["build_id"] = build_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def create_deploy_key(self) -> DeployKey:
        """  """
        endpoint = f"/deploy_keys"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = DeployKey.from_dict(response)
        return response

    def cancel_site_deploy(self, deploy_id: str) -> Deploy:
        """  """
        endpoint = f"/deploys/{deploy_id}/cancel"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["deploy_id"] = deploy_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def lock_deploy(self, deploy_id: str) -> Deploy:
        """  """
        endpoint = f"/deploys/{deploy_id}/lock"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["deploy_id"] = deploy_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def unlock_deploy(self, deploy_id: str) -> Deploy:
        """  """
        endpoint = f"/deploys/{deploy_id}/unlock"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["deploy_id"] = deploy_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def create_dns_zone(self, request_body: DNSZoneSetup) -> DNSZone:
        """  """
        endpoint = f"/dns_zones"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = DNSZone.from_dict(response)
        return response

    def create_dns_record(self, request_body: DNSRecordCreate, zone_id: str) -> DNSRecord:
        """  """
        endpoint = f"/dns_zones/{zone_id}/dns_records"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["zone_id"] = zone_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = DNSRecord.from_dict(response)
        return response

    def create_hook_by_site_id(self, request_body: Hook, site_id: str) -> Hook:
        """  """
        endpoint = f"/hooks"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Hook.from_dict(response)
        return response

    def enable_hook(self, hook_id: str) -> Hook:
        """  """
        endpoint = f"/hooks/{hook_id}/enable"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["hook_id"] = hook_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Hook.from_dict(response)
        return response

    def create_ticket(self, client_id: str) -> Ticket:
        """  """
        endpoint = f"/oauth/tickets"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["client_id"] = client_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Ticket.from_dict(response)
        return response

    def exchange_ticket(self, ticket_id: str) -> AccessToken:
        """  """
        endpoint = f"/oauth/tickets/{ticket_id}/exchange"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["ticket_id"] = ticket_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = AccessToken.from_dict(response)
        return response

    def create_site(self, request_body: typing.Any, configure_dns: typing.Optional[bool] = None) -> Site:
        """ **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site. """
        endpoint = f"/sites"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        if configure_dns is not None:
            params["configure_dns"] = configure_dns
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Site.from_dict(response)
        return response

    def create_site_asset(self, site_id: str, content_type: str, name: str, size: int, visibility: typing.Optional[str] = None) -> AssetSignature:
        """  """
        endpoint = f"/sites/{site_id}/assets"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["content_type"] = content_type
        params["name"] = name
        params["size"] = size
        if visibility is not None:
            params["visibility"] = visibility
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = AssetSignature.from_dict(response)
        return response

    def create_site_build_hook(self, request_body: BuildHookSetup, site_id: str) -> BuildHook:
        """  """
        endpoint = f"/sites/{site_id}/build_hooks"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = BuildHook.from_dict(response)
        return response

    def create_site_build(self, request_body: BuildSetup, site_id: str) -> Build:
        """  """
        endpoint = f"/sites/{site_id}/builds"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Build.from_dict(response)
        return response

    def create_site_deploy(self, request_body: DeployFiles, site_id: str, branch: typing.Optional[str] = None, deploy_previews: typing.Optional[bool] = None, latest_published: typing.Optional[bool] = None, production: typing.Optional[bool] = None, state: typing.Optional[str] = None, title: typing.Optional[str] = None) -> Deploy:
        """  """
        endpoint = f"/sites/{site_id}/deploys"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        if branch is not None:
            params["branch"] = branch
        if deploy_previews is not None:
            params["deploy_previews"] = deploy_previews
        if latest_published is not None:
            params["latest_published"] = latest_published
        if production is not None:
            params["production"] = production
        if state is not None:
            params["state"] = state
        if title is not None:
            params["title"] = title
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def restore_site_deploy(self, site_id: str, deploy_id: str) -> Deploy:
        """  """
        endpoint = f"/sites/{site_id}/deploys/{deploy_id}/restore"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["deploy_id"] = deploy_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def create_service_instance(self, request_body: typing.Any, site_id: str, addon: str) -> ServiceInstance:
        """  """
        endpoint = f"/sites/{site_id}/services/{addon}/instances"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["addon"] = addon
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = ServiceInstance.from_dict(response)
        return response

    def create_site_snippet(self, request_body: Snippet, site_id: str) -> Snippet:
        """  """
        endpoint = f"/sites/{site_id}/snippets"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Snippet.from_dict(response)
        return response

    def provision_site_tls_certificate(self, site_id: str, ca_certificates: typing.Optional[str] = None, certificate: typing.Optional[str] = None, key: typing.Optional[str] = None) -> SniCertificate:
        """  """
        endpoint = f"/sites/{site_id}/ssl"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        if ca_certificates is not None:
            params["ca_certificates"] = ca_certificates
        if certificate is not None:
            params["certificate"] = certificate
        if key is not None:
            params["key"] = key
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = SniCertificate.from_dict(response)
        return response

    def create_split_test(self, request_body: SplitTestSetup, site_id: str) -> SplitTest:
        """  """
        endpoint = f"/sites/{site_id}/traffic_splits"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = SplitTest.from_dict(response)
        return response

    def enable_split_test(self, site_id: str, split_test_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/traffic_splits/{split_test_id}/publish"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["split_test_id"] = split_test_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def disable_split_test(self, site_id: str, split_test_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/traffic_splits/{split_test_id}/unpublish"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["split_test_id"] = split_test_id
        raw_response = self.session.post(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def add_member_to_account(self, request_body: AccountAddMemberSetup, account_slug: str) -> typing.List[Member]:
        """  """
        endpoint = f"/{account_slug}/members"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_slug"] = account_slug
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, Member)
        return response

    def create_site_in_team(self, request_body: typing.Any, account_slug: str, configure_dns: typing.Optional[bool] = None) -> Site:
        """ **Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site. """
        endpoint = f"/{account_slug}/sites"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_slug"] = account_slug
        if configure_dns is not None:
            params["configure_dns"] = configure_dns
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.post(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Site.from_dict(response)
        return response

    def update_account(self, request_body: AccountUpdateSetup, account_id: str) -> AccountMembership:
        """  """
        endpoint = f"/accounts/{account_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = AccountMembership.from_dict(response)
        return response

    def update_env_var(self, request_body: PutAccountsAccountIDEnvKeyBody, account_id: str, key: str, site_id: typing.Optional[str] = None) -> EnvVar:
        """ Updates an existing environment variable and all of its values. Existing values will be replaced by values provided. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;&quot;https://docs.netlify.com/environment-variables/classic-experience/&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI. """
        endpoint = f"/accounts/{account_id}/env/{key}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_id"] = account_id
        params["key"] = key
        if site_id is not None:
            params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = EnvVar.from_dict(response)
        return response

    def upload_deploy_file(self, request_body: str, deploy_id: str, path: str, size: typing.Optional[int] = None) -> File:
        """  """
        endpoint = f"/deploys/{deploy_id}/files/{path}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["deploy_id"] = deploy_id
        params["path"] = path
        if size is not None:
            params["size"] = size
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = File.from_dict(response)
        return response

    def upload_deploy_function(self, request_body: str, deploy_id: str, name: str, invocation_mode: typing.Optional[str] = None, runtime: typing.Optional[str] = None, size: typing.Optional[int] = None) -> Function:
        """  """
        endpoint = f"/deploys/{deploy_id}/functions/{name}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["deploy_id"] = deploy_id
        params["name"] = name
        if invocation_mode is not None:
            params["invocation_mode"] = invocation_mode
        if runtime is not None:
            params["runtime"] = runtime
        if size is not None:
            params["size"] = size
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Function.from_dict(response)
        return response

    def transfer_dns_zone(self, zone_id: str, account_id: str, transfer_account_id: str, transfer_user_id: str) -> DNSZone:
        """  """
        endpoint = f"/dns_zones/{zone_id}/transfer"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["zone_id"] = zone_id
        params["account_id"] = account_id
        params["transfer_account_id"] = transfer_account_id
        params["transfer_user_id"] = transfer_user_id
        raw_response = self.session.put(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = DNSZone.from_dict(response)
        return response

    def update_hook(self, request_body: Hook, hook_id: str) -> Hook:
        """  """
        endpoint = f"/hooks/{hook_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["hook_id"] = hook_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Hook.from_dict(response)
        return response

    def update_site_asset(self, site_id: str, asset_id: str, state: str) -> Asset:
        """  """
        endpoint = f"/sites/{site_id}/assets/{asset_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["asset_id"] = asset_id
        params["state"] = state
        raw_response = self.session.put(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Asset.from_dict(response)
        return response

    def update_site_build_hook(self, request_body: BuildHookSetup, site_id: str, id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/build_hooks/{id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["id"] = id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def update_site_deploy(self, request_body: DeployFiles, site_id: str, deploy_id: str) -> Deploy:
        """  """
        endpoint = f"/sites/{site_id}/deploys/{deploy_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["deploy_id"] = deploy_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Deploy.from_dict(response)
        return response

    def configure_dns_for_site(self, site_id: str) -> typing.List[DNSZone]:
        """  """
        endpoint = f"/sites/{site_id}/dns"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.put(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = self._cast_list(response, DNSZone)
        return response

    def update_site_metadata(self, request_body: typing.Any, site_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/metadata"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def rollback_site_deploy(self, site_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/rollback"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.put(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def update_service_instance(self, request_body: typing.Any, site_id: str, addon: str, instance_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/services/{addon}/instances/{instance_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["addon"] = addon
        params["instance_id"] = instance_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def update_site_snippet(self, request_body: Snippet, site_id: str, snippet_id: str) -> typing.Any:
        """  """
        endpoint = f"/sites/{site_id}/snippets/{snippet_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["snippet_id"] = snippet_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        return response

    def update_split_test(self, request_body: SplitTestSetup, site_id: str, split_test_id: str) -> SplitTest:
        """  """
        endpoint = f"/sites/{site_id}/traffic_splits/{split_test_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        params["split_test_id"] = split_test_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = SplitTest.from_dict(response)
        return response

    def unlink_site_repo(self, site_id: str) -> Site:
        """ [Beta] Unlinks the repo from the site. -  - This action will also: - - Delete associated deploy keys - - Delete outgoing webhooks for the repo - - Delete the site&#x27;s build hooks """
        endpoint = f"/sites/{site_id}/unlink_repo"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["site_id"] = site_id
        raw_response = self.session.put(url, params=params)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Site.from_dict(response)
        return response

    def update_account_member(self, request_body: AccountUpdateMemberSetup, account_slug: str, member_id: str) -> Member:
        """  """
        endpoint = f"/{account_slug}/members/{member_id}"
        url = urljoin(self.base_url, endpoint)
        params = {} #type: dict[str, typing.Any]
        params["account_slug"] = account_slug
        params["member_id"] = member_id
        json_data = self._to_json_encodable(request_body)
        raw_response = self.session.put(url, params=params, json=json_data)
        response = raw_response.json() if raw_response.ok else self._raise_exception(raw_response)
        response = Member.from_dict(response)
        return response


