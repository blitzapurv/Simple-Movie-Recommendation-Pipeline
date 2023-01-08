# Set as you wish
DOCKER_ACCOUNT := apurva543
CONTAINER_NAME := movie_recommendation
CONTAINER_VERSION := recommendation.0
CONTAINER_TAG := $(DOCKER_ACCOUNT)/$(CONTAINER_NAME):$(CONTAINER_VERSION)
DOCKER_FILE := Dockerfile_recommendation
PATH := recommendation/recommendation.json

# Build Tag Push a new image to Docker Hub
docker-image:
	@docker build -t $(CONTAINER_TAG) -f $(DOCKER_FILE) .

enter-image:
	@docker run -it $(CONTAINER_TAG) bash

docker-push:
	@docker image push $(CONTAINER_TAG)


# Create pipelines
create-pipeline:
	@pachctl create pipeline -f $(PATH)

