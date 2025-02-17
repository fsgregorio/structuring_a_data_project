# 📊 Structuring a Data Project

Welcome to the documentation for the **Structuring a Data Project**.

This project implements a **data pipeline** that extracts, transforms, and consolidates **Excel files**. It processes `.xlsx` files from the `data/input` folder and saves the output in `data/output`.

## Features
✔ Extracts multiple Excel files  
✔ Transforms and merges data  
✔ Generates a single consolidated file  
✔ CI/CD integration with GitHub Actions  
✔ Fully automated pipeline

## 🚀 Installation
Make sure you have [Poetry](https://python-poetry.org/docs/) installed.

### Clone the repository
```bash
git clone https://github.com/fsgregorio/structuring_a_data_project.git
cd structuring_a_data_project

poetry install
```
---

### ▶️ **How to Run the Project**

### 1️⃣ Add input files
Place your `.xlsx` files inside the `data/input` folder.

### 2️⃣ Run the pipeline
Execute the following command:
```bash
poetry run python app/main.py
```

---

### 🔍 Running Tests

To ensure everything is working properly, run the tests using `pytest`:

```bash
poetry run pytest -v
```
Test coverage includes:

Data extraction from Excel files
Data transformation logic
Saving and formatting of the output file

### 📁 Project Structure

```graphql
.
├── app/
│   ├── pipeline/
│   │   ├── extract.py  # Data extraction
│   │   ├── transform.py  # Data transformation
│   │   ├── load.py  # Processed data saving
│   ├── main.py  # Main script to run the pipeline
├── data/
│   ├── input/  # Folder for input (.xlsx) files
│   ├── output/  # Folder where processed files will be saved
├── tests/  # Automated tests
├── docs/  # Project documentation
├── .github/workflows/  # CI/CD configuration for GitHub Actions
├── mkdocs.yml  # MkDocs configuration for documentation
├── pyproject.toml  # Poetry configuration
├── README.md  # Project documentation
```

### 🔧 CI/CD on GitHub

This project has **CI/CD configured using GitHub Actions**, ensuring:
✔ Automatic test execution on every push/pull request  
✔ Dependency installation via Poetry  

Check the CI/CD status on the **Actions** tab of the repository.


### 🤝 Contribution

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b my-feature