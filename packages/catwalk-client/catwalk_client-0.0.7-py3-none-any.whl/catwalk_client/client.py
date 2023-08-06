import logging
import os
import requests

from datetime import datetime, timedelta
from pydantic import error_wrappers

from ._case_builder import CaseBuilder
from ._case_exporter import CaseExporter
from catwalk_client.common.constants import CATWALK_AUTH_HEADER
from catwalk_common import CommonCaseFormat


logger = logging.getLogger("catwalk_client")
logging.basicConfig(level=logging.INFO)


def _hour_range(start, end):
    while start < end:
        yield start
        start += timedelta(hours=1)


class CatwalkClient:
    submitter_name: str
    submitter_version: str
    catwalk_url: str
    auth_token: str = None

    def __init__(
        self,
        auth_token: str = None,
        submitter_name: str = None,
        submitter_version: str = None,
        catwalk_url: str = None,
    ):
        self.catwalk_url = catwalk_url or os.environ.get("CATWALK_URL")
        self.auth_token = auth_token
        self.submitter_name = submitter_name
        self.submitter_version = submitter_version

    def get_auth_token(self) -> str:
        return self.auth_token

    def new_case(self) -> CaseBuilder:
        return CaseBuilder(client=self)

    def _get_url(self, path: str):
        return self.catwalk_url.rstrip("/") + path

    def send(self, case_id: str, case: dict):
        try:
            case = CommonCaseFormat(
                submitter={
                    "name": self.submitter_name,
                    "version": self.submitter_version,
                },
                case_id=case_id,
                **case,
            )

            response = requests.post(
                self.__get_url("/api/cases/collect"),
                data=case.json(),
                headers={CATWALK_AUTH_HEADER: f"Bearer {self.auth_token}"},
            )

            if response.ok:
                logger.info(f" Collected catwalk case: {response.json()['id']}")
            else:
                logger.error(
                    f" Error while collecting catwalk case:\n[{response.status_code}]: \n{response.json()['error_type']}\n{str(response.json()['error'])}"
                )
        except requests.exceptions.ConnectionError as ex:
            logger.error(" Couldn't connect with the server!")
        except error_wrappers.ValidationError as ex:
            logger.error(f" {ex}")
        except Exception as ex:
            logger.error(f" {type(ex).__name__}: \n{str(ex)}")

    def export_cases(
        self,
        from_datetime: datetime,
        to_datetime: datetime,
        submitter_name: str = None,
        submitter_version: str = None,
        max_retries: int = 5,
    ):
        exporter = CaseExporter(
            auth_token=self.auth_token,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            catwalk_url=self.catwalk_url,
            submitter_name=submitter_name,
            submitter_version=submitter_version,
            max_retries=max_retries,
        )
        yield from exporter.export()

    def __get_url(self, path: str):
        return self.catwalk_url.rstrip("/") + path
