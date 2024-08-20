from collections import defaultdict

def aggregate_languages(followers, token):
    from github_api import get_languages  # Import here to avoid circular imports
    language_dict = defaultdict(int)
    for follower in followers:
        languages = get_languages(follower['login'], token)
        for language in languages:
            language_dict[language] += 1
    return language_dict
