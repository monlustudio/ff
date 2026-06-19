import streamlit as st

# 資料庫設定
FLOWER_TYPES = ["盆花", "捧花"]
MATERIALS = ["玫瑰", "繡球花", "康乃馨", "太陽玫瑰", "滿天星", "兔尾草", "卡斯比亞", 
             "尤加利葉", "黃金球", "薰衣草", "千日紅", "雪松", "麥桿菊", "珍珠草", 
             "小蒼蘭", "陸蓮", "星辰花", "海芋", "紅掌", "大波斯菊", "鈴蘭", "鐵線蓮", 
             "罌粟花", "藍星花", "小米果", "山防風", "繡線菊", "白梅", "臘菊", "無"]

WRAP_TYPES = ["霧面防水紙", "韓系透光薄紗", "金屬質感紙", "復古牛皮紙", "絲絨緞帶包裝"]

# 顏色調色盤 (Hex Code)
COLORS = {
    "乾燥玫瑰粉": "#DCAE96", "奶茶色": "#D2B48C", "奶油白": "#FFFDD0", 
    "深紅色": "#8B0000", "莫蘭迪藍": "#778899", "鼠尾草綠": "#9DC183", "無": "#FFFFFF"
}

st.set_page_config(page_title="永生花設計助手", layout="centered")
st.title("🌸 永生花設計提示詞產生器")

# --- 第一階段：選項設定 ---
with st.form("design_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        type_select = st.selectbox("花的類型", FLOWER_TYPES)
        main_a = st.selectbox("主花 A", MATERIALS)
        main_b = st.selectbox("主花 B", MATERIALS)
        main_c = st.selectbox("主花 C", MATERIALS)
        aux_a = st.selectbox("輔助花 A", MATERIALS)
        aux_b = st.selectbox("輔助花 B", MATERIALS)
        leaf_a = st.selectbox("葉材 A", MATERIALS)
        leaf_b = st.selectbox("葉材 B", MATERIALS)
    
    with col2:
        st.write("### 顏色選擇")
        color_main_a = st.color_picker("主花 A 顏色", COLORS["乾燥玫瑰粉"])
        color_main_b = st.color_picker("主花 B 顏色", COLORS["奶油白"])
        color_main_c = st.color_picker("主花 C 顏色", "#FFFFFF")
        color_aux = st.color_picker("輔助花顏色", COLORS["莫蘭迪藍"])
        color_leaf = st.color_picker("葉材顏色", COLORS["鼠尾草綠"])
        wrap_style = st.selectbox("包裝紙材質", WRAP_TYPES)
        wrap_color = st.color_picker("包裝紙顏色", COLORS["奶茶色"])

    submitted = st.form_submit_button("生成提示詞")

# --- 生成與輸出 ---
if submitted:
    prompt = f"""
    Professional product photography of a {type_select}. 
    Featuring {main_a}, {main_b}, {main_c} as main flowers. 
    Accented with {aux_a}, {aux_b} and {leaf_a}, {leaf_b}. 
    Wrapped in {wrap_style}. 
    Color palette: {color_main_a}, {color_main_b}, {color_aux}, {color_leaf}, {wrap_color}.
    High-end floral design, studio lighting, soft bokeh, 8k resolution, realistic textures, preserved flower aesthetics.
    """
    
    st.subheader("生成的提示詞：")
    st.code(prompt, language="text")
    
    # 複製功能
    if st.button("複製提示詞"):
        st.write("已複製到剪貼簿！")
        st.toast("提示詞已複製")
