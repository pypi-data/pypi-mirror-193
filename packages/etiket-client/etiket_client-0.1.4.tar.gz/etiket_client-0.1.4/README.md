# etiket-client

A client library for accessing etiket  $e|i>$ 

## Logging in to etiket

First, create a client:

```python
from etiket_client import Client

client = Client(base_url="https://etiket.example.com") #of course change base_url
```

You can only use the unauthenticated client to call the login endpoint with your credentials to obtain a valid token:

```python
from etiket_client import Client
from etiket_client.api.access import login_for_access_token as get_token
from etiket_client.models import BodyLoginForAccessToken

client = Client(base_url="https://etiket.example.com")
form_data = BodyLoginForAccessToken(username=username, password=password)

token = get_token.sync(client=client, form_data=form_data)
access_token = token.access_token
refresh_token = token.refresh_token
```

Other endpoints require authentication, use `AuthenticatedClient` with obtained access token as above:

```python
from etiket_client import AuthenticatedClient

client = AuthenticatedClient(
                base_url="https://etiket.example.com", #of course change base_url
                token="SuperSecretToken"
)
```

## Creating datasets

A minimal example of creating a dataset is shown below. Note that a scope should already be created and available to you. 

```python
import shortuuid

from etiket_client.models import DatasetIn, DatasetOut
from etiket_client.api.datasets import create_dataset
from etiket_client.types import Response

<...you have obtained tokens and created client: AuthenticatedClient...>

dataset_new = DatasetIn(
                    name='awesomedataset',
                    uid=shortuuid.ShortUUID().random(length=10),
                    scope='somescope',
)
response: DatasetOut = create_dataset.sync(
                            client=client, 
                            json_body = dataset_new
)
# or if you need more info (e.g. status_code)
response: Response[DatasetOut] = create_dataset.sync(
                                    client=client,
                                    json_body = dataset_new,
)
```

When a dataset is created, it requires a unique identifer string, uid. Above we created a random string of length 10 which would be unique enough for a lifetime, but you can choose your own way to create a unique identifier. This also allows already created datasets with a different type of uid (e.g. UUID, TUID) to be added easily to $e|i>$.  A single dataset can then be uniquely identified through 'scope/uid'. Although, a dataset is uniquely defined by the combination of a scope and uid, it is typically recognized by name, description, ranking and additional user defined metadata. 

Additionally, a list of files can also be defined upon creation of the dataset. Note that the files will **not** be uploaded upon creation of datasets. Upload is done explicitly via `/uploads` endpoint or with `etiket_client.api.tus` methods.   

```python
from etiket_client.models import DatasetIn, DatasetOut
from etiket_client.api.datasets import create_dataset
from etiket_client.types import Response

file1 = FileDatasetIn(name='filename1',uid=shortuuid.ShortUUID().random(length=10))
file2 = FileDatasetIn(name='filename2',uid=shortuuid.ShortUUID().random(length=10))
dataset_new = DatasetIn(
                    name='awesomedataset', 
                    scope='somescope',
                    uid=shortuuid.ShortUUID().random(length=10),
                    files=[file1,file2]
)
dataset: DatasetOut = create_dataset.sync(
                            client=client,
                            json_body = dataset_new
)
```

Files can of course also be added after dataset creation by calling `etiket_client.api.file.add_file`. 

## Collections and metadata

Datasets can be grouped into collections. First a collection needs to be created, and subsequently datasets can be added to the collection:

```python
from etiket_client.models import CollectionIn
from etiket_client.api.collections import create_collection, add_dataset_to_collection

collection  = create_collection.sync(
                client=client,
                json_body=CollectionIn(
                                name='somecollection',
                                scope='somescope',
                          )            
)

response = add_dataset_to_collection.sync(
                client=client,
                scope='somescope',
                name=collection.name,
                dataset_uuid=dataset.uuid,
)
```

Datasets can also be removed from collections. 

Additional user defined metadata can be provided to datasets in JSON format, either upon creation of the dataset by adding a meta field or explicitly via metadata functions:

```python
dataset_new = DatasetIn(
                name='awesomedataset',
                scope='somescope',
                uid=shortuuid.ShortUUID().random(length=10),
                files=[file1,file2],
                meta={'key1':'value1', 'key2':['value2a','value2b']},
)
```

Note that the JSON document that can be added is limited in format. Only key-value pairs or key-list(values) pairs are allowed, where all keys and values are strings ( more than 2 and less than  20 characters). Arbitrary keys can be added, but not all keys can be used in dataset query. Only a predefined list of keys can be used when  querying datasets: sample, fridge, setup, measurement_type, variablesMeasured, keywords. 

## Exploring datasets

A dataset is identified by a scope and UUID, but you can query or list datasets given a scope filtering on additional metadata to be able to browse through datasets:

```python
from etiket_client.api.datasets import get_datasets

datasets  = get_datasets.sync(
                client=client,
                scope='somescope',
                collection='somecollection',
                name='prefixofdataset',
                since=datetime.utcnow() - timedelta(days=100),
                until=datetime.utcnow() + timedelta(days=1),
                ranking=0,
                sample='samplename',
                fridge='bluefors',                
)
```

Datasets are ordered by date of creation and use pagination to limit the number of datasets per request. Use offset and limit to move through pages.

Via the ranking attribute of a dataset you can specify which datasets are filtered out of the query. Only datasets larger than the requested ranking will be returned. In this way, you can favour datasets over others. 

## Uploading files

File uploads are done using the tus.io protocol. `tuspy` package which is included in this client can be used: [tuspy docs](https://tus-py-client.readthedocs.io/en/latest/).

An etiket upload client can be initalized:

```python
from etiket_client import AuthenticatedClient, UploadClient

client = AuthenticatedClient(
                base_url="https://etiket.example.com", #of course change base_url
                token="SuperSecretToken"
)

#initialize tus client with autenticated client
tus = UploadClient(client)
#or optinally specify scope
tus = UploadClient(client,scope=scope)

#create uploader by specifying scope and file_uid
uploader = tus.uploader('path/to/file',scope=scope, file_uid=file_uid)

#or only file_uid if scope is already specified in UploadClient
uploader = tus.uploader('path/to/file',file_uid=file_uid)

#chunk size is sys.maxsize by default (probably quite large)
#you can specify chunksize
uploader = tus.uploader('path/to/file', scope=scope, file_uid=file_uid, chunk_size=1024)

#instead of path provide filestream
fs = open('path/to/file.ext', mode=)
uploader = tus.uploader(file_stream=fs, scope=scope, file_uid=file_uid, chunk_size=200)

# Upload a chunk i.e 200 bytes.
uploader.upload_chunk()

# Uploads the entire file.
# This uploads chunk by chunk.
uploader.upload()

# you could increase the chunk size to reduce the
# number of upload_chunk cycles.
uploader.chunk_size = 800
uploader.upload()

# Continue uploading chunks till total chunks uploaded reaches 1000 bytes.
uploader.upload(stop_at=1000)
```


## Downloading files

File downloads are done by using the ```get_file``` method. Optionally a range_ header can be added to do a partial download and perform downloads in parallel.
