# first draft of visualizing my followers languages.
# second draft trying to use as a github action.
import os
from github_api import get_followers, get_languages
from data_processing import aggregate_languages
from visualization import plot_language_distribution, plot_language_distribution_plotly

def main():
    username = os.getenv("FOLLOWERS_USERNAME")
    token = os.getenv("FOLLOWERS_TOKEN")

    if not token or not username:
        raise ValueError("GitHub token or username not found. Please set the GITHUB_TOKEN and GITHUB_USERNAME environment variables.")
    
    followers = get_followers(username, token)
    language_data = aggregate_languages(followers, token)
    
    plot_language_distribution(language_data)  # or plot_language_distribution_plotly(language_data)

if __name__ == "__main__":
    main()



