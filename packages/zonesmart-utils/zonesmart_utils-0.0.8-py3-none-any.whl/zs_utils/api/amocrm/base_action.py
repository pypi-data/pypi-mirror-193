import requests

from zs_utils.api.constants import API_ERROR_REASONS
from zs_utils.api.base_action import APIAction
from zs_utils.api.amocrm import services


class AmoCRMAction(APIAction):
    description = "Взаимодествие с API amoCRM"

    VALIDATE_PARAMS = True

    def get_api_class_init_params(self, **kwargs) -> dict:
        return {
            "access_token": services.AmocrmService.retrieve_access_token(),
        }

    def process_custom_fields(self, data: dict, fields_mapping: dict):
        result = {"custom_fields_values": []}

        for key, value in data.items():
            if key in fields_mapping:
                if isinstance(value, list):
                    if not value:
                        continue
                    values = [{"value": item} for item in value]
                else:
                    if (value is None) or (value == ""):
                        continue
                    values = [{"value": value}]
                result["custom_fields_values"].append(
                    {"field_id": fields_mapping[key], "values": values}
                )
            else:
                result[key] = value

        if not result["custom_fields_values"]:
            result.pop("custom_fields_values")

        return result

    def get_error_message(self, results: dict, response: requests.Response) -> str:
        message = ""

        if results.get("detail"):
            message = results["detail"]
        elif results.get("title"):
            message = results["title"]

        if results.get("hint"):
            message += ". " + results["hint"]

        # TODO
        # if results.get("validation-errors"):
        #     message += str(results["validation-errors"])

        return message

    def get_error_reason(
        self, results: dict, response: requests.Response, error_message: str
    ) -> API_ERROR_REASONS:
        if results and results.get("hint") and (results["hint"] == "Token has expired"):
            return API_ERROR_REASONS.invalid_token
        return super().get_error_reason(results, response, error_message)
