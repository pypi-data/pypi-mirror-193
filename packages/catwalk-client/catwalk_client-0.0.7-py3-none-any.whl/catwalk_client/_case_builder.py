from typing import Any, Union, List


class CaseBuilder:

    _case_id = ""
    _query: List[dict]
    _context: List[dict]
    _response: List[dict]
    _metadata: dict

    def __init__(self, client):
        self._client = client
        self._case_id = ""
        self._query = []
        self._context = []
        self._response = []
        self._metadata = {}

    def set_case_id(self, case_id: str):
        self._case_id = case_id
        return self

    def add_query(self, name: str, value: Any, type: Union[str, dict]):
        self._query.append({"name": name, "value": value, "type": type})
        return self

    def add_context(self, name: str, value: Any, type: Union[str, dict]):
        self._context.append({"name": name, "value": value, "type": type})
        return self

    def add_response(
        self,
        name: str,
        value: Any,
        type: Union[str, dict],
        evaluation: List[dict] = None,
    ):
        self._response.append(
            {"name": name, "value": value, "type": type, "evaluation": evaluation or []}
        )
        return self

    def add_evaluation(self, question: str, name: str, **kwargs):
        self._response[-1]["evaluation"].append(
            {"question": question, "name": name, **kwargs}
        )
        return self

    def set_metadata(self, **kwargs):
        self._metadata = kwargs
        return self

    def send(self):
        self._client.send(
            self._case_id,
            {
                "query": self._query,
                "context": self._context,
                "response": self._response,
                "metadata": self._metadata,
            },
        )
