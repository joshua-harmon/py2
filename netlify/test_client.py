import typing

from .main import Client
from .custom_types import *

def deep_flatten(li, result=None):
    result = result or []
    for i in li:
        if isinstance(i, list):
            result = deep_flatten(i, result=result)
        else:
            result.append(i)
    return result

def test_init():
    client = Netlify("API_TOKEN")
    assert client

def test_cancel_account():
    client = Netlify("API_TOKEN")
    response = client.cancel_account(
        account_id="string",
    )

    assert response is not None
    print(response)

def test_delete_env_var():
    client = Netlify("API_TOKEN")
    response = client.delete_env_var(
        account_id="string",
        key="string",
        site_id="string",
    )

    assert response is not None
    print(response)

def test_delete_env_var_value():
    client = Netlify("API_TOKEN")
    response = client.delete_env_var_value(
        account_id="string",
        key="string",
        id="string",
        site_id="string",
    )

    assert response is not None
    print(response)

def test_delete_deploy_key():
    client = Netlify("API_TOKEN")
    response = client.delete_deploy_key(
        key_id="string",
    )

    assert response is not None
    print(response)

def test_delete_deploy():
    client = Netlify("API_TOKEN")
    response = client.delete_deploy(
        deploy_id="string",
    )

    assert response is not None
    print(response)

def test_delete_dns_zone():
    client = Netlify("API_TOKEN")
    response = client.delete_dns_zone(
        zone_id="string",
    )

    assert response is not None
    print(response)

def test_delete_dns_record():
    client = Netlify("API_TOKEN")
    response = client.delete_dns_record(
        zone_id="string",
        dns_record_id="string",
    )

    assert response is not None
    print(response)

def test_delete_hook():
    client = Netlify("API_TOKEN")
    response = client.delete_hook(
        hook_id="string",
    )

    assert response is not None
    print(response)

def test_delete_site():
    client = Netlify("API_TOKEN")
    response = client.delete_site(
        site_id="string",
    )

    assert response is not None
    print(response)

def test_delete_site_asset():
    client = Netlify("API_TOKEN")
    response = client.delete_site_asset(
        site_id="string",
        asset_id="string",
    )

    assert response is not None
    print(response)

def test_delete_site_build_hook():
    client = Netlify("API_TOKEN")
    response = client.delete_site_build_hook(
        site_id="string",
        id="string",
    )

    assert response is not None
    print(response)

def test_delete_site_deploy():
    client = Netlify("API_TOKEN")
    response = client.delete_site_deploy(
        site_id="string",
        deploy_id="string",
    )

    assert response is not None
    print(response)

def test_delete_site_form():
    client = Netlify("API_TOKEN")
    response = client.delete_site_form(
        site_id="string",
        form_id="string",
    )

    assert response is not None
    print(response)

def test_delete_service_instance():
    client = Netlify("API_TOKEN")
    response = client.delete_service_instance(
        site_id="string",
        addon="string",
        instance_id="string",
    )

    assert response is not None
    print(response)

def test_delete_site_snippet():
    client = Netlify("API_TOKEN")
    response = client.delete_site_snippet(
        site_id="string",
        snippet_id="string",
    )

    assert response is not None
    print(response)

def test_delete_submission():
    client = Netlify("API_TOKEN")
    response = client.delete_submission(
        submission_id="string",
    )

    assert response is not None
    print(response)

def test_remove_account_member():
    client = Netlify("API_TOKEN")
    response = client.remove_account_member(
        account_slug="string",
        member_id="string",
    )

    assert response is not None
    print(response)

def test_list_accounts_for_user():
    client = Netlify("API_TOKEN")
    response = client.list_accounts_for_user()

    items = deep_flatten(response)
    assert all(isinstance(i, AccountMembership) for i in items )
    print(response)

def test_list_account_types_for_user():
    client = Netlify("API_TOKEN")
    response = client.list_account_types_for_user()

    items = deep_flatten(response)
    assert all(isinstance(i, AccountType) for i in items )
    print(response)

def test_get_account():
    client = Netlify("API_TOKEN")
    response = client.get_account(
        account_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, AccountMembership) for i in items )
    print(response)

def test_list_account_audit_events():
    client = Netlify("API_TOKEN")
    response = client.list_account_audit_events(
        account_id="string",
        log_type="string",
        page=123,
        per_page=123,
        query="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, AuditLog) for i in items )
    print(response)

def test_get_env_vars():
    client = Netlify("API_TOKEN")
    response = client.get_env_vars(
        account_id="string",
        context_name="string",
        scope="string",
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, EnvVar) for i in items )
    print(response)

