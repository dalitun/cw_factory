#!/usr/bin/env bash

IMG_TMP_ID=$(cat outputs-glance/id.txt)


heat stack-create -f sources/v2/heat/template-network.yaml factory_network



TACK_STATUS=$(heat stack-list | grep factory_network  | cut -d "|" -f4)

while true
  do
   STACK_STATUS=$(heat stack-list | grep factory_network  | cut -d "|" -f4)
   if  [ "$STACK_STATUS" == "CREATE_COMPLETE" ]
      then
        echo $STACK_STATUS
        NET_ID=$(heat output-show factory_network Network_id)
        echo ${NET_ID}
        SG_ID=$(heat output-show factory_network Security_group)
        echo ${SG_ID}
        break
      else
        echo "Wait for factory_network stack will be up"
    fi
 done




DATE=$(date +%Y-%m-%d:%H:%M:%S)

IMG_NAME=${OS_NAME}-${OS_VERSION}-${DATE}




packer build -var "source_image=${IMG_TMP_ID}" -var "image_name=${IMG_NAME}" -var "factory_network=${NET_ID}" \
  -var "factory_security_group_name=${SG_ID}" -var 'ansible_dir=sources/v2/ansible' sources/v2/packer/packer_apt.json


heat stack-delete factory_network


glance image-delete ${IMG_TMP_ID}


mkdir result

openstack image list | grep ${IMG_NAME} | awk {'print $2'} >> result/id.txt

cat result/id.txt

ls result/*