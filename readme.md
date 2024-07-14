# Recommendation System Exploration

This folder contains Jupyter Notebook files exploring various aspects of a recommendation system. There is no frontend in the project due to time constraints.

## Datasets

5 datasets are used in this project, given below with the column names in each file. 

1. interactions_100k_with_relationships.csv
    * Interaction ID, User ID, PostID, Interaction Type, Interaction Timestamp, Watch Duration
2. posts_100k_with_relationships.csv
    * Post ID, Tags/Keywords, Category (Reel or Image), UploaderID, Upload Time, Timestamp, Views, Likes, Dislikes, Comments
3. users_100k_with_relationships.csv
    * UserID, Username, Full Name, Gender, Country, Language Preference, Interests
4. TikTok Data.csv (obtained from kaggle)
5. UserData.csv (obtained from kaggle)

**Note : First 3 datasets are custom generated**

## Notebooks

**1. AllParamsRec.ipynb**

This notebook implements a recommendation system that blends posts based on:

* **20% liked by friends:** Recommendations based on friends' interactions.
* **30% new:** Exploration of potentially interesting unseen content.
* **50% past interactions:** Leverages user's past preferences.

**2. Top_Users.ipynb**

This identifies the top 10 users most similar to a target user using cosine similarity. It utilizes user information such as demographics, interests, and gender. Can be modified to use bio, age, language etc for each user.

**3. VideoRecommendation.ipynb**

This notebook recommends video content based on transcript similarity. It employs the following techniques:

* **CountVectorizer:** Creates a numerical representation of the video transcripts, focusing on word frequencies.
* **Stemming:** Reduces words to their base forms (e.g., "running" and "runs" become "run").
* **Cosine Similarity:** Measures the similarity between video transcripts based on their word representations.

## Running the Notebooks

1. Clone this repository to your local machine.
2. Install the required Python libraries using `pip install <library_name>`.
3. Open the notebooks in a Jupyter Notebook environment.
4. Download and load the datasets in your environment.
5. Update the code to point to your specific data paths.
6. Run the code cells to execute the recommendation algorithms.

## Disclaimer

This code is for educational purposes only and may require modifications for specific use cases. The datasets used are provided in the repository.