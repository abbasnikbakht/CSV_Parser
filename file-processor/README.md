# Csv File Processor Script

Script to insert the csv file to the Database

## Run

To run the script, execute the __csv-file-processor.py__ script.

We need to update settings variables defined in _settings/default.py_ file before we can run the script.


#### Example

```sh
python csv-file-processor.py
```

### Settings Variables Explained

Variables | Required? | Purpose             | Sample Value
-------- | --------- | ------------------- | ------------
INPUT_PATH | :white_check_mark: | Source Folder path with the files to be formatted | /home/seqato/knowesis/data/input
OUTPUT_FOLDER_NAME | :white_check_mark: | Output Folder to save the formatted files | formatted
PROCESSED_FOLDER_NAME | :white_check_mark: | Folder to move successfully formatted source files | processed
FAILURE_FOLDER_NAME | :white_check_mark: | Folder to move source files that failed to be formatted | failed
SCP_FAILURE_FOLDER_NAME | :white_check_mark: | Folder to move formatted files that failed to be copied to the server | scp-failed
LOG_FILE_PATH | :white_check_mark: | Path to Log File | /tmp/csv-file-processor.log
HOST_NAME | :white_check_mark: | IP for the server to scp the formatted file | 13.76.176.58
USERNAME | :white_check_mark: | Username for the server | siftuser
HOST_LOCATION | :white_check_mark: | Location to which the filed should be copied on the server | ~/Desktop/
LOG_SIZE | :white_check_mark: | Log file size limit in MB  | 5
BACKUP_COUNT | :white_check_mark: | Log file back up count | 5
