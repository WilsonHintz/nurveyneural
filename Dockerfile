FROM heroku/miniconda

# Grab requirements.txt.
ADD ./restLayer/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD ./restLayer /opt/restLayer/
WORKDIR /opt/restLayer

RUN conda install scikit-learn

CMD gunicorn --threads 20 --bind 0.0.0.0:$PORT --timeout 120 wsgi
