# Scheduled Job Runner

This project is a Python-based scheduled job runner that uses APScheduler to manage and execute periodic tasks.

## Features

- Configurable job scheduling using APScheduler
- SQLite database for job persistence
- Thread and process pool executors for job execution
- Logging functionality
- Sample jobs demonstrating different scheduling patterns

## Requirements

- Python 3.x
- APScheduler
- SQLAlchemy

## Installation

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Configure your jobs in the `jobs` directory. Two sample jobs are provided:
   - `job1.py`: A simple job that creates an in-memory SQLite database and performs some operations.
   - `job2.py`: An empty file where you can add your own job.

2. Adjust the scheduler configuration in `config/scheduler_config.py` if needed.

3. Modify `main.py` to add or remove jobs from the scheduler as required.

4. Run the main script:
   ```
   python main.py
   ```

## Project Structure

- `main.py`: The entry point of the application.
- `config/scheduler_config.py`: Configuration for the APScheduler.
- `jobs/`: Directory containing job definitions.
- `requirements.txt`: List of Python package dependencies.

## Adding New Jobs

1. Create a new Python file in the `jobs` directory.
2. Define your job function.
3. Import the job in `main.py`.
4. Add the job to the scheduler in the `main()` function of `main.py`.

## Logging

The application logs events to a file. You can configure the log file name and logging level in `main.py`.