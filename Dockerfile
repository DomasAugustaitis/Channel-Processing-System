FROM python

LABEL Maintainer="augustaitis.domas@gmail.com"

COPY * ./
RUN pip install numpy
CMD [ "python", "main.py" ]

