# Five Visualisations — Employee Data Analysis

## Project Overview
This project analyses employee data using Python, Pandas, and Matplotlib. It includes five visualisations to explore salary distribution, department-level salary patterns, and other data patterns.

## Dataset
- **File:** `employees.csv`
- **Records:** 8 employees
- **Columns:** `id`, `name`, `department`, `salary`, `city`

## Visualisations
The following charts are saved in `reports/figures/`:

1. `bar_chart.png` — Bar chart
2. `histogram.png` — Salary histogram
3. `scatter_plot.png` — Scatter plot
4. `line_chart.png` — Line chart
5. `box_plot.png` — Box plot

## Project Structure

```text
Five Visualisation/
├── employees.csv
├── five_visualisation.ipynb
├── five_visualisation.html
├── README.md
├── requirements.txt
└── reports/
    └── figures/
        ├── bar_chart.png
        ├── box_plot.png
        ├── histogram.png
        ├── line_chart.png
        └── scatter_plot.png
```

## Requirements
- Python 3
- Pandas
- Matplotlib
- Jupyter Notebook
- nbconvert

## How to Run

1. Open a terminal in the project directory.
2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Open the notebook:

   ```bash
   jupyter notebook five_visualisation.ipynb
   ```

4. Run all notebook cells from top to bottom.
5. Export the notebook as HTML:

   ```bash
   python -m nbconvert --to html five_visualisation.ipynb
   ```

6. Open `five_visualisation.html` in a browser to view the report.

## Findings and Limitations
The dataset contains 8 employees. The results provide a small-scale view of employee salaries and department patterns and may not represent a larger workforce. The monthly sales line chart uses separate sample data.

## Output
The notebook, exported HTML report, and five chart images are included in this project.
