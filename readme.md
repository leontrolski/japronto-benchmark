python web app that:
- creates 50000 products with id and random description in an sqlite db
- has an endpoint `/{product_id}` that returns a description from the db

On my laptop: `Requests/sec: 24130.8596`

# Install:
```bash
virtualenv --python=python3.5 venv
source venv/bin/activate
pip install uvloop==0.8.1
pip install japronto==0.1.1
# install `hey`
mkdir go
export GOPATH=./go
go get -u github.com/rakyll/hey
```

# Run
```bash
python app.py
# in another shell to see if it works
curl 0.0.0.0:8080/1
```

# Benchmark with `hey`
```bash
./go/bin/hey -n 10000 http://0.0.0.0:8080/1
```
