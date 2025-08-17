CREATE DATABASE IF NOT EXISTS movies_db;
USE movies_db;

CREATE TABLE IF NOT EXISTS movie (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200),
  genre VARCHAR(100),
  mood VARCHAR(100)
);

INSERT INTO movie (title, genre, mood) VALUES
  ('The Shawshank Redemption', 'Drama', 'inspiring'),
  ('Forrest Gump', 'Comedy', 'happy'),
  ('The Notebook', 'Romance', 'romantic'),
  ('Inception', 'Thriller', 'intense'),
  ('Inside Out', 'Animation', 'sad'),
  ('La La Land', 'Romance', 'happy'),
  ('Parasite', 'Thriller', 'intense');
