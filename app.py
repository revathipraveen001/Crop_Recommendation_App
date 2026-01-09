import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Page config
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# Title
st.markdown(
    "<h1 style='text-align: center;'>🌱 Crop Recommendation System</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# Load data
data = pd.read_csv("crop_data.csv")

# Encode target
le = LabelEncoder()
data['crop_encoded'] = le.fit_transform(data['crop'])

X = data[['temperature', 'rainfall']]
y = data['crop_encoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = DecisionTreeClassifier(max_depth=4)
model.fit(X_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test))

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌡 Input Parameters")
    temp = st.slider("Temperature (°C)", 10, 45, 25)
    rain = st.slider("Rainfall (mm)", 20, 300, 120)

    if st.button("🌾 Predict Crop"):
        prediction = model.predict([[temp, rain]])
        crop_name = le.inverse_transform(prediction)[0]

        st.success(f"✅ Recommended Crop: **{crop_name}**")
        st.info(f"📊 Model Accuracy: **{accuracy*100:.2f}%**")

with col2:
    st.subheader("📈 Data Insights")

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=data,
        x="temperature",
        y="rainfall",
        hue="crop",
        s=100,
        ax=ax
    )
    ax.set_title("Crop Distribution based on Temperature & Rainfall")
    st.pyplot(fig)

st.markdown("---")

# Footer
st.markdown(
    "<p style='text-align:center;'>Developed for Academic Mini Project 🎓</p>",
    unsafe_allow_mp
