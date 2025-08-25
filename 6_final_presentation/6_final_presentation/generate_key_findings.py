#!/usr/bin/env python

"""
Quick script to extract key findings from our analysis
for the final presentation.
"""

import pandas as pd

# Load the latest data
df = pd.read_csv('../data/wage_equity/wage_equity_data_20250820_151048.csv')

def generate_key_stats():
    """Generate key statistics for presentation"""
    
    print("\n=== Overall Salary Statistics ===")
    print(df['salary'].describe())
    
    print("\n=== Gender Wage Comparison ===")
    gender_stats = df.groupby('gender')['salary'].agg(['mean', 'count']).round(2)
    print(gender_stats)
    
    print("\n=== Education Level Impact ===")
    edu_stats = df.groupby('education_level')['salary'].agg(['mean', 'count']).sort_values('mean', ascending=False).round(2)
    print(edu_stats)
    
    print("\n=== Geographic Differences ===")
    loc_stats = df.groupby('location')['salary'].agg(['mean', 'count']).sort_values('mean', ascending=False).round(2)
    print(loc_stats)
    
    # Calculate percentage differences
    overall_mean = df['salary'].mean()
    print("\n=== Key Findings ===")
    print(f"1. Overall average salary: ${overall_mean:,.2f}")
    
    gender_gap = ((gender_stats.loc['Male', 'mean'] - gender_stats.loc['Female', 'mean']) / 
                 gender_stats.loc['Male', 'mean'] * 100)
    print(f"2. Gender wage gap: {gender_gap:.1f}%")
    
    highest_paying_city = loc_stats.index[0]
    lowest_paying_city = loc_stats.index[-1]
    city_gap = ((loc_stats.loc[highest_paying_city, 'mean'] - loc_stats.loc[lowest_paying_city, 'mean']) /
                loc_stats.loc[highest_paying_city, 'mean'] * 100)
    print(f"3. Geographic wage gap: {city_gap:.1f}% between {highest_paying_city} and {lowest_paying_city}")
    
    highest_edu = edu_stats.index[0]
    lowest_edu = edu_stats.index[-1]
    edu_gap = ((edu_stats.loc[highest_edu, 'mean'] - edu_stats.loc[lowest_edu, 'mean']) /
               edu_stats.loc[highest_edu, 'mean'] * 100)
    print(f"4. Education impact: {edu_gap:.1f}% difference between {highest_edu} and {lowest_edu}")

if __name__ == "__main__":
    generate_key_stats()
