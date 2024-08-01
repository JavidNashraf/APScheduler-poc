import logging
from config.scheduler_config import configure_scheduler
from jobs.job1 import job1

# Configure logging
logging.basicConfig(filename='your_filename', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    scheduler = configure_scheduler()

    # Add jobs to the scheduler
    scheduler.add_job(job1, 'interval', seconds=30)  # Runs every 30 seconds

    # New job scheduler below
    # scheduler.add_job(job2, 'cron', day_of_week='mon-fri', hour=17) # Runs every weekday (Monday to Friday) at 5 PM.
    
    # Start the scheduler
    scheduler.start()
    logger.info("Scheduler started.")
    
    try:
        # Keep the script running
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler shut down.")

if __name__ == '__main__':
    main()
