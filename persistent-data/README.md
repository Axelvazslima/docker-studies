# Persistent Data: Volumes...

## Container Lifetime and Persistent Data

Containers are usually immutable and ephemeral.

> Immutable infrastructure: Only re-deploy containers, never change.

## Union File System (UFS)

The Docker file system.

## Separation of Concerns

What about databases or unique data?

The persistent layers only goes away when you remove a container - not when you stop it.

### Volumes and Bind Mounts

Volumes: Make special location outside of container UFS. So it is preserved across container removals and allows us to attach it to wherever container we want.

Bind Mounts: Link container path to host path.

## Data Volumes

**VOLUME** command in Dockerfile

In Dockerfile:
```sh
VOLUME <path>
```
It tells Docker to create a new volume location and assign it to the path direction.

The volume **outlives** the container and only 'dies' when you *manually* delete them.

To cleanup unused volumes, you can run:
```sh
docker volume prune
```

You can see an image's volume by inspecting it:
```sh
docker image inspect <image-name>
```

You can list your current volumes by running:
```sh
docker volume ls
```
By doing that, you get a list of current volumes and its rivers and names.

You can also inpect a volume by running:
```sh
docker volume inspect <volume-name>
```

### Naming volumes

A friendly way to assign vols to containers.

Vey useful to tell volumes apart.

To do it use the '-d' prefix followed by its name and its path separated by a ':', like '-v mysql-db:/var/lib/mysql'. Run:
```sh
docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql
```

### docker volume create

It is a command that is required to be ran before "docker run" to use *custom drivers* and *labels*.

```sh
docker volume create
```

Why doing it? Specify a different driver (only way), put labels on it.

## Bind Mounting

A mapping of a host file or directory to a container file or directory. -> Having both locations pointing at the same files.

Can't be used in Dockerfile, but at container run, like <host-file-path>:<container-path>. Run this
```sh
container run -v $(pwd):<container-path> image
```

## How File Permissions Works Across Multiple Containers accessing the same volume or bind-mounting

File ownerships between containers and the host are just numbers. It stays consistent, no matter how you run them. The displayed names are there to be human-friendly, the Linux Kernel only cares about IDs - which are attached to each file and directory in the file system itself, and those IDs are the same no matter which process accesses them.

For multiple containers accessing the same volume or bind-mounting, some problems may arise:
* 1- The `etc/password` is different accross them. Different names are fine (because only IDs matter). Two processes trying to access the same file must have a matching user ID or group ID.
* 2- Your two containers are running as different users.

### Troubleshooting Issues

Run `ps aux` in each container to see a list of *processes* and *usernames*. The process needs a matching user ID or group ID to access the files in question.

Find the UID/GID in each containers `etc/password` and `etc/group` to translate names to numbers. It will probably have a missmatch there.

It is easier to be fixed in your own image - third parties images like ngix or mysql may be harder. Read its docs.

User and groups with hard-coded IDs will look something like this in your Dockerfile:
```sh
RUN groupadd --gid 1000 node \\
        && useradd --uid 1000 --gid node --shell /bin/bash --create-home node
USER 1000:1000
```