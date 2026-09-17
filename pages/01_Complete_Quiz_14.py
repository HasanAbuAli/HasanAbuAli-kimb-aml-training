"""KIMB complete training quiz: deepfake question followed by the original question bank."""
import ast
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="KIMB | 14-Question Compliance Quiz", page_icon="🏦")
st.markdown("""<style>.stApp{direction:rtl;text-align:right} h1,h2,h3,p,label{text-align:right!important}div[role='radiogroup']{direction:rtl}</style>""", unsafe_allow_html=True)

# Read the existing question bank without executing the original Streamlit page.
source = (Path(__file__).resolve().parents[1] / "streamlit_app.py").read_text(encoding="utf-8")
module = ast.parse(source)
original_questions = next(ast.literal_eval(node.value) for node in module.body
    if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "questions" for target in node.targets))

deepfake = {
    "category": "الاحتيال باستخدام الذكاء الاصطناعي – التزييف العميق (Deepfake)",
    "question": "تلقى موظف في البنك مكالمة فيديو تبدو وكأنها من أحد كبار المسؤولين؛ كان الوجه والصوت مقنعين، وطُلب منه تنفيذ تحويل عاجل إلى حساب جديد مع تجاوز إجراءات الاعتماد المعتادة بحجة السرية. ما التصرف الأنسب؟",
    "options": [
        "تنفيذ التحويل فورًا لأن الوجه والصوت يطابقان المسؤول الظاهر في الفيديو.",
        "طلب رسالة من حساب المراسلة نفسه، ثم تنفيذ التحويل دون تطبيق ضوابط الاعتماد.",
        "عدم تنفيذ التحويل أو تجاوز الضوابط؛ والتحقق المستقل عبر رقم أو قناة رسمية معروفة مسبقًا، واتباع إجراءات الاعتماد والتصعيد وفق سياسة البنك.",
        "تنفيذ جزء صغير من التحويل أولًا لاختبار مصداقية الطلب."
    ],
    "answer": "عدم تنفيذ التحويل أو تجاوز الضوابط؛ والتحقق المستقل عبر رقم أو قناة رسمية معروفة مسبقًا، واتباع إجراءات الاعتماد والتصعيد وفق سياسة البنك.",
    "explanation": "يمكن للتزييف العميق تقليد الوجه والصوت، فلا تكفي مكالمة الفيديو للتحقق من الهوية أو التفويض المالي. الاستعجال والسرية والحساب الجديد وطلب تجاوز ضوابط الاعتماد مؤشرات خطر. أوقف التنفيذ لحين التحقق المستقل من قناة معروفة مسبقًا، وطبّق الموافقات المعتمدة، ووثّق الواقعة وصعّدها إلى الجهات المختصة وفق إجراءات البنك."
}
questions = [deepfake, *original_questions]

st.title("🏦 اختبار التوعية بالامتثال ومكافحة الجرائم المالية")
st.caption("KIMB | Deepfake, AML/CFT & Sanctions | بنك الاختبارات الكامل")
st.info("حالات افتراضية للتدريب؛ تطبّق السياسات والصلاحيات والإجراءات المعتمدة في الحالات الفعلية.")

if "kimb14_position" not in st.session_state:
    st.session_state.kimb14_position = 0
    st.session_state.kimb14_score = 0
    st.session_state.kimb14_answered = False
    st.session_state.kimb14_selected = None

position = st.session_state.kimb14_position
total = len(questions)
question = questions[position]
st.progress(position / total)
st.subheader(f"السؤال {position + 1} من {total}")
st.caption("الموضوع: " + question["category"])
st.write(question["question"])
choice = st.radio("اختر إجابة واحدة:", question["options"], index=None, key=f"kimb14_choice_{position}", disabled=st.session_state.kimb14_answered)

if not st.session_state.kimb14_answered and st.button("إرسال الإجابة ✅"):
    if choice is None:
        st.warning("يرجى اختيار إجابة أولًا.")
    else:
        st.session_state.kimb14_selected = choice
        st.session_state.kimb14_answered = True
        if choice == question["answer"]:
            st.session_state.kimb14_score += 1
        st.rerun()

if st.session_state.kimb14_answered:
    if st.session_state.kimb14_selected == question["answer"]:
        st.success("✅ إجابة صحيحة!")
    else:
        st.error("❌ إجابة غير صحيحة.")
        st.write("**الإجابة الصحيحة:** " + question["answer"])
    st.info("💡 " + question["explanation"])
    st.write(f"**نتيجتك الحالية: {st.session_state.kimb14_score} / {position + 1}**")
    if position < total - 1:
        if st.button("السؤال التالي ←"):
            st.session_state.kimb14_position += 1
            st.session_state.kimb14_answered = False
            st.session_state.kimb14_selected = None
            st.rerun()
    else:
        st.success(f"اكتمل الاختبار! النتيجة النهائية: {st.session_state.kimb14_score} / {total}")
        if st.button("إعادة الاختبار 🔄"):
            st.session_state.kimb14_position = 0
            st.session_state.kimb14_score = 0
            st.session_state.kimb14_answered = False
            st.session_state.kimb14_selected = None
            for index in range(total):
                st.session_state.pop(f"kimb14_choice_{index}", None)
            st.rerun()
