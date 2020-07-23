# A skeleton of a GCloud function interact with Datastore in Python

### Main requirements
1. GCloud SDK with `emulators` component;
1. **Firestore** in **Datastore** mode;
1. Function API is enabled.
1. A key JSON file of a service account with Datastore write permission.

### Setup env for development
```
    python3 -mvenv venv
    source venv/bin/activate
    pip install -r requirements-test.txt -r requirements.txt
```

### Setup a local instance of Datastore
By running the commands, SDK will create a `datastore_emulator` directory to store local testing data.
```
    export CLOUDSDK_CORE_PROJECT=a_project
    gcloud beta emulators datastore start --data-dir=datastore_emulator
```

If there are some existing data in *Datastore*, import it by:
```
    # first back up Storage
    gcloud datastore export ...
    # use gsutil to manage
    gsutil ls gs://url
    # download to local
    gsutil cp -r gs://url ds_backups
    curl -X POST localhost:8081/v1/projects/a_project:import \
        -H 'Content-Type: application/json' \
        -d '{"input_url":"ds_backups/20200722-055802/20200722-055802.overall_export_metadata","entity_filter":{"kinds":[[MyKind]]}}'
```

### Run test
```
    # start emulator in one terminal
    # in another terminal
    source venv/bin/activate
    # set up environment variables for local Datastore
    $(gcloud beta emulators datastore env-init --data-dir=datastore_emulator)
    export GOOGLE_APPLICATION_CREDENTIALS=some_key.json
    pytest
    deactivate
```

### Deploy
```
    gcloud functions list --project a_project
    # gcloud functions delete list --project a_project
    # a basic checking function
    gcloud functions deploy hello --runtime=python37 --allow-unauthenticated --trigger-http --project a_project
    # a list function of entities in Datastore
    gcloud functions deploy list --runtime=python37 --trigger-http --project a_project
```
