# Healthcare Analysis

|               |   |                       |
|---------------|---|-----------------------|
|   Author      | : |   Ethan Tan Wee En    |
|   Admin       | : |   p2012085            |
|   Class       | : |   DAAA/1B/03          |
|   Language    | : |   Python              |
|   Date        | : |   December 2020       |

## Setup

1. Ensure that Python (at least v3.8) is installed locally
2. Ensure that Python Packages `NumPy` and `MatPlotLib` are installed locally
3. Navigate to Healthcare Analysis through command line (cmd, pwsh, terminal)

## Running

> Run the following commands:
> 1. `python src/obesity-rates.py`
> 2. `python src/defective-vision-rates.py`
> 3. `python src/number-of-pharmacists.py`

## Program

* Data summaries will be generated and logged to the console
* Data visualisations will pop out and be saved to the `assets` directory

## File Structure

    Healthcare Analysis ---- assets ---- defective-vision-rates.png
                         |           |-- number-of-pharmacists.png
                         |           `-- obesity-rates.png
                         |
                         |-- data ---- defective-vision-rates.csv
                         |         |-- number-of-pharmacists.csv
                         |         `-- obesity-rates.csv
                         |
                         |-- docs ---- CA1 Brief.pdf
                         |         `-- insights.pptx
                         |
                         |-- src ---- utils ---- __init__.py
                         |        |          |-- stats_options.py
                         |        |          |-- summaries.py
                         |        |          `-- switch.py
                         |        |
                         |        |-- defective-vision-rates.py
                         |        |-- number-of-pharmacists.py
                         |        `-- obesity-rates.py
                         |
                         `-- README.md

## Insights

For further details on data processing and insights gained, please refer to `docs/insights.pptx`