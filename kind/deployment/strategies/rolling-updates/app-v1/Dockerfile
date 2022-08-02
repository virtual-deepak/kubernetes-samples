FROM python:alpine
LABEL author="Deepak Agarwal"
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]