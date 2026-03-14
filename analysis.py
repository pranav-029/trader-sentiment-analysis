import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
sentiment = pd.read_csv("sentiment.csv")
trades = pd.read_csv("trader_data.csv")

# Show first 5 rows
print("Sentiment Dataset:")
print(sentiment.head())

print("\nTrader Dataset:")
print(trades.head())

# Check the shapes of the datasets
print("\nDataset Shapes:")

print("Sentiment dataset shape:", sentiment.shape)
print("Trader dataset shape:", trades.shape)

# Check for missing values 
print("\nMissing values in Sentiment dataset:")
print(sentiment.isnull().sum())

print("\nMissing values in Trader dataset:")
print(trades.isnull().sum())

print("\nDuplicate rows in Sentiment dataset:")
print(sentiment.duplicated().sum())

print("\nDuplicate rows in Trader dataset:")
print(trades.duplicated().sum())


print("\nConverting timestamps to date...")

# Convert trader timestamp (milliseconds)
trades['Timestamp'] = pd.to_datetime(trades['Timestamp'], unit='ms')

# Extract date
trades['date'] = trades['Timestamp'].dt.date

print("\nTrader dataset after timestamp conversion:")
print(trades[['Timestamp','date']].head())


print("\nMerging trader data with sentiment data...")

# Convert sentiment date column to datetime (just to be safe)
sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

# Merge datasets on date
merged = pd.merge(trades, sentiment, on='date', how='left')

print("\nMerged dataset preview:")
print(merged.head())

print("\nCalculating daily PnL per trader...")

daily_pnl = merged.groupby(['Account','date'])['Closed PnL'].sum().reset_index()

print("\nDaily PnL preview:")
print(daily_pnl.head())

print("\nCalculating win rate...")

# Create a column to mark winning trades
merged['win'] = merged['Closed PnL'] > 0


# Remove extreme outliers (top 1%)
upper_limit = merged['Size USD'].quantile(0.99)
filtered_trades = merged[merged['Size USD'] <= upper_limit]

# Calculate statistics
mean_trade = filtered_trades['Size USD'].mean()
median_trade = filtered_trades['Size USD'].median()

plt.figure(figsize=(10,6))

sns.histplot(filtered_trades['Size USD'], bins=40, kde=True)

# Add statistical lines
plt.axvline(mean_trade, color='red', linestyle='--', label=f"Mean: {mean_trade:.0f}")
plt.axvline(median_trade, color='green', linestyle='--', label=f"Median: {median_trade:.0f}")

plt.title("Trade Size Distribution (Filtered Top 1% Outliers)")
plt.xlabel("Trade Size (USD)")
plt.ylabel("Number of Trades")

plt.legend()

plt.show()

print("\nAnalyzing PnL during Fear vs Greed sentiment...")

sentiment_pnl = merged.groupby('classification')['Closed PnL'].mean().reset_index()

print(sentiment_pnl)

plt.figure(figsize=(7,5))

sns.barplot(data=sentiment_pnl, x='classification', y='Closed PnL')

plt.title("Average Trader PnL during Fear vs Greed Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Average Closed PnL")

plt.show()

print("\nAnalyzing PnL during Fear vs Greed sentiment...")

# Step 1: Calculate average PnL by sentiment
sentiment_pnl = merged.groupby('classification')['Closed PnL'].mean().reset_index()

print(sentiment_pnl)

# Step 2: Create the chart
plt.figure(figsize=(7,5))

sns.barplot(data=sentiment_pnl, x='classification', y='Closed PnL')

plt.title("Average Trader PnL during Fear vs Greed Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Average Closed PnL")

# Step 3: Save the chart (important for submission)
plt.savefig("pnl_vs_sentiment.png")

# Step 4: Show the chart
plt.show()

print("\nAnalyzing long vs short behavior during Fear vs Greed...")

side_sentiment = merged.groupby(['classification','Side']).size().reset_index(name='count')

print(side_sentiment)

plt.figure(figsize=(8,5))

sns.barplot(data=side_sentiment, x='classification', y='count', hue='Side')

plt.title("Trader Long vs Short Behavior during Fear vs Greed")
plt.xlabel("Market Sentiment")
plt.ylabel("Number of Trades")

plt.savefig("long_short_sentiment.png")

plt.show()