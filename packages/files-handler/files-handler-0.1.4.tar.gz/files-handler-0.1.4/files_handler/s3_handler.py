# Importing libraries
import boto3
import botocore
import os
from files_handler.folders_handler import folders_handler

# Local execution paths
result_path = 'output'
input_path = 'input'

class s3_handler:
    """
    Deal with files and connection to S3.
    
    :param bucket: The Bucket.
    :type bucket: string
    :param path_ref: Reference Path to manage the files and folders.
    :type path_ref: string
    """

    def __init__(self, bucket, path_ref):
        self.access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
        self.secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        self.region_name = os.environ.get('AWS_REGION_NAME')
        self.bucket = bucket
        self.path_ref = path_ref
        self.path_to_predict_images = os.path.join(path_ref, input_path)
        self.folders_handler = folders_handler(self.path_ref)

    # Get image from s3 bucket 
    def get_image_from_s3_bucket(self, s3_image_path):
        """
        Get an image from S3 passing the image path on s3 and saving on reference path + input
        
        :param s3_image_path: The s3 path of image with the image name.
        :type s3_image_path: string
    
        :return: If the image was downloaded or not.
        :rtype: boolean
        """
        try:
            self.folders_handler.verify_and_create_folder(self.path_ref, 'Creating reference directory...')
            self.folders_handler.verify_and_create_folder(self.path_to_predict_images, 'Creating input directory...')

            image_name = os.path.basename(s3_image_path)
            print(f'Downloading file: {image_name} to {self.path_to_predict_images} folder') 
            s3 = boto3.resource('s3', aws_access_key_id=self.access_key_id,  aws_secret_access_key=self.secret_access_key, region_name=self.region_name)
            bucket = s3.Bucket(self.bucket)
            
            bucket.download_file(s3_image_path, os.path.join(self.path_to_predict_images, image_name))
            print(f'File Downloaded')
            return True
        
        except botocore.exceptions.ClientError as e:
            return False

    # Upload resulting image to s3 bucket
    def upload_image_to_s3_bucket(self, image_path, s3_output_path):
        """
        Upload an image to S3 passing the image path on s3 and the S3 Output Path
        
        :param image_path: the path of the image locally with the image name
        :type image_path: string
        :param s3_output_path: the path of the image on S3
        :type s3_output_path: string
    
        :return: If the image was uploaded or not.
        :rtype: boolean
        """
        try:
            print(f'Uploading results to {s3_output_path}')
            s3 = boto3.resource('s3', aws_access_key_id=self.access_key_id,  aws_secret_access_key=self.secret_access_key, region_name=self.region_name)
            bucket = s3.Bucket(self.bucket)

            image_name = os.path.basename(image_path)
            print(f'Complete path: {s3_output_path}/{image_name}')
            bucket.upload_file(image_path, os.path.join(s3_output_path, image_name))
            return True

        except botocore.exceptions.ClientError as e:
            return False

    def check_if_file_already_exists(self, file_name, s3_output_path):
        """
        Check if file already exists in s3
        
        :param file_name: the name of the file 
        :type file_name: string
        :param s3_output_path: the path of the file on S3
        :type s3_output_path: string
    
        :return: If the file exists or not.
        :rtype: boolean
        """
        try:
            s3 = boto3.resource('s3', aws_access_key_id=self.access_key_id,  aws_secret_access_key=self.secret_access_key, region_name=self.region_name)
            try:
                s3.Object(self.bucket, os.path.join(s3_output_path, file_name)).load()
                return True
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    # The object does not exist.
                    return False
                else:
                    # Something else has gone wrong.
                    raise
        except botocore.exceptions.ClientError as e:
            return False
