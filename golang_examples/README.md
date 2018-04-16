# Go example

This example uses Viper to access the values for the public and
secret keys. The values are stored in `config.yml` (see below),
which has been added to `.gitignore` so you can't easily
push it to Github accidentally.

To run this example, do the following:
```bash
export GOPATH=`pwd`
cd src/github.com/bitcoinaverage.com/golang-example
go get github.com/golang/dep
dep ensure -v
cat >>config.yml
publickey: "paste public key here"
secretkey: "paste secret key here"
go run basic_req.go
```

