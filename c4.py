"""""
d1 ={ 
    key:value,
    key:value
}

|ips:
|Devices_names:
|Policies:
|staus:


d1={
    ip:'172.0.0.1',
    d_name:'pc#1',
    policy:'Avoid. 2,3,5'
    status:True
},
{5 devices}

d1.get(ip)=172....
"""""


network_config= {
    "0001":{
        "ip": "172.0.0.1",
        "device":"switch",
        "policy":"Deny All",
        "status":False,
        "lista": [1,4,6,0,8]
    },

    "0002":{
        "ip": "192.168.0.1",
        "device":"firewall",
        "policy":"Avoid .2 .3 .3",
        "status":True
    },
    "0003":{
        "ip": "10.0.0.1",
        "device":"router",
        "policy":"Allow All",
        "status":True
    },
    "0004":{
        "ip": "172.16.1.10",
        "device":"switch", 
        "policy":"Deny All",
        "status":False
    },
    "0005":{
        "ip": "192.168.1.0",
        "device":"firewall",   
        "policy":"Avoid .2 .3 .3",
        "status":True
}

}

a = [1,2,3, [7,8,1]]
yaEnUso = a.pop(3)
print(yaEnUso)
#print(a[3][1])
contenido = network_config.get("0001")
listaA = contenido.get('lista')
num = listaA[2]

net_config ={ "0002" : { "ip":1}}
print(net_config)
#print(num)
#print(network_config.get("0001").get("lista")[2])