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


def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Modified from https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()

    modification_container = st.container()

    with modification_container:
        to_filter_index = st.multiselect("Filter rows on", df.index)
        if to_filter_index:
            df = pd.DataFrame(df.loc[to_filter_index])

        to_filter_columns = st.multiselect("Filter columns on", df.columns)
        if to_filter_columns:
            df = pd.DataFrame(df[to_filter_columns])

    return df


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
    st.markdown("### Leaderboard")
    st.dataframe(filter_dataframe(df))


def setup_benchmarks():
    csv_table = grab_file_from_repo(REPO_URL, "benchmarks.csv")
    df = pd.read_csv(io.StringIO(csv_table), index_col=0)
    df = df.sort_index(ascending=True)

    st.markdown("### Covered Benchmarks")

    selected_benchmark = st.selectbox("Select a benchmark to learn more:", df.index.unique())
    df_selected = df.loc[selected_benchmark]
    text = [
        f"Name: {selected_benchmark} ",
    ]
    for key in df_selected.keys():
        text.append(f"{key}: {df_selected[key]}")
    st.markdown("\n".join(text))


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
    setup_benchmarks()
    setup_footer()


if __name__ == "__main__":
    main()
