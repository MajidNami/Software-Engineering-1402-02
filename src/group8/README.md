# Tick 8 Microservice

## Project Description

This project is part of a language learning and test practicing website for English language. It specifically handles the Tick 8 vocabulary learning method, implemented using Nuxt.js, Prisma, and PostgreSQL.

## Features

- User authentication
- Vocabulary management
- Tick 8 progress tracking
- Responsive user interface

## Prerequisites

- Node.js (>=14.x)
- npm (>=6.x)
- PostgreSQL

## Installation

### Steps

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd tick8-microservice
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Set up environment variables by creating a `.env` file:
    ```env
    DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
    API_BASE_URL=http://localhost:8000/api
    ```

4. Start the development server:
    ```bash
    npm run dev
    ```

## Usage

- Navigate to `http://localhost:3000/group8/` in your web browser.
- Register or log in.
- Add, view, and manage vocabulary.
- Track your Tick 8 progress.

## Directory Structure

