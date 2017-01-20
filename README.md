Copyright 2016

The guy who gave me this project did not pay me for the work. So I am making this project opensource so that anyone can make use of this.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# CloudITAM Web Project


# Development
Make sure
```python
DEVELOPMENT = True
``` 
in app/settings.py

## Installation
```bash
pip install -r requirements.txt
```
## Running application
```bash
python manage.py migrate
python manage.py runsever
```

# Production
After fetch data from github you have to restart uwsgi
```bash
sudo service uwsgi restart
```
Also if you change css/js files restart to nginx server
```bash
sudo service nginx restart
```
