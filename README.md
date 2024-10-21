# Steps to run this repository
  1. `git clone https://github.com/kisharnath/Flask-Mongodb-docker-app.git`
  2. Type in command line `cd Flask-Mongodb-docker-app`
  3. create .env file and put MONGO_URI=<Mongodb database url>
  4. Run this command `docker build -t python-app .`  Make sure docker is running  
  5. then run this ` docker run -p 5000:5000 python-app`
  6. in app/utility.py file change 
  `db = client['Yourdatabase']  # Your database name
  collection = db['yourdatabase']  # Your database collection`
