# CargoLink Docker Lab

An isolated Docker lab that simulates CargoLink's IT environment. It runs a small web app that lists sample IT assets from a CSV file. All testing happens inside this local lab only.

## Requirements

- Docker Desktop installed and running

## How to Start

```
docker compose up --build
```

Then open <http://localhost:5000> in your browser.

## How to Stop

Press `Ctrl+C` in the terminal, or run:

```
docker compose down
```

## How to Reset

To remove the containers and rebuild from scratch:

```
docker compose down -v
docker compose up --build
```

## What's Inside

- `app.py` - Flask app that reads and displays `assets.csv`
- `assets.csv` - sample CargoLink IT asset data (10 assets)
- `Dockerfile` - builds the Python/Flask container
- `requirements.txt` - Python dependencies
- `docker-compose.yml` - runs the web service on port 5000
- `test-plan.md` - checks to confirm the lab works

## Notes

The data is sample data only. The app is a development server meant for local lab use, not production.
