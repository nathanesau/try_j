# j-app

start up flask app using port 80.

```bash
# build the image
docker build -t j-app .

# run the image
docker run -p 80:80 --name j-app -d j-app

# push to github container registry
# run using git bash
docker tag j-app docker.pkg.github.com/nathanesau/try_j/j-app:1.0
docker push docker.pkg.github.com/nathanesau/try_j/j-app:1.0
```
