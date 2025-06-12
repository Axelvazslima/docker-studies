# Kubernetes Basics

Kubernetes is the whole orchestration system. It is pretty much a Docker 'Framework'.

It is a series of containers, CLI's and configurations.

## K8s Terminology

K8s: Kubernetes (K [8 letters] s);

Kubectl: CLI to configure Kubernetes and manage apps;

Node: Simple server in the Kubernetes cluster;

Kubelet: Kubernets agent running on nodes;

Kube-proxy: Controls the network;

Control Plane ("master"): Set of containers that manage the cluster.
* Includes API server, scheduler, controller manager, etcd, and more.

## Setting it up

You can set it up inside Docker Desktop on its Linux VM.
* For Docker ToolBox, use: MiniKube (it uses VirtualBox to make a Linux VM);
* For your own Linux Host or VM, use: MicroK8s (install Kubernetes right in the OS).
* You may just want to learn it and use it in a Browser, use: [Play with k8s](www.play-with-k8s.com) or [Katacoda](www.katacoda.com)

## Kubernetes Container Abstractions

Pod is the basic unit of deployment. Containers are always in pods.

Pods are the resource object that control its individual containers on a node.

Pod: One or more container running together on one node.

Controller are used to control pods.
* It is used for creating/updating pods and other objects.
* There are many types of controllers, like: Deployment; ReplicaSet; StatefulSet; DaemonSet; Job; CronJob; etc.

Service is the network endpoint to connect to a pod.

Namespace is a filtered group of objects in cluster.
* It is a filter, **not** a security feature.
