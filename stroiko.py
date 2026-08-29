import streamlit as st

st.set_page_config(page_title="Майстор Ремонт - Строителни Услуги", page_icon="🏗️", layout="wide")

st.title("🏗️ Майстор Ремонт - Строителни Услуги")
st.write("Качествени строително-ремонтни дейности,довършителни работи и майсторски услуги.")

st.markdown("---")

# Секция Услуги и Цени
st.header("🛠️ Услуги и Калкулатор")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Изчислете приблизителна цена")
    area = st.number_input("Квадратура (кв.м):", min_value=1, value=50)
    service = st.selectbox("Тип услуга:", [
        "Шпакловка и боядисване (15 лв/кв.м)",
        "Полагане на плочки и фаянс (35 лв/кв.м)",
        "Монтаж на гипсокартон (25 лв/кв.м)",
        "Цялостен ремонт (80 лв/кв.м)"
    ])
    
    price_per_m2 = 15
    if "плочки" in service:
        price_per_m2 = 35
    elif "гипсокартон" in service:
        price_per_m2 = 25
    elif "Цялостен" in service:
        price_per_m2 = 80
        
    total_price = area * price_per_m2
    st.success(f"Ориентировъчна сума: **{total_price} лв.**")

with col2:
    st.subheader("Защо да изберете нас?")
    st.write("✅ Дългогодишен опит и професионализъм")
    st.write("✅ Спазване на уговорените срокове")
    st.write("✅ Прозрачни цени без скрити такси")
    st.write("✅ Качествени материали и прецизна изработка")

st.markdown("---")

# Секция Форма за контакт
st.header("📋 Изпратете запитване за оферта")
st.write("Попълнете формата и ще се свържем с вас бързо!")

contact_form = """
<form action="https://formspree.io/f/xrpgbzko" method="POST">
    <input type="text" name="name" placeholder="Вашето име" required style="width: 100%; margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
    <input type="email" name="email" placeholder="Вашият имейл" required style="width: 100%; margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
    <input type="text" name="phone" placeholder="Телефон за връзка" required style="width: 100%; margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
    <textarea name="message" placeholder="Опишете накратко какъв ремонт ви е необходим..." required style="width: 100%; height: 120px; margin-bottom: 10px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
    <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 12px 24px; border-radius: 5px; cursor: pointer; font-weight: bold;">Изпрати запитване</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
