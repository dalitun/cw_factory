#!/usr/bin/env bash

## Ubuntu
fly set-pipeline --target factory --config base-image-factory.yml --pipeline ubuntu-14.04 --load-vars-from credentials.yml -v OS_URL=http://cloud-images.ubuntu.com/releases/14.04/release/ubuntu-14.04-server-cloudimg-amd64-disk1.img -v OS_NAME=ubuntu -v OS_VERSION=14.04 -v OS_LOGO=lin-ubuntu.png
fly set-pipeline --target factory --config base-image-factory.yml --pipeline ubuntu-16.04 --load-vars-from credentials.yml -v OS_URL=http://cloud-images.ubuntu.com/releases/16.04/release/ubuntu-16.04-server-cloudimg-amd64-disk1.img -v OS_NAME=ubuntu -v OS_VERSION=16.04 -v OS_LOGO=lin-ubuntu.png

## Debian
fly set-pipeline --target factory --config base-image-factory.yml --pipeline debian-8 --load-vars-from credentials.yml -v OS_URL=http://cdimage.debian.org/cdimage/openstack/current-8/debian-8-openstack-amd64.qcow2 -v OS_NAME=debian -v OS_VERSION=8 -v OS_LOGO=lin-debian.png

## Fedora
fly set-pipeline --target factory --config base-image-factory.yml --pipeline fedora-25 --load-vars-from credentials.yml -v OS_URL=http://mirrors.ircam.fr/pub/fedora/linux/releases/25/CloudImages/x86_64/images/Fedora-Cloud-Base-25-1.3.x86_64.qcow2 -v OS_NAME=fedora -v OS_VERSION=25 -v OS_LOGO=lin-fedora.png
fly set-pipeline --target factory --config base-image-factory.yml --pipeline fedora-24 --load-vars-from credentials.yml -v OS_URL=http://mirrors.ircam.fr/pub/fedora/linux/releases/24/CloudImages/x86_64/images/Fedora-Cloud-Base-24-1.2.x86_64.qcow2 -v OS_NAME=fedora -v OS_VERSION=24 -v OS_LOGO=lin-fedora.png


## CentOS
fly set-pipeline --target factory --config base-image-factory.yml --pipeline centos-6 --load-vars-from credentials.yml -v OS_URL=http://cloud.centos.org/centos/6/images/CentOS-6-x86_64-GenericCloud.qcow2 -v OS_NAME=centos -v OS_VERSION=6 -v OS_LOGO=lin-centos.png
fly set-pipeline --target factory --config base-image-factory.yml --pipeline centos-7 --load-vars-from credentials.yml -v OS_URL=http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2 -v OS_NAME=centos -v OS_VERSION=7 -v OS_LOGO=lin-centos.png
