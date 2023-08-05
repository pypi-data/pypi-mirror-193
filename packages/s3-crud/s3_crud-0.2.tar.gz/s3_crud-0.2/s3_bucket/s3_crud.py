from boto3 import Session
import os
from robot.api.logger import console
import mimetypes
import logging
from robot.libraries.BuiltIn import BuiltIn
from dotenv import load_dotenv

class s3_crud(object):
  
    load_dotenv()
    ROBOT_LISTENER_API_VERSION = 3
   
    def __init__(self):
        try:
            aws_access_key_id = os.getenv('ACCESS_KEY_ID')
            aws_secret_access_key = os.getenv('SECRET_KEY')
            aws_region_name = os.getenv('REGION_NAME')
            self.session = Session(aws_access_key_id, aws_secret_access_key)
            self.s3 = self.session.resource("s3")
            self.bucket_name = os.getenv('BUCKET_NAME')
            self.my_bucket = self.s3.Bucket(self.bucket_name)
        except Exception as e:
            logging.error('Exception was thrown %s' % e)
            print("Error is {}".format(e))
            raise e
       
    def read_content(self, file):
        try:
            # reading all the files in the bucket
            new_file_name= None
            file_read = None
            for s3_files in self.my_bucket.objects.all():
                key = s3_files.key
                if key == file:
                    file_read = s3_files.get()['Body'].read()
                    new_file_name = key
                    break
            return file_read, new_file_name
        except Exception as e:
            raise e   

    def upload_files(self, path, filename):
        try:
            # uploading a file to s3 bucket from your locla machine
            console("*** Objects avilable before uploading a new file ***")
            files_before_upload = []
            files_after_upload = []
            object_name = filename
            for s3_files in self.my_bucket.objects.all(): 
                files_before_upload.append(s3_files.key)
            before_upload= files_before_upload
            key = object_name
            objs = list(self.my_bucket.objects.filter(Prefix=key))
            if (len(objs)>0):
                console(f"{object_name} file exists is s3 bucket")
            else:
                file_to_be_uploaded = path+ '/' +filename  
                mt= mimetypes.guess_type(file_to_be_uploaded)
                if mt[0] == "image/png" or mt[0] == "image/jpeg":  
                    self.my_bucket.upload_file(file_to_be_uploaded, object_name)
                    console("file is uploaded in s3 bucket")
                elif mt[0] == "application/json":
                    self.my_bucket.upload_file(file_to_be_uploaded, object_name)
                    console("file is uploaded in s3 bucket")
                elif mt[0] == 'text/csv':
                    self.my_bucket.upload_file(file_to_be_uploaded, object_name)
                    console("file is uploaded in s3 bucket")
                elif mt[0] == 'text/x-python':
                    self.my_bucket.upload_file(file_to_be_uploaded, object_name)
                    console("file is uploaded in s3 bucket")
                else:
                    console(f"new file type found and the file type is {mt[0]}")
            for s3_files in self.my_bucket.objects.all():
                files_after_upload.append(s3_files.key)
            after_upload = files_after_upload
            return before_upload, after_upload
        except Exception as e:
            print(e)

    def delete_file(self, fileName):
        try:
            # deleting a file from s3 bucket
            files_before_delete = []
            files_after_delete = []
            console("Objects available in the s3 bucket")
            for s3_files in self.my_bucket.objects.all():
                files_before_delete.append(s3_files.key)
            before_delete = files_before_delete
            key = fileName
            self.my_bucket.delete_objects(Delete={"Objects":[{"Key":key}]})
            console("Objects available in the s3 bucket after deletion")
            for s3_files in self.my_bucket.objects.all():
                files_after_delete.append(s3_files.key)
            after_delete = files_after_delete
            return before_delete, after_delete
        except Exception as e:
            raise e

    def download_file(self, fileName, path):
        try:
        # downloading a file from s3 bucket to your local machine
            files_before_download = []
            files_after_download = []
            key = fileName
            objs = list(self.my_bucket.objects.filter(Prefix=key))
            for s3_files in self.my_bucket.objects.all():
                files_before_download.append(s3_files.key)
            before_download = files_before_download
            if (len(objs)>0):
                console("Donloading a file from s3....")
                file_to_save = path+ '/' +fileName
                file_to_download = fileName
                mt= mimetypes.guess_type(fileName)
                if mt[0] == "image/png" or mt[0] == "image/jpeg":   
                    self.my_bucket.download_file(file_to_download, file_to_save)
                    console("file is downloaded successfully")
                elif mt[0] == "application/json":   
                    self.my_bucket.download_file(file_to_download, file_to_save)
                    console("file is downloaded successfully")
                elif mt[0] == 'text/csv':
                    self.my_bucket.download_file(file_to_download, file_to_save)
                    console("file is downloaded successfully")
                elif mt[0] == 'text/x-python':
                    self.my_bucket.download_file(file_to_download, file_to_save)
                    console("file is downloaded successfully")
            else:
                console("file is not available in s3 bucket")
            for s3_files in self.my_bucket.objects.all():
                files_after_download.append(s3_files.key)
            after_download = files_after_download
            return before_download, after_download
        except Exception as e:
            raise e

    def start_suite(self, name, data):
        try:
            path = os.getenv('UPLOAD_PATH')
            csv_file = os.getenv('CSV_FILE')
            file_content, file_name = self.read_content(csv_file)
            if file_name is None:
                console("file is not available in s3 bucket, so upload theis file in s3 buclet")
                self.upload_files(path, csv_file)           
                console("FILE IS UPLOADED")
            else:
                BuiltIn().set_suite_variable('${csv_file_content}', file_content)

            json_file = os.getenv('JSON_FILE')
            file_content, file_name = self.read_content(json_file)
            if file_name is None:
                console("file is not available in s3 bucket, so upload theis file in s3 buclet")
                self.upload_files(path, json_file)           
                console("FILE IS UPLOADED")
            else:
                BuiltIn().set_suite_variable('${json_file_content}', file_content)

            user_json = os.getenv('USER_JSON')
            file_content, file_name = self.read_content(user_json)
            if file_name is None:
                console("file is not available in s3 bucket, so upload theis file in s3 buclet")
                self.upload_files(path, user_json)           
                console("FILE IS UPLOADED")
            else:
                BuiltIn().set_suite_variable('${user_json_file_content}', file_content)
                BuiltIn().set_suite_variable('${user_json_file_name}', file_name)

            # Read any file from s3 bucket
            file_Name = os.getenv('PY_FILE')
            file_content, file_name = self.read_content(file_Name)
            if file_name is None:
                console("file is not available in s3 bucket, so upload theis file in s3 buclet")
                self.upload_files(path, file_Name)           
                console("FILE IS UPLOADED")
            else:
                BuiltIn().set_suite_variable('${diff_file_content}', file_content)
                # console(file_content)
            before_upload, after_upload = self.upload_files(path, file_Name)  
            BuiltIn().set_suite_variable('${before_upload}', before_upload)
            BuiltIn().set_suite_variable('${after_upload}', after_upload)

        except Exception as e:
            raise e
    
    def end_suite(self,name,data):
        pass
    
    def start_test(self,name,data):
        try:
            file = os.getenv('FILE')
            path = os.getenv('DOWNLOAD_PATH')
            before_download, after_download = self.download_file(file, path)
            BuiltIn().set_test_variable('${before_download}', before_download)
            BuiltIn().set_test_variable('${after_download}', after_download)
            before_delete, after_delete = self.delete_file(file)
            BuiltIn().set_test_variable('${before_delete}', before_delete)
            BuiltIn().set_test_variable('${after_delete}', after_delete)
        except Exception as e:
            raise e
        
    def end_test(self,name,data):
        pass

    def start_keyword(self, data, kw):
        pass

    def log_message(s, msg):
        pass   

    def output_file(self, path):
        pass 

    def log_file(self, path):
        pass 

    def report_file(self, path):
        pass 

    def xunit_file(self, path):
        pass

    def debug_file(self, path):
        pass