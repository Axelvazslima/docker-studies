# Images

## What is an Image?

Image is the app binary and its dependencies

> "An image is an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime."

It is not a complete Os, nor a Kernel.

Small as one file (your app binary).

Or, big as a Ubuntu distro with apt and other dependencies installed.

## Versions

Images often have versions, specially the official ones (by docker itself).

These versions can be specific or tagged as 'latest'.

### Latest

Latest seem pretty good. You are always up-to-date, but that's not always the case.

By using it, you may encounter compability issues by updating it frequently and maybe lose control of the program.

> Breaking changes, upredictable updates, difficulty in debugging... It all may come in the 'latest' packages and all its simplicities.

### Docker Hub

Docker official website that lists public images for you to use. These images may be created by Docker itself (official) or by other users (its name comes before the image name in the hub, like 'user-name/image-name').

The list shows how many pulls and stars that image have and its description.

## Image Layers and Cache

```sh
docker history [image]:[version]
```

Every images starts with a blank layer called scratch and every set of changes thats happens after that is a new layer created.

```sh
docker image inspect

old way: docker inspect
```

This command returns a JSON metadata about the image

## Image tagging and Pushing to Docker Hub

Tags are labels that point to images IDs.

```sh
docker image tag [source-image[:tag]] target_image[:tag]
```

This command creates a tag TARGET_IMAGE that refers to SOURCE_IMAGE

### Docker Hub

To publish to Docker Hub, you must login first

```sh
docker login
```

docker logout removes your auth code to the machine you logged in.

```sh
docker logout
```

To publish to Docker Hub, run (while logged in)

```sh
docker image push [image-name]
```

The latest tag is the default tag.

## DOCKERFILE basics

Looks like a bash script, but it is not.

The top of the file must contain a FROM command

```sh
FROM [distro-image]
```

You should pay attention to package managers.

Environment variables are key-value pairs that define containers configurations.

```sh
ENV [environment-variables]
```

To expose ports, you must explicitly do it. No ports are exposed by default.

```sh
EXPOSE [ports...]
```

## Running Docker Builds

```sh
docker image build -t [name] [directory-path]
```


