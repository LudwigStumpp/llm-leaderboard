import pandas as pd
import streamlit as st
import io
import requests
import re

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


def modify_from_markdown_links_to_html_links(text: str) -> str:
    """Modifies a markdown text to replace all markdown links with HTML links.

    Example: [DISPLAY](LINK) to <a href=LINK, target="_blank">DISPLAY</a>

    First find all markdown links with regex.
    Then replace them with: <a href=$2, target="_blank">$1</a>

    Args:
        text (str): Markdown text containing markdown links

    Returns:
        str: Markdown text with HTML links.
    """

    # find all markdown links
    markdown_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)

    # replace them with HTML links
    for display, link in markdown_links:
        text = text.replace(f"[{display}]({link})", f'<a href="{link}" target="_blank">{display}</a>')

    return text


def remove_markdown_links(text: str) -> str:
    """Modifies a markdown text to remove all markdown links.

    Example: [DISPLAY](LINK) to DISPLAY

    First find all markdown links with regex.
    Then replace them with: $1

    Args:
        text (str): Markdown text containing markdown links

    Returns:
        str: Markdown text without markdown links.
    """

    # find all markdown links
    markdown_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)

    # remove link keep display text
    for display, link in markdown_links:
        text = text.replace(f"[{display}]({link})", display)

    return text


def extract_table_and_format_from_markdown_text(markdown_table: str) -> pd.DataFrame:
    """Extracts a table from a markdown text and formats it as a pandas DataFrame.

    Args:
        text (str): Markdown text containing a table.

    Returns:
        pd.DataFrame: Table as pandas DataFrame.
    """
    df = (
        pd.read_table(io.StringIO(markdown_table), sep="|", header=0, index_col=1)
        .dropna(axis=1, how="all")  # drop empty columns
        .iloc[1:]  # drop first row which is the "----" separator of the original markdown table
    )

    # change all column datatypes to numeric
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    # remove whitespace from column names and index
    df.columns = df.columns.str.strip()
    df.index = df.index.str.strip()

    return df


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
    markdown_table = remove_markdown_links(markdown_table)
    df = extract_table_and_format_from_markdown_text(markdown_table)
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
