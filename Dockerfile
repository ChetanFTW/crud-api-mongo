FROM python:3.11-slim
# main application path
WORKDIR /app
# all libaries in requirement
COPY requirements.txt requirements.txt
# instalation of req file
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# setup a run env for flask
ENV FLASK_APP=run.py
# terminal exicution
CMD ["flask", "run", "--host=0.0.0.0"]
