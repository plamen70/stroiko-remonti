import streamlit as st

# Настройки на страницата
st.set_page_config(
    page_title="Строителни Ремонти Попово - Майстор за Вашия Дом",
    page_icon="🏗️",
    layout="wide"
)

# Заглавие и банер
st.title("🏗️ Строителни Ремонти Попово - Майстор за Вашия Дом")
st.write("Качествени строително-ремонтни дейности, лепене на плочки, шпакловка, боядисване и довършителни работи за гр. Попово и региона.")
st.markdown("[📞 **Директна връзка: 088 600 3363**](tel:0886003363)")

# Начална снимка (банер)
st.image(
    "banner.jpg",
    caption="Професионално полагане на плочки, фаянс и строителни ремонти",
    use_container_width=True
)

st.markdown("---")

# Секция Услуги с галерия
st.header("🛠️ Основно Предлагани Услуги в Попово и Района")

col_u1, col_u2, col_u3 = st.columns(3)

with col_u1:
    st.subheader("🧱 Плочки & Бани")
    st.image(
        "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=600&auto=format&fit=crop",
        caption="Полагане на плочки, фаянс и теракота",
        use_container_width=True
    )
    st.write("Професионално полагане на фаянс, теракота, гранитогрес, хидроизолация и цялостен ремонт на бани.")

with col_u2:
    st.subheader("🎨 Шпакловка & Боя")
    st.image(
        "https://images.unsplash.com/photo-1562259949-e8e7689d7828?q=80&w=600&auto=format&fit=crop",
        caption="Шпакловане и боядисване",
        use_container_width=True
    )
    st.write("Фино и грубо шпакловане, шкурене, боядисване с латекс, отстраняване на влага и козметични ремонти.")

with col_u3:
    st.subheader("🔨 Гипсокартон & Довършителни")
    st.image(
        "https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=600&auto=format&fit=crop",
        caption="Монтаж на гипсокартон, окачени тавани и довършителни работи",
        use_container_width=True
    )
    st.write("Монтаж на гипсокартон, окачени тавани, замазки, обръщане на врати и прозорци.")

st.markdown("---")

# Секция Калкулатор
st.header("🧮 Калкулатор за ориентировъчна цена")
st.write("Изберете услуга и площ, за да получите приблизителна стойност за труд:")

col_c1, col_c2 = st.columns(2)

with col_c1:
    service = st.selectbox(
        "Изберете вид услуга:",
        [
            "Лепене на плочки (фаянс/теракота)",
            "Шпакловка + Боядисване",
            "Монтаж на гипсокартон",
            "Замазка / Подови настилки"
        ]
    )
    area = st.number_input("Площ в квадратни метри (кв.м):", min_value=1, value=20, step=1)

# Ориентировъчни базисни цени за труд за кв.м. в евро (€)
prices = {
    "Лепене на плочки (фаянс/теракота)": 20.00,
    "Шпакловка + Боядисване": 9.00,
    "Монтаж на гипсокартон": 13.00,
    "Замазка / Подови настилки": 8.00
}

unit_price = prices[service]
total_price = area * unit_price

with col_c2:
    st.info(f"**Избрана услуга:** {service}")
    st.metric(label="Ориентировъчна сума за труд:", value=f"{total_price:.2f} €")
    st.caption("* Забележка: Цената е примерна само за труд и зависи от състоянието на обекта. Крайна оферта се дава след оглед.")

st.markdown("---")

# Форма за контакт
st.header("📬 Изпратете запитване за оферта")
st.write("Попълнете формата по-долу и ще се свържем с вас възможно най-скоро:")

contact_form = """
<form action="https://formspree.io/f/xbldqwwp" method="POST">
    <input type="text" name="name" placeholder="Вашето име" required style="width: 100%; padding: 8px; margin-bottom: 10px;">
    <input type="email" name="email" placeholder="Вашият имейл или телефон" required style="width: 100%; padding: 8px; margin-bottom: 10px;">
    <textarea name="message" placeholder="Опишете накратко ремонта (напр. квадратни метри, вид услуга)" required style="width: 100%; padding: 8px; margin-bottom: 10px; height: 100px;"></textarea>
    <button type="submit" style="background-color: #ff4b4b; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Изпрати запитване</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
