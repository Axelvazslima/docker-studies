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
The deletion should be made in a non-running container. If you try to delete an active one, it will give an error. Unless you force it.
> docker container rm `-f` `<id0 id1 id2 id...>`

The '-f' indicates the forced operation and the 'id...' means that you can delete more than one container at once, simply pass them IDs side to side.
