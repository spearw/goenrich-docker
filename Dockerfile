# Pin base image
# See: https://hub.docker.com/r/continuumio/miniconda3
FROM continuumio/miniconda3@sha256:166ff37fba6c25fcad8516aa5481a2a8dfde11370f81b245c1e2e8002e68bcce
LABEL description="Base docker image with conda and util libraries"

# Install procps (so that Nextflow can poll CPU usage)
RUN apt-get update && \
    apt-get install -y procps && \
    apt-get clean -y

# Work in root
WORKDIR /root

# Install the conda environment
ARG ENV_NAME=goenrich
COPY environment.yaml /
RUN conda env create --quiet --name ${ENV_NAME} --file /environment.yaml -y && \
  conda clean -a

# Copy in tests
COPY tests /root

# Add conda installation and root dirs to PATH (instead of doing
# 'conda activate' or specifiying path to tool)
ENV PATH="/opt/conda/envs/$ENV_NAME/bin:$PATH"
