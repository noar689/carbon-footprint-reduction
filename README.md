# 🌱 Low-Carbon Product Recommendation System

## 📌 Project Overview

This project is a **FastAPI-based recommendation system** that suggests **low-carbon alternative products**. It helps users find products with a lower carbon footprint based on their input. The system uses **TF-IDF and Cosine Similarity** to generate recommendations.

## 🚀 Features

- **Low-carbon product recommendations** using content-based filtering.
- **FastAPI** for API-based interactions.
- **TF-IDF & Cosine Similarity** for similarity calculations.
- **Custom stopwords filtering** for better accuracy.

## 💄 Project Structure

```
📎 Project Folder
|── 📂 dataset/             # Contains product dataset
|── 📝 api.py               # FastAPI server
|── 📝 recommendation1.py   # Recommendation logic
|── 📝 data_preprocessing.ipynb  # Data preprocessing notebook
|── 📝 README.md            # Documentation
```

## 🦭 Setup & Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

## 🚀 Running the API

Start the FastAPI server using `uvicorn`:

```sh
uvicorn api:app --reload
```

If successful, you'll see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

## 🔗 API Endpoints

| Method | Endpoint                                      | Description                            |
| ------ | --------------------------------------------- | -------------------------------------- |
| `GET`  | `/recommend/?product_name=<name>&top_n=<num>` | Get low-carbon product recommendations |

### 🛠 Example API Request:

```sh
GET http://127.0.0.1:8000/recommend/?product_name=Tomato,%20dried&top_n=5
```

**🛥 Expected JSON Response:**

```json
[
    {
        "id_ra": 123,
        "name": "Cucumber, fresh",
        "total_kg_co2-eq/kg": 0.5,
        "Price": 1.99
    },
    ...
]
```

## 📊 How It Works

1. **Data Processing:** TF-IDF applied to product names and categories.
2. **Similarity Matching:** Uses cosine similarity to find similar products.
3. **Filtering:** Ensures recommendations have a lower carbon footprint.
4. **Result:** Returns top N eco-friendly alternatives.


- If `uvicorn` is not recognized, install it with:
  ```sh
  pip install uvicorn
  ```
- If the dataset is missing, ensure the `dataset/` folder is present.

## 🤝 Contribution

Feel free to fork, improve, and submit a pull request!

---

🔹 **Developed with ❤️ using FastAPI, Pandas, and Scikit-learn** 🔹


