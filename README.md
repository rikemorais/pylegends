# PyLegends

Project designed to collect data from the League of Legends Game API. The objective is to demonstrate some of my skills
as a Software and Data Engineer.

📖 [Documentation](https://rikemorais.github.io/pylegends/)

![](docs/assets/interrogate_badge.svg)


## How to use Pylegends

- First, you need the API key on the [Riot Developer Platform](https://developer.riotgames.com/). Open your terminal
and pass the key to the Environment variable called API_KEY.
- After that, you must inform the PUUID that you want to consult the data in `pylegends/utils/config.py.
- Now you run the `make run` command in the terminal to run the pipeline.
- Run the `make app` command in the terminal to run Dash.