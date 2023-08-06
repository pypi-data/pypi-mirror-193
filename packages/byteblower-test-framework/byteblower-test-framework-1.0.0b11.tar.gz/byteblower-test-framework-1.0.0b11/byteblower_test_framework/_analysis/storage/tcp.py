import pandas

from .data_store import DataStore


class HttpData(DataStore):

    __slots__ = (
        '_df_tcp_client',
        '_df_tcp_server',
        '_avg_data_speed',
    )

    def __init__(self) -> None:
        self._df_tcp_client = pandas.DataFrame(
            columns=[
                'duration',
                'TX Bytes',
                'RX Bytes',
                'AVG dataspeed',
            ]
        )

        self._df_tcp_server = pandas.DataFrame(
            columns=[
                'duration',
                'TX Bytes',
                'RX Bytes',
                'AVG dataspeed',
            ]
        )
        self._avg_data_speed: float = None

    @property
    def df_tcp_client(self) -> pandas.DataFrame:
        """TCP result history."""
        return self._df_tcp_client

    @property
    def df_tcp_server(self) -> pandas.DataFrame:
        """TCP result history."""
        return self._df_tcp_server

    @property
    def avg_data_speed(self) -> float:
        """Average data speed in Bytes."""
        return self._avg_data_speed
