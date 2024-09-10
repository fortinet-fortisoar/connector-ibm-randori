## About the connector
IBM Randori is an attack surface management SaaS that monitors internal and external attack surfaces for unexpected changes, blind spots, misconfigurations, and process failures. This connector facilitates automated operations to fetch network, target, service etc.
<p>This document provides information about the IBM Randori Connector, which facilitates automated interactions, with a IBM Randori server using FortiSOAR&trade; playbooks. Add the IBM Randori Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with IBM Randori.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-ibm-randori</pre>

## Prerequisites to configuring the connector
- You must have the credentials of IBM Randori server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the IBM Randori server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>IBM Randori</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Service based URI to which you will connect and perform the automated operations.
</td>
</tr><tr><td>API Token</td><td>API token configured for your account for using the IBM Randori API.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get IP Objects</td><td>Retrieves IP objects based on the query, limit, offset parameter you have specified.</td><td>get_ips <br/>Investigation</td></tr>
<tr><td>Get IPs for Hostname</td><td>Retrieves IPs for hostname based on the query, limit, offset parameter you have specified.</td><td>get_ips_for_hostname <br/>Investigation</td></tr>
<tr><td>Get IPs for Network</td><td>Retrieves IPs for network based on the query, limit, offset parameter you have specified.</td><td>get_ips_for_network <br/>Investigation</td></tr>
<tr><td>Get Hostnames</td><td>Retrieves hostnames based on the query, limit, offset parameter you have specified.</td><td>get_hostnames <br/>Investigation</td></tr>
<tr><td>Get Networks</td><td>Retrieves networks based on the query, limit, offset parameter you have specified.</td><td>get_networks <br/>Investigation</td></tr>
<tr><td>Get Targets</td><td>Retrieves targets based on the query, limit, offset parameter you have specified.</td><td>get_targets <br/>Investigation</td></tr>
<tr><td>Get Services</td><td>Retrieves services based on the query, limit, offset parameter you have specified.</td><td>get_services <br/>Investigation</td></tr>
<tr><td>Get All Detections for Target</td><td>Retrieves all detections for target objects based on the query, limit, offset parameter you have specified.</td><td>get_all_detections_for_target <br/>Investigation</td></tr>
<tr><td>Get Single Detection for Target</td><td>Retrieves single detection for target objects based on the query, limit, offset parameter you have specified.</td><td>get_single_detection_for_target <br/>Investigation</td></tr>
<tr><td>Get Policy</td><td>Retrieves policies based on the query, limit, offset parameter you have specified.</td><td>get_policy <br/>Investigation</td></tr>
<tr><td>Get Report</td><td>Retrieves report based on the query, limit, offset parameter you have specified.</td><td>get_report <br/>Investigation</td></tr>
<tr><td>Get Statistics</td><td>Retrieves statistics based on the query, limit, offset parameter you have specified.</td><td>get_statistics <br/>Investigation</td></tr>
<tr><td>Get Artifact</td><td>Retrieves artifact based on the artifact UUID parameter you have specified.</td><td>get_artifact <br/>Investigation</td></tr>
</tbody></table>

### operation: Get IP Objects
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve the list of IP objects from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get IPs for Hostname
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve the IPs for hostname from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get IPs for Network
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve the IPs for network from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Hostnames
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve the list of hostnames from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Networks
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve the list of networks from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Targets
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve the list of targets from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Services
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve the list of services from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get All Detections for Target
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve all detections for target from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Single Detection for Target
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve single detection for target from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Policy
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve policies from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Report
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve report from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Statistics
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>(Optional) Specify the query to retrieve statistics from IBM Randori. e.g., {
  "condition": "AND",
  "rules": [
    {
      "field": "table.confidence",
      "operator": "greater_or_equal",
      "value": 60
    },
    {
      "field": "table.target_temptation",
      "operator": "greater_or_equal",
      "value": 15
    }
  ]
}
</td></tr><tr><td>Limit</td><td>(Optional) Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr><tr><td>Offset</td><td>(Optional) Index of the first item to be returned by this operation. By default, this is set as 0 and the minimum supported value is 0.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
### operation: Get Artifact
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Artifact UUID</td><td>Maximum number of records that this operation should return. Values supported are: Default: 50 Min: 1 Max: 2000
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "count": "",
    "data": "",
    "offset": "",
    "total": ""
}</pre>
## Included playbooks
The `Sample - ibm-randori - 1.0.0` playbook collection comes bundled with the IBM Randori connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the IBM Randori connector.

- Get All Detections for Target
- Get Artifact
- Get Hostnames
- Get IP Objects
- Get IPs for Hostname
- Get IPs for Network
- Get Networks
- Get Policy
- Get Report
- Get Services
- Get Single Detection for Target
- Get Statistics
- Get Targets

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
