# Cryptocurrency Candlesticks Visualization

![alt text](https://github.com/nikhilnlakhwani/crypto-candlesticks/blob/main/doge_sample.png?raw=true)

## Overview
The "Cryptocurrency Candlesticks Visualization" tool is designed to extract price history data for a chosen cryptocurrency from Yahoo Finance, save it to a CSV file, and then generate a detailed candlestick chart visualization. This Python-based tool leverages Plotly and Pandas packages for data manipulation and visualization. 

A unique feature is its ability to annotate significant market events, such as Elon Musk's tweets, and their potential impact on the cryptocurrency's value. The `doge.py` script provides a sample visualization for DOGE-USD, including these annotations.

## Features
- **Data Extraction**: Fetches historical price data of cryptocurrencies from Yahoo Finance.
- **Customizable Input**: Allows users to select their cryptocurrency of interest.
- **Candlestick Chart Visualization**: Generates an interactive candlestick chart for the selected cryptocurrency.
- **Event Annotations**: Includes the option to annotate specific events and their potential impact on the market (featured in `doge.py` for DOGE-USD).

## Requirements
- Python 3.x
- Plotly
- Pandas
- Yahoo Finance API or compatible library for data extraction

## Installation
1. Clone the repository:
2. Install required dependencies:
   ```
   pip install pandas plotly yfinance  
   ```

## Usage
1. Run the main script to extract data and generate a basic candlestick chart:
   ```
   python chart_generator.py
   ```
2. For the annotated DOGE-USD chart:
   ```
   python doge.py
   ```

## Customization
- Modify `chart_generator.py` to change the cryptocurrency selection or adjust the date range for data extraction.
- Edit `doge.py` to update or add new annotations related to market-influencing events.

## Contributing
Contributions to enhance the functionality or efficiency of this tool are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## Disclaimer
This tool is intended for educational and informational purposes only. It does not constitute financial advice. Cryptocurrency markets are volatile, and users should conduct their own research before making investment decisions.
