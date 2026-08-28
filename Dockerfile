
FROM python:3.11-slim
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
RUN poetry install --no-root 
CMD [ "poetry", "run", "python", "manage.py", "runserver", ]