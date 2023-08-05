from typing import List, Union
import requests, json
from .do import (
    AutodlContainerUserSettingDO,
    AutodlImageDO,
    AutodlNodeUserSettingDO,
    AutodlNodeInfoDO,
    AutodlContainerDO,
    AutodlContainerInfoDO
)

class AO:
    def __init__(self, token: str) -> None:
        self.url = "https://www.autodl.com/api/v1/dev"
        self.header = {
            "Authorization": token,
            "Content-Type": "application/json"
        }

    
    def __extract_response(self, response):
        return json.loads(response.content)



    def fetch_images(self)->List[AutodlImageDO]:
        url = self.url+"/image/private/list"
        body = {"page_index":1, "page_size": 100}
        response = requests.post(url, json=body, headers=self.header)
        response = self.__extract_response(response)
        if response['code']!='Success':
            raise ValueError(f"Fail to fetch image list: {response['msg']}")
        return [AutodlImageDO(
                    name=img['image_name'], 
                    image_id=img['id'],
                    image_uuid=img['image_uuid'],
                ) for img in response['data']['list']]



    def create_deployment(self, setting: AutodlNodeUserSettingDO)->str:
        url = self.url+"/deployment"
        body = setting.dict()
        print(body)
        response = requests.post(url, json=body, headers=self.header)
        response = self.__extract_response(response)
        print(response['data'], response['code'], response['msg'])
        if response['code']!='Success':
            raise ValueError(f"Fail to create node: {response['msg']}")
        return response['data']['deployment_uuid']



    def delete_deployment(self, deployment_uuid:str)->bool:
        url = self.url+"/deployment"
        body = {"deployment_uuid": deployment_uuid}
        response = requests.delete(url, json=body, headers=self.header)
        response = self.__extract_response(response)
        if response['code']!='Success':
            raise ValueError(f"Fail to delete deployment {deployment_uuid}: {response['msg']}")
        return True



    def list_deployment(self):
        url = self.url+"/deployment/list"
        body = {"page_index":1, "page_size": 100}
        response = requests.post(url, json=body, headers=self.header)
        response = self.__extract_response(response)
        if response['code']!='Success':
            raise ValueError(f"Fail to fetch deployment list: {response['msg']}")
        return [AutodlNodeInfoDO(
            id=node['id'],
            uid=node['uid'],
            uuid=node['uuid'],
            name=node['name'],
            deployment_type=node['deployment_type'],
            replica_num=node['replica_num'],
            parallelism_num=node['parallelism_num'],
            image_uuid=node['image_uuid'],
            template=AutodlContainerUserSettingDO(
                region_sign=node['template']['region_sign'],
                gpu_name_set=node['template']['gpu_name_set'],
                gpu_num=node['template']['gpu_num'],
                memory_size_from=node['template']['memory_size_from'],
                memory_size_to=node['template']['memory_size_to'],
                cpu_num_from=node['template']['cpu_num_from'],
                cpu_num_to=node['template']['cpu_num_to'],
                price_from=node['template']['price_from'],
                price_to=node['template']['price_to'],
                image_uuid=node['template']['image_uuid'],
                cmd=node['template']['cmd']
            )
        ) for node in response['data']['list']]
        


    def list_container(self, deployment_uuid):
        url = self.url+"/deployment/container/list"
        body = {"deployment_uuid": deployment_uuid, "page_index":1, "page_size": 100}
        response = requests.post(url, json=body, headers=self.header)
        response = self.__extract_response(response)
        if response['code']!='Success':
            raise ValueError(f"Fail to fetch container list: {response['msg']}")
        return [AutodlContainerDO(
            uuid=c['uuid'],
            deployment_uuid=c['deployment_uuid'],
            machine_id = c['machine_id'],
            status = c['status'],
            gpu_num = c['gpu_num'],
            gpu_name = c['gpu_name'],
            cpu_num = c['cpu_num'],
            memory_size = c['memory_size'],
            image_uuid = c['image_uuid'],
            price = c['price'],
            info = AutodlContainerInfoDO(
                ssh_command = c['info']['ssh_command'],
                root_password = c['info']['root_password'],
                proxy_host = c['info']['proxy_host'],
                custom_port = c['info']['custom_port']
            )
        ) for c in response['data']['list']]