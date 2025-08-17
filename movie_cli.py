import mysql.connector
from tabulate import tabulate

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "YES"  # Change this to your actual password!
MYSQL_DB = "movies_db"

def get_recommendations(mood):
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASS,
            database=MYSQL_DB
        )
        cursor = conn.cursor()
        query = "SELECT title, genre, mood FROM movie WHERE mood = %s"
        cursor.execute(query, (mood,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []

def main():
    print("Welcome to the Movie Recommendation CLI!")
    mood = input("Enter your mood (e.g., happy, sad, romantic, intense): ").lower().strip()
    movies = get_recommendations(mood)
    if movies:
        print("\nRecommended Movies:")
        print(tabulate(movies, headers=['Title', 'Genre', 'Mood'], tablefmt='grid'))
    else:
        print("Sorry, no recommendations found for that mood.")

if __name__ == "__main__":
    main()
