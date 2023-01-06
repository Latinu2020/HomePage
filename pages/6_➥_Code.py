import streamlit as st

st.set_page_config(page_title="CODE", page_icon="📊")

st.markdown("# CODE")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)

"""### gif from url"""
st.markdown("![Alt Text](https://media.giphy.com/media/7FrOU9tPbgAZtxV5mb/giphy-downsized-large.gif)")