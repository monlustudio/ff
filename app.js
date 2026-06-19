import streamlit as st

# 資料庫
DB = {
    "flowers": ["厄瓜多玫瑰", "奧斯汀玫瑰", "太陽玫瑰", "康乃馨", "牡丹", "繡球花", "無"], 
    "aux": ["滿天星", "卡斯比亞", "兔尾草", "加那利草", "臘梅", "無"],
    "leaf": ["圓葉尤加利", "細葉尤加利", "銀葉桉", "雪松", "苔蘚", "無"],
    "wraps": ["霧面紙", "反光紙", "金屬紙", "薄紗", "牛皮紙"]
}

st.title("永生花設計提示詞生成器")

# 介面配置
flower_type = st.selectbox("花藝類型", ["盆花", "捧花"])

col1, col2 = st.columns(2)
with col1:
    mainA = st.selectbox("主花 A", DB["flowers"])
    mainB = st.selectbox("主花 B", DB["flowers"])
    mainC = st.selectbox("主花 C", DB["flowers"])
with col2:
    auxA = st.selectbox("輔助花 A", DB["aux"])
    auxB = st.selectbox("輔助花 B", DB["aux"])
    leafA = st.selectbox("葉材 A", DB["leaf"])
    leafB = st.selectbox("葉材 B", DB["leaf"])

wrap = st.selectbox("包裝材質", DB["wraps"])

# 生成邏輯
if st.button("生成提示詞"):
    # 過濾掉「無」的選項
    items = [i for i in [mainA, mainB, mainC, auxA, auxB, leafA, leafB] if i != "無"]
    
    prompt = f"Professional preserved flower {flower_type}, featuring {', '.join(items)}, wrapped in {wrap}. High-end commercial product photography, 8k, soft lighting, photorealistic."
    
    st.success("生成成功！")
    st.text_area("複製提示詞:", value=prompt, height=150)
    st.write("提示：點擊右上方複製按鈕即可使用。")
