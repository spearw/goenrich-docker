[![Build a Docker image](https://github.com/spearw/goenrich-docker/actions/workflows/docker-image.yml/badge.svg)](https://github.com/spearw/goenrich-docker/actions/workflows/docker-image.yml)[![Build and push a Docker image](https://github.com/spearw/goenrich-docker/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/spearw/goenrich-docker/actions/workflows/docker-publish.yml)

# goenrich-docker

[GOEnrich](https://pypi.org/project/goenrichment/) This package execute GO enrichment analysis from a list of gene names using a precomputed database. The GO terms are analyze using a hypergeometric test. goenrich-docker provides Docker files and GitHub Action workflows for building and publishing a Docker image so that GOEnrich can be used in Nextflow workflows.

### Build

To build your image from the command line:
* You can do this on [Google shell](https://shell.cloud.google.com) since docker is installed and available.

```bash
docker build --platform linux/amd64 -t spearw/goenrich:latest .
```

### Test

To test this tool from the command line:

```bash
docker run -it spearw/goenrich:latest goenrich -h
```

Disclaimer
THIS WEBSITE AND CONTENT AND ALL SITE-RELATED SERVICES, INCLUDING ANY DATA, ARE PROVIDED "AS IS," WITH ALL FAULTS, WITH NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTIES OF MERCHANTABILITY, SATISFACTORY QUALITY, NON-INFRINGEMENT OR FITNESS FOR A PARTICULAR PURPOSE. YOU ASSUME TOTAL RESPONSIBILITY AND RISK FOR YOUR USE OF THIS SITE, ALL SITE-RELATED SERVICES, AND ANY THIRD PARTY WEBSITES OR APPLICATIONS. NO ORAL OR WRITTEN INFORMATION OR ADVICE SHALL CREATE A WARRANTY OF ANY KIND. ANY REFERENCES TO SPECIFIC PRODUCTS OR SERVICES ON THE WEBSITES DO NOT CONSTITUTE OR IMPLY A RECOMMENDATION OR ENDORSEMENT BY SCIENCE and TECHNOLOGY CONSULTING LLC.
