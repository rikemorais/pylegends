from typing import Any, Dict, List

import dash
import pandas as pd
from dash import Input, Output, dash_table, dcc, html

from pylegends.utils.config import LocalPathMastery


class Dashboard:
    """Class to create an interactive dashboard using Dash.

    This dashboard displays a periodically updated table with data on champions' mastery.

    Attributes:
        app (dash.Dash): Dash app instance.
        data (pd.DataFrame): DataFrame containing the data to be displayed on the dashboard.
        columns (List[Dict[str, str]]): configuration of columns for the Dash table.
    """

    def __init__(self) -> None:
        """Initializes the Dashboard class, loads the data and configures the Dash layout and callbacks."""
        self.data = pd.read_csv(LocalPathMastery.FINAL)
        self.app = dash.Dash(__name__)
        self.load_data()
        self.columns = [{"name": col.capitalize(), "id": col} for col in self.data.columns]
        self.app.layout = self.create_layout()
        self.setup_callbacks()

    def run(self) -> None:
        """Starts the Dash server."""
        self.app.run_server(debug=True)

    def load_data(self) -> None:
        """Loads data from the CSV file specified in the config."""
        self.data["title"] = self.data["title"].str.title()

    def create_layout(self) -> html.Div:
        """Creates the HTML layout of the dashboard.

        Returns:
            html.Div: A Dash HTML component that represents the dashboard layout.
        """
        return html.Div(
            [
                html.H1("Champion Mastery", style={"textAlign": "center"}),
                dcc.Interval(
                    id="interval-component",
                    interval=1 * 1000,  # in milliseconds
                    n_intervals=0,
                ),
                dash_table.DataTable(
                    id="data-table",
                    columns=self.columns,
                    data=self.data.to_dict("records"),
                    sort_action="native",
                    style_header={
                        "backgroundColor": "darkblue",
                        "color": "white",
                        "fontWeight": "bold",
                        "textAlign": "center",
                    },
                    sort_by=[
                        {"column_id": "level", "direction": "desc"},
                        {"column_id": "points", "direction": "desc"},
                    ],
                ),
            ]
        )

    def setup_callbacks(self) -> None:
        """Configures callbacks for the Dash application."""
        self.app.callback(Output("data-table", "data"), Input("interval-component", "n_intervals"))(self.update_data)

    def update_data(self, n_intervals: int) -> List[Dict[str, Any]]:
        """Updates table data every defined time interval.

        Args:
            n_intervals (int): The number of times the interval has been triggered.

        Returns:
            List[Dict[str, Any]]: List of dictionaries representing the updated rows of the table.
        """
        self.load_data()
        return self.data.to_dict("records")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()
