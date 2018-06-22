import logging
from logging.handlers import RotatingFileHandler


# Settings to be updated as per Server

# Input folder for the files
INPUT_PATH = "/home/seqato/knowesis/data/inputs"

# Database details
# HOST_NAME = "localhost"
# USERNAME = "knowesis"
# PASSWORD = "123"
# DATABASE = "xe"
DATABASE_ENGINE = "oracle://"
# TABLE_NAME = "CSV_DATA"

HOST_NAME = "localhost"
USERNAME = "knowesisuser"
PASSWORD = "knowesis123##"
DATABASE = "knowesis"
TABLE_NAME = "test"


# TABLE_COLUMNS = ["COLUMN1", "COLUMN2", "COLUMN3", "COLUMN4", "COLUMN5", "COLUMN6", "COLUMN7", "COLUMN8",
#                  "COLUMN9", "COLUMN10", "COLUMN11", "COLUMN12", "COLUMN13", "COLUMN14", "COLUMN15",
#                  "COLUMN16", "COLUMN17", "COLUMN18", "COLUMN19", "COLUMN20", "COLUMN21", "COLUMN22", "COLUMN23",
#                  "COLUMN24", "COLUMN25", "COLUMN26", "COLUMN27", "COLUMN28", "COLUMN29", "COLUMN30", "COLUMN31",
#                  "COLUMN32", "COLUMN33", "COLUMN34", "COLUMN35", "COLUMN36", "COLUMN37", "COLUMN38",
#                  "COLUMN39", "COLUMN40", "COLUMN41", "COLUMN42", "COLUMN43", "COLUMN44", "COLUMN45", "COLUMN46"
#                  "COLUMN47", "COLUMN48", "COLUMN49", "COLUMN50", "COLUMN51", "COLUMN52", "COLUMN53", "COLUMN54",
#                  "COLUMN55", "COLUMN56", "COLUMN57", "COLUMN58", "COLUMN59", "COLUMN60", "COLUMN61", "COLUMN62",
#                  "COLUMN63", "COLUMN64"]

# TABLE_COLUMNS = ["COLUMN1", "COLUMN2", "COLUMN3", "COLUMN4", "COLUMN5", "COLUMN6", "COLUMN7", "COLUMN8",
#                  "COLUMN9", "COLUMN10", "COLUMN11", "COLUMN12", "COLUMN13", "COLUMN14", "COLUMN15",
#                  "COLUMN16", "COLUMN17", "COLUMN18", "COLUMN19", "COLUMN20"]
#
TABLE_COLUMNS = ["COLUMN1", "COLUMN2", "COLUMN3", "COLUMN4", "COLUMN5", "COLUMN6", "COLUMN7", "COLUMN8",
                 "COLUMN9", "COLUMN10", "column11", "column12", "column13", "column14", "column15",
                 "column16", "column17", "column18", "column19", "column20", "column21", "column22", "column23"]


# cols_to_use = range(1,25)

# Below folders will be generated if not present at location

PROCESSED_FOLDER_NAME = "processed"

FAILURE_FOLDER_NAME = "failed"

LOG_FILE_PATH = "/home/seqato/workspace/Knowesis_poc/logs/csv-file-processor.log"

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
