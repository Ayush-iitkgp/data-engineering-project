# data-engineering-project
A Python Service to perform checks for duplicates in a dataset

### Prerequisites
Project requires python 3.10.11, docker, and poetry 1.6.1.

### Running

```bash
# via docker
docker compose up -d
```

#### Running tests
```bash
docker-compose exec app bash
poetry run pytest
```

#### How do we handle Null values?

If one of the rows in the column list is None/Nan, it is treated as a separate group

#### What is the maximum size of the dataset than can be processed?
Since, Pandas Dataframe is loaded in the memory, we can only process the dataset of size one-third of the RAM size.
