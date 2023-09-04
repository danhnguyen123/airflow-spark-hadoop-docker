# FROM jupyter/pyspark-notebook:spark-3.1.2
# # spark-3.1.2 must match with spark service version
# USER root
# ARG shared_workspace=/opt/workspace

# RUN mkdir -p ${shared_workspace}

# RUN mkdir -p ${shared_workspace}
#     # apt-get update -y && \
#     # apt-get install -y python3 && \
#     # apt-get install -y python3-pip && \
#     # pip3 install wget pyspark==${spark_version} jupyterlab==${jupyterlab_version}

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # -- Runtime

# WORKDIR ${shared_workspace}
# CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=danhnguyen123 --NotebookApp.password=danhnguyen56