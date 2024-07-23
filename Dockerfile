FROM python:3.12.4-alpine3.20
LABEL maintainer="Mohab Gabber"
############################
ENV PYTHONUNBUFFERED=1
############################
RUN mkdir -p /app/fphlcore/
WORKDIR /app/fphlcore
COPY requirements.txt ./
RUN pip install -r requirements.txt
############################
COPY . .
RUN adduser --disabled-password runner
RUN chown -R runner:runner /app/fphlcore
USER runner
############################
RUN python manage.py makemigrations landing
RUN python manage.py migrate --no-input
RUN python manage.py collectstatic --no-input
############################
EXPOSE 8000
############################
CMD ["gunicorn", "-c", "deploy/prod.py"]