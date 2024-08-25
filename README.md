# ncv-contactcard

Here’s a revised README focused on the contact card project for students:

---

# NCV Student Association Contact Card Generator

## Overview

This project is designed for the NCV Student Association to generate contact cards for all its students. The provided Python script processes a CSV file containing student information and creates a standardized contact card that can be easily imported into address books or contact management systems.

## Project Structure

- **`vcf.py`**: The main Python script that reads student data from `NCV.csv` and generates a contact card file (.vcf) that can be imported into various applications like Outlook, Gmail, and more.
- **`NCV.csv`**: A dataset containing the student contact information such as name, email, phone number, and address.

## Installation

Follow these simple steps to set up and run the project on Windows and macOS:

### Step 1: Install Python

If you don’t have Python installed, download it from [python.org](https://www.python.org/downloads/).

For Windows, during installation, make sure to check the box that says "Add Python to PATH."

### Step 2: Install Required Packages

Once Python is installed, open your terminal (Command Prompt/PowerShell on Windows or Terminal on macOS) and run the following command to install the required Python packages:

```bash
pip3 install csv
```

### Step 3: Run the Script

To generate the contact cards, run the script with:

```bash
python3 path-to-vcf.py
```

The script will read the `NCV.csv` file and generate a `.vcf` file containing contact cards for all students.

## How the Script Works

The Python script, `vcf.py`, reads the student data from `NCV.csv` using the `pandas` library. The script processes each student's information, such as their name, email, phone number, and address, and then formats this data into a vCard (.vcf) file format.

### Script Explanation

1. **Reading Data**: The script reads the `NCV.csv` file using `pandas`. The CSV file should have columns like `Name`, `Email`, `Phone`, `Address`, etc.
2. **Generating vCards**: For each row in the CSV, the script formats the student’s details into a vCard format and saves it into a single `.vcf` file.
3. **Output**: The output is a `.vcf` file that can be imported into contact management systems (like Gmail, Outlook, etc.), allowing easy access to student contact details.

### Example CSV Format

Ensure that your `NCV.csv` file is structured in the same way.

## Acknowledgments

A special thanks to [Julian de Haas](https://www.linkedin.com/in/julian-de-haas/) making this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
