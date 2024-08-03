# Django CSV Analysis Web Application

## Overview

This project is a Django-based web application that allows users to upload CSV files, perform data analysis using `pandas` and `numpy`, and display the results and visualizations on the web interface.

## Features

- **File Upload**: Users can upload CSV files via a web form.
- **Data Processing**: 
  - Reads CSV files and performs basic data analysis.
  - Calculates summary statistics (mean, median, standard deviation) for numerical columns.
  - Identifies and handles missing values.
- **Data Visualization**:
  - Generates histograms and pair plots for data visualization.
  - Displays plots on the web page.
- **User Interface**: 
  - Simple and user-friendly web interface to view data analysis results and visualizations.

## Technologies Used

- **Backend**: Django
- **Data Analysis**: Pandas, Numpy
- **Data Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML, CSS (Bootstrap)

## Setup and Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Anujc07/Data-Analysis.git
    cd Data-Analysis
    ```

2. **Create a Virtual Environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

7. **Navigate to the Application**:

    Open your web browser and go to `http://127.0.0.1:8000` to view the application.

## Usage

1. **Upload CSV File**:
   - Go to the home page.
   - Use the file upload form to select and upload your CSV file.

2. **View Analysis Results**:
   - After uploading, the application will process the file and redirect you to the results page.
   - View summary statistics, null values, and data visualizations.

## Directory Structure

- `ass_app/`: Contains the Django app with views, models, and templates.
- `media/`: Directory for storing uploaded files and generated plots.
- `static/`: Directory for static files like CSS.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please reach out to [Anuj Choubey](mailto:choubeyanuj44@gmail.com).
