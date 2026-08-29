import streamlit as st

st.set_page_config(page_title="Майстор Ремонт - Строителни Услуги", page_icon="🏗️", layout="wide")

st.title("🏗️ Майстор Ремонт - Строителни Услуги")
st.write("Качествени строително-ремонтни дейности за вашия дом и офис.")

st.markdown("---")

st.header("📋 Запитване за оферта")
st.write("Попълнете формата по-долу и ние ще се свържем с вас възможно най-скоро!")

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
