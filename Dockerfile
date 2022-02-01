FROM python:3.8-slim-buster
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "project/__main__.py"]