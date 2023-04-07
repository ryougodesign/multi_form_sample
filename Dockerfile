FROM python:3.10.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /multi_form_sample
WORKDIR /multi_form_sample
ADD requirements.txt /multi_form_sample/
RUN pip install --upgrade pip && pip install -r requirements.txt