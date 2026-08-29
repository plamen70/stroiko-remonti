import os
import pandas as pd
import streamlit as st

# 1. Настройки на страницата и персонализиран дизайн (Стил)
st.set_page_config(
    page_title="Майстор Ремонт - Строителни Услуги",
    page_icon="🏗️",
    layout="wide",
)

# Промяна на основните цветове с персонализиран CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
    .main-title {
        color: #1b5e20;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Заглавна част (Hero секция)
st.markdown(
    '<h1 class="main-title">🏗️ Строително-Ремонтни Услуги & Качество</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: #555;'>Цялостни ремонти, довършителни дейности и монтажи с гаранция</h4>",
    unsafe_allow_html=True,
)
st.divider()

# 3. Нашите услуги
st.header("🛠️ Какво предлагаме")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧱 Довършителни работи")
    st.write("• Полагане на плочки (фаянс, теракота)")
    st.write("• Гипсокартон и окачени тавани")
    st.write("• Шпакловка и боядисване")

with col2:
    st.subheader("⚡ Инсталации & ВиК")
    st.write("• Подмяна на Ел. табла и окабеляване")
    st.write("• ВиК услуги и монтаж на санитария")
    st.write("• Монтаж на осветителни тела")

with col3:
    st.subheader("🪵 Монтажни дейности")
    st.write("• Полагане на ламиниран паркет")
    st.write("• Сглобяване на мебели и кухни")
    st.write("• Монтаж на интериорни врати")

st.divider()

# 4. Галерия с проекти (Визуален вариант)
st.header("📸 Галерия от изпълнени обекти")
g_col1, g_col2, g_col3 = st.columns(3)

with g_col1:
    st.image(
        "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=500",
        caption="Баня - фаянс и санитария",
    )

with g_col2:
    st.image(
        "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=500",
        caption="Всекидневна - шпакловка и боя",
    )

with g_col3:
    st.image(
        "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=500",
        caption="Кухня - монтаж и паркет",
    )

st.divider()

# 5. Интерактивен калкулатор за цена
st.header("🧮 Калкулатор за ориентировъчна оферта")
area = st.number_input(
    "Площ на помещенията (в кв.м):", min_value=10, max_value=500, value=50
)

services = st.multiselect(
    "Изберете нужните дейности:",
    [
        "Шпакловка и боядисване (15 лв./кв.м)",
        "Полагане на плочки (45 лв./кв.м)",
        "Гипсокартон (30 лв./кв.м)",
        "Подмяна на Ел. / ВиК (20 лв./кв.м)",
    ],
)

total_price = 0
if "Шпакловка и боядисване (15 лв./кв.м)" in services:
    total_price += area * 15
if "Полагане на плочки (45 лв./кв.м)" in services:
    total_price += area * 45
if "Гипсокартон (30 лв./кв.м)" in services:
    total_price += area * 30
if "Подмяна на Ел. / ВиК (20 лв./кв.м)" in services:
    total_price += area * 20

if total_price > 0:
    st.success(f"💰 Ориентировъчна стойност за труд: **{total_price:.2f} лв.**")

st.divider()

# 6. Форма за контакт със записване в Excel
st.header("📞 Изпратете запитване за оглед")

excel_file = "zapitvania.xlsx"

with st.form("contact_form"):
    name = st.text_input("Вашето име:")
    phone = st.text_input("Телефон за връзка:")
    city = st.text_input("Град / Населено място:")
    details = st.text_area("Описание на ремонта:")

    submitted = st.form_submit_button("Изпрати запитване")

    if submitted:
        if name and phone:
            # Данни от новата заявка
            new_data = pd.DataFrame(
                [
                    {
                        "Име": name,
                        "Телефон": phone,
                        "Град": city,
                        "Описание": details,
                        "Ориентировъчна сума": f"{total_price:.2f} лв.",
                    }
                ]
            )

            # Проверка дали файлът вече съществува
            if os.path.exists(excel_file):
                df_existing = pd.read_excel(excel_file)
                df_updated = pd.concat(
                    [df_existing, new_data], ignore_index=True
                )
                df_updated.to_excel(excel_file, index=False)
            else:
                new_data.to_excel(excel_file, index=False)

            st.balloons()
            st.success(
                f"Благодарим Ви, {name}! Запитването беше изпратено и записано успешно!"
            )
        else:
            st.error("Моля, попълнете поне име и телефон за връзка.")
