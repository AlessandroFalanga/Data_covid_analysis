# COVID-19 Data Analysis

## Project Overview

This project analyzes an example of COVID-19 data in Italy using Python.

The objective is to explore the evolution of daily cases,
calculate descriptive statistics and visualize the
trend of new infections over time.

## Technologies

- Python
- Pandas
- Matplotlib
- Seaborn

## Project Structure

```text
covid-data-analysis/
│
├── data/
│   └── covid_sample.csv
│
├── outputs/
│    └── Covid_trend_italy.png
├── src/
│   └── analisi_dati_covid.py
│
├── README.md
├── requirements.txt
├── .gitignore
```

## Dataset

The project uses a CSV dataset containing:

- Location
- Date
- New cases
- Total cases
- New deaths
- Total deaths
- Population
- 7-day moving average
- Cases per 100k inhabitants

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Execute the following command
from the project root directory:

```bash
python src/analisi_dati_covid.py
```

## Analysis

The script performs:

1. Dataset loading.
2. Data selection and preprocessing.
3. Filtering of Italian data.
4. Descriptive statistical analysis.
5. Visualization of daily new cases.

The generated chart is saved in the outputs folder.

## Author

Alessandro Falanga
