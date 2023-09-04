FROM bitnami/spark:3.1.2

USER root

ARG shared_workspace=/opt/workspace

RUN mkdir -p ${shared_workspace}
