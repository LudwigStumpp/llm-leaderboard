import io

import pandas as pd
import requests
import streamlit as st

REPO_URL = "https://github.com/LudwigStumpp/llm-leaderboard"


def grab_file_from_repo(repo_url: str, filename: str) -> str:
    """Grabs a file from a GitHub repository.

    Args:
        repo_url (str): URL of the GitHub repository.
        filename (str): Name of the file to grab.

    Returns:
        str: Content of the file.
    """
    url = repo_url.replace("github.com", "raw.githubusercontent.com") + f"/main/{filename}"
    return requests.get(url).text


def setup_basic():
    title = "LLM-Leaderboard"

    st.set_page_config(
        page_title=title,
        page_icon="🏆",
    )
    st.title(title)

    st.markdown(
        """
        A joint community effort to create one central leaderboard for LLMs.
        Visit [llm-leaderboard](https://github.com/LudwigStumpp/llm-leaderboard) to contribute.
        """
    )


def setup_table():
    csv_table = grab_file_from_repo(REPO_URL, "leaderboard.csv")
    df = pd.read_csv(io.StringIO(csv_table), index_col=0)
    st.dataframe(df)


def setup_footer():
    st.markdown(
        """
        ---
        Made with ❤️ by the awesome open-source community from all over 🌍.
        """
    )


def main():
    setup_basic()
    setup_table()
    setup_footer()


if __name__ == "__main__":
    main()
