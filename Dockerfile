FROM python:3.11-alpine
RUN mkdir /app
WORKDIR /app
COPY req.txt /app/
COPY modul_4_lesson_3.py /app/
RUN pip install -r req.txt
ENTRYPOINT ["python","modul_4_lesson_3.py"]
