# Currency Converter API

### Overview

This Currency Converter API provides endpoints for obtaining current exchange rates, converting between currencies, and retrieving information about currencies. It is built using FastAPI, SQLAlchemy, and Docker.

### Features

- Convert between currencies
- Get information about currencies
- Automatic updates of exchange rates
- Containerized using Docker for easy deployment

### Installation

To run the Currency Converter API, you need to have Docker installed on your system. Follow the instructions for your operating system to install Docker:

- Install Docker on Windows
- Install Docker on macOS
- Install Docker on Linux

### Usage

Clone this repository to your local machine:

```html
git clone https://github.com/barkhayot/currency-exchange.git
```

Open main folder

```html
cd currency-converter-api
```

Build and run the Docker containers using docker-compose:

```html
docker-compose up --build
```

Once the containers are up and running, you can access the API at http://localhost:8000.

### Endpoints
- `/update`: Update exchange rates in the database to current rates.
- `/currency`: Get all currency data.
- `/updated_time`: Display the date and time of the last update of rates in the database.
- `/convert`: Convert between currencies.

### Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
