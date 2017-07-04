import boto3;
import os;


BUCKET='BUCKET_NAME';

"""
url: BUCKET.s3.amazonaws.com/
"""



client = boto3.client('s3');
s3 = boto3.resource('s3');


#list of bucket
response = client.list_buckets()
for bucket_n in response["Buckets"]:
	print bucket_n["Name"],"==============",bucket_n["CreationDate"];



#Upload Folder
readFolderToUploadAmazon="./FOLDER_NAME/";
for root, dirs, files in os.walk(readFolderToUploadAmazon):
	for file in files:
			fileAbs=os.path.join(root, file);
			fileToUpload=fileAbs.replace(readFolderToUploadAmazon,"");
			print fileToUpload;
			data=open(fileAbs, 'rb');
			response = client.put_object(
									ACL='public-read',
									Body=data,
									Bucket=BUCKET,
							    	Key=fileToUpload,
									); 	



# delete object from bucket

#'m.jpg' | '1/m.jpg'

response = client.delete_object(
    Bucket=BUCKET,
    Key='m.jpg'
);
print response; 


#List of Object in Bucket
bucket = s3.Bucket(BUCKET)
bucket.Acl().put(ACL='public-read');
for obj in bucket.objects.all():
    print(obj.key)


#Upload file on s3

data=open('m.jpg', 'rb');
response = client.put_object(
    ACL='public-read',
    Body=data,
    Bucket=BUCKET,
     Key='test/preview/1.jpg',
    ); 	
    
print response;

#Get Object description
response = client.get_object(
    Bucket=BUCKET,
    Key='1/3335355.png',
)
print response;



