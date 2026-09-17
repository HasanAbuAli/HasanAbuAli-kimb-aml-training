"""Main KIMB AML/CFT quiz: AI deepfake question first, followed by original 13."""
from pathlib import Path

original = Path(__file__).with_name("quiz_original_13.py").read_text(encoding="utf-8")
needle = "questions = ["
if original.count(needle) != 1:
    raise RuntimeError("Original question-bank structure has changed; review before injecting questions.")

new_question = '''
    {
        "category": "الاحتيال بالذكاء الاصطناعي – التزييف العميق (Deepfake)",
        "question": "تلقى موظف في البنك مكالمة فيديو تبدو وكأنها من أحد كبار المسؤولين؛ كان الوجه والصوت مقنعين، وطُلِب منه تنفيذ تحويل عاجل إلى حساب جديد مع تجاوز إجراءات الاعتماد المعتادة بحجة السرية. ما التصرف الأنسب؟",
        "options": [
            "تنفيذ التحويل فورًا لأن الوجه والصوت يطابقان المسؤول الظاهر في الفيديو.",
            "طلب رسالة من حساب المراسلة نفسه، ثم تنفيذ التحويل دون تطبيق ضوابط الاعتماد.",
            "عدم تنفيذ التحويل أو تجاوز الضوابط؛ والتحقق المستقل عبر رقم أو قناة رسمية معروفة مسبقًا، واتباع إجراءات الاعتماد والتصعيد إلى الجهات المختصة وفق سياسة البنك.",
            "تنفيذ جزء صغير من التحويل أولًا لاختبار مصداقية الطلب."
        ],
        "answer": "عدم تنفيذ التحويل أو تجاوز الضوابط؛ والتحقق المستقل عبر رقم أو قناة رسمية معروفة مسبقًا، واتباع إجراءات الاعتماد والتصعيد إلى الجهات المختصة وفق سياسة البنك.",
        "explanation": "قد يقلّد التزييف العميق الوجه والصوت بدقة. الاستعجال والسرية والحساب الجديد وطلب تجاوز الموافقات مؤشرات احتيال. لا تنفذ العملية قبل التحقق المستقل عبر قناة موثوقة ومعروفة مسبقًا، والالتزام بالصلاحيات والموافقات، وتوثيق الواقعة وتصعيدها وفق إجراءات البنك."
    },
'''

# Preserve the original page appearance, answer controls, feedback, and scoring.
updated = original.replace(needle, needle + new_question, 1)
exec(compile(updated, str(Path(__file__).with_name("quiz_original_13.py")), "exec"))
