from flask import Flask, request, render_template,jsonify   #Import necessary packages
app = Flask(__name__)

def string_cutter(string_to_cut):     #define functions and include parameters needed
    """Input can only be one argument which is 'string_to_cut', the function then creates
        a new string with every third letter from the input string. It then joins the
        letters into one string and returns it in JSON format."""

    return_string = "".join([string_to_cut[i] for i in range(len(string_to_cut)) if i % 3 == 2])

    return return_string

@app.route('/')   #include html template
def home():
    return render_template('home.html')
@app.route('/test', methods=['GET','POST'])
def my_form_post():
    string_to_cut = request.form['string_to_cut']
    word = request.args.get('string_to_cut')
    return_string = string_cutter(string_to_cut)
    result = {
        "output": return_string
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True)










