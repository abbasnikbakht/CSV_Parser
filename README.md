# Csv File Processor Script

Script to process the csv file and insert to the Database using python pandas

## Run

To run the script, execute the __csv-file-processor.py__ script.

We need to update settings variables defined in _settings/default.py_ file before we can run the script.

### Project Dependencies
Make sure all the below dependencies are imported before you run the script.
1. Python Pandas V 0.17.1
2. Sqlalchemy V 1.2.8
3. Pymysql V 0.8.1

Note: You can either download this package and import it as modules or install using pip.

#### Example

```sh
python csv-file-processor.py
```

### Settings Variables Explained

Variables | Required? | Purpose             | Sample Value
-------- | --------- | ------------------- | ------------
INPUT_PATH | :white_check_mark: | Source Folder path with the files to be formatted | /home/seqato/knowesis/data/input
PROCESSED_FOLDER_NAME | :white_check_mark: | Folder to move successfully formatted source files | processed
FAILURE_FOLDER_NAME | :white_check_mark: | Folder to move source files that failed to be formatted | failed
LOG_FILE_PATH | :white_check_mark: | Path to Log File | /tmp/csv-file-processor.log
HOST_NAME | :white_check_mark: | Host name for Database | localhost
USERNAME | :white_check_mark: | Username of Database user | knowesisuser
PASSWORD | :white_check_mark: | Password for Database user | "use your password"
DATABASE | :white_check_mark: | Name of the Database | knowesis
TABLE_NAME | :white_check_mark: | Name of the Table | TOPUP_TRIGGER
TABLE_COLUMNS | :white_check_mark: | Name of the columns of the table | name of the columns
LOG_SIZE | :white_check_mark: | Log file size limit in MB  | 5
BACKUP_COUNT | :white_check_mark: | Log file back up count | 5



