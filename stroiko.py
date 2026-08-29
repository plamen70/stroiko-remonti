import streamlit as st

st.set_page_config(
    page_title="Майстор Ремонт - Строителни Услуги", 
    page_icon="🏗️", 
    layout="wide"
)

# Заглавие и банер
st.title("🏗️ Майстор Ремонт - Професионални Строителни Услуги")
st.write("Качествени строително-ремонтни дейности, довършителни работи и майсторски решения за вашия дом и офис.")

st.image(
    "https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=1200&auto=format&fit=crop", 
    caption="Професионализъм и качество във всеки детайл", 
    use_container_width=True
)

st.markdown("---")

# Секция Услуги с галерия
st.header("🛠️ Нашите Основни Услуги")

col_u1, col_u2, col_u3 = st.columns(3)

with col_u1:
    st.subheader("🚿 Ремонт на бани и плочки")
    st.image(
        "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=600&auto=format&fit=crop", 
        use_container_width=True
    )
    st.write("Полагане на фаянс, теракота, гранитогрес, хидроизолация и монтаж на санитария.")

with col_u2:
    st.subheader("🎨 Шпакловка и боядисване")
    st.image(
        "https://images.unsplash.com/photo-1562259949-e8e7689d7828?q=80&w=600&auto=format&fit=crop", 
        use_container_width=True
    )
    st.write("Фино шпакловане, грундиране, шлайфане и боядисване с висококачествени латекси.")

with col_u3:
    st.subheader("📐 Гипсокартон и окачени тавани")
    st.image(
        "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=600&auto=format&fit=crop", 
        use_container_width=True
    )
    st.write("Изграждане на преградни стени, окачени тавани, скрито осветление и изолации.")

st.markdown("---")

# Секция Калкулатор и предимства
st.header("🧮 Калкулатор на оферта & Предимства")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Изчислете ориентировъчна цена")
    area = st.number_input("Площ за ремонт (кв.м):", min_value=1, value=50)
    service = st.selectbox("Изберете услуга:", [
        "Шпакловка и боядисване (15 лв/кв.м)",
        "Полагане на плочки и фаянс (35 лв/кв.м)",
        "Монтаж на гипсокартон (25 лв/кв.м)",
        "Цялостен довършителен ремонт (80 лв/кв.м)"
    ])
    
    price_per_m2 = 15
    if "плочки" in service:
        price_per_m2 = 35
    elif "гипсокартон" in service:
        price_per_m2 = 25
    elif "Цялостен" in service:
        price_per_m2 = 80
        
    total_price = area * price_per_m2
    st.info(f"💡 Ориентировъчна крайна сума: **{total_price} лв.**")

with col2:
    st.subheader("Защо да се доверите на нас?")
    st.success("✅ **Дългогодишен опит:** Гаранция за качество при всеки обект.")
    st.success("✅ **Коректни срокове:** Работим бързо и спазваме уговорените дати.")
    st.success("✅ **Чистота и ред:** Оставяме обекта почистен след приключване.")
    st.success("✅ **Без скрити разходи:** Всички цени са прозрачни и предварително уговорени.")

st.markdown("---")

# Секция Истинска Streamlit форма за запитване (работеща с Formspree)
st.header("📩 Изпратете Запитване за Безплатен Оглед")
st.write("Попълнете полетата по-долу и съобщението ще стигне директно до нашия имейл!")

with st.form("contact_form"):
    name = st.text_input("Вашето име")
    email = st.text_input("Вашият имейл адрес")
    phone = st.text_input("Телефон за връзка")
    message = st.text_area("Описание на ремонта")
    
    submit_button = st.form_submit_button("🚀 Изпрати запитването")
    
    if submit_button:
        if name and email and phone and message:
            import requests
            response = requests.post("https://formspree.io/f/xrpgbzko", data={
                "name": name,
                "email": email,
                "phone": phone,
                "message": message
            })
            if response.status_code == 200:
                st.success("✅ Запитването е изпратено успешно! Ще се свържем с вас скоро.")
            else:
                st.error("❌ Възникна грешка при изпращането. Моля, опитайте отново.")
        else:
            st.warning("⚠️ Моля, попълнете всички полета преди да изпратите.")
