
FROM python:3.13-slim

WORKDIR /app

COPY app.py test_app.py ./

RUN useradd --create-home appuser

USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
