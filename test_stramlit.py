import streamlit as st
import pandas as pd
import random
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="给仔仔的浪漫仪式感", layout="centered")

st.title("给仔仔的生日礼物选啥好捏")

st.markdown("""
    <style>
        .stApp {
            background-image: url("https://i.imgur.com/j6CjBvn.jpeg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .title {
            font-size: 40px;
            font-weight: bold;
            color: #ffecec;
            text-shadow: 2px 2px 4px #000000;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #fff0f0 !important;
            text-shadow: 1px 1px 2px #000;
        }

        .dataframe {
            background-color: rgba(255, 255, 255, 0.75);
            color: #333;
            font-family: "serif";
            border-radius: 10px;
        }

        .stAlert-success {
            color: #004d00 !important;
            background-color: rgba(232, 255, 232, 0.95) !important;
        }

        button[kind="primary"] {
            background-color: #ff6699 !important;
            color: white !important;
            border: None;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🎈🗼 给仔仔的生日礼物随机抽选器</p>', unsafe_allow_html=True)

gift_list = [
    ["Marshall 音箱", "想每天在你的小窝里放我们都爱的杯糕姐和BRAT"],
    ["Balenciaga Track 鞋", "想你走路都帅得冒火，踩在航航身上看世界"],
    ["Dior 邮差包", "放我的思念和你未来的登机牌，一起邮寄到未来"],
    ["Goyard 邮差包", "让你的土逼同事知道什么叫做巴黎左岸，欧拜托，我仔仔秒了"],
    ["Celine 内袋银铅包", "委屈都给我背，你负责可爱"],
    ["Maison Margiela 壳头鞋", "每一步都像踩在Louvre和Rue Rivoli的红毯"],
    ["Tiffany 钻石项链", "想让你的锁骨比东京塔埃菲尔铁塔还闪，最好每天晃我一下哈"],
    ["Sandro 大衣", "冷的时候我不在，就让这件大衣代替我抱你"],
    ["Acne Studios 卡兰大衣", "Sandro平替但是还是我们made in paris 的sandro秒了"],
    ["LV 银色吊链手链", "每次你一抬手就能想到东京塔下面六本木的亮晶晶"],
    ["梵克雅宝手链", "不是宝诗龙买不起，是我想你一抬手就让全世界知道你有人宠啊"]
]

df = pd.DataFrame(gift_list, columns=["🎁 礼物名称", "💌 航航想说"])

st.dataframe(df)


if st.button("🍀 抽一件礼物"):
    selected = random.choice(gift_list)

    st.markdown(
        f"""
        <div style="
            background-color: rgba(255, 255, 255, 0.85);
            border-left: 5px solid #FF6699;
            padding: 16px;
            border-radius: 10px;
            margin-top: 20px;
            font-family: serif;
            color: #2c2c2c;
        ">
            <h4 style="margin-bottom: 8px;">🎁 <b>今年选中的礼物是：</b>{selected[0]}</h4>
            <p style="margin: 0;">💌 航航想说：{selected[1]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.header("🌍 航航想和仔仔去这些地方")

places = [
    {"name": "北海道·雪地温泉", "lat": 43.2203,
        "lon": 142.8635, "note": "想和你泡在雪地温泉里，头顶飘雪"},
    {"name": "南法·普罗旺斯", "lat": 43.8367, "lon": 4.3601, "note": "薰衣草开的时候，想带你去闻一整片夏天"},
    {"name": "京都·清水寺", "lat": 34.9948, "lon": 135.7850,
        "note": "一起穿和服去抽签，如果是凶我们就抱紧一点吓死所有人"},
    {"name": "冰岛·极光", "lat": 64.9631, "lon": -19.0208, "note": "想看一场极光，然后在幸福里睡去"},
    {"name": "巴黎·塞纳河游船", "lat": 48.8566, "lon": 2.3522, "note": "我们去看铁塔一闪一闪亮晶晶✨"},
    {"name": "尼斯·海边", "lat": 43.7102, "lon": 7.2620,
        "note": "我们光脚踩在沙里，我踩踩踩踩，她朴彩英算个啥"},
    {"name": "特内里费岛", "lat": 28.2916, "lon": -
        16.6291, "note": "想带你躺在海边的酒店一周，从早到晚陪你看你爱的海"},
    {"name": "巴厘岛·乌布", "lat": -8.5069, "lon": 115.2625,
        "note": "我们像zqz那样在乌布的瀑布坦胸露乳"}
]

m = folium.Map(location=[48.8566, 2.3522], zoom_start=2)


for place in places:
    html_popup = f"""
    <div style='width: 200px; font-size: 14px; font-family: serif; 
                text-align: center; line-height: 1.5; color: #333;'>
        <b>{place['name']}</b><br>{place['note']}
    </div>
    """
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=folium.Popup(html_popup, max_width=250),
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="heart")
    ).add_to(m)


st_folium(m, width=700, height=450)
