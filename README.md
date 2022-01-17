# Piccolo-FastAPI project template with authentication
- Integrated with Piccolo ecosystem (orm, admin panel and api).
- Authentication with OAuth2 and JWT.


See each project's documentation for more information.


## Setup

### build the containers

```bash
docker-compose build
```
### run the server

```bash
docker-compose up
```


### Running tests

```bash
docker-compose run web sh -c "piccolo tester run"
```


## todo:
  - [ ] add load balancer
  - [ ] add caching system
  - [ ] optimization for production
