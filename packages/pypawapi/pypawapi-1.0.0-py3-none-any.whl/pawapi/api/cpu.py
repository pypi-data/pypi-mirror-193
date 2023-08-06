__all__ = ["Cpu"]

from pawapi.abc import AbstractEndpoint
from pawapi.response import Response


class Cpu(AbstractEndpoint):
    __endpoint = "cpu"

    def get_info(self) -> Response:
        """ Information about cpu usage """

        return self._client.get(f"{self.__endpoint}/")
