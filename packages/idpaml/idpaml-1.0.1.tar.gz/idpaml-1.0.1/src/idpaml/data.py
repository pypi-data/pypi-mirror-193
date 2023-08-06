#!/usr/bin/env python

import os
from time import sleep
from typing import Union
import io
import pandas as pd
from azure.ai.ml.entities import Data
from typing import Optional, Dict, Any
from azure.ai.ml.constants._common import AssetTypes
from azure.identity import ManagedIdentityCredential, DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobClient, DelimitedTextDialect
from ._initialization import client


class AzureMLDataAsset(Data):
    """Data wrapper class for azureml data assets
    
    A child class of the SDKv2 AzureML data class to expedite the creation and maintenance of 
    data assets for workflow assignments and pipeline jobs.

    Params:
        name (str) : Name of the resource
        version (str) : version of the resource
        description (str) : description of the resource
        tags (Dict) : dictionary tags for the resource
        properties (Dict) : asset properties dictionary from artifact class https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-ml_1.3.0/sdk/ml/azure-ai-ml/azure/ai/ml/entities/_assets/asset.py
        path (str) : path to access resource

    """
    def __init__(
        self,
        *,
        description: Optional[str] = None,
        tags: Optional[Dict] = None,
        properties: Optional[Dict] = None,
        path: Optional[str] = None,
        type: str = AssetTypes.URI_FOLDER,
        **kwargs,
    ):
        # replicate init function from data class from AzureML sdk documentation
        logger, ml_client, credential = client()
        self._ml_client = ml_client
        self._skip_validation = kwargs.pop("skip_validation", False)
        self._mltable_schema_url = kwargs.pop("mltable_schema_url", None)
        self._referenced_uris = kwargs.pop("referenced_uris", None)
        self.type = type
        
        # set name equal to file name (sans suffix) from path
        self.name = path.split("/")[-1].split(".")[0]
        super().__init__(
            name=self.name,
            path=path,
            description=description,
            tags=tags,
            type=type,
            properties=properties,
            **kwargs,
        )
        self.path = path
        try:
            latest_version = {d.name: d.latest_version for d in ml_client.data.list()}[self.name]
            self.latest_version = latest_version
        except KeyError as e:
            logger.error(e)
            logger.info("Data asset does not exist. Creating first version.")
            self.latest_version = "1"

    def _get_all_latest_assets(self) -> Dict[str, str]:
        """Get all data assets registered in workspace

        Params:
            self (AzureMLDataAsset) : object
        """
        # use client to retrieve available assets and asset latest versions
        asset_versions = {d.name: d.latest_version for d in self._ml_client.data.list()}
        return asset_versions
    
    def _get_latest_version(self) -> int:
        """Get latest version for specified asset

        Params:
            self (AzureMLDataAsset) : object
        """
        # use client to retrieve available assets and asset latest versions
        asset_version = self._get_all_latest_assets()[self.name]
        return asset_version

    @property 
    def latest_version(self):
        return self._latest_version
    
    @latest_version.setter
    def latest_version(self, value):
        self._latest_version = value

    def update_to_new_version(self) -> Any:
        """Create resource if this currently does not exist.
        
        Params:
            self (AzureMLDataAsset) : object 
        """
        # check to see if current object exists
        if self.name not in self._get_all_latest_assets().keys():
            # create data resource if not extant
            self.latest_version = "1"
            self._ml_client.data.create_or_update(self)
            return self
        else:
            self._ml_client.data.create_or_update(self)
            sleep(3)
            self.latest_version = self._get_latest_version()
            return self

def df_from_delimited_blob(
    blob_url: str, 
    credential: Union[DefaultAzureCredential, ManagedIdentityCredential], 
    **kwargs: Any    
) -> pd.DataFrame:
    """Returns a pandas dataframe from a blob URL

    Args: 
        blob_url (str): blob url string including account and container names on url path
        credential (Union[DefaultAzureCredential, ManagedIdentityCredential]): auth credential for Azure Blob Client

    Returns: 
        df (pd.DataFrame): returned dataframe decoded from bytes

    """
    # retrieve keyvault from os environment vars
    assert "KEY_VAULT_NAME" in os.environ, KeyError("KEY_VAULT_NAME must be set in environment vars to access storage token.")
    keyVaultName = os.environ["KEY_VAULT_NAME"]
    KVUri = f"https://{keyVaultName}.vault.azure.net"
    # get kv client from credential
    kv_client = SecretClient(vault_url=KVUri, credential=credential)
    retrieved_secret = kv_client.get_secret("amldevsaidp-access-key-1")
    # parse blob url for storage account url, container, and blob 
    blob_url_split = blob_url.split("/")
    account_url = "/".join(blob_url_split[:3])+"/"
    container = blob_url_split[3]
    blob = "/".join(blob_url_split[4:])
    # connect to blob through client
    blob_client = BlobClient(account_url=account_url, credential=retrieved_secret.value, container_name=container, blob_name=blob)
    # specify IO format (include header)
    input_format = DelimitedTextDialect(delimiter=',', quotechar='"', lineterminator='\n', escapechar="", has_header=True)
    output_format = DelimitedTextDialect(delimiter=',', quotechar='"', lineterminator='\n', escapechar="", has_header=True)
    reader = blob_client.query_blob("SELECT * from BlobStorage", blob_format=input_format, output_format=output_format)
    # read into bytes-like object
    content = reader.readall()
    # decode dataframe from bytes
    df = pd.read_csv(io.StringIO(content.decode('utf-8')))
    return df


