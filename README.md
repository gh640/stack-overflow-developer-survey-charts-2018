# Stack Overflow Developer Survey Charts

This repository is made for visualizing the Stack Overflow Developer Survey results. Currently only Python related stats are visualized.

## Charts

You can see generated charts for Python related stats in the following pages.

- [plot_so_developer_survey_python.ipynb](https://github.com/gh640/stack-overflow-developer-survey-charts/blob/master/plot_so_developer_survey_python.ipynb)
- [charts.md](https://github.com/gh640/stack-overflow-developer-survey-charts/blob/master/charts.md)

## Usage

If you want to run the notebook in your environment, follow the steps below.

1. Clone this repo.
2. Install Python 3.x.
3. Install necessary Python modules.
4. Download the survey data.
5. Run Jupyter notebook.

### 1. Clone this repo.

Clone this repository.

```bash
$ git clone https://github.com/gh640/stack-overflow-developer-survey-charts
```

### 2. Install Python 3.x.

Install Python 3.x in your preferred way. The easiest way to install Python is to use a package manager like `yum`, `apt-get` or `brew`. You can also use officially distributed Python installers:

- [Download Python | Python.org](https://www.python.org/downloads/)

### 3. Install necessary Python modules.

Install Python modules necessary to run the notebook.

```bash
$ cd stack-overflow-developer-survey-charts
$ python3 -m pip install pipenv
$ python3 -m pipenv install
```

### 4. Download the survey data.

Download the csv file which contains the survey results by clicking `Download Full Data Set (CSV)` in `2018` section in the following page.

- [Stack Overflow Insights - Developer Hiring, Marketing, and User Research](https://insights.stackoverflow.com/survey)

Then, extract the zip file and put the csv file named `survey_results_public.csv` under `data/` directory.

You can use the script in this repo `download_data.py` to do this step in a command.

```bash
$ python3 download_data.py
Fetching the remote zip file...
Extracting the zip file...
Zip file has been extracted successfully to "/path/to/data".
```

### 5. Run Jupyter notebook.

Now you've finished to prepare the environment and run the command below to see the Jupyter notebook.

```bash
pipenv run jupyter notebook
```

Once a browser tab has opened automatically, click `plot_so_developer_survey_python.ipynb`.

## References

- [Stack Overflow Insights - Developer Hiring, Marketing, and User Research](https://insights.stackoverflow.com/survey)
- [Stack Overflow Developer Survey 2018](https://insights.stackoverflow.com/survey/2018)

## License

Licensed under MIT license.
