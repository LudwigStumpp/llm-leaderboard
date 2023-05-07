import pandas as pd
import streamlit as st
import io
import requests

REPO_URL = "https://github.com/LudwigStumpp/llm-leaderboard"


def grab_readme_file_from_repo(repo_url: str) -> str:
    """Grabs the README.md file from a GitHub repository.

    Args:
        repo_url (str): URL of the GitHub repository.

    Returns:
        str: Content of the README.md file.
    """
    readme_url = repo_url.replace("github.com", "raw.githubusercontent.com") + "/main/README.md"
    readme = requests.get(readme_url).text
    return readme


def extract_markdown_table_from_multiline(multiline: str, table_headline: str) -> str:
    """Extracts the markdown table from a multiline string.

    Args:
        multiline (str): content of README.md file.
        table_headline (str): Headline of the table in the README.md file.

    Returns:
        str: Markdown table.

    Raises:
        ValueError: If the table could not be found.
    """
    # extract everything between the table headline and the next headline
    table = []
    start = False
    for line in multiline.split("\n"):
        if line.startswith(table_headline):
            start = True
        elif line.startswith("###"):
            start = False
        elif start:
            table.append(line + "\n")

    if len(table) == 0:
        raise ValueError(f"Could not find table with headline '{table_headline}'")

    return "".join(table)


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
    readme = grab_readme_file_from_repo(REPO_URL)
    markdown_table = extract_markdown_table_from_multiline(readme, table_headline="### Leaderboard")

    df = (
        pd.read_table(io.StringIO(markdown_table), sep="|", header=0, skipinitialspace=True, index_col=1)
        .dropna(axis=1, how="all")  # drop empty columns
        .iloc[1:]  # drop first row which is the "----" separator of the original markdown table
    )

    # show interactive table
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
