import streamlit as st
import pandas as pd

# Load your data
books = pd.read_csv("Books.csv")
ratings = pd.read_csv("Ratings.csv")
users = pd.read_csv("Users.csv")

# Merge book and rating data
book_data = pd.merge(ratings, books, on="ISBN")

# Remove books with zero ratings
book_data = book_data[book_data["Book-Rating"] > 0]

# Simulate a genre filter by searching Book-Title or Publisher (for simplicity)
def filter_books_by_genre(keyword):
    keyword = keyword.lower()
    return book_data[
        book_data["Book-Title"].str.lower().str.contains(keyword) |
        book_data["Publisher"].str.lower().str.contains(keyword)
    ]

# Initialize session state for favorites
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# --- UI ---
st.title("📚 Book Recommendation System")

# Genre filter (keyword-based simulation)
genre = st.text_input("🔍 Search by Genre / Keyword (e.g., fiction, science, mythology):", "")

if genre:
    filtered_books = filter_books_by_genre(genre).drop_duplicates("ISBN")
    st.subheader(f"Books matching: '{genre}'")

    for _, row in filtered_books.iterrows():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(row["Image-URL-M"], width=80)
        with col2:
            st.markdown(f"**{row['Book-Title']}** by *{row['Book-Author']}*")
            st.caption(f"Publisher: {row['Publisher']}, Year: {row['Year-Of-Publication']}")
            if st.button("❤️ Add to Favorites", key=row["ISBN"]):
                if row["ISBN"] not in st.session_state.favorites:
                    st.session_state.favorites.append(row["ISBN"])
                st.success("Added to Favorites!")

# Display favorites
if st.session_state.favorites:
    st.markdown("## 💖 Your Favorites")
    fav_books = books[books["ISBN"].isin(st.session_state.favorites)]
    for _, row in fav_books.iterrows():
        st.markdown(f"- **{row['Book-Title']}** by *{row['Book-Author']}*")