def test_get_env_var():
    client = Netlify("API_TOKEN")
    response = client.get_env_var(
        account_id="string",
        key="string",
        site_id="string",
    )

    assert isinstance(response, EnvVar)
    print(response)

def test_list_payment_methods_for_user():
    client = Netlify("API_TOKEN")
    response = client.list_payment_methods_for_user()

    items = deep_flatten(response)
    assert all(isinstance(i, PaymentMethod) for i in items )
    print(response)

def test_get_site_build():
    client = Netlify("API_TOKEN")
    response = client.get_site_build(
        build_id="string",
    )

    assert isinstance(response, Build)
    print(response)

def test_list_deploy_keys():
    client = Netlify("API_TOKEN")
    response = client.list_deploy_keys()

    items = deep_flatten(response)
    assert all(isinstance(i, DeployKey) for i in items )
    print(response)

def test_get_deploy_key():
    client = Netlify("API_TOKEN")
    response = client.get_deploy_key(
        key_id="string",
    )

    assert isinstance(response, DeployKey)
    print(response)

def test_get_deploy():
    client = Netlify("API_TOKEN")
    response = client.get_deploy(
        deploy_id="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_get_dns_zones():
    client = Netlify("API_TOKEN")
    response = client.get_dns_zones(
        account_slug="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, DNSZone) for i in items )
    print(response)

def test_get_dns_zone():
    client = Netlify("API_TOKEN")
    response = client.get_dns_zone(
        zone_id="string",
    )

    assert isinstance(response, DNSZone)
    print(response)

def test_get_dns_records():
    client = Netlify("API_TOKEN")
    response = client.get_dns_records(
        zone_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, DNSRecord) for i in items )
    print(response)

def test_get_individual_dns_record():
    client = Netlify("API_TOKEN")
    response = client.get_individual_dns_record(
        zone_id="string",
        dns_record_id="string",
    )

    assert isinstance(response, DNSRecord)
    print(response)

def test_list_form_submissions():
    client = Netlify("API_TOKEN")
    response = client.list_form_submissions(
        form_id="string",
        page=123,
        per_page=123,
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Submission) for i in items )
    print(response)

def test_list_hooks_by_site_id():
    client = Netlify("API_TOKEN")
    response = client.list_hooks_by_site_id(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Hook) for i in items )
    print(response)

def test_list_hook_types():
    client = Netlify("API_TOKEN")
    response = client.list_hook_types()

    items = deep_flatten(response)
    assert all(isinstance(i, HookType) for i in items )
    print(response)

def test_get_hook():
    client = Netlify("API_TOKEN")
    response = client.get_hook(
        hook_id="string",
    )

    assert isinstance(response, Hook)
    print(response)

def test_show_ticket():
    client = Netlify("API_TOKEN")
    response = client.show_ticket(
        ticket_id="string",
    )

    assert isinstance(response, Ticket)
    print(response)

def test_get_services():
    client = Netlify("API_TOKEN")
    response = client.get_services(
        search="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Service) for i in items )
    print(response)

def test_show_service():
    client = Netlify("API_TOKEN")
    response = client.show_service(
        addon_name="string",
    )

    assert isinstance(response, Service)
    print(response)

def test_show_service_manifest():
    client = Netlify("API_TOKEN")
    response = client.show_service_manifest(
        addon_name="string",
    )

    assert response is not None
    print(response)

def test_list_sites():
    client = Netlify("API_TOKEN")
    response = client.list_sites(
        filter="string",
        name="string",
        page=123,
        per_page=123,
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Site) for i in items )
    print(response)

def test_get_site():
    client = Netlify("API_TOKEN")
    response = client.get_site(
        site_id="string",
    )

    assert isinstance(response, Site)
    print(response)

def test_list_site_assets():
    client = Netlify("API_TOKEN")
    response = client.list_site_assets(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Asset) for i in items )
    print(response)

def test_get_site_asset_info():
    client = Netlify("API_TOKEN")
    response = client.get_site_asset_info(
        site_id="string",
        asset_id="string",
    )

    assert isinstance(response, Asset)
    print(response)

def test_get_site_asset_public_signature():
    client = Netlify("API_TOKEN")
    response = client.get_site_asset_public_signature(
        site_id="string",
        asset_id="string",
    )

    assert isinstance(response, AssetPublicSignature)
    print(response)

def test_list_site_build_hooks():
    client = Netlify("API_TOKEN")
    response = client.list_site_build_hooks(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, BuildHook) for i in items )
    print(response)

