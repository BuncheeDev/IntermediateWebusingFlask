from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    make_response,
    jsonify,
)
from mylib import myfunc


app = Flask(__name__)


@app.route("/")
def index():
    # หน้าแนะนำสถานที่ท่องเที่ยว
    attraction = {
        "name": "วัดพระแก้ว (Wat Phra Kaew)",
        "location": "กรุงเทพมหานคร, ประเทศไทย",
        "description": "วัดพระแก้วหรือวัดพระศรีรัตนศาสดาราม เป็นวัดที่มีความสำคัญทางประวัติศาสตร์และศิลปะวัฒนธรรมของไทย ตั้งอยู่ในพระบรมมหาราชวัง เป็นที่ประดิษฐานพระแก้วมรกต พระพุทธรูปคู่บ้านคู่เมืองของไทย",
        "highlights": [
            "พระแก้วมรกต - พระพุทธรูปศักดิ์สิทธิ์ที่สำคัญที่สุดของประเทศไทย",
            "สถาปัตยกรรมไทยที่งดงามประณีต",
            "จิตรกรรมฝาผนังเรื่องรามเกียรติ์",
            "พระมณฑปทองคำและพระปรางค์ต่างๆ",
        ],
        "tips": "ควรแต่งกายสุภาพ ปกปิดไหล่และเข่า เปิดทุกวัน 8:30-15:30 น.",
    }
    return render_template("index.html", attraction=attraction)


@app.route("/tech")
def tech():
    # หน้าแสดงข้อมูลเทคโนโลยีที่สนใจ
    tech_interests = {
        "title": "เทคโนโลยีที่สนใจ",
        "technologies": [
            {
                "name": "Python",
                "category": "Programming Language",
                "description": "ภาษาโปรแกรมที่ใช้งานง่าย เหมาะสำหรับ Web Development, Data Science, และ AI/Machine Learning",
                "why": "มีไลบรารีมากมาย เรียนรู้ง่าย และมีชุมชนขนาดใหญ่",
            },
            {
                "name": "Flask",
                "category": "Web Framework",
                "description": "Web framework ขนาดเล็กแต่ทรงพลังสำหรับ Python เหมาะสำหรับการสร้าง Web Application และ API",
                "why": "เรียนรู้ง่าย ยืดหยุ่น และเหมาะกับโปรเจกต์ทุกขนาด",
            },
            {
                "name": "Machine Learning",
                "category": "AI Technology",
                "description": "เทคโนโลยีที่ให้คอมพิวเตอร์เรียนรู้จากข้อมูลและปรับปรุงประสิทธิภาพโดยอัตโนมัติ",
                "why": "เป็นอนาคตของเทคโนโลยี มีการประยุกต์ใช้งานในหลายอุตสาหกรรม",
            },
            {
                "name": "Docker",
                "category": "DevOps Tool",
                "description": "แพลตฟอร์มสำหรับการพัฒนา deploy และรันแอปพลิเคชันใน Container",
                "why": "ทำให้การ deploy และจัดการแอปพลิเคชันง่ายและสม่ำเสมอ",
            },
        ],
    }
    return render_template("tech.html", tech_data=tech_interests)


@app.route("/myid")
def my_id():
    # แสดงรหัสนักศึกษา (ไม่ต้องเป็นหน้าเว็บ)
    return "68130712"


@app.route("/blog")
def blog():
    return render_template("blog_post.html")


@app.route("/user/<name>/<int:age>")
def user_profile(name, age):
    return "%s is %d years old" % (name, age)


@app.route("/set-cookie")
def set_cookie():
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("cookie_name", "cookie_value")
    return resp


@app.route("/login-success")
def login_success():
    session["user"] = "example_user"
    return redirect(url_for("index"))


# JSON API endpoint
@app.route("/api/data")
def return_json():
    num_list = [1, 2, 3, 4, 5]
    num_dict = {"numbers": num_list, "name": "Numbers"}
    return jsonify({"output": num_dict})


@app.route("/submit", methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        details = request.form
        first_name = details.get("fname")
        last_name = details.get("lname")

        return f"Success! Received: {first_name} {last_name}"
    return render_template("index.html")


@app.route("/draw/<int:num>")
def draw_stars(num):
    try:
        turns = num  # Number of iterations to draw
        results = []
        for i in range(1, turns + 1):
            result = myfunc(" (\_/)", i)
            result1 = myfunc("( •_•)", i)
            result2 = myfunc("/ > > ", i)

            # Still print to console for debugging
            print(result)
            print(result1)
            print(result2)

            # Collect results for display
            results.append({"line1": result, "line2": result1, "line3": result2})

        return render_template("draw.html", num=num, results=results)
    except Exception as e:
        return str(e), 400


# 2. เพิ่ม path /sum/xx/yy แล้วแสดงหน้าเว็บเป็น "The result of sum between xx and yy is zz" เมื่อ zz = xx+yy เช่น xx=12 และ yy=3 ดังนั้น zz=15
@app.route("/sum/<xx>/<yy>")
def sum_xy(xx, yy):
    try:
        x = int(xx)
        y = int(yy)
        z = x + y

        return render_template("2025-10-19_Sum.html", z=z, x=x, y=y)
    except ValueError:
        return "You are using miss data type for operation"


# 3. เพิ่ม path /concat/xx/yy แล้วแสดงหน้าเว็บเป็น "The result of cancatenate between xx and yy is xxyy" เช่น xx=12 และ yy=3 ดังนั้น xxyy=123
@app.route("/concat/<xx>/<yy>")
def concat_xy(xx, yy):
    try:
        x = int(xx)
        y = int(yy)
        xy = str(x) + str(y)
        return render_template("2025-10-19_Concat.html", xy=xy, x=x, y=y)
    except ValueError:
        return "You are using miss data type for operation"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
