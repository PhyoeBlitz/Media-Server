// Movie data list (example)
const movies = [
  { title: 'Movie 1', year: 2022, genre: 'Action' },
  { title: 'Movie 2', year: 2021, genre: 'Comedy' },
  { title: 'Movie 3', year: 2020, genre: 'Drama' },
  // ... add more movies to the list
];

// Generate movie cards
const moviesGrid = document.querySelector('.movies-grid');

movies.forEach((movie) => {
  const movieCard = document.createElement('div');
  movieCard.className = 'movie-card';
  movieCard.innerHTML = `
    <h3>${movie.title}</h3>
    <p>Year: ${movie.year}</p>
    <p>Genre: ${movie.genre}</p>
  `;
  moviesGrid.appendChild(movieCard);
});