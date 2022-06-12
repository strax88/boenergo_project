FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR boenergo_project/
COPY requirements.txt /boenergo_project/
RUN pip install -r requirements.txt
RUN ls
copy . /boenergo_project/
RUN python manage.py migrate

