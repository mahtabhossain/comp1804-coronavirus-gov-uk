FROM python:3
COPY ./model_inference.py /usr/src/app/
COPY ./requirements.txt /usr/src/app/
COPY ./model.pkl /usr/src/app/
WORKDIR /usr/src/app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "model_inference.py"]
