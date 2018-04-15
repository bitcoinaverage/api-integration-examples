package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"
	"time"

	"github.com/pkg/errors"
	"github.com/spf13/viper"
)

const (
	baseURL = "https://apiv2.bitcoinaverage.com"
)

func main() {
	viper.AddConfigPath(".")    // optionally look for config in the working directory
	err := viper.ReadInConfig() // Find and read the config file
	if err != nil {             // Handle errors reading the config file
		panic(errors.Wrap(err, "config file error"))
	}
	p := viper.Get("publickey")
	if p == nil {
		panic("missing publickey")
	}
	publicKey := p.(string)

	s := viper.Get("secretkey")
	if s == nil {
		panic("missing secretkey")
	}
	secretKey := []byte(s.(string))

	// get timestamp
	t := time.Now()
	ts := int(t.Unix())
	timestamp := strconv.Itoa(ts)

	payload := timestamp + "." + publicKey

	// prepare the hmac with sha256
	hash := hmac.New(sha256.New, []byte(secretKey))
	hash.Write([]byte(payload))
	// hex representation
	hexValue := hex.EncodeToString(hash.Sum(nil))

	// defining signature
	signature := payload + "." + hexValue

	uriPath := "/indices/global/ticker/BTCUSD"

	// make request
	req, _ := http.NewRequest("GET", baseURL+uriPath, nil)

	// add needed header
	req.Header.Add("X-signature", signature)

	// read response
	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))
}
