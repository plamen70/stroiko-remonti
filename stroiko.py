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

# Секция Форма за запитване
st.header("📩 Изпратете Запитване за Безплатен Оглед")
st.write("Попълнете формата и ние ще се свържем с вас възможно най-скоро!")

contact_form = """
<form action="https://formspree.io/f/xrpgbzko" method="POST" style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #eee;">
    <label style="font-weight: bold;">Име и Фамилия</label><br>
    <input type="text" name="name" placeholder="Вашето име" required style="width: 100%; margin-top: 5px; margin-bottom: 15px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;"><br>
    
    <label style="font-weight: bold;">Имейл адрес</label><br>
    <input type="email" name="email" placeholder="Вашият имейл" required style="width: 100%; margin-top: 5px; margin-bottom: 15px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;"><br>
    
    <label style="font-weight: bold;">Телефон за връзка</label><br>
    <input type="text" name="phone" placeholder="08XX XXX XXX" required style="width: 100%; margin-top: 5px; margin-bottom: 15px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;"><br>
    
    <label style="font-weight: bold;">Описание на ремонта</label><br>
    <textarea name="message" placeholder="Опишете накратко какъв ремонт ви предстои..." required style="width: 100%; height: 120px; margin-top: 5px; margin-bottom: 15px; padding: 10px; border-radius: 5px; border: 1px solid #ccc;"></textarea><br>
    
    <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 12px 30px; border-radius: 5px; cursor: pointer; font-weight: bold; font-size: 16px;">🚀 Изпрати запитването</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
