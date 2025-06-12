# Dockerfile

Dockerfile was already talked about previously in other topics, but this one will have it as its focus.

## Recap: The Seven Dockerfile Statements

1- `FROM <image-name:and-version>` Statement;
* **Always** needed and let you select the base image you want to start your build from.

2- `ENV <env-variables>` Statement;
* The way for you to use environment variables and later build statements and any containers created from that image can use those environment variables.

3- `WORKDIR <workdir-path>` Statement;
* The proper way of going to a directory to work on - or create it, if not already created.

4- `COPY <from destination>` Statement;
* Typical way to copy your source code in and any local files you need;

5- `RUN <terminal-command>` Statement;
* Universal way of running commands inside the container image while it's building - linux binary must exist in the image already.

Then, the changes this RUN statement made in this file system are saved to a new image layer using `COPY . .`

6 - `EXPOSE <port>` Statement;
It will tell your container runtime which port your application will be listening on.

7 - `CMD[<commands>]` Statement.
It sets the default command your container will execute when it starts.

There are about 20 Dockerfiles instructions in total: FROM; ADD; COPY; RUN; ARG; ONBUILD; LABEL; EBV; USER; SHELL; WORKDIR; EXPOSE; VOLUME; STOPSIGNAL; CMD; ENTRYPOINT; HEALTHCHECK.

## Buildtime VS Runtime

Two main questions to think about with every new instruction you write in a Dockerfile:

1- Does it overwrite its previous use?
* Overwrite VS Additive

2- Does it change my image or my container?
* Buildtime VS Runtime

## Buildtime VS Runtime

Runtime: It is only used when you run the container later.
* CMD Statement...
* `"docker run"`.

Runtime statements include: EXPOSE; VOLUME; STOPSIGNAL; CMD; ENTRYPOINT; HEALTHCHECK.

Buildtime: Used to change files and directories in the image layers.
* Copy and RUN Statements...
* `"docker build"`.

Buildtime statements include: FROM; ADD; COPY; RUN; ARG; ONBUILD.

Some statements affects both runtime and buildtime.
* ENV...
* Build and run.

The statements that affect both runtime and buildtime include: LABEL; ENV; USER; SHELL; WORKDIR.

## Overwrite VS Additive

Overwrite: Only one statement will run, the other one will be ignored.
* CMD and WORKIR statements (only the last one will be used). -> The last WORKDIR declares where the last CMD executes from.

The statements that will overwrite are: ARG; LABEL; ENV; SHELL; USER; WORKDIR; STOPSIGNAL; CMD; ENTRYPOINT; HEALTHCHECK.

Additive: Every statement will be used even if you do it more than once with different args.
* EXPOSE statement -> It lists all the ports exposed (you cana also do it in a single line, like `EXPOSE <port-1> <port-2> <port-x> <port...>`)

The statements that are additive are: ADD; COPY; FROM; RUN; ONBUILD; EXPOSE; VOLUME

> There is no statement that affects both runtime and buildtime and is additive.

# Dockerfile 1.1: Dockerfile Entrypoint

