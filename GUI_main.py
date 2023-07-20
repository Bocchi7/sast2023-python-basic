import argparse
import json
import random
import re
import streamlit as st

def callback_but1():
    #st.write("run callback_but1()")
    file = st.session_state.get("upload")
    if file is not None:
        st.session_state.content = file.read()
    #st.write(st.session_state.uploaded)

def get_data():
    #if "cnt" not in st.session_state:
    #    st.session_state.cnt = 0
    #st.session_state.cnt += 1
    #st.write("cnt = ", st.session_state.cnt)
    #st.write(st.session_state.get("upload"))
    if st.session_state.get("content") is None:
        st.write("## 文章填空")
        upload = st.file_uploader("请上传题库文件", type=[".json"], key="upload")
        but1 = st.button("确定", key="but1", on_click=callback_but1)
        st.stop()
    #st.write(st.session_state.content)
    try:
        data = json.loads(st.session_state.content)
    except Exception:
        st.session_state.error = "该json文件不能被解析"
        st.experimental_rerun()
    return data

def callback_but2(articles):
    name = st.session_state.selection
    if name == "随机":
        name = random.choice(list(data["articles"].keys()))
    st.session_state.name = name

def replace(article, substitutions):
    text = article["text"]
    for key in article["hints"].keys():
        text = re.sub("\{\{"+key+"\}\}", substitutions[key], text)
    return text

def callback_but4():
    st.session_state.name = None

def callback_but5():
    st.session_state.content = None
    #st.session_state.upload = None
    st.session_state.name = None

if __name__ == "__main__":
    if (st.session_state.get("error")) is not None:
        st.error(st.session_state.error)
        st.session_state.error = None
        restart = st.button("重新开始", key="but5", on_click=callback_but5)
        st.stop()

    data = get_data()
    #st.write("已经上传成功！")
    try:
        articles = data["articles"]
        if st.session_state.get("name") is None:
            st.write("请选择一篇文章") 
            name = st.selectbox("", ["随机"] + list(articles.keys()), key="selection")
            but2 = st.button("确定", key="but2", on_click=callback_but2, args=(articles,))
            st.stop()
        name = st.session_state.name
    except Exception:
        st.session_state.error = "json文件格式错误!"
        st.experimental_rerun()

    article = articles[name]
    hints = article["hints"]
    
    back = st.button("返回", key="but4", on_click=callback_but4)
    st.write("### " + name);

    try:
        st.write(article["text"])
        st.write("请根据提示输入你的答案：")
        answers = {}
        for key in hints.keys():
            hint = hints[key]
            answers[key] = st.text_input("{key} : {hint}".format(key=key, hint=hint))
    except Exception:
        st.session_state.error = "《{name}》在json文件中格式错误!".format(name=name)
        st.experimental_rerun()

    if (st.button("提交", key="but3")):
        replaced_text=replace(article, answers)
        st.write(replaced_text)
    