# Stack Overflow Developer Survey Charts 2018

This repository is made for visualizing the Stack Overflow Developer Survey 2018 results. Currently only Python related stats are visualized.

## Charts

You can see generated charts for Python related stats in the following pages.

- [plot_so_developer_survey_python.ipynb](https://github.com/gh640/stack-overflow-developer-survey-charts/blob/master/plot_so_developer_survey_python.ipynb)
- [charts.md](https://github.com/gh640/stack-overflow-developer-survey-charts/blob/master/charts.md)

## Prerequisites

- Docker
- Docker Compose

## Usage

If you want to run the notebook in your environment, follow the steps below.

1. Clone this repo.
2. Build Docker image.
3. Download the survey data.
4. Run Jupyter notebook.

### 1. Clone this repo.

Clone this repository.

```bash
$ git clone https://github.com/gh640/stack-overflow-developer-survey-charts-2018
```

### 2. Build Docker image.

```bash
```

### 3. Download the survey data.

Download the csv file which contains the survey results by clicking `Download Full Data Set (CSV)` in `2018` section in the following page.

- [Stack Overflow Insights - Developer Hiring, Marketing, and User Research](https://insights.stackoverflow.com/survey)

Then, extract the zip file and put the csv file named `survey_results_public.csv` under `data/` directory.

### 4. Run Jupyter notebook.

Now you've finished to prepare the environment and run the command below to see the Jupyter notebook. It can be done with Docker easily.

```bash
docker-compose up -d
docker-compose logs -f
```

Open the URL in the log stream with your browser. Then click `plot_so_developer_survey_python.ipynb` in the list.

## References

- [Stack Overflow Insights - Developer Hiring, Marketing, and User Research](https://insights.stackoverflow.com/survey)
- [Stack Overflow Developer Survey 2018](https://insights.stackoverflow.com/survey/2018)

## License

Licensed under MIT license.
