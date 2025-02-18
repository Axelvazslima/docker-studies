# 🐳 BASICS 🐳

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
Basic web service for docker containers.
