from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/quis/bmi', methods=['POST'])
def bmi():
    tinggi = float(request.form.get('tinggi'))
    berat = float(request.form.get('berat'))
    bmi = berat / (tinggi/100)**2
    msg = "BMI anda " + str(bmi)
    if bmi < 18.5 :
        ket = " kurus "
    elif bmi <= 25 :
        ket = " normal"
    elif bmi <= 40 :
        ket = "berlebih"
    else :
        ket = "berbahaya"
    data = {'msg': msg, 'ket':ket}
    return jsonify(data)



if __name__ == "__main__":
    app.run(port=3000, debug=True) 
   



