FROM python:alpine

RUN apk --no-cache add git

RUN git clone https://github.com/dylantheriot/valorant-match-history.git

WORKDIR /valorant-match-history

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

RUN sed -i 's/host="127.0.0.1", port=5000, debug=True/host="0.0.0.0", port=5000, debug=False/g' wsgi.py

CMD [ "wsgi.py" ]
