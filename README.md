# draugnet-docker

This repository contains a Docker-based setup for the Draugnet backend, UI, and Redis.

## Usage

Start the application stack:

```sh
docker compose up --build
```

Update the settings:
1. Create your own settings
```sh
cp config/draugnet/settings.default.py config/draugnet/settings.py
cp config/draugnetUI/config.default.json config/draugnet/config.json
```
2. Provide the MISP access in `config/draugnet/settings.py`
3. [optional] Update other settings

Access:
- UI: [http://localhost:8080](http://localhost:8080)
- API: [http://localhost:8000](http://localhost:8000)

## Structure

- `backend`: FastAPI service
- `ui`: Nginx serving the frontend
- `redis`: Valkey (Redis-compatible)

## Configuration

Mount your custom config files into:
- `./config/draugnet` → `/app/config`
- `./config/draugnetUI` → `/usr/share/nginx/html/config`
