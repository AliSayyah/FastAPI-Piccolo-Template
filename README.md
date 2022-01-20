# FastAPI-Piccolo project template
- Full Docker integration 
- Docker Compose integration and optimization for local development.
- JWT token authentication.
- Secure password hashing by default.
- Piccolo Admin frontend 
- Piccolo async ORM
- simple CI/CD


See each project's documentation for more information.


## Setup

### build the containers

```bash
docker-compose build
```
### run the server for local development

```bash
docker-compose up
```


### Running tests

```bash
docker-compose run web sh -c "piccolo tester run"
```


## todo:
  - [ ] add load balancer (Traefik)
  - [ ] add caching mechanism
  - [ ] add celery and flower for monitoring jobs
  - [ ] add pgadmin
  - [ ] full CI/CD actions
  - [ ] optimization for production
  - [ ] Docker swarm mode integration + kubernetes 
  - [ ] CookieCutter
