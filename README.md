# Introduction
# Install Docker
- <b> Run command: </b>
    - <em style="color:red">docker-compose up </em>
# Install Python
- <b> Require: Python 3.10+ </b>
- <b> Install Virtual Environment module: </b>
    - <em style="color:red">pip install virtualenv</em>
- <b> Create Virtual Environment: </b>
    - <em style="color:red">python -m venv name_of_your_env </em>
- <b> Activate Virtual Environment: </b>
    - <em style="color:red">Windows: \root_directory\venv_directory\bin\activate </em>
    - <em style="color:red">MacOS: source /root_directory/venv_directory/bin/activate </em>
- <b> Install Dependencies: </b>
    - <em style="color:red">pip install -r requirements.txt </em>
# Start application
- <b> Run command to start FastAPI App: </b>
    - <em style="color:red">uvicorn app:app --port 8001 --reload </em>
- <b> Run command to start Celery Worker: </b>
    - <em style="color:red">celery -A app.celery worker --loglevel=info</em>
- <b> Run command to start Celery Monitor: </b>
    - <em style="color:red">celery -A app.celery flower --port=5555</em>
