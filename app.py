from flask import Flask, render_template, send_file, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

	if request.method == "POST" :  #post request
		# with open("resume.pdf", "rb") as f:
		return send_file("./resume.pdf", attachment_filename="resume.pdf", as_attachment=True)

	else: #get request
		return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
	