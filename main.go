package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"github.com/joeshaw/envdecode"
)

type GitHub struct {
	Token string `env:"GITHUB_TOKEN,required"`
}

type RepoOwner struct {
	Login string
}

type Repos struct {
	Items []Repo
}

// https://developer.github.com/v3/repos/
type Repo struct {
	Owner          RepoOwner
	Name           string
	FullName       string `json:"full_name"`
	Description    string
	Fork           bool
	ForkCount      int    `json:"forks_count"`
	WatcherCount   int    `json:"watchers_count"`
	StargazerCount int    `json:"stargazers_count"`
	Language       string `json:"language"`
}

func getProjects(user string, g GitHub) {
	client := &http.Client{}
	url := "https://api.github.com/users/" + user + "/repos"
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Println("creating filter request failed:", err)
	}
	req.Header.Add("Authorization", "token "+g.Token)
	req.Header.Set("content-type", "application/json")
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("error reading " + url)
		return
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("%s", err)
		return
	}
	if resp.StatusCode != 200 {
		fmt.Println("problem with" + url)
		return
	}
	//fmt.Printf("%s\n", string(body))
	var r []Repo
	//var rr interface{}
	err = json.Unmarshal(body, &r)
	if err != nil {
		log.Fatal("Error unmarshalling: ", err)
	}
	//fmt.Printf("%v\n", r)
	for _, proj := range r {
		fmt.Printf("%s %s %d %t %d %s\n",
			proj.FullName,
			proj.Owner.Login,
			proj.StargazerCount,
			proj.Fork,
			proj.ForkCount,
			proj.Language)
	}

}

func main() {
	// read the file.
	var readfile = flag.String("f", "accounts.txt", "List of users to run stats on")
	flag.Parse()

	// get the github token
	var github GitHub
	err := envdecode.Decode(&github)

	file, err := os.Open(*readfile)
	if err != nil {
		log.Fatal("Error opening file: ", err)
	}

	// create a new scanner
	scanner := bufio.NewScanner(file)
	// go through each line of the file
	for scanner.Scan() {
		//fmt.Println(scanner.Text())
		getProjects(scanner.Text(), github)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}
