# ec2connection
Getting live data from Binance API in EC2 server and connecting to AWS RDS 

Create a EC2 instance in AWS  and setup a RDS connection for the virtual sql server in AWS
Here's a document on how to connect to your ec2 instance -https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0
To establish ec2 connection in your terminal:
In your terminal ssh -i /path/my-key-pair.pem ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com
<https://github.com/Priyarag/ec2connection/blob/master/Screen%20Shot%202019-07-01%20at%207.23.10%20PM.png>
Once the ec2 connection is established , install all the dependencies needed for your flask app (use sudo yum install)
Create your flask app by using nano app.py like the example below:
<https://github.com/Priyarag/ec2connection/blob/master/Screen%20Shot%202019-07-01%20at%207.24.35%20PM.png>


