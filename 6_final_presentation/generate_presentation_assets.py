#!/usr/bin/env python

"""
Quick script to extract key findings from our analysis notebooks
for the final presentation.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the latest data
df = pd.read_csv('../data/wage_equity/wage_equity_data_20250820_151048.csv')

def generate_key_stats():
    """Generate key statistics for presentation"""
    
    # Overall salary stats
    print("\n=== Overall Salary Statistics ===")
    print(df['salary'].describe())
    
    # Gender wage comparison
    print("\n=== Gender Wage Comparison ===")
    print(df.groupby('gender')['salary'].mean())
    
    # Education impact
    print("\n=== Education Level Impact ===")
    print(df.groupby('education_level')['salary'].mean().sort_values(ascending=False))
    
    # Geographic differences
    print("\n=== Geographic Differences ===")
    print(df.groupby('location')['salary'].mean().sort_values(ascending=False))

def save_key_visualizations():
    """Save key visualizations for presentation"""
    
    # Salary by gender boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='gender', y='salary')
    plt.title('Salary Distribution by Gender')
    plt.savefig('presentation_assets/gender_salary_dist.png')
    plt.close()
    
    # Education level impact
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x='education_level', y='salary')
    plt.xticks(rotation=45)
    plt.title('Average Salary by Education Level')
    plt.savefig('presentation_assets/education_impact.png')
    plt.close()

if __name__ == "__main__":
    # Create assets directory if it doesn't exist
    import os
    os.makedirs('presentation_assets', exist_ok=True)
    
    # Generate statistics and visualizations
    generate_key_stats()
    save_key_visualizations()
    
    print("\nPresentation assets generated in 'presentation_assets' directory")
