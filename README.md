# python.amazon_s3_bucket
manipulate s3 bucket


1) Install pip.

  https://pip.pypa.io/en/stable/installing/
   Download get-pip.py;
   Run: python get-pip.py

2) Install boto3.

3) Install awscli.
  sudo apt-get install awscli
  aws configure
  
   ~/.aws/credentials
   
     [default]
     
     aws_access_key_id = YOUR_ACCESS_KEY
     
     aws_secret_access_key = YOUR_SECRET_KEY

   ~/.aws/config
   
     [default]
     
     region=us-east-1

Reference: 
http://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation
http://boto3.readthedocs.io/en/latest/reference/services/s3.html
