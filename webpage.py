from flask import Flask, render_template, url_for, request
from postcodeform import PCform
from CrimeData import GetData


app = Flask(__name__)
app.config['SECRET_KEY'] = '03383ba7b06539d803bd0c05ebbc4f15'

posts = [
	{
	'author': 'me',
			'title': 'blog'

		

	},
		{
		'author': 'too',
			'title': 'blog2'
		}


		]

pageheading = [
	{
	'heading': 'Home',
	},
	{
	'heading': 'howsafe'
	}
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, pageheading=pageheading)


@app.route("/howsafe", methods=["POST","GET"])
def address(postcode):
	
	
	if request.method == "POST":
		postcode = request.form.get('postcode')

		
	
	
	
	
	form = PCform()
    
	return postcode, render_template('howsafe.html', title='HowSafe', form=form,postcode=postcode, pageheading=pageheading,Safety_rating=Safety_rating)


@app.route("/twitterbot")
def twitterbot():

    return render_template('twitterbot.html', title='TwitterBot',pageheading=pageheading)


@app.route("/youtubebot")
def youtubebot():

    return render_template('youtubebot.html', title='YoutubeBot',pageheading=pageheading)


@app.route("/signup")
def signup():

    return render_template('signup.html', title='SignUp',pageheading=pageheading)

@app.route("/about")
def about():

    return render_template('about.html', title='About',pageheading=pageheading)



