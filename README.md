# GitHub Follower Language Analysis

### Overview
The **GitHub Follower Language Analysis** tool is designed to analyze the programming languages used by your GitHub followers. This tool fetches data from the GitHub API and visualizes the programming languages your followers use, helping you gain insights into your network's technical landscape.

### Features
- **Fetch Followers:** Retrieve a list of your GitHub followers.
- **Analyze Repositories:** Determine the primary programming languages used by each follower.
- **Data Visualization:** Display the analysis results using Matplotlib or Plotly, providing an intuitive visual representation of the programming languages.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/followersLanguages.git
   cd followersLanguages
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up GitHub API Token:**
   - Generate a GitHub Personal Access Token from [GitHub's Token Settings](https://github.com/settings/tokens).
   - Replace `"your_github_token"` in `main.py` with your actual token.

### Usage

1. **Update the Username:**
   - Replace `"your_github_username"` in `main.py` with your actual GitHub username.

2. **Run the Program:**
   ```bash
   python main.py
   ```

3. **View Results:**
   - The program will generate a bar chart or pie chart (depending on your choice) that visualizes the programming languages used by your followers.

![GUI](https://github.com/tomemme/followersLanguages/blob/master/graphExample.PNG)

### Project Structure

- **`main.py`**: The entry point for running the analysis.
- **`github_api.py`**: Handles API interactions with GitHub.
- **`data_processing.py`**: Processes and aggregates the data fetched from GitHub.
- **`visualization.py`**: Contains functions for visualizing the analysis results.
- **`.gitignore`**: Excludes unnecessary files like virtual environments and `__pycache__` from the repository.

### Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch for your feature or bug fix, and submit a pull request. Contributions are welcome!

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgments

Special thanks to the open-source community for providing the tools and libraries that made this project possible.