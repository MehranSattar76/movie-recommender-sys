# 🎬 Movie Recommender System

This is a simple **Content-Based Movie Recommender System** built using **Flask** and **HTML**. It suggests similar movies based on a selected title using cosine similarity and movie metadata.

## 🔧 Features

- Recommends top 5 similar movies based on content similarity
- Clean and responsive web interface (HTML/CSS)
- Flask backend with pre-trained model
- Uses `rec.pkl` and `movie_dict.pkl` for fast recommendations

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Pickle
- HTML / CSS

## 🚀 How to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/movie-recommender-system.git
   cd movie-recommender-system
   
2. **Create a virtual environment (optional but recommended)**
   # For Windows
    
    python -m venv venv
    venv\Scripts\activate
    
    # **For macOS/Linux**
    ```bash
    python3 -m venv venv
    source venv/bin/activate

  

4. **Install dependencies**
    ```bash
    pip install -r requirements.txt

5. **Run Flask Server**
    ```bash
    python app.py

6. **Open your browser and go to**
    ```cpp
    http://127.0.0.1:5000/
7. **🌐 Live Demo**
    Try the app hosted on Render:

    🔗 https://movie-recommender-sys-wddb.onrender.com/

8. **Project Structure**
      ```php
      movie_recommender_system/
      │
      ├── app.py                   # Main Flask application
      ├── rec.pkl                  # Pickled recommendation model
      ├── movie_dict.pkl           # Pickled movie data dictionary
      ├── templates/
      │   └── index.html           # Frontend template
      ├── static/                  # (Optional) For CSS/JS/images
      ├── requirements.txt         # Python dependencies
      └── README.md                # Project documentation

9. **Credits**

     Created by myself with guidance from Nitish Singh (LinkedIn: nitish-singh-03412789) youtube tutorial on subject (https://youtu.be/1xtrIEwY_zY)

     Feel free to contribute, fork, or open issues!
