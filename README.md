# ZiTrade

## Setup

1. clone this repo with `git clone <repo-ssh-url>`
2. install local packages with `pip install -e ./lib`

## odds-api-gateway

This is the first gateway of the codebase. [Odds-api](https://the-odds-api.com/) is a sports betting api that covers odds from all over the world (by that it means US, UK, EU, and AU, a bit like a band's "world tour", where the world is coincidentally centred around those countries). This gateway is relatively easier to implement because 

1. There's a swagger page for the api, so some code-autogeneration will be leveraged (will look at swagger-codegen) 
2. the dev version of the api is free to use, with a cap of 500 requests/month. 
3. It integrates the odds in many bookies (and some exchanges), so saves the effort of a mapper that integrates the odds on the event/market/contract level

The architecture of the gateway can be seen here: 