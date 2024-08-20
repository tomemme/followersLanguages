import matplotlib.pyplot as plt
import plotly.express as px

def plot_language_distribution(language_data):
    languages = list(language_data.keys())
    counts = list(language_data.values())

    plt.figure(figsize=(10, 8))
    plt.barh(languages, counts, color='skyblue')
    plt.xlabel('Number of Repositories')
    plt.ylabel('Programming Language')
    plt.title('Programming Languages Used by Your Followers')
    plt.show()

def plot_language_distribution_plotly(language_data):
    languages = list(language_data.keys())
    counts = list(language_data.values())

    fig = px.pie(values=counts, names=languages, title='Programming Languages Used by Your Followers')
    fig.show()
