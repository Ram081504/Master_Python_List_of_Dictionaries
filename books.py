Books_list = {
 "Name": "The Great Gatsby", 
 "Author": "F. Scott Fitzgerald",
 "Genre": "Tragedy",
 "Date": 1925,
 "Ratings": 3.9,
}, {
 "Name": "Ulysses", 
 "Author": "James Joyce",
 "Genre": "Modernist novel",
 "Date": 1920,
 "Ratings": 3.8,
}, {
 "Name": "In Search of Lost Time", 
 "Author": "Marcel Proust",
 "Genre": "Philosophical fiction",
 "Date": 1913,
 "Ratings": 4.3,
}, {
 "Name": "One Hundred Years of Solitude", 
 "Author": "Gabriel García Márquez",
 "Genre": "Novel",
 "Date": 1967,
 "Ratings": 4.1,
}, {
 "Name": "The Catcher in the Rye", 
 "Author": "J. D. Salinger",
 "Genre": "Realistic fiction",
 "Date": 1951,
 "Ratings": 3.8,
}

for Book in Books_list:
   print(f"Name: {Book['Name']}, Author: {Book['Author']}, Genre: {Book['Genre']}, Date: {Book['Date']}, Ratings: {Book['Ratings']}")