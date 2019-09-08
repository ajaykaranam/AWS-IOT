	# Steps to connect Sensortag , Raspberry pi, AWS IoT, Mysql and Grafana  

		# Connecting Raspberry pi to AWS IOT Core: 

			# On Raspberry Pi : 

				1. On the Raspberry pi , open the browser and login to AWS console
				2. Select the IOTcore service
				3. Click on the "Onboard" option
				4. Select the "Configuring a device" option
				5. Click on "Get started"
				6. Choose a platform as "Linux" and choose a AWS IoT Device SDK as Python
				7. Register a thing
				8. Download the "connect_device_package.zip" on to the raspberry Pi
				9. unzip the "connect_device_package.zip" file using 
						$ unzip connect_device_package.zip
				10. Make sure root-CA.crt file, .crt and private.key certificate files are present.  
				11. Change the execution mode of start.sh file 
						$ chomd +x start.sh
				12. Replace the aws-iot-device-sdk-python.git
						git clone https://github.com/aws/aws-iot-device-sdk-python.git
						cd aws-iot-device-sdk-python
						python setup.py install
				13. If root-CA.crt file doesnt exists then use the following command
						curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > root-CA.crt
				14. Update the basicpubsub.py file as attached here.
				15. Run the below command after setting up the AWS console 
						$ ./start.sh command

			# Connecting sensor tag to Raspberry pi
				Install bluepy on the raspberry pi using the following commands  
						$ sudo apt-get install python-pip libglib2.0-dev
						$ sudo pip install bluepy 
						$ sudo apt-get install git build-essential libglib2.0-dev
						$ git clone https://github.com/IanHarvey/bluepy.git
						$ cd bluepy
						$ python setup.py build
						$ sudo python setup.py install

			git link for bluepy:  
			https://github.com/IanHarvey/bluepy/tree/master/bluepy

			# On AWS Console : 
				1. Click on "Secure" to create required policy for the Thing create in the above step 7 
				2. Select the recently created certificate and attach thing and the policy
				3. Select the Test and subscribe to sdk/test/Python
			
			# Creating the mysql Data base in AWS
				1. Select the AWS RDS service 
				2. Click on create Data base 
				3. Select mysql 
				4. Selct the template as Free Tier
				5. Provide the master password
				6. If required disable the AutoScaling
				7. Make RDS Publicly accessible
				8. Click on create data base
				9. Wait for the database to create 
				10. Click on the secuirty group  
				11. Select the Inbound from dropdown option in "Actions" tab
				12. Edit the Inbound Rule by change the "source" option as any
				13. Repeat the same for the outbound.
				14. Create DB using the HeidiSQL console or using MySQL workbench
				
			I prefer using the HeidiSQL because its lot easier to setup and can be used to all the AWS DB connectivity.

			# Connecting AWS IOT core to Lambda function
				1. Login into the AWS console and select the "ACT".
				2. Create the Rule to send the payload to the lambda function through following steps : 	
				1. Click on Create. 
				2. Add Name of the rule.
				3. Add the query statement to process the paload from Raspberry Pi
						SELECT * from "sdk/test/Python" 
				4. Add action as Send message to Lambda function.
				5. Create the new Lambda function that inserts the records to DB.
				6. The attached Lambda function can be used to insert the record to DB.

			# Connecting AWS RDS mysql to Grafana :
				1. Login to grafana 
				2. Click on MyGrafana
				3. Select the "Hosted Grafana" and click on the grafan instance
				4. Select the Data source
				5. Selct Mysql and then add End point of the AWS RDS end point .
				6. Get the DB name from configuration tab of AWS RDS instancce
				7. Provide your master username and pwd 
				8. Setup the dasboard on the Grafana
				
			Now from the Raspberry Pi run the ./start.sh command boom now you can see values from sensor tag on the "Grafana" 
	 
