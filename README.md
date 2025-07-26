# Software Engineer Earnings Analysis

## Quick Links

- [Dataset (Google Drive)](https://drive.google.com/file/d/13S9KWvOleAu-V_32Cpyrn8KHm1BnURN0/view?usp=sharing)
- [Analysis Notebook](4_data_analysis/software_engineering_dataset_analysis.ipynb)
- [Data Cleaning Process](2_data_preparation/employment_dataset_cleaning_script.ipynb)
- [Dataset Documentation](1_datasets/data_source.md)

## Project Overview

This project analyzes demographic factors influencing software engineer
earnings
in the U.S. tech industry. We explore patterns in wages across gender,
education,
race, and age groups using statistical analysis.

## Repository Structure

```markdown
├── 0_domain_study/          # Background research and problem definition
├── 1_datasets/              # Data files and documentation
├── 2_data_preparation/      # Data cleaning scripts
├── 3_data_exploration/      # Initial data exploration
├── 4_data_analysis/         # Statistical analysis and findings
├── 5_communication_strategy/# Presentation and communication
└── 6_final_presentation/    # Final results and presentation
```

## Getting Started

### 1. Get the Data

- Download the dataset from [Google Drive](https://drive.google.com/file/d/13S9KWvOleAu-V_32Cpyrn8KHm1BnURN0/view?usp=sharing)
- Place it in the `1_datasets` directory

### 2. Set Up Environment

```bash
python -m venv cdsp_env
source cdsp_env/bin/activate  # On Windows: cdsp_env\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Analysis

Open and run the notebooks in this order:

1. [Data Cleaning](2_data_preparation/employment_dataset_cleaning_script.ipynb)
2. [Data Exploration](3_data_exploration/explore_software_engineers_dataset.ipynb)
3. [Statistical Analysis](4_data_analysis/software_engineering_dataset_analysis.ipynb)

## Key Findings

- Significant wage differences across demographic groups
- Education level strongly correlates with earnings
- Multiple factors contribute to wage disparities
- See detailed results in the [analysis notebook](4_data_analysis/software_engineering_dataset_analysis.ipynb)

## Contributors

Team members from MIT Emerging Talent Program (CDSP Group 11)

## License

See [LICENSE](LICENSE) file for details

## Tools We Use

- Python
- pandas, numpy, matplotlib
- Git and GitHub for version control and collaboration
- Google Docs for planning and communication

## Team Values

- **Curiosity** – We ask questions, explore possibilities,
and stay open to new insights.  
- **Clarity** – We aim for clean code, clear documentation,
and effective communication.  
- **Collaboration** – We support each other, share responsibilities,
and value every contribution.  
- **Growth** – We’re here to learn, give feedback, and improve with
every iteration.
- **Mutual Respect** – We value diverse perspectives, listen actively,
and create a safe, inclusive team environment.

## Learning Goals

- **Ensure Clear Documentation**  
  Maintain well-structured READMEs and comments to support project
  clarity and onboarding.

- **Develop Clean, Modular Code**  
  Write readable, reusable Python code following consistent
  style and best practices.

- **Reinforce Data Science Fundamentals**  
  Apply key concepts such as exploratory data analysis
  and basic statistics throughout the project.

- **Foster Effective Collaboration**  
  Communicate proactively, coordinate with teammates,
  and contribute to a supportive group dynamic.

- **Communicate Insights Clearly**  
  Translate technical findings into concise, accessible
  summaries or visualizations.

- **Engage in Constructive Feedback**  
  Provide meaningful code reviews and iterate based on team feedback.
