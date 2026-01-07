# 📊 Automated Exploratory Data Analysis Dashboard

A powerful and user-friendly Streamlit application for automated exploratory data analysis (EDA). Upload your CSV or Excel files and instantly get comprehensive data insights, visualizations, and statistical summaries.

## Features

- **File Upload Support**: Upload CSV or Excel files with ease
- **Dataset Overview**: Quick preview of your data with head rows
- **Dataset Metrics**: Automatically calculate rows, columns, and duplicate count
- **Column Type Detection**: Automatically identify numeric and categorical columns
- **Interactive Visualizations**:
  - Histograms for numeric data distribution
  - Box plots for outlier detection
  - Correlation heatmaps for numeric relationships
- **Automated Insights**: 
  - Statistical insights on numeric columns
  - Missing value analysis and recommendations
- **Responsive Design**: Wide layout for optimal data exploration

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quickstart

1. Clone the repository and enter the project folder:
```bash
git clone https://github.com/MohitGaur17/EDA-Dashboard.git
cd EDA-Dashboard
```
2. (Optional) Create and activate a virtual environment on Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Steps to Analyze Data

1. **Upload Your File**: Click the "Upload CSV or Excel file" button and select your data file
2. **View Dataset Overview**: See a preview of the first few rows
3. **Check Metrics**: View the number of rows, columns, and duplicate records
4. **Explore Visualizations**: 
   - Select a numeric column to view its histogram and box plot
   - View correlation heatmap if you have at least 2 numeric columns
5. **Review Insights**: Check automated insights about your numeric columns and missing values

## Project Structure

```
EDA-Dashboard/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── modules/
  ├── data_loader.py        # Data loading utilities
  ├── profiler.py           # Dataset profiling functions
  ├── visualizer.py         # Plotly visualization functions
  ├── insights.py           # Automated insight generation
  └── utils.py              # Utility functions
```

## Modules

### `data_loader.py`
Handles loading data from uploaded CSV and Excel files.

### `profiler.py`
Profiles datasets by calculating basic statistics (rows, columns, duplicates).

### `visualizer.py`
Creates interactive visualizations using Plotly:
- Histograms for distribution analysis
- Box plots for outlier detection
- Correlation heatmaps

### `insights.py`
Generates automated insights including:
- Numeric column statistics and trends
- Missing value analysis

### `utils.py`
Utility functions for data type detection and other helper operations.

## Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **plotly**: Interactive visualizations
- **scipy**: Scientific computing (statistical functions)

See `requirements.txt` for specific versions.

## Tips for Best Results

- **Data Format**: Ensure your CSV/Excel files are well-formatted with clear column headers
- **File Size**: Works best with datasets under 100MB for optimal performance
- **Data Types**: Mix of numeric and categorical columns provides the richest insights
- **Missing Values**: The app automatically detects and reports on missing values

## Troubleshooting

### Application won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're in the correct directory
- Verify Python 3.8+ is installed

### No visualizations appearing
- Ensure your dataset has numeric columns for visualization
- Check that the file was uploaded successfully

### Slow performance
- Try with a smaller dataset first
- Close other applications to free up system resources

## Future Enhancements

Potential improvements for future versions:
- Advanced statistical tests
- Machine learning model recommendations
- Data quality scoring
- Custom filtering and sampling
- Report generation and export