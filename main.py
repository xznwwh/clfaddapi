import requests

def getAPI(url):
	response = requests.get(url)
	ip_addresses = []
	idx = 1 
	if response.status_code == 200:
	    json_data = response.json()
	    for item in json_data['data']['good']:
	    	ip_addresses.append(f"{item['ip']}#y{idx}")
	    	idx = idx + 1  	
	return(ip_addresses)    	
	    
def w2d(dat):
	csv_file_path = "./clfgoodip.csv"
	with open(csv_file_path, 'w', newline='') as file:
	    for ip in dat[:10]:
	        file.write(ip + "\n")               

if __name__ == '__main__':
	api_url = "https://vps789.com/vps/sum/cfIpTop20"
	w2d(getAPI(api_url))
