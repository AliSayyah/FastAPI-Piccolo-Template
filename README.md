# FastAPI-Piccolo project template
- Amazing [FastAPI](https://github.com/tiangolo/fastapi) framework.
- Full Docker integration 
- Docker Compose integration and optimization for local development.
- JWT token authentication.
- Secure password hashing by default.
- [Piccolo Admin](https://github.com/piccolo-orm/piccolo_admin) frontend 
- [Piccolo async ORM](https://github.com/piccolo-orm/piccolo)
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
  - [ ] Gunicorn integration for single server mode
  - [ ] Docker swarm integration + kubernetes for cluster mode
  - [ ] CookieCutter
