from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

try:
    # Sending a GET request to the URL
    response = requests.get(
        'https://timesofindia.indiatimes.com/entertainment/top-rated-movies/tamil/best-movies/2023/2742916',
    )

    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with class "mr_lft_box"
    movie_divs = soup.find_all('div', class_='mr_lft_box')
    data_set = []
    titles = []
    ratings = []

    # Loop through each movie div
    for movie_div in movie_divs:
        # Find the h3 tag within the specified div for movie title
        h3_tag = movie_div.find('div', class_='FIL_right').find('h3')

        # Extract the text from the h3 tag for movie title
        movie_title = h3_tag.text.strip()

        # Find the movie rating within the specified div
        movie_rating = movie_div.find('div', class_='md_info').find('span', class_='cricrating').text.strip()
        data_set.append({'Title': movie_title, 'Movie Rating': movie_rating})
        titles.append(movie_title)
        ratings.append(float(movie_rating))

        # Print the result
        print(f"Title: {movie_title}, Movie Rating: {movie_rating}")

    # Plotting the bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(titles, ratings, color='skyblue')
    plt.xlabel('Movie Title')
    plt.ylabel('Movie Rating')
    plt.title('Ratings for Movies')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.ylim(0, 5)  # Set the y-axis limit from 0 to 5
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the ratings on top of the bars
    for i, rating in enumerate(ratings):
        plt.text(i, rating + 0.1, str(rating), ha='center', va='bottom', fontsize=8)

    # Show the plot
    plt.tight_layout()
    plt.show()

except Exception as e:
    # Print any exceptions that occur
    print(e)
