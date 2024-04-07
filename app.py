import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

res=requests.get("http://ilex.in-addr.jp/cgi-bin/presume-rh1.cgi?amds=44132")
soup=BeautifulSoup(res.text,"html.parser")
text1=soup.find_all("font",size="7")
list=str(text1).split(" ")
ondo=float(list[3])
sitsudo=int(list[8])
hukai=round(0.81*ondo+0.01*sitsudo*(0.99*ondo-14.3)+46.3)
st.title("ただいまの不快指数(1時間ごとに更新)")
st.subheader("気温    "+str(ondo)+" ℃")
st.subheader("湿度    "+str(sitsudo)+" %RH")
st.subheader("不快指数 "+str(hukai))
comment =[[55,"寒い"],[60,"肌寒い"],[65,"何も感じない"],[70,"快い"],[75,"暑くない"],[80,"やや暑い"],[85,"暑くて汗が出る"],[300,"寒い"]]

for x in range(8):
    if hukai<comment[x][0]:
        comment1=comment[x][1]
        break
st.subheader(comment1)
st.text("東京の気温湿度 from アメダス")
