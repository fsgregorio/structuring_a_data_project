# 📊 Structuring a Data Project

This project implements a **data pipeline** that extracts and transforms **Excel files**, merging them into a single consolidated file. It processes `.xlsx` files from the `data/input` folder and saves the output in `data/output`.

## 🚀 Installation

Make sure you have [Poetry](https://python-poetry.org/docs/) installed. Then, follow these steps:

```bash
# Clone the repository
git clone https://github.com/fsgregorio/structuring_a_data_project.git
cd structuring_a_data_project

# Install dependencies
poetry install
```

## ▶️ How to Run the Project

1. Place the input files in the data/input folder.
2. Run the pipeline using the following command:

```bash
poetry run python app/main.py
```
3. The consolidated file will be saved in the data/output folder.

## 🔍 Running Tests

To run automated tests using pytest, execute:
```bash
poetry run pytest -v
```

## 📁 Project Structure

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

## 🔧 CI/CD on GitHub

This project has CI/CD configured on GitHub Actions, ensuring that:

Tests are automatically executed on every push/pull request.
Dependencies are installed correctly via Poetry.
You can check the execution status in the Actions tab of the repository.

## 🤝 Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b my-feature
3. Make your changes and commit:
   ```bash
   git commit -m "Add new feature"
4. Submit a Pull Request.


## 📩 Contact

📧 Email: fsgregorio92@gmail.com