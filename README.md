# Zscaler Python SDK 

This is a Python SDK for Zscaler Internet Access (ZIA).  This client library is designed to support the ZIA [API](https://help.zscaler.com/zia/about-api) and ZIA [Partner API](https://help.zscaler.com/zia/sd-wan-api-integration) (aka "SD-WAN" API) in ZIA 6.1 or newer.  All API referecnes can be found here [[LINK](https://help.zscaler.com/zia/api)].  **PLEASE READ THE DOCUMENTATION BEFORE CONTACTING ZSCALER**

This SDK has been developed mainly using Python 3.8.2 on macOS (10.15.7) and Ubuntu 18.04.1 LTS (Bionic Beaver).  

**NOTE:** This repository will experience frequent updates.  To minimize breakage, public method names will not change.  If you run into any defects, please open issues [[HERE.](https://github.com/eparra/zscaler-python-sdk/issues)]   

## Quick Start 

1) If you have not verified your credentials, we suggest starting [[HERE](https://help.zscaler.com/zia/configuring-postman-rest-api-client)], unless you are already familar with this API.

2) Set Environment Variables   
 
```$ <text-editor> ~/.bash_profile 
export ZIA_USERNAME="<ZIA-ADMIN-USER-ID>"
export ZIA_PASSWORD="<ZIA-ADMIN-USER-PASSWORD>"
export ZIA_API="<ZIA-API-KEY>" 

export ZIA_PARTNER_USERNAME="<ZIA-PARTNER-ADMIN-USER-ID>"
export ZIA_PARTNER_PASSWORD="<ZIA-PARTNER-ADMIN-USER-PASSWORD>"
export ZIA_PARTNER_API="<ZIA-PARTNER-API-KEY>"
```

3) Setup Virtual Environment (optional)

```
python3 -m venv zscaler-sdk
cd zscaler-sdk 
source bin/activate
```
        
4) Clone Repository (OS must have git installed)

```
$ git clone https://github.com/eparra/zscaler-python-sdk.git
$ cd zscaler-python-sdk/
```

5) Install SDK requirements

```
$ pip3 install -r requirements.txt
...
```

6) Install SDK

```
$ python3 setup.py install
...
```

7) Check out examples

```
$ ls examples/
...
```

## API Support

### SD-WAN (Partner) API

* **Locations**
* **VPN Credentials**
* **Static IP**
* **GRE Tunnels**

### FAQs

**Create Location:**

* Can we create location without **name** & **VPN credentials**? - **No**
* Can we create sub-location without **name**, **parentId** & **Ip Addresses**? - No
* Can we create sub-location with **port** & **VPN credentials**? - **No we can't create both**
* Can we create location & sub-location with **same name**? - **Yes**

**Delete Location:**

* Can we **delete parent location** without deleting its sub-location? - **Yes, and its all sub-locations will get deleted**
* Can we **delete sub-location** without deleting the parent location? - **Yes**
* Can we **delete others** sub-location? - **No, it automatically gets deleted, if all the sub-locations are deleted**
* Can we **update others** sub-location? - **Yes**
* Can we pass multiple ip address to sub-location ipAddress list? -
* Can we **delete VPN credentials** if any of the associated location is present? - **No, need to delete all associated locations**



## Licensing

This work is released under the MIT license. A copy of the license is provided in the [LICENSE](https://github.com/eparra/zscaler-python-sdk/blob/master/LICENSE) file.

## Reporting Issues

If you have bugs or other issues specifically pertaining to this library, file them [here](https://github.com/eparra/zscaler-python-sdk/issues).

## References

* https://help.zscaler.com/zia/api
* https://help.zscaler.com/zia/zscaler-api-developer-guide
* https://help.zscaler.com/zia/sd-wan-api-integration

## References

Thanks to [Sofian Halim](https://www.linkedin.com/in/sofian-halim-9237b25/) and [Lidor Pergament](https://www.linkedin.com/in/lidorp/).
