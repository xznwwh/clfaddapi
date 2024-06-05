import requests

def getAPI(url):
	response = requests.get(url)
	ip_addresses = []
	ips = []
	idx = 1 
	if response.status_code == 200:
	    json_data = response.json()
	    for item in json_data['outbounds']:
	    	if item["type"]=="trojan":
	    		tag = item["tag"]
	    		server = item["server"]
	    		if server in ips:
	    			continue
	    		server_port = item["server_port"]
	    		if isselect(tag):
	    			ips.append(server)
	    			ip_addresses.append(f"{server}:{server_port}#HKG{idx}")
	    			idx = idx + 1  	
	return(ip_addresses)
	    
def w2d(dat):
	if len(dat) > 0 :
		csv_file_path = "./myips.csv"
		with open(csv_file_path, 'w', newline='') as file:
		    for ip in dat[:10]:
		        file.write(str(ip).strip() + "\n")               


def isselect(tag):
	vls = ["HKG","HK","hkg","hk","联通","电信","移动"]
	for v in vls : 
		if v in tag:
			return(True)

if __name__ == '__main__':
	api_url = "https://ctjg.consi.site/hzSoC52WPgrv0Xon?singbox"
	w2d(getAPI(api_url))
