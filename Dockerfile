FROM python

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY . .


EXPOSE 5000

CMD ["python", "front_end.py"]