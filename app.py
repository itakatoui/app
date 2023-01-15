import streamlit as st

st.set_page_config(page_title="新年の挨拶カード", page_icon=":tada:", layout="wide")

st.title("新年の挨拶カードジェネレータ")

name = st.text_input("あなたの名前を入力してください: ")
message = st.text_area("メッセージを入力してください: ")

if st.button("カードを生成"):
    st.success(name + "さん、謹賀新年!")
    st.markdown(message)
    st.markdown("下のボタンをクリックしてカードをダウンロードできます")
    if st.button("カードをダウンロード"):
        pass  # Add code here to download the card as an image.
