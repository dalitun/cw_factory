#!/usr/bin/env bash

IMG_ID=$(cat outputs-packer/id.txt)

DATE=$(date +%Y-%m-%d:%H:%M:%S)
IMG_NAME="${OS_NAME}-${OS_VERSION}_${DATE}"

glance image-download --file ./current.qcow2 ${IMG_ID}

virt-sparsify --convert qcow2 --compress  "current.qcow2" "current-c.qcow2"  || exit 1

rm -rf current.qcow2

glance image-create --name ${IMG_NAME}-compress --disk-format qcow2 --container-format bare --file current-c.qcow2

rm -rf current-c.qcow2

openstack image list | grep ${IMG_NAME}-compress | awk {'print $2'} > result/id.txt
