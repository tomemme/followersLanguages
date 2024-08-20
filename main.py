# first draft of visualizing my followers languages.
from github_api import get_followers, get_languages
from data_processing import aggregate_languages
from visualization import plot_language_distribution, plot_language_distribution_plotly

def main():
    username = "your_actual_github_username"
    token = "your_actual_github_token"
    
    followers = get_followers(username, token)
    language_data = aggregate_languages(followers, token)
    
    plot_language_distribution(language_data)  # or plot_language_distribution_plotly(language_data)

if __name__ == "__main__":
    main()