def test_get_site_build_hook():
    client = Netlify("API_TOKEN")
    response = client.get_site_build_hook(
        site_id="string",
        id="string",
    )

    assert isinstance(response, BuildHook)
    print(response)

def test_list_site_builds():
    client = Netlify("API_TOKEN")
    response = client.list_site_builds(
        site_id="string",
        page=123,
        per_page=123,
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Build) for i in items )
    print(response)

def test_list_site_deployed_branches():
    client = Netlify("API_TOKEN")
    response = client.list_site_deployed_branches(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, DeployedBranch) for i in items )
    print(response)

def test_list_site_deploys():
    client = Netlify("API_TOKEN")
    response = client.list_site_deploys(
        site_id="string",
        branch="string",
        deploy_previews=True,
        latest_published=True,
        page=123,
        per_page=123,
        production=True,
        state="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Deploy) for i in items )
    print(response)

def test_get_site_deploy():
    client = Netlify("API_TOKEN")
    response = client.get_site_deploy(
        site_id="string",
        deploy_id="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_get_dns_for_site():
    client = Netlify("API_TOKEN")
    response = client.get_dns_for_site(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, DNSZone) for i in items )
    print(response)

def test_list_site_files():
    client = Netlify("API_TOKEN")
    response = client.list_site_files(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, File) for i in items )
    print(response)

def test_get_site_file_by_path_name():
    client = Netlify("API_TOKEN")
    response = client.get_site_file_by_path_name(
        site_id="string",
        file_path="string",
    )

    assert isinstance(response, File)
    print(response)

def test_list_site_forms():
    client = Netlify("API_TOKEN")
    response = client.list_site_forms(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Form) for i in items )
    print(response)

def test_get_site_metadata():
    client = Netlify("API_TOKEN")
    response = client.get_site_metadata(
        site_id="string",
    )

    assert response is not None
    print(response)

def test_list_service_instances_for_site():
    client = Netlify("API_TOKEN")
    response = client.list_service_instances_for_site(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, ServiceInstance) for i in items )
    print(response)

def test_show_service_instance():
    client = Netlify("API_TOKEN")
    response = client.show_service_instance(
        site_id="string",
        addon="string",
        instance_id="string",
    )

    assert isinstance(response, ServiceInstance)
    print(response)

def test_list_site_snippets():
    client = Netlify("API_TOKEN")
    response = client.list_site_snippets(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Snippet) for i in items )
    print(response)

def test_get_site_snippet():
    client = Netlify("API_TOKEN")
    response = client.get_site_snippet(
        site_id="string",
        snippet_id="string",
    )

    assert isinstance(response, Snippet)
    print(response)

def test_show_site_tls_certificate():
    client = Netlify("API_TOKEN")
    response = client.show_site_tls_certificate(
        site_id="string",
    )

    assert isinstance(response, SniCertificate)
    print(response)

def test_list_site_submissions():
    client = Netlify("API_TOKEN")
    response = client.list_site_submissions(
        site_id="string",
        page=123,
        per_page=123,
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Submission) for i in items )
    print(response)

def test_get_split_tests():
    client = Netlify("API_TOKEN")
    response = client.get_split_tests(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, SplitTest) for i in items )
    print(response)

def test_get_split_test():
    client = Netlify("API_TOKEN")
    response = client.get_split_test(
        site_id="string",
        split_test_id="string",
    )

    assert isinstance(response, SplitTest)
    print(response)

def test_list_form_submission():
    client = Netlify("API_TOKEN")
    response = client.list_form_submission(
        submission_id="string",
        page=123,
        per_page=123,
        query="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Submission) for i in items )
    print(response)

def test_get_current_user():
    client = Netlify("API_TOKEN")
    response = client.get_current_user()

    items = deep_flatten(response)
    assert all(isinstance(i, User) for i in items )
    print(response)

def test_get_account_build_status():
    client = Netlify("API_TOKEN")
    response = client.get_account_build_status(
        account_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, BuildStatus) for i in items )
    print(response)

def test_list_members_for_account():
    client = Netlify("API_TOKEN")
    response = client.list_members_for_account(
        account_slug="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Member) for i in items )
    print(response)

def test_get_account_member():
    client = Netlify("API_TOKEN")
    response = client.get_account_member(
        account_slug="string",
        member_id="string",
    )

    assert isinstance(response, Member)
    print(response)

def test_list_sites_for_account():
    client = Netlify("API_TOKEN")
    response = client.list_sites_for_account(
        account_slug="string",
        name="string",
        page=123,
        per_page=123,
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Site) for i in items )
    print(response)

