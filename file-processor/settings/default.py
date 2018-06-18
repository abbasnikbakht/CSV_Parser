import logging
from logging.handlers import RotatingFileHandler

# Settings to be updated as per Server

INPUT_PATH = "/home/seqato/knowesis/data/inputs"

# Database details

HOST_NAME = "localhost"
USERNAME = "knowesisuser"
PASSWORD = "knowesis123##"
DATABASE = "knowesis"
TABLE_NAME = "test"
TABLE_COLUMNS = ["COLUMN1", "COLUMN2", "COLUMN3", "COLUMN4", "COLUMN5", "COLUMN6", "COLUMN7", "COLUMN8",
                      "COLUMN9", "COLUMN10", "COLUMN11", "COLUMN12", "COLUMN13", "COLUMN14", "COLUMN15",
                      "COLUMN16", "COLUMN17", "COLUMN18", "COLUMN19", "COLUMN20", "COLUMN21", "COLUMN22",
                      "COLUMN23"]

# below folders will be generated if not present at location: INPUT_PATH/../


PROCESSED_FOLDER_NAME = "processed"

FAILURE_FOLDER_NAME = "failed"


LOG_FILE_PATH = "/tmp/csv-file-processor.log"

# Log size in MB
LOG_SIZE = 1

# Log file back up count
BACKUP_COUNT = 5

# Settings that need not be changed

EXTENSIONS = ["csv"]

# Logger Settings

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger('csv-file-processor-logger')
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILE_PATH, maxBytes=LOG_SIZE * 1024 * 1024,
                                               backupCount=BACKUP_COUNT)
logger.addHandler(handler)
