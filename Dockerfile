FROM python

COPY . /app

RUN pip install pygame

WORKDIR /app

CMD [ "python", "main" ]