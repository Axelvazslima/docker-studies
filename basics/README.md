# BASICS 🐳


Docker is a platform that allows developers to package, distribute and run applications in different environments called [containers](#container). It is a <mark>fundamental concept about docker</mark> alongside [images](#image). We'll dive into it later.
## Checking docker version

Check the version of your client; CLI. And the server.

It returns their configurations and informations.

The values ideally are the same, but it *isn't* a must.

To get a basic overview, run: `docker version`

Proper when you jast wanto to check if the cli can talk to engine.

For a more detailed one, run: `docker info`

Ideal when you want to know more config values of the engine.

## Docker commands

There are tons of docker commands and instead of using chatgpt or having to google everytime what to do, simply run: `docker`

## Manager commands

You can also see them in the `docker` prompt. It's a way of organizing commands.

The still functional old way: `docker <command> (options)`

It still works.

But the new way is: `docker <command> <sub-command> (options)`

EXAMPLE:

> `docker run` **vs** `docker container run`

## Dockerfile

> Used to create your own [images](#image).

A text based file with no extension. It contains a sequence of instructions - really a sequence, it executes them in order.

It has its own language, but its really simple. *Pretty much english*.

### Dockerfile base commands

`FROM <base image>` It can be an OS, like ubuntu.

```ENV APP_NAME="docker-studies" \ APP_ENV="production"``` Set environment variables.

`WORKDIR <working directory inside the container>`

`COPY ..` Copy application files from the host to the container.

`RUN apt-get update && apt-get install -y curl` Install necessary dependencies.

`EXPOSE <PORT>` Exposes a port, it is useful for web applications.

`ARG BUILD_VERSION=1.0.0` Defines an argument that can be passed during build.

`ENV VERSION=$BUILD_VERSION` Uses the argument to create an environment variable.

`CMD ["echo", "Hello, Docker!"]` Defines the default command that runs when the container starts.

### Building a Dockerfile

Just run: `docker build -t <name> --build-arg <build argument>` "-t" tags the image as "\<name\>" and "build-arg" passes a "\<build argument\>".

### Run the container

Run `docker run --rm \<name\>` "--rm" automatically removes the container after it stops.

You will understand more about [these commands](#docker-container-run) later.

## Image

> Read-only template that contains everything needed to run an application. Static blueprint.

The binaries, libraries and dependencies, source code, operational system, application code, environment variables, configuration files(...) that makes your application.

[Nginx](#nginx), for example

### Images key characteristics

🧍‍♂️ Immutable;

☁️ Stored in Docker registries, like [Docker Hub](https://hub.docker.com) - or locally;

🛠️ Used to create docker [containers](#container).

## Container

*Isolated, lightweight and portable execution environment* that includes the application and all its dependencies.

> An instance of that image running as a process. You can have multiples container running off the same image.

### Containers key characteristics

🏃‍♂️‍➡️ Runs as a process on the host machine;

🌬️ Ephemeral, by default: can be removed or restarted - also, paused;

🏠 Uses an image as its foundation.

## Usual misconception

[Images](#image) and [containers](#container) definitions often confuses people. They tend to think they are pretty much the same thing, but that's not true.

So, it is important for you to really understand each one of them.

[Know more about it.](https://circleci.com/blog/docker-image-vs-container/)

## The pull command

> Download image from docker registries.

If you try to run a container from an image that doesn't exist locally (first place it looks for), it will automatically install it from the docker registries.

But, if you want to manually install it, run: `docker pull <image>`

## Nginx

Basic web service for docker containers.

To run it just prompt: `docker container run --publish 80:80 nginx`

Downloaded image nginx  from Docker Hub
Started a new container form that image
Opened port 80 on the Host IP
Routes the traffic to the container IP -> port 80

⚠️ You may need to change the port -> Something else is already running on that port.

`docker container run --publish 80:80 --detach nginx`

This way, the container runs in the background.

## Seeing the containers running

Each container has its unique ID, you may want to know if you want to stop them, for example.

To know this IDs, simply run: `docker container ls`

It will show all the containers running.

Or, run: `docker container ls -a`

It shows all the containers, even the ones that aren't running.

It is going to be useful when you are managing them: renaming, deleting and etc.

To know all the commands in the *docker container* command, run: `docker container`

## Deleting  container

If you run the `docker ls -a` you will notce that the ID is huge, but you actually only need the first three chars to delete it.

The deletion should be made in a non-running container. If you try to delete an active one, it will give an error. Unless you force, `-f`, it.

Stopping a container: `docker stop <name>`

Deleting a container
`docker container rm -f <id0 id1 id2 id...>`

The '-f' indicates the forced operation and the 'id...' means that you can delete more than one container at once, simply pass them IDs side to side.

## Docker container run

It is a command that first looks for that image locally in image cache. If it isn't there, it looks for it in remote images repositories (Docker Hub, by default).

Now, it downloads its latest version available and creates a new container based on that image and prepares to start.

Gives it a virtual IP on a private network inside docker engine and opens up port 80 on host and forward to port 80 in container.

Starts container by using the CMD in the image Dockerfile.

### Changing the defaults

The port, version and CMD run you seen above👆 are defaults, but all that can be changed when running the command.

`docker container run --publish *8080:80* --name webhost -d *nginx* -T`

Respectively, host listening port, image version and CMD run.

## A small dive into detach

When you run a container in the terminal, you will notice that the terminal is now just the process running and the informations bout it being logged there.

If this behaviour is not wanted, simply detach, `-d` or `--detach`, the command and now it only runs in the background. If want to see something about it, just run the desired commands.

## --name

Naming a container is good for practicability, because you can now run commands for it using it and not its ID, making things faster for you.

`--name 'name'`

For example, the [nginx process](#changing-the-defaults) we ran before is now named 'webserver'

## Container VS Virtual Machines (VM)

There are a lot of confusion and misconceptions about these two. There are similarities, but they are *not the same*.

Containers are simply processes running in a machine, not a machine itself.

## What goes on in containers

Run `docker container top <name/id>` to process list in one container.

Run `docker container inspect <name/id>` to know details about one container config.

Run `docker container stats <name/id>*` to know perfomance stats for all running containers. If you specify a container identification it will be exclusive for that container.

## Getting a shell inside container

No need for SSH.

Run `docker container run -it <name/id>` to start a new container interactively.

Run `docker container exec -it` to run additional command in existing container.

`-it`starts a ==terminal inside== the container.

`docker container run` command accepts commands. These commands replace the default commands of your run.

> E.g. the nginx default command is "nginx -g 'daemon ...'", but if run it with a *bash* command it will be replaced by *bash*. You can see it in the docker `container ls -a`.

## Linux distros

There are lots of linux distros you can download, like *ubuntu* or *[alpine](#alpine-linux)*.

The distros commands might change (e.g. alpine *doesn't have a bash*, but it does have a shell, *the sh* - works similarly.)

### Alpine Linux

*Ideal for images creation*, because it's lightweight and secure.

It lacks some features, but that's the reason it's light.

Running it with it's shell, remember it doesnt have a 'bash' command: `docker container run -it alpine sh`.

[Know more about alpine.](https://www.alpinelinux.org/)
