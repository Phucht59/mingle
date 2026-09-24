FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.lock /app/requirements.lock
RUN pip install --no-cache-dir -r requirements.lock
COPY . /app
RUN pip install --no-cache-dir --no-deps . && useradd --uid 10001 --create-home app && mkdir -p /data/objects && chown -R app:app /data
USER app
CMD ["uvicorn", "all_foundation.api:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
