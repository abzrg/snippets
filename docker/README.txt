DOCKER
======

Source: https://www.youtube.com/watch?v=b0HMimUb4f0

Basics
------

Pull/download an image from an image registry (by defautl: dockerhub)

    docker pull hello-world

Run a container from an image

    docker run hello-world

List all images

    docker image ls

Lists running containers

    docker ps

List all containers including stopped ones

    docker ps -a/--all


Port Mapping
------------

By default containers are isolated from the host network. In order to
interact with, for example, a web server container, we need to publish
the port that it is listening on, so that our host can see it.

    docker run -p/--publish host_port:container_port image


Running in background
---------------------

Detach after start

    docker run -d/--detach image

    * It outputs the container-id of the detached container
    * Containers can also be identified by their name as well.
      * Unless specified (by --name <cntnr-name>), docker generates a
        random name for each new container, e.g.,

        docker run -d --name my-nginx nginx

To see the logs generated by the detached container:

    docker logs <container-name/id>

    * Logs is also available in the GUI: simply click on the desired
      docker container and select the 'Logs' tab

To stop a running container

    docker stop <container-name/id>

    * Containers can be stopped from the GUI: click on the container
      and then click on the stop button.

Stopped containers will still show up in the list of all docker
containers (docker ps -a/--all). To prune (remove all stopped
containers)

    docker container prune

    * When running a container, --rm removes the container when it
      stops

        docker run --rm image


Tags and Digests
----------------

pin by a tag

If a tag is not specified, docker pulls the 'latest' version or runs
the 'latest' version pulled. To pick a specific version

    docker run image:tag

    docker run nginx:1.27

    * Note that tags are mutable: 1.27.0 may bump up to 1.27.1. To
      mitigate that either choose more specific tag (e.g.
      1.27.0-bookworm) or pin the image by its (sha-256) digest. To
      get the digest of the of the image:

        docker image ls --digest

      To get the tag of a specific image from dockerhub, go to 'Tags'
      tab, click on the desired image, and copy the image digest. Once
      you have the digest,

        docker run/pull image@digest

        docker run/pull image:tag@digest

        ** Note that when <digest> is specified, the <tag> is ignored,
        but the tag can be there for humans to tell which version the
        digest refers to.

    ! For production applications prefer pinning by digests not by
    version.


Environmental variables and arguments (Runtime)
-----------------------------------------------

To pass environment variables to container use the -e/--env option to
docker run,

    docker run -e/--env ABC=123 -e DEF=456 image


Slim images, and Alpine images
------------------------------

Python image by default comes with a full featured Debian image. To
fix that for python or any other image, one can use the '-slim'
version of an image which is the bare bone version of that image.

    docker pull python:3.12-slim

For even larger decrease in size look for images that 'alpine' tag in
them.

    docker pull python:alpine

    * NOTE: Look for the differences between slim and alpine versions.
    Notably alpine uses the musl libc whereas slim uses the Debian
    based glibc. Another difference is that slim uses gnu coreutils
    but slim uses busybox utilities.


Debugging running containers
----------------------------

Sometimes it's necessary to go beyond logs (docker logs) and poke
around in the terminal.

GUI: select Containers on the left bar; click on the container; click
on the 'Exec' tab to get the terminal.

CLI: 'exec' allows execution of a process on an already running
     container.

    docker exec -it/--interactive,--tty <container-name/id> <process>

    docker exec -it <id> /bin/bash


Persistence Storage (Volumes, Bind-mounts)
------------------------------------------

Any new container is a fresh and starts with the same file system
every time. Any time written from previous runs are gone.

    docker run python:3.12 \
        python -c 'f="/data.txt";open(f,"a").write("Ran!\n");print(open(f).read())'

    * It will output every time the following

        Ran!

However, many applications, for example, databases, have data that
they want to persist across runs, even to persist across image
changes (e.g., upgrading the database version). It can be achieved
using a "mount".

    docker run -v/--volume mydata/:/data <image> <command/process>

    docker run -rm -v mydata:data/ python:slim \
        python -c 'f="/data/data.txt";open(f,"a").write("Ran!\n");print(open(f).read())'

  * Mount types:
    1. Volumes                PERSISTENT
    2. Bind mounts            PERSISTENT
    3. Tempfs mounts          NOT PERSISTENT

  * Persistence comparison
    Volumes                                    | Bind Mounts
    -------------------------------------------+---------------------------------------------------------------
    Newer                                      | Older (but still useful)
    More features                              | Less features
    Managed by docker daemon                   | Mounts host file/dir into container
    Syntax: provide name of the volume in host | Syntax: Provide relative/absolute path in host
        -v mydata:/path/in/container           |     -v ./mydata:/path/in/container (file/dir editable in host)
        or more verbose --mount                |     -v /mydata:/path/in/container

  * Which Mount?
    Volumes                                | Bind Mounts
    ---------------------------------------+--------------------------------------
    Often better in production             | Often convenient in development
    Not dependent on host filesystem       | Quickly share with host
    Easy to share across containers        |    Gives containers access to host
    Can use remote or cloud storage:       |    Consider read-only mount
        AWS EFS                            |        -v ./mydata:/path/in/container
        NFS                                |
        SSHFS                              |
    Container does not need access to host |
    Not convenient to share with host      |


Custom Images (build your own Dockerfiles)
------------------------------------------



Multistage builds
-----------------

Multiple FROMS
COPY --from=builder



Docker Compose
--------------

Manage/orchestrate multiple image build and container spawns.
Basically solves the problem of starting and stopping containers
manually.

docker-compose.yml in the root of the project

docker compose build
docker compose up
docker compose down (--rm is passed to docker run)
docker compose stop (only stops the container)


Publishing/Pushing images on a registry
-------------------------------

...