def test_set_env_var_value():
    client = Netlify("API_TOKEN")
    request_body = PatchAccountsAccountIDEnvKeyBody.from_dict({
      "context": "string",
      "context_parameter": "string",
      "value": "string"
    })
    
    response = client.set_env_var_value(
        request_body=request_body,
        account_id="string",
        key="string",
        site_id="string",
    )

    assert isinstance(response, EnvVar)
    print(response)

def test_update_site():
    client = Netlify("API_TOKEN")
    request_body = {
      "account_name": "string",
      "account_slug": "string",
      "admin_url": "string",
      "branch_deploy_custom_domain": "string",
      "build_image": "string",
      "build_settings": {
        "allowed_branches": [
          "string"
        ],
        "cmd": "string",
        "deploy_key_id": "string",
        "dir": "string",
        "env": {},
        "functions_dir": "string",
        "id": 123,
        "installation_id": 123,
        "private_logs": True,
        "provider": "string",
        "public_repo": True,
        "repo_branch": "string",
        "repo_path": "string",
        "repo_url": "string",
        "stop_builds": True
      },
      "capabilities": {},
      "created_at": "string",
      "custom_domain": "string",
      "default_hooks_data": {
        "access_token": "string"
      },
      "deploy_hook": "string",
      "deploy_preview_custom_domain": "string",
      "deploy_url": "string",
      "domain_aliases": [
        "string"
      ],
      "force_ssl": True,
      "git_provider": "string",
      "id": "string",
      "id_domain": "string",
      "managed_dns": True,
      "name": "string",
      "notification_email": "string",
      "password": "string",
      "plan": "string",
      "prerender": "string",
      "processing_settings": {
        "css": {
          "bundle": True,
          "minify": True
        },
        "html": {
          "pretty_urls": True
        },
        "images": {
          "optimize": True
        },
        "js": {
          "bundle": True,
          "minify": True
        },
        "skip": True
      },
      "published_deploy": {
        "admin_url": "string",
        "branch": "string",
        "build_id": "string",
        "commit_ref": "string",
        "commit_url": "string",
        "context": "string",
        "created_at": "string",
        "deploy_ssl_url": "string",
        "deploy_url": "string",
        "draft": True,
        "error_message": "string",
        "framework": "string",
        "function_schedules": [
          {
            "cron": "string",
            "name": "string"
          }
        ],
        "id": "string",
        "locked": True,
        "name": "string",
        "published_at": "string",
        "required": [
          "string"
        ],
        "required_functions": [
          "string"
        ],
        "review_id": 123.45,
        "review_url": "string",
        "screenshot_url": "string",
        "site_capabilities": {
          "large_media_enabled": True
        },
        "site_id": "string",
        "skipped": True,
        "ssl_url": "string",
        "state": "string",
        "title": "string",
        "updated_at": "string",
        "url": "string",
        "user_id": "string"
      },
      "repo": {
        "allowed_branches": [
          "string"
        ],
        "cmd": "string",
        "deploy_key_id": "string",
        "dir": "string",
        "env": {},
        "functions_dir": "string",
        "id": 123,
        "installation_id": 123,
        "private_logs": True,
        "provider": "string",
        "public_repo": True,
        "repo_branch": "string",
        "repo_path": "string",
        "repo_url": "string",
        "stop_builds": True
      },
      "screenshot_url": "string",
      "session_id": "string",
      "ssl": True,
      "ssl_url": "string",
      "state": "string",
      "updated_at": "string",
      "url": "string",
      "user_id": "string"
    }
    
    response = client.update_site(
        request_body=request_body,
        site_id="string",
    )

    assert isinstance(response, Site)
    print(response)

def test_create_account():
    client = Netlify("API_TOKEN")
    request_body = AccountSetup.from_dict({
      "extra_seats_block": 123,
      "name": "string",
      "payment_method_id": "string",
      "period": "string",
      "type_id": "string"
    })
    
    response = client.create_account(
        request_body=request_body,
    )

    assert isinstance(response, AccountMembership)
    print(response)

def test_create_env_vars():
    client = Netlify("API_TOKEN")
    request_body = [PostAccountsAccountIDEnvBodyItem.from_dict({
      "is_secret": True,
      "key": "string",
      "scopes": [
        "string"
      ],
      "values": [
        {
          "context": "string",
          "context_parameter": "string",
          "id": "string",
          "value": "string"
        }
      ]
    })]
    
    response = client.create_env_vars(
        request_body=request_body,
        account_id="string",
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, EnvVar) for i in items )
    print(response)

def test_update_site_build_log():
    client = Netlify("API_TOKEN")
    response = client.update_site_build_log(
        build_id="string",
    )

    assert response is not None
    print(response)

