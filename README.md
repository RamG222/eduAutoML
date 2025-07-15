# 🎓 eduAutoML

**eduAutoML** is a beginner-friendly AutoML Python library designed for students and educators.  
It simplifies machine learning model selection, training, and evaluation — for both classification and regression — using a clean CLI and optional Gradio GUI.

---

## 📦 Features

- 📊 **Automatic model selection** (Logistic Regression, Random Forest, XGBoost)
- 🧠 **Auto-detects task type** (classification or regression)
- ⚙️ **Data preprocessing**: missing value handling, encoding, scaling
- 📈 **Performance metrics and visualizations**
- 🖥️ **Gradio GUI** (coming soon)
- ✅ CLI support for quick runs

---

## 🔧 Installation

```bash
pip install eduautoml


## CLI Usage

eduautoml run --input path/to/your.csv --target target_column

Example:

eduautoml run --input sample.csv --target species

🔍 Features
✅ Auto detection of best classification model

✅ CLI interface with Typer

✅ Preprocessing: missing value imputation, one-hot encoding, scaling

✅ Model evaluation: accuracy, precision, recall, F1, confusion matrix

✅ Stratified train-test split

✅ Beginner-friendly and well-commented codebase

🛠️ Upcoming Features
📊 Auto EDA using pandas-profiling / sweetviz

🧠 Regression support (Linear, XGBoost, etc.)

🖼️ Gradio-based drag-and-drop GUI

📈 Model performance visualization
