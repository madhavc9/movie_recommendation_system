<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">🎬 Movie Recommendation System</h3>
  <img src="/MRS_logo.png" alt="Movie Recommendation Logo" width="600">
  <p align="center">
    <br />
    <a href="https://drive.google.com/file/d/15EqioqNxrb90jf70SSsfNXDwz37_o3wj/view?usp=sharing" target="_blank"><strong>Explore the documentation »</strong></a>
    <br />
    <a href="https://drive.google.com/file/d/1GlUXc6Hzm5zCzHawjl8RtxAPqNpRqVwn/view?usp=sharing" target="_blank"><strong>Video Demonstration »</strong></a>
    <br />
  </p>
</div>
<hr>
Overview

The Movie Recommendation System is an AI-powered web application that helps users find movies similar to their preferences. Built with machine learning and natural language processing techniques, this system provides personalized recommendations based on movie content, such as genre, cast, and keywords. Users can select a movie and receive a list of similar movies with accompanying posters, making movie discovery easy and visually engaging.

The project consists of two main parts:

	1. Data Processing and Model Development in a Jupyter Notebook (movie recommender system.ipynb).
	2. Web Application built with Streamlit (app.py) for an interactive user experience.
<hr>
Features

	• Content-Based Filtering: Recommends movies based on the content (genre, cast, etc.) of the selected movie.
	• Interactive Web Application: Simple and intuitive interface powered by Streamlit.
	• Visual Enhancements: Displays movie posters using The Movie Database (TMDb) API for a rich user experience.
<hr>
Installation and Usage

Prerequisites

Ensure you have the following installed:

	• Python 3.8 or higher
	• pip (Python package manager)
<hr>
Setup Instructions

	1. Clone the Repository:
  		  git clone https://github.com/madhavc9/movie-recommendation-system.git
  		  cd movie-recommendation-system

	2. Install Dependencies:
  		  Install the necessary Python libraries using:
  		  pip install -r requirements.txt

   		  Note: The requirements.txt file should include the following libraries:
		• streamlit
		• pandas
		• scikit-learn
		• requests

	3. Obtain TMDb API Key:
		• Sign up on TMDb and obtain an API key.
		• Add your API key to the app.py file in the fetch_poster function.

	4. Run the Streamlit Application:
    	streamlit run app.py

    5. Using the Application:
		• Open your browser and navigate to the local URL provided by Streamlit.
		• Select a movie from the dropdown menu to get personalized movie recommendations.
<hr>
How It Works

	1. Data Processing (movie recommender system.ipynb):
		• Loads and preprocesses movie data.
		• Generates a “tags” column for each movie, combining its genre, cast, and other details.
		• Converts this text data into vectors using TF-IDF (Term Frequency-Inverse Document Frequency) to      facilitate similarity measurement.
		• Computes cosine similarity between movies and saves the processed data and similarity matrix.

	2. Web Application (app.py):
		• Loads precomputed data and similarity matrix.
		• Provides an interface where users can choose a movie and receive similar movie suggestions.
		• Fetches movie posters using the TMDb API and displays them alongside recommendations.
<hr>
Future Enhancements

		• Hybrid Recommendation: Combine content-based filtering with collaborative filtering for improved recommendations.
		• User Profiles: Store user preferences and create personalized recommendation lists.
		• Improved Similarity Calculation: Experiment with other NLP techniques, such as Word2Vec, for vectorization.
<hr>
Contributing

Feel free to open issues or create pull requests if you’d like to contribute to the project.
<hr>
Acknowledgments

		• TMDb for movie poster API access.
		• Scikit-Learn for machine learning utilities.
		• Streamlit for creating a simple and powerful UI.
<hr>
<div align="center">
Enjoy discovering your next favorite movie! 🎥
</div>