def test_notify_build_start():
    client = Netlify("API_TOKEN")
    response = client.notify_build_start(
        build_id="string",
    )

    assert response is not None
    print(response)

def test_create_deploy_key():
    client = Netlify("API_TOKEN")
    response = client.create_deploy_key()

    assert isinstance(response, DeployKey)
    print(response)

def test_cancel_site_deploy():
    client = Netlify("API_TOKEN")
    response = client.cancel_site_deploy(
        deploy_id="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_lock_deploy():
    client = Netlify("API_TOKEN")
    response = client.lock_deploy(
        deploy_id="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_unlock_deploy():
    client = Netlify("API_TOKEN")
    response = client.unlock_deploy(
        deploy_id="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_create_dns_zone():
    client = Netlify("API_TOKEN")
    request_body = DNSZoneSetup.from_dict({
      "account_slug": "string",
      "name": "string",
      "site_id": "string"
    })
    
    response = client.create_dns_zone(
        request_body=request_body,
    )

    assert isinstance(response, DNSZone)
    print(response)

def test_create_dns_record():
    client = Netlify("API_TOKEN")
    request_body = DNSRecordCreate.from_dict({
      "flag": 123,
      "hostname": "string",
      "port": 123,
      "priority": 123,
      "tag": "string",
      "ttl": 123,
      "type": "string",
      "value": "string",
      "weight": 123
    })
    
    response = client.create_dns_record(
        request_body=request_body,
        zone_id="string",
    )

    assert isinstance(response, DNSRecord)
    print(response)

def test_create_hook_by_site_id():
    client = Netlify("API_TOKEN")
    request_body = Hook.from_dict({
      "created_at": "string",
      "data": {},
      "disabled": True,
      "event": "string",
      "id": "string",
      "site_id": "string",
      "type": "string",
      "updated_at": "string"
    })
    
    response = client.create_hook_by_site_id(
        request_body=request_body,
        site_id="string",
    )

    assert isinstance(response, Hook)
    print(response)

def test_enable_hook():
    client = Netlify("API_TOKEN")
    response = client.enable_hook(
        hook_id="string",
    )

    assert isinstance(response, Hook)
    print(response)

def test_create_ticket():
    client = Netlify("API_TOKEN")
    response = client.create_ticket(
        client_id="string",
    )

    assert isinstance(response, Ticket)
    print(response)

def test_exchange_ticket():
    client = Netlify("API_TOKEN")
    response = client.exchange_ticket(
        ticket_id="string",
    )

    assert isinstance(response, AccessToken)
    print(response)

def test_create_site():
    client = Netlify("API_TOKEN")
    request_body = {
      "account_name": "string",
      "account_slug": "string",
      "admin_url": "string",
      "branch_deploy_custom_domain": "string",
      "build_image": "string",
      "build_settings": {
        "allowed_branches": [
          "string"
        ],
        "cmd": "string",
        "deploy_key_id": "string",
        "dir": "string",
        "env": {},
        "functions_dir": "string",
        "id": 123,
        "installation_id": 123,
        "private_logs": True,
        "provider": "string",
        "public_repo": True,
        "repo_branch": "string",
        "repo_path": "string",
        "repo_url": "string",
        "stop_builds": True
      },
      "capabilities": {},
      "created_at": "string",
      "custom_domain": "string",
      "default_hooks_data": {
        "access_token": "string"
      },
      "deploy_hook": "string",
      "deploy_preview_custom_domain": "string",
      "deploy_url": "string",
      "domain_aliases": [
        "string"
      ],
      "force_ssl": True,
      "git_provider": "string",
      "id": "string",
      "id_domain": "string",
      "managed_dns": True,
      "name": "string",
      "notification_email": "string",
      "password": "string",
      "plan": "string",
      "prerender": "string",
      "processing_settings": {
        "css": {
          "bundle": True,
          "minify": True
        },
        "html": {
          "pretty_urls": True
        },
        "images": {
          "optimize": True
        },
        "js": {
          "bundle": True,
          "minify": True
        },
        "skip": True
      },
      "published_deploy": {
        "admin_url": "string",
        "branch": "string",
        "build_id": "string",
        "commit_ref": "string",
        "commit_url": "string",
        "context": "string",
        "created_at": "string",
        "deploy_ssl_url": "string",
        "deploy_url": "string",
        "draft": True,
        "error_message": "string",
        "framework": "string",
        "function_schedules": [
          {
            "cron": "string",
            "name": "string"
          }
        ],
        "id": "string",
        "locked": True,
        "name": "string",
        "published_at": "string",
        "required": [
          "string"
        ],
        "required_functions": [
          "string"
        ],
        "review_id": 123.45,
        "review_url": "string",
        "screenshot_url": "string",
        "site_capabilities": {
          "large_media_enabled": True
        },
        "site_id": "string",
        "skipped": True,
        "ssl_url": "string",
        "state": "string",
        "title": "string",
        "updated_at": "string",
        "url": "string",
        "user_id": "string"
      },
      "repo": {
        "allowed_branches": [
          "string"
        ],
        "cmd": "string",
        "deploy_key_id": "string",
        "dir": "string",
        "env": {},
        "functions_dir": "string",
        "id": 123,
        "installation_id": 123,
        "private_logs": True,
        "provider": "string",
        "public_repo": True,
        "repo_branch": "string",
        "repo_path": "string",
        "repo_url": "string",
        "stop_builds": True
      },
      "screenshot_url": "string",
      "session_id": "string",
      "ssl": True,
      "ssl_url": "string",
      "state": "string",
      "updated_at": "string",
      "url": "string",
      "user_id": "string"
    }
    
    response = client.create_site(
        request_body=request_body,
        configure_dns=True,
    )

    assert isinstance(response, Site)
    print(response)

def test_create_site_asset():
    client = Netlify("API_TOKEN")
    response = client.create_site_asset(
        site_id="string",
        content_type="string",
        name="string",
        size=123,
        visibility="string",
    )

    assert isinstance(response, AssetSignature)
    print(response)

def test_create_site_build_hook():
    client = Netlify("API_TOKEN")
    request_body = BuildHookSetup.from_dict({
      "branch": "string",
      "title": "string"
    })
    
    response = client.create_site_build_hook(
        request_body=request_body,
        site_id="string",
    )

    assert isinstance(response, BuildHook)
    print(response)

def test_create_site_build():
    client = Netlify("API_TOKEN")
    request_body = BuildSetup.from_dict({
      "clear_cache": True,
      "image": "string"
    })
    
    response = client.create_site_build(
        request_body=request_body,
        site_id="string",
    )

    assert isinstance(response, Build)
    print(response)

def test_create_site_deploy():
    client = Netlify("API_TOKEN")
    request_body = DeployFiles.from_dict({
      "async": True,
      "branch": "string",
      "draft": True,
      "files": {},
      "framework": "string",
      "function_schedules": [
        {
          "cron": "string",
          "name": "string"
        }
      ],
      "functions": {},
      "functions_config": {}
    })
    
    response = client.create_site_deploy(
        request_body=request_body,
        site_id="string",
        branch="string",
        deploy_previews=True,
        latest_published=True,
        production=True,
        state="string",
        title="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_restore_site_deploy():
    client = Netlify("API_TOKEN")
    response = client.restore_site_deploy(
        site_id="string",
        deploy_id="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_create_service_instance():
    client = Netlify("API_TOKEN")
    request_body = {}
    
    response = client.create_service_instance(
        request_body=request_body,
        site_id="string",
        addon="string",
    )

    assert isinstance(response, ServiceInstance)
    print(response)

def test_create_site_snippet():
    client = Netlify("API_TOKEN")
    request_body = Snippet.from_dict({
      "general": "string",
      "general_position": "string",
      "goal": "string",
      "goal_position": "string",
      "id": 123,
      "site_id": "string",
      "title": "string"
    })
    
    response = client.create_site_snippet(
        request_body=request_body,
        site_id="string",
    )

    assert isinstance(response, Snippet)
    print(response)

def test_provision_site_tls_certificate():
    client = Netlify("API_TOKEN")
    response = client.provision_site_tls_certificate(
        site_id="string",
        ca_certificates="string",
        certificate="string",
        key="string",
    )

    assert isinstance(response, SniCertificate)
    print(response)

def test_create_split_test():
    client = Netlify("API_TOKEN")
    request_body = SplitTestSetup.from_dict({
      "branch_tests": {}
    })
    
    response = client.create_split_test(
        request_body=request_body,
        site_id="string",
    )

    assert isinstance(response, SplitTest)
    print(response)

def test_enable_split_test():
    client = Netlify("API_TOKEN")
    response = client.enable_split_test(
        site_id="string",
        split_test_id="string",
    )

    assert response is not None
    print(response)

def test_disable_split_test():
    client = Netlify("API_TOKEN")
    response = client.disable_split_test(
        site_id="string",
        split_test_id="string",
    )

    assert response is not None
    print(response)

def test_add_member_to_account():
    client = Netlify("API_TOKEN")
    request_body = AccountAddMemberSetup.from_dict({
      "email": "string",
      "role": "string"
    })
    
    response = client.add_member_to_account(
        request_body=request_body,
        account_slug="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, Member) for i in items )
    print(response)

def test_create_site_in_team():
    client = Netlify("API_TOKEN")
    request_body = {
      "account_name": "string",
      "account_slug": "string",
      "admin_url": "string",
      "branch_deploy_custom_domain": "string",
      "build_image": "string",
      "build_settings": {
        "allowed_branches": [
          "string"
        ],
        "cmd": "string",
        "deploy_key_id": "string",
        "dir": "string",
        "env": {},
        "functions_dir": "string",
        "id": 123,
        "installation_id": 123,
        "private_logs": True,
        "provider": "string",
        "public_repo": True,
        "repo_branch": "string",
        "repo_path": "string",
        "repo_url": "string",
        "stop_builds": True
      },
      "capabilities": {},
      "created_at": "string",
      "custom_domain": "string",
      "default_hooks_data": {
        "access_token": "string"
      },
      "deploy_hook": "string",
      "deploy_preview_custom_domain": "string",
      "deploy_url": "string",
      "domain_aliases": [
        "string"
      ],
      "force_ssl": True,
      "git_provider": "string",
      "id": "string",
      "id_domain": "string",
      "managed_dns": True,
      "name": "string",
      "notification_email": "string",
      "password": "string",
      "plan": "string",
      "prerender": "string",
      "processing_settings": {
        "css": {
          "bundle": True,
          "minify": True
        },
        "html": {
          "pretty_urls": True
        },
        "images": {
          "optimize": True
        },
        "js": {
          "bundle": True,
          "minify": True
        },
        "skip": True
      },
      "published_deploy": {
        "admin_url": "string",
        "branch": "string",
        "build_id": "string",
        "commit_ref": "string",
        "commit_url": "string",
        "context": "string",
        "created_at": "string",
        "deploy_ssl_url": "string",
        "deploy_url": "string",
        "draft": True,
        "error_message": "string",
        "framework": "string",
        "function_schedules": [
          {
            "cron": "string",
            "name": "string"
          }
        ],
        "id": "string",
        "locked": True,
        "name": "string",
        "published_at": "string",
        "required": [
          "string"
        ],
        "required_functions": [
          "string"
        ],
        "review_id": 123.45,
        "review_url": "string",
        "screenshot_url": "string",
        "site_capabilities": {
          "large_media_enabled": True
        },
        "site_id": "string",
        "skipped": True,
        "ssl_url": "string",
        "state": "string",
        "title": "string",
        "updated_at": "string",
        "url": "string",
        "user_id": "string"
      },
      "repo": {
        "allowed_branches": [
          "string"
        ],
        "cmd": "string",
        "deploy_key_id": "string",
        "dir": "string",
        "env": {},
        "functions_dir": "string",
        "id": 123,
        "installation_id": 123,
        "private_logs": True,
        "provider": "string",
        "public_repo": True,
        "repo_branch": "string",
        "repo_path": "string",
        "repo_url": "string",
        "stop_builds": True
      },
      "screenshot_url": "string",
      "session_id": "string",
      "ssl": True,
      "ssl_url": "string",
      "state": "string",
      "updated_at": "string",
      "url": "string",
      "user_id": "string"
    }
    
    response = client.create_site_in_team(
        request_body=request_body,
        account_slug="string",
        configure_dns=True,
    )

    assert isinstance(response, Site)
    print(response)

def test_update_account():
    client = Netlify("API_TOKEN")
    request_body = AccountUpdateSetup.from_dict({
      "billing_details": "string",
      "billing_email": "string",
      "billing_name": "string",
      "extra_seats_block": 123,
      "name": "string",
      "slug": "string",
      "type_id": "string"
    })
    
    response = client.update_account(
        request_body=request_body,
        account_id="string",
    )

    assert isinstance(response, AccountMembership)
    print(response)

def test_update_env_var():
    client = Netlify("API_TOKEN")
    request_body = PutAccountsAccountIDEnvKeyBody.from_dict({
      "is_secret": True,
      "key": "string",
      "scopes": [
        "string"
      ],
      "values": [
        {
          "context": "string",
          "context_parameter": "string",
          "id": "string",
          "value": "string"
        }
      ]
    })
    
    response = client.update_env_var(
        request_body=request_body,
        account_id="string",
        key="string",
        site_id="string",
    )

    assert isinstance(response, EnvVar)
    print(response)

def test_upload_deploy_file():
    client = Netlify("API_TOKEN")
    request_body = "path/to/file.pdf"
    
    response = client.upload_deploy_file(
        request_body=request_body,
        deploy_id="string",
        path="string",
        size=123,
    )

    assert isinstance(response, File)
    print(response)

def test_upload_deploy_function():
    client = Netlify("API_TOKEN")
    request_body = "path/to/file.pdf"
    
    response = client.upload_deploy_function(
        request_body=request_body,
        deploy_id="string",
        name="string",
        invocation_mode="string",
        runtime="string",
        size=123,
    )

    assert isinstance(response, Function)
    print(response)

def test_transfer_dns_zone():
    client = Netlify("API_TOKEN")
    response = client.transfer_dns_zone(
        zone_id="string",
        account_id="string",
        transfer_account_id="string",
        transfer_user_id="string",
    )

    assert isinstance(response, DNSZone)
    print(response)

def test_update_hook():
    client = Netlify("API_TOKEN")
    request_body = Hook.from_dict({
      "created_at": "string",
      "data": {},
      "disabled": True,
      "event": "string",
      "id": "string",
      "site_id": "string",
      "type": "string",
      "updated_at": "string"
    })
    
    response = client.update_hook(
        request_body=request_body,
        hook_id="string",
    )

    assert isinstance(response, Hook)
    print(response)

def test_update_site_asset():
    client = Netlify("API_TOKEN")
    response = client.update_site_asset(
        site_id="string",
        asset_id="string",
        state="string",
    )

    assert isinstance(response, Asset)
    print(response)

def test_update_site_build_hook():
    client = Netlify("API_TOKEN")
    request_body = BuildHookSetup.from_dict({
      "branch": "string",
      "title": "string"
    })
    
    response = client.update_site_build_hook(
        request_body=request_body,
        site_id="string",
        id="string",
    )

    assert response is not None
    print(response)

def test_update_site_deploy():
    client = Netlify("API_TOKEN")
    request_body = DeployFiles.from_dict({
      "async": True,
      "branch": "string",
      "draft": True,
      "files": {},
      "framework": "string",
      "function_schedules": [
        {
          "cron": "string",
          "name": "string"
        }
      ],
      "functions": {},
      "functions_config": {}
    })
    
    response = client.update_site_deploy(
        request_body=request_body,
        site_id="string",
        deploy_id="string",
    )

    assert isinstance(response, Deploy)
    print(response)

def test_configure_dns_for_site():
    client = Netlify("API_TOKEN")
    response = client.configure_dns_for_site(
        site_id="string",
    )

    items = deep_flatten(response)
    assert all(isinstance(i, DNSZone) for i in items )
    print(response)

def test_update_site_metadata():
    client = Netlify("API_TOKEN")
    request_body = {}
    
    response = client.update_site_metadata(
        request_body=request_body,
        site_id="string",
    )

    assert response is not None
    print(response)

def test_rollback_site_deploy():
    client = Netlify("API_TOKEN")
    response = client.rollback_site_deploy(
        site_id="string",
    )

    assert response is not None
    print(response)

def test_update_service_instance():
    client = Netlify("API_TOKEN")
    request_body = {}
    
    response = client.update_service_instance(
        request_body=request_body,
        site_id="string",
        addon="string",
        instance_id="string",
    )

    assert response is not None
    print(response)

def test_update_site_snippet():
    client = Netlify("API_TOKEN")
    request_body = Snippet.from_dict({
      "general": "string",
      "general_position": "string",
      "goal": "string",
      "goal_position": "string",
      "id": 123,
      "site_id": "string",
      "title": "string"
    })
    
    response = client.update_site_snippet(
        request_body=request_body,
        site_id="string",
        snippet_id="string",
    )

    assert response is not None
    print(response)

def test_update_split_test():
    client = Netlify("API_TOKEN")
    request_body = SplitTestSetup.from_dict({
      "branch_tests": {}
    })
    
    response = client.update_split_test(
        request_body=request_body,
        site_id="string",
        split_test_id="string",
    )

    assert isinstance(response, SplitTest)
    print(response)

def test_unlink_site_repo():
    client = Netlify("API_TOKEN")
    response = client.unlink_site_repo(
        site_id="string",
    )

    assert isinstance(response, Site)
    print(response)

def test_update_account_member():
    client = Netlify("API_TOKEN")
    request_body = AccountUpdateMemberSetup.from_dict({
      "role": "string",
      "site_access": "string",
      "site_ids": [
        "string"
      ]
    })
    
    response = client.update_account_member(
        request_body=request_body,
        account_slug="string",
        member_id="string",
    )

    assert isinstance(response, Member)
    print(response)


