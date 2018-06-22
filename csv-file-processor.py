import sys
import os
import glob
import shutil
import logging
import commands
import time
import datetime

from sqlalchemy import create_engine
import pandas
from settings import INPUT_PATH, EXTENSIONS, PROCESSED_FOLDER_NAME, FAILURE_FOLDER_NAME, USERNAME, PASSWORD, HOST_NAME,\
    DATABASE, TABLE_NAME, DATABASE_ENGINE, TABLE_COLUMNS
from datetime import datetime as dt


class CsvFileProcessor(object):
    """
    Csv data uploader Class
    """

    # Folder path for processed files
    processed_path = None

    # Folder path for processing failed files
    failure_path = None

    # creating the mysql engine
    # csvEngine = create_engine(DATABASE_ENGINE + USERNAME + ":" + PASSWORD + "@" + HOST_NAME + ":1521/" + DATABASE)
    csvEngine = create_engine("mysql+pymysql://" + USERNAME + ":" + PASSWORD + "@" + HOST_NAME + "/" + DATABASE)

    def __init__(self, args):
        super(CsvFileProcessor, self).__init__()
        self.args = args
        self.set_processed_path()
        self.set_failure_path()

    def set_processed_path(self):
        """
        Set Prcoessed folder path for source files
        """
        self.processed_path = os.path.join(os.path.abspath(os.path.join(INPUT_PATH, os.pardir)), PROCESSED_FOLDER_NAME)
        if not os.path.exists(self.processed_path):
            os.mkdir(self.processed_path)

    def set_failure_path(self):
        """
        Set Failure folder path for source files which fails formatting
        """
        self.failure_path = os.path.join(os.path.abspath(os.path.join(INPUT_PATH, os.pardir)), FAILURE_FOLDER_NAME)
        if not os.path.exists(self.failure_path):
            os.mkdir(self.failure_path)

    def move_file(self, file_path, status=True):
        """
        Move file to processed folder
        """
        if status:
            path = self.processed_path
        else:
            path = self.failure_path
        dst_filename = os.path.join(path, os.path.basename(file_path))
        shutil.move(file_path, dst_filename)

    def get_files(self, path, extensions):
        """
        Return all files which has dumped before the day of script execution with the extensions provided from the path
        as a list
        """
        files_grabbed = []
        today = datetime.datetime.now().date()
        for ext in extensions:

            grabbed_files_list = glob.glob(os.path.join(path, "*.{0}".format(ext)))

            for grabbed_file in grabbed_files_list:
                epoch_string = grabbed_file.split("-")[1]
                date_obj_converted = self.convert_epoch_time(int(epoch_string[0:10]))
                if date_obj_converted < today:
                    files_grabbed.append(grabbed_file)
        return files_grabbed

    def convert_epoch_time(self, epoch_date):
        """Returns the date from epoch datetime"""

        converted_date = dt.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_date)),
                                     '%Y-%m-%d %H:%M:%S').date()
        return converted_date

    def process_file(self, csv_file):
        """
        Method to read and insert the file to database and move it to processed/failure folders
        """
        is_success = True

        logger.info("Processing file: %s started at %s" % (csv_file, datetime.datetime.now()))

        try:
            df = pandas.read_csv(csv_file, header=None, engine='python')
            df.columns = TABLE_COLUMNS
            df.to_sql(TABLE_NAME, self.csvEngine, if_exists='append', index=False)
            logger.info("File processing succeeded for:  %s at %s " % (csv_file, datetime.datetime.now()))
        except Exception, e:
            is_success = False
            logger.error("File processing failed for:  %s with message as : %s" % (csv_file, e))
            logger.error("Copied the file: %s to failed folder " % csv_file)

        # self.move_file(csv_file, is_success)

    @staticmethod
    def stop_if_already_running():
        """
        Method to stop the script if already running
        """
        script_name = os.path.basename(__file__)
        status_output = commands.getstatusoutput(
            "ps aux | grep -e '%s' | grep -v grep | awk '{print $2}'| awk '{print $2}'" % script_name)
        if status_output[1]:
            logger.info("Already Running. Exiting")
            sys.exit(0)

    def run(self):
        """
        Main method for the script
        """
        all_files = self.get_files(INPUT_PATH, EXTENSIONS)
        if all_files:

            # call the main function to process each file
            for single_file in all_files:
                self.process_file(single_file)

        else:
            logger.info("No files found. Exiting")


if __name__ == "__main__":
    # Rotating handler logger
    logger = logging.getLogger('csv-file-processor-logger')
    logger.info("Starting the csv processing script")
    obj = CsvFileProcessor(sys.argv[1:])
    obj.stop_if_already_running()
    # run the script if not already runnning
    obj.run()
    logger.info("Script Completed")
