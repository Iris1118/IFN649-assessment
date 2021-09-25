import time
# Read data from csv file
import csv
import paho.mqtt.publish as publish


def readFromFile():
	with open('soilmoisture_dataset.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		alert = ''
		for row in csv_reader:
			if line_count == 0:  # Display column name
				print(f'Column names are {", ".join(row)}')
				line_count += 1
			else:  # display data
				print(f'\tdatetime : {row[1]}, soil_moisture:{row[2]}, soil_temperature:{row[3]}')
				if float(row[2]) < 30:
					print("\t too dry, need some water")
					alert = 'too dry, need some water'
				# elif float(row[2]) < 40:
				# 	print("suitable zone")
				elif float(row[2]) > 40:
					print('too wet')
					alert = 'too wet'
				line_count += 1
# 				TODO: Prepocess and send data to MQTT at this point
# 				publish.single(topic="Test_IFN649", payload=alert, hostname="localhost")
				print()
				publish.single(topic="Test_IFN649", payload=f'\tdatetime : {row[1]}, moisture:{row[2]}, \
			soil_temperature:{row[3]}', hostname="localhost")
				publish.single(topic="Test_IFN649", payload=alert, hostname="localhost")
				time.sleep(2)
		print(f'Processed {line_count} lines.')


def main():
	readFromFile()


if __name__ == '__main__':
	main()
