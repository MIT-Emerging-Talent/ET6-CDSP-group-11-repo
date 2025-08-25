import pandas as pd
import numpy as np
from datetime import datetime
import os

# Set random seed for reproducibility
np.random.seed(42)

def ensure_directory_exists(path):
    """Create directory if it doesn't exist"""
    os.makedirs(os.path.dirname(path), exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

def generate_wage_data(n_records=1000):
    # Base salary parameters from research findings
    base_salary = 120000
    std_dev = 30000

    # Generate base data
    data = {
        'employee_id': range(1, n_records + 1),
        'gender': np.random.choice(
            ['Male', 'Female', 'Non-Binary'], 
            n_records, 
            p=[0.65, 0.30, 0.05]
        ),
        'race_ethnicity': np.random.choice(
            ['White', 'Asian', 'Black', 'Hispanic', 'Other'],
            n_records,
            p=[0.45, 0.30, 0.12, 0.10, 0.03]
        ),
        'education_level': np.random.choice(
            ['Bachelors', 'Masters', 'PhD', 'Bootcamp'],
            n_records,
            p=[0.50, 0.35, 0.10, 0.05]
        ),
        'years_experience': np.random.randint(0, 25, n_records),
        'job_title': np.random.choice(
            ['Software Engineer', 'Senior Engineer', 'Tech Lead', 'Principal Engineer'],
            n_records,
            p=[0.40, 0.35, 0.15, 0.10]
        ),
        'location': np.random.choice(
            ['San Francisco', 'New York', 'Seattle', 'Austin', 'Boston'],
            n_records
        )
    }

    # Generate salaries with researched wage gaps
    base_salaries = np.random.normal(base_salary, std_dev, n_records)
    
    # Apply multipliers based on research findings
    gender_multiplier = {'Male': 1.0, 'Female': 0.85, 'Non-Binary': 0.90}
    education_multiplier = {
        'Bachelors': 1.0,
        'Masters': 1.15,
        'PhD': 1.25,
        'Bootcamp': 0.90
    }
    
    # Calculate final salaries
    data['salary'] = base_salaries * \
                     np.array([gender_multiplier[g] for g in data['gender']]) * \
                     np.array([education_multiplier[e] for e in data['education_level']]) * \
                     np.array([1 + (0.03 * yoe) for yoe in data['years_experience']])

    # Create DataFrame
    df = pd.DataFrame(data)
    
    try:
        # Create timestamp for filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'wage_equity_data_{timestamp}.csv'
        
        # Construct full path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_dir, output_file)
        
        # Ensure directory exists
        ensure_directory_exists(output_path)
        
        # Save to CSV
        df.to_csv(output_path, index=False)
        print(f"Data successfully saved to: {output_path}")
        
        # Print summary statistics
        print("\nData Summary:")
        print("-" * 50)
        print(f"Total records: {len(df)}")
        print("\nSalary Statistics:")
        print(df['salary'].describe())
        print("\nGender Distribution:")
        print(df['gender'].value_counts(normalize=True))
        
    except Exception as e:
        print(f"Error saving data: {str(e)}")
        raise
    
    return df

if __name__ == "__main__":
    print("Generating wage equity sample data...")
    try:
        df = generate_wage_data()
        print("Data generation completed successfully!")
    except (OSError, ValueError) as e:
        print(f"Error generating data: {str(e)}")