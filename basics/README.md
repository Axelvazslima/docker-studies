# BASICS 🐳

## Checking docker version
Check the version of your client; CLI. And the server.<br>
It returns theis configurations and informations. The values ideally are the same, but it *isn't* a must.<br>

To get a basic overview, run:
> docker version

Proper when you jast wanto to check if the cli can talk to engine.

For a more detailed one, run:
> docker info

Ideal when you want to know more config values of the engine.

## Docker commands
There are tons of docker commands and instead of using chatgpt or having to google everytime what to do, simply run:
> docker

## Manager commands
You can also see them in the `docker` prompt. It's a way of organizing commands.<br>
The old way:
> docker <command> (options)

It still works.<br>
But the new way is:
> docker <command> <sub-command> (options)

EXAMPLE:<br>
> docker run **vs** docker container run

## Image
The binaries, libraries and source code that makes your application.
> Nginx, for example.

## Container
An instance of that image running as a process
> You can have multiples container running off the same image.

## Nginx
Basic web service for docker containers.<br>
> docker container run --publish 80:80 nginx

Downloaded image 'nginx  from Docker Hub
Started a new container form that image
Opened port 80 on the Host IP
Routes the traffic to the container IP -> port 80

⚠️ You may need to change the port -> Something else is already running on that port.

> docker container run --publish 80:80 --detach nginx

This way, the container runs in the background.

## Seeing the containers running
Each container has its unique ID, you may want to know if you want to stop them, for example.<br>
To know this IDs, simply run:<br>
> docker container ls

It will show all the containers running.<br>
Or, run:
> docker container ls -a

It shows all the containers, even the ones that aren't running.

It is going to be useful when you are managing them: renaming, deleting and etc.

To know all the commands in the `docker container` command, run:
> docker container

## Deleting  container
If you run the `docker ls -a` you will notce that the ID is huge, but you actually only need the first three chars to delete it.<br>
The deletion should be made in a non-running container. If you try to delete an active one, it will give an error. Unless you force it.<br>
Stopping a container:
> docker stop <name>

Deleting a container
> docker container rm `-f` `<id0 id1 id2 id...>`

The '-f' indicates the forced operation and the 'id...' means that you can delete more than one container at once, simply pass them IDs side to side.

## Docker container run
It is a command that first looks for that image locally in image cache. If it isn't there, it looks for it in remote images repositories (Docker Hub, by default).<br>
Now, it downloads its latest version available and creates a new container based on that image and prepares to start.<br>
Gives it a virtual IP on a private network inside docker engine and opens up port 80 on host and forward to port 80 in container.<br>
Starts container by using the CMD in the image Dockerfile.

### Changing the defaults
The port, version and CMD run you seen above👆 are defaults, but all that can be changed when running the command.
> docker container run --publish `8080:80` --name webhost -d `nginx -T`

Respectively, host listening port, image version and CMD run.

## A small dive into detach
When you run a container in the terminal, you will notice that the terminal is now just the process running and the informations bout it being logged there.<br>
If this behaviour is not wanted, simply detach the command and now it only runs in the background. If want to see something about it, just run the desired commands.
> -d

## --name
Naming a container is good for practicability, because you can now run commands for it using it and not its ID, making things faster for you.
> --name 'name'

For example, the [nginx process](#-changing-the-defaults) we ran before is now named 'webserver'

## Container VS Virtual Machines (VM)
There are a lot of confusion and misconceptions about these two. There are similarities, but they are *not the same*.<br>
Containers are simply processes running in a machine, not a machine itself.
