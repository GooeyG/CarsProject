FROM python:3.9
copy . .
#ARG SECRET_KEY
#ARG DATABASE_URI
ENV SECRET_KEY=my-secret
ENV DATABASE_URI=sqlite:///data.db
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]