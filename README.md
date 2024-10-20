# Steps to run this repository
  1. `git clone https://github.com/kisharnath/Flask-Mongodb-docker-app.git`
  2. create .env file and put MONGO_URI=mongodb+srv://<username>:<password>@cluster0.la507.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
  3. Type in command line `cd Flask-Mongodb-docker-app`
  4. Run this command `docker build -t python-app .` { Make sure docker is running or not }
  5. then run this ` docker run -p 5000:5000 python-app`
