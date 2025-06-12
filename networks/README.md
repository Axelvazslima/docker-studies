# Docker network 🐳🛜

> System that allows Docker container to communicate with each other and with external networks.

It provides connectivity between containers running on the same host or different hosts.

Docker <mark>creates</mark> and manages these networks to ensure <mark>secure and efficient</mark> communication.

To know more about Docker networks access the [docker network docs](https://docs.docker.com/engine/network/).

## Docker network Defaults

Each container connected to a private virtual network "bridge".

Each virtual network routes out through NAT firewall on host IP.

All container on a virtual network can talk to each other without `-p` -> this commands exposes your port to a connection.

### Best practice - Docker network

Creating a new virtual network for each app

```
network <app_name> for <image_name> and <container_name(s)> containers

network <api_name> for <container_name> and <container_name(s)> containers
```

> "Batteries included, but removable"

Defaults work well in many cases, but it is easy to change things as you need.

Make new virtual networks.

Attach containers to more than one virtual nerwork - or none.

Skip virtual networks and use host IP: `--net=host`. You lose some of the containerization benefits, but sometimes it's needed.


## Why is it needed?

* Container Communication
    * *Allows containers to communicate with each other within the same host or across multiple hosts*

* Isolation -> <mark style="background:green; color:white">Security</mark>
    * *Ensures that containers are only exposed to specific networks, improving security.*

* Port management
    * *Prevents conflicts by allowing containers to communicate using <mark>container names</mark> instead of managing IP addresses manually.*
    * *Controls how container ports map to the host machine's port.*
    * *Used when exposing a container's service to the **outside world** (e.g., web server).*

* External access
    * *Enables containers to access the internet or be accessed from external clients.*

* Service discovery
    * *Containers in a network can find and connect to each other using container names, simplifying application deployment.*
    * *Essential for scaling services dynamically because **container IP's can change**.*

## Types of Docker Networks

1. Bridge network (default)
    * *Sometimes reffered to as **docker0**.*
    * *Container on the same bridge network can **communicate using their names**.*
    * Use case: *standalone applications that need **internal communication**.*
    * `docker network create <network_name>`

2. Host Network
    * *Removes network isolation and makes the **container use the host machine's network** directly.*
    * Use case: *Performance is critical and you don't need network isolation.*
    * `docker run --network=host <container_name>`

3. Overlay network
    * *Enables communication between containers running on **different Docker Hosts** in a [Swarm cluster](https://docs.docker.com/engine/swarm/).*
    * Use case: *Multi-host networking in **distributed applications**.*
    * `docker network create --driver overlay <overlay_name>`

4. Macvlan Network
    * *Assignes MAC address to containers, making them appear as **physical devices** on the network.*
    * Use case: *Integrating with legacy applications that require direct network access.*
    * `docker network create -d macvlan <macvlan_name>`

5. None network
    * *Completely isolates the container with **no network access**.*
    * Use case: Security-focused applications.
    * `docker run --network=none <container_name>`

## Managing Docker Networks

* List networks:
    * `docker network ls`

* Inspect a network:
    * `docker network inspect <network_name>`

* Create a network:
    * `docker network create --driver <network_name>`

* Remove a network:
    * `docker network rm <my_network>`

* Connect a container to a network:
    * `docker network connect <network_name> <container_name>`

* Disconnect a container from a network:
    * `docker network disconnect <network_name> <container_name>`

## Container IP addresses

The container doesn't use the same IP address as the host, by default.

Getting the container's IP address:

```
docker container inspect --format "{{ .NetworkSettings.IPAddress }}" <container_name>
```

The network blocks the outside-inside ports. They will use their ports. -> If the container's port is not `--publish`ed.

To see a specific exposed port, run:
```
docker container port <continer_name>
```

## Traffic flow and firewalls

> How Docker network move packets in and out.

Ethernet Interface in the Host Machine blocks all the incoming traffic from the physical network by default.

You can't listen on more than one port for multiple containers: Each container's host port **must** be unique.

## CLI management

`--network host` gains *performance* by skipping virtual networks, but **sacrifices security of container model**.

### Creating my own network

```
docker network create <network_name>
```

Spawns a new virtual network for you to attach containers to.

Run `docker network --help` to know more about it.

### Network Driver

> Built in 3rd party extensions that give you virtual network features.

## Default security

Create your apps so frontend/backend sit on same network.

Their inter-communication never leaver host.

All externally exposed ports closed by default.

You must manually expose, `-p` -> better default security.

## DNS (Domain Name System)

It translates human-readable domain names into numerical IP addresses that computers use to identify ech other on the network.

### Naming

Forget IPs -> Static IPs and using IPs for talking to containers is an anti-pattern. Avoid it.

Built-in DNS server that containers use by default.

### DNS Default Names

Docker defaults the hostname to the container's name, but you can also set aliases.
