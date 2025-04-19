import requests, json
md_version_table = requests.get("https://gist.githubusercontent.com/cliffano/77a982a7503669c3e1acb0a0cf6127e9/raw/8d7fef701c026c009260171f0e50ea32450fff2a/minecraft-server-jar-downloads.md").text
data = [list(map(lambda x: x.strip(),line.split('|')))[1:-1] for line in md_version_table.splitlines()[2:]]
p_data = {datum[0]: {'server':datum[1], 'client':datum[2]} for datum in data}
print(json.dumps(p_data, indent=4))