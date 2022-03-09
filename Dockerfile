FROM python:3.9
copy . .
ARG SECRET_KEY
ARG DATABASE_URI
ARG APP_RUN
ENV SECRET_KEY=my-secret
ENV DATABASE_URI=sqlite:///data.db
ENV APP_RUN=True
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]