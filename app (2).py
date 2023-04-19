from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home_page():
    return render_template('index.html')

@app.route("/math",methods=["POST","GET"])
def calculator():
    if (request.method=="POST"):
        ops = request.form["measures"]
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        if ops=="standard":
            bmi = (weight/ (height** 2)) * 703
            if bmi < 18.5:
              result = "YOU ARE UNDERWEIGHT."
            elif bmi < 25:
              result = "YOU ARE NORMAL. "
            elif bmi < 30:
              result = "YOU ARE OVERWEIGHT. "
            else:
              result = "YOU ARE OBESE. "
            result += "  YOUR BMI IS {:f}".format(bmi)
            return render_template("results.html", result=result)

        elif ops=="metric":
            bmi = weight / (((height * 30.48) / 100) ** 2)
            if bmi < 18.5:
              result = "YOU ARE UNDERWEIGHT."
            elif bmi < 25:
              result = "YOU ARE NORMAL."
            elif bmi < 30:
              result = "YOU ARE OVERWEIGHT. "
            else:
              result = "YOU ARE OBESE."  
            result += "  YOUR BMI IS {:f}".format(bmi)
            return render_template("results.html", result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)
