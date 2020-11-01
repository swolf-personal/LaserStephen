import requests

while(1):
  action = input("Laser [On/Off/Get/Exit]: ")
  r = None
  if(action.lower() == "on"):
    r = requests.get("http://192.168.0.12/laser/1")
  elif(action.lower() == "off"):
    r = requests.get("http://192.168.0.12/laser/0")
  elif(action.lower() == "get"):
    r = requests.get("http://192.168.0.12/read")
    print(r.content.split("<br>")[2].split("</html>")[0])
  elif(action.lower() == "exit"):
    break
  else:
    continue
