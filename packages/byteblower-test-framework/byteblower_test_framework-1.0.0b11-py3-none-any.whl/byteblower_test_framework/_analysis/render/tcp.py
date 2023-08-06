from typing import Optional  # for type hinting

from ..data_analysis.tcp import HttpDataAnalyser
from ..plotting import GenericChart
from .renderer import AnalysisDetails, Renderer


class HttpRenderer(Renderer):

    __slots__ = ('_data_analyser', )

    def __init__(self, data_analyser: HttpDataAnalyser) -> None:
        super().__init__()
        self._data_analyser = data_analyser

    def render(self) -> str:
        analysis_log = self._data_analyser.log

        # Get the data
        # df_tx = self._data_analyser.df_tx
        # df_rx = self._data_analyser.df_rx
        df_dataspeed = self._data_analyser.df_dataspeed

        # Set the summary
        result = self._verbatim(analysis_log)

        # Build the graph
        chart = GenericChart(
            "HTTP statistics",
            x_axis_options={"type": "datetime"},
            chart_options={"zoomType": "x"}
        )
        # chart.add_series(list(df_tx.itertuples(index=True)), "line", "TX",
        #                  "Data count", "bytes")
        # chart.add_series(list(df_rx.itertuples(index=True)), "line", "RX",
        #                  "Data count", "bytes")
        chart.add_series(
            list(df_dataspeed.itertuples(index=True)), "line", "AVG dataspeed",
            "Dataspeed", "bytes/s"
        )
        result += chart.plot()

        return result

    def details(self) -> Optional[AnalysisDetails]:

        # Get the data
        df_http_client = self._data_analyser.df_http_client
        df_http_server = self._data_analyser.df_http_server

        df_overtimeresults_client = df_http_client[[
            'duration', 'TX Bytes', 'RX Bytes'
        ]]

        df_overtimeresults_client = df_overtimeresults_client.rename(
            columns={
                'TX Bytes': 'txBytes',
                'RX Bytes': 'rxBytes',
            }
        )

        df_overtimeresults_server = df_http_server[[
            'duration', 'TX Bytes', 'RX Bytes'
        ]]

        df_overtimeresults_server = df_overtimeresults_server.rename(
            columns={
                'TX Bytes': 'txBytes',
                'RX Bytes': 'rxBytes',
            }
        )

        details: AnalysisDetails = {
            'httpClient': {
                'overTimeResult': df_overtimeresults_client
            },
            'httpServer': {
                'overTimeResult': df_overtimeresults_server
            }
        }

        return details
