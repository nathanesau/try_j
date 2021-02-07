# CONTRIBUTING

Features that would be nice to have:

* Syntax highlighting for CodeMirror for J language.
* Collecting analytics for site
* HTTPS using letsencrypt
* Use NGINX and proxy pass to port 80 (flask)
* GitHub actions for re-build docker image and re-deploy to heroku

## Additional Information

Scripts are run using Python ``subprocess`` module.

<!--
create local symlink:

```bash
sudo ln -s /home/esna0001/jsource/build/jsrc/Release/jconsole /usr/bin/jconsole
```

sample script:

```python
from subprocess import Popen, PIPE
p = Popen("jconsole", stdin=PIPE)
p.communicate("1+2*i.10\n".encode())
```

run sample script:

```bash
python script > script_out.txt
```
-->