# Trader Performance vs Market Sentiment Analysis

## Objective
The objective of this project is to analyze how Bitcoin market sentiment (Fear / Greed Index) affects trader behavior and profitability on the Hyperliquid platform.
This analysis aims to identify patterns that could help traders make more informed decisions.

## Dataset

Two datasets were used:

1. **Bitcoin Market Sentiment Dataset**
   - Columns: timestamp, value, classification (Fear, Greed, etc.), date
   - Represents daily sentiment of the crypto market.

2. **Hyperliquid Historical Trader Data**
   - Includes fields such as:
     - Account
     - Execution Price
     - Size USD
     - Side (BUY / SELL)
     - Closed PnL
     - Timestamp
   - Represents individual trading activity.

## Methodology

The analysis followed these steps:

1. **Data Preparation**
   - Loaded datasets using Pandas
   - Checked dataset shapes
   - Handled missing values
   - Checked duplicates
   - Converted timestamps into readable dates

2. **Data Integration**
   - Merged trader data with market sentiment dataset based on date.

3. **Feature Engineering**
   - Daily PnL per trader
   - Win rate
   - Trade frequency
   - Trade size analysis

4. **Data Visualization**
   - PnL vs Market Sentiment
   - Trade Size Distribution
   - Long vs Short Behavior

## Key Insights

### 1. Trader Profitability vs Market Sentiment
Trader profitability is highest during **Greed sentiment periods**.

This suggests that bullish market conditions create more profitable opportunities.

### 2. Extreme Greed Shows Lower Profitability
Average PnL during **Extreme Greed** is lower than normal Greed.

This may indicate market overheating and late trader entries.

### 3. Trade Size Distribution
Trade sizes show a **right-skewed distribution**.

Most traders place smaller trades while a few large trades significantly increase the average trade size.

## Strategy Recommendations

### Strategy 1
Increase trading participation during **Greed sentiment periods**, where profitability is historically higher.

### Strategy 2
Reduce aggressive trading during **Extreme Greed periods**, as the market may become overheated and volatile.

## Project Files

- `analysis.py` → Main Python analysis script
- `pnl_vs_sentiment.png` → Trader profitability vs market sentiment
- `trade_size_distribution.png` → Trade size distribution analysis
- `long_short_sentiment.png` → Trader long vs short behavior
- `trader_sentiment_insights.pdf` → Summary insights report

## Tools & Libraries

- Python
- Pandas
- Matplotlib
- Seaborn
- NumPy

## Author
**Pranav Bhamre**
Data Science Internship Assignment  
Trader Behavior Insights Analysis
