FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    ORTHOINFO_ROOT=/app \
    ORTHOINFO_DATASET_VERSION=v2026-10-26

WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir ".[prod]"

# Only what the running app needs: config, the processed dataset, the website, server settings.
# (data/raw is for rebuilding the dataset and is not shipped; see .dockerignore.)
COPY config ./config
COPY data/processed/v2026-10-26 ./data/processed/v2026-10-26
COPY index.html gunicorn.conf.py ./

RUN useradd --system --no-create-home app && chown -R app /app/data
USER app

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request,os;urllib.request.urlopen('http://127.0.0.1:%s/api/health'%os.environ.get('PORT','8000'))"
CMD ["gunicorn", "-c", "gunicorn.conf.py", "orthoinfo.wsgi:app"]
