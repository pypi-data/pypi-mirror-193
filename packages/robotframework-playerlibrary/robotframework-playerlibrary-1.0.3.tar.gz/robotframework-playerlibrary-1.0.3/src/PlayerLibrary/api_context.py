import json
from json import JSONDecodeError
from playwright.sync_api import APIResponse, expect
from .base_context import BaseContext
from .utils import pretty_logging
from robotlibcore import keyword


class APIContext(BaseContext):

    DEFAULT_CONTENT_TYPE_JSON = "application/json"
    DEFAULT_CONTENT_TYPE_FORM = "application/x-www-form-urlencoded"
    DEFAULT_HEADER_FORM = {"content-type": "application/x-www-form-urlencoded"}
    DEFAULT_HEADER_JSON = {"content-type": "application/json"}
    api_context = None

    def __init__(self):
        super().__init__()
        self.api = self.get_api_context()

    def get_api_context(self):
        if not APIContext.api_context:
            APIContext.api_context = self.player.request.new_context()
        return APIContext.api_context

    @keyword("rest post")
    def rest_post(self, url, headers, body, code=200):
        response = self.api.post(
            url,
            headers=json.loads(headers),
            data=body,
        )
        try:
            resp_body = response.json()
        except (JSONDecodeError, TypeError):
            resp_body = str(response.body())
        self.http_request_should_be_successful(response, code)
        pretty_logging(url)
        pretty_logging(headers)
        pretty_logging(body)
        pretty_logging(response.status)
        pretty_logging(resp_body)
        return resp_body

    @keyword("rest patch")
    def rest_patch(self, url, headers, body, code=200):
        response = self.api.patch(
            url,
            headers=json.loads(headers),
            data=body,
        )
        try:
            resp_body = response.json()
        except (JSONDecodeError, TypeError):
            resp_body = str(response.body())
        self.http_request_should_be_successful(response, code)
        pretty_logging(url)
        pretty_logging(headers)
        pretty_logging(body)
        pretty_logging(response.status)
        pretty_logging(resp_body)
        return resp_body

    @keyword("rest put")
    def rest_put(self, url, headers, body, code=200):
        response = self.api.put(
            url,
            headers=json.loads(headers),
            data=body,
        )
        try:
            resp_body = response.json()
        except (JSONDecodeError, TypeError):
            resp_body = str(response.body())
        self.http_request_should_be_successful(response, code)
        pretty_logging(url)
        pretty_logging(headers)
        pretty_logging(body)
        pretty_logging(response.status)
        pretty_logging(resp_body)
        return resp_body

    @keyword("rest delete")
    def rest_delete(self, url, headers, body, code=200):
        response = self.api.delete(
            url,
            headers=json.loads(headers),
            data=body,
        )
        try:
            resp_body = response.json()
        except (JSONDecodeError, TypeError):
            resp_body = str(response.body())
        self.http_request_should_be_successful(response, code)
        pretty_logging(url)
        pretty_logging(headers)
        pretty_logging(body)
        pretty_logging(response.status)
        pretty_logging(resp_body)
        return resp_body

    @keyword("rest get")
    def rest_get(self, url, headers, code=200):
        response = self.api.get(
            url,
            headers=json.loads(headers)
        )
        try:
            resp_body = response.json()
        except (JSONDecodeError, TypeError):
            resp_body = str(response.body())
        self.http_request_should_be_successful(response, code)
        pretty_logging(url)
        pretty_logging(headers)
        pretty_logging(response.status)
        pretty_logging(resp_body)
        return resp_body

    def rest_dispose(self):
        self.api.dispose()

    @keyword("http status code should be", tags=["deprecated"])
    def http_status_code_should_be(self, code):
        pass

    @keyword("http request should be successful")
    def http_request_should_be_successful(self, response: APIResponse, code):
        if str(code).startswith("2"):
            expect(response).to_be_ok()
        else:
            expect(response).not_to_be_ok()

    @keyword("create header")
    def create_header(self, token, content_type=DEFAULT_CONTENT_TYPE_JSON, x_time_travel_date=None, **kwargs):
        """
         Supported content-types:
         > application/json
         > application/x-www-form-urlencoded
         > multipart/form-data
         > undefined
        :param token:
        :param content_type:
        :param x_time_travel_date:
        :param kwargs:
        :return:
        """
        header = kwargs
        if token:
            header["Authorization"] = f"Bearer {token}"
        if content_type:
            header["content-type"] = content_type
        if x_time_travel_date:
            header["x-time-travel-date"] = x_time_travel_date
        return json.dumps(header)
