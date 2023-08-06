from zs_utils.api.amocrm.base_api import AmocrmAPI


class GetAmocrmLeadAPI(AmocrmAPI):
    http_method = "GET"
    resource_method = "api/v4/leads/{lead_id}"
    required_params = ["lead_id"]
    allowed_params = ["with"]


class CreateAmocrmLeadAPI(AmocrmAPI):
    http_method = "POST"
    resource_method = "api/v4/leads"
    required_params = [
        "pipeline_id",
        "_embedded",
    ]
    allowed_params = [
        "status_id",
        "custom_fields_values",
        "name",
        "responsible_user_id",
    ]


class UpdateAmocrmLeadAPI(AmocrmAPI):
    http_method = "PATCH"
    resource_method = "api/v4/leads"
    required_params = [
        "id",
    ]
    allowed_params = [
        "name",
        "pipeline_id",
        "_embedded",
        "status_id",
        "custom_fields_values",
    ]


class CreateAmocrmContactAPI(AmocrmAPI):
    http_method = "POST"
    resource_method = "api/v4/contacts"
    required_params = []
    allowed_params = [
        "name",
        "first_name",
        "last_name",
        "custom_fields_values",
        "responsible_user_id",
    ]


class CreateAmocrmTaskAPI(AmocrmAPI):
    http_method = "POST"
    resource_method = "api/v4/tasks"
    required_params = [
        "text",
        "complete_till",
    ]
    allowed_params = [
        "responsible_user_id",
        "created_by",
        "entity_id",
        "entity_type",
    ]
