#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Load dataset
df = pd.read_csv('C:/Users/Administrator/Desktop/measurements_coding_challenge.csv', delimiter=";")


# Replace invalid entries with NaN
df.replace(["n/a", "null", "NULL", "NaN", ""], pd.NA, inplace=True)

# Drop irrelevant column
df.drop(columns=["direct_consumption"], inplace=True)

# Convert columns to appropriate types
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["grid_purchase"] = pd.to_numeric(df["grid_purchase"], errors="coerce")
df["grid_feedin"] = pd.to_numeric(df["grid_feedin"], errors="coerce")

# Drop rows with invalid timestamps or serials
df.dropna(subset=["timestamp", "serial"], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Extract hour and date
df["hour"] = df["timestamp"].dt.hour
df["date"] = pd.to_datetime(df["timestamp"].dt.date)

# Group by hour to compute total grid_purchase and grid_feedin
hourly_summary = df.groupby("hour", as_index=False)[["grid_purchase", "grid_feedin"]].sum()

# Compute max grid_feedin hour per day
daily_hourly_feedin = df.groupby(["date", "hour"], as_index=False)["grid_feedin"].sum()
max_hour_per_day = daily_hourly_feedin.loc[daily_hourly_feedin.groupby("date")["grid_feedin"].idxmax()]
max_hour_per_day["is_max_hour"] = True

# Merge back into main dataframe
df = df.merge(max_hour_per_day[["date", "hour", "is_max_hour"]],
              on=["date", "hour"], how="left")

df["is_max_hour"] = df["is_max_hour"].fillna(False)

# Save outputs
df.to_csv("cleaned_measurements.csv", index=False)
hourly_summary.to_csv("hourly_summary.csv", index=False)

print("Transformation done ")
print("coped to cleanzed df.csv")
print("hourly_summary.csv")







