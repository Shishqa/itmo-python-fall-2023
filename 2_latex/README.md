## Как сгенерировать артефакты

```
virtualenv .venv
source .venv/bin/activate

make gen_artifacts
```

## Docker

```
docker build --network host --tag "latex" .
docker run -v ./artifacts:/app/artifacts --rm -it --name latex latex:latest
```
