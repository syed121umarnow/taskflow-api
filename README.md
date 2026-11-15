# taskflow-api
A production-style task management REST API built with Python, FastAPI, PostgreSQL and Docker.

## Local PostgreSQL with Podman

On macOS, Podman runs containers inside a Linux virtual machine. Start one if you have not created it yet:

```sh
podman machine init
podman machine start
```

The repository includes a Compose file for PostgreSQL. `podman compose` requires a Compose provider (such as `podman-compose`). If you do not have one, install it with Homebrew:

```sh
brew install podman-compose
```

Then start the database with:

```sh
podman compose up -d db
podman compose ps
```

PostgreSQL is available on `localhost:5432`. The defaults are database `taskflow`, user `taskflow`, and password `taskflow-local`. To change them, set `POSTGRES_DB`, `POSTGRES_USER`, and `POSTGRES_PASSWORD` in your local `.env` file; `.env.example` lists the development defaults. The port is bound to localhost, and database files persist in the `postgres_data` volume.

Stop the container without deleting database data:

```sh
podman compose down
```

To delete the database and its stored data, run `podman compose down -v`.

**Note:** The API currently uses an in-memory task repository, so starting PostgreSQL does not yet make API tasks persistent. The database connection and a PostgreSQL-backed repository still need to be implemented.
