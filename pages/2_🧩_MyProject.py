import streamlit as st

st.set_page_config(page_title="My Project", page_icon="📈")


html_page="""
    <!DOCTYPE html>  
    <html>  
    <head>  
    <style>   
    div {  
        width: 100px;  
        height: 100px;  
        background: red;  
        position: relative;  
        -webkit-animation: myfirst 5s; /* Chrome, Safari, Opera */  
        animation: myfirst 5s;  
    }  
    /* Chrome, Safari, Opera */  
    @-webkit-keyframes myfirst {  
        0%   {background:red; left:0px; top:0px;}  
        25%  {background:yellow; left:300px; top:0px;}  
        50%  {background:blue; left:200px; top:300px;}  
        75%  {background:green; left:0px; top:200px;}  
        100% {background:red; left:0px; top:0px;}  
    }  
    /* Standard syntax */  
    @keyframes myfirst {  
        0%   {background:red; left:0px; top:0px;}  
        25%  {background:yellow; left:300px; top:0px;}  
        50%  {background:blue; left:300px; top:200px;}  
        75%  {background:green; left:0px; top:200px;}  
        100% {background:red; left:0px; top:0px;}  
    }  
    </style>  
    </head>  
    <body>  
    <p><b>Note:</b> The Internet Explorer 9 and its earlier versions don't support this example.</p>  
    <div></div>  
    </body>  
    </html>  
"""


st.markdown(html_page.format(),unsafe_allow_html=True)

"""### My Project"""
st.markdown("![Alt Text](https://media.giphy.com/media/fixyBa6ainp5yUQPhU/giphy.gif)")