__all__ = ["Students"]

from pawapi.abc import AbstractEndpoint
from pawapi.response import Response


class Students(AbstractEndpoint):
    __endpoint = "students"

    def list(self) -> Response:
        """ List of students """

        return self._client.get(f"{self.__endpoint}/")

    def delete(self, student: str) -> Response:
        """ Delete a student """

        return self._client.delete(f"{self.__endpoint}/{student}/")
