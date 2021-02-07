# j-app

start up flask app using port 80.

```bash
# build the image
docker build -t j-app .

# run the image
docker run -p 80:80 --name j-app -d j-app

# push to docker hub
docker tag j-app nathanesau/try_j:j-app
docker push nathanesau/try_j:j-app
```

heroku container instructions:

```bash
# curl https://cli-assets.heroku.com/install.sh | sh
heroku login
heroku container:login
heroku container:push web
heroku container:push web -a try-jlang
heroku container:release web -a try-jlang

heroku logs --tail -a try-jlang
```
