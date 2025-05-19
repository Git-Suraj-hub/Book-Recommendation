# 📚 Book Recommendation System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![GitHub stars](https://img.shields.io/github/stars/Git-Suraj-hub/Book-Recommendation?style=social)](https://github.com/Git-Suraj-hub/Book-Recommendation.git)


A personalized book recommendation system built with Python and Streamlit. It recommends books to users based on collaborative filtering and supports genre filtering and favorites management.

---

## 🚀 Features

* 🔍 **Search & Filter**: Keyword-based genre filtering (e.g., fiction, mystery, science).
* ⭐ **Top Recommendations**: Shows highly-rated books based on user interactions.
* ❤️ **Favorites**: Add or remove books from your favorites list.
* 📊 **Collaborative Filtering**: Memory-based user-user and item-item recommendations.

---

## 📂 Project Structure

```text
book-recommender/
├── app.py              # Streamlit application code
├── Books.csv           # Book metadata (ISBN, Title, Author, Publisher, Cover URLs)
├── Ratings.csv         # User-Book ratings
├── Users.csv           # User demographics (Location, Age)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/book-recommender.git
   cd book-recommender
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deployment

You can deploy this app on **Streamlit Cloud**:

1. Push your code to GitHub (if not already):

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and log in.

3. Click **New app** and select your GitHub repository.

4. Specify:

   * **Branch**: `main`
   * **File path**: `app.py`

5. Click **Deploy**.

Your app will be live at `https://<your-username>-book-recommender.streamlit.app`.

---

## 🛠️ Usage

1. **Open the web app** on your browser.
2. **Search** by entering a keyword (e.g., `mythology`, `science`).
3. **Add to Favorites** by clicking the ❤️ button next to each book.
4. **View Favorites** at the bottom of the page.

---

## 🔧 Configuration

You can customize the app behavior by editing `app.py`:

* Change the **filter logic** in `filter_books_by_genre()` to use real genres.
* Modify the **recommendation algorithm** (e.g., integrate Surprise SVD or NeuralCF).

---

## 🤝 Contributing

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: \`git commit -m "Add new feature"
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📫 Contact

Created by **Suraj**. For questions or feedback, reach out at `your.email@example.com`.
