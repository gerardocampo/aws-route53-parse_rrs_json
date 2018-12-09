#!/usr/bin/env python

import json

# INPUT FILENAME OF JSON TO PARSE BELOW:
filename = "hz.json"

fh = open(filename, "r")
data = json.loads(fh.read())

for dnsstuff in data['ResourceRecordSets']:
    record_type = dnsstuff['Type']
    record_name = dnsstuff['Name']
    hostedzoneid = ''
    is_alias = ''

    if record_type == 'CNAME':
        if 'AliasTarget' in dnsstuff:
            is_alias = 'ALIAS'
            alias_target = dnsstuff['AliasTarget']
            hostedzoneid = alias_target['HostedZoneId']
            value = alias_target['DNSName']
        else:
            resource_recs = dnsstuff['ResourceRecords']
            for cname_records in resource_recs:
                value = cname_records['Value']
    elif record_type == 'A':
        if 'AliasTarget' in dnsstuff:
            is_alias = 'ALIAS'
            alias_target = dnsstuff['AliasTarget']
            hostedzoneid = alias_target['HostedZoneId']
            value = alias_target['DNSName']
        else:
            resource_recs = dnsstuff['ResourceRecords']
            for a_record in resource_recs:
                value = a_record['Value']
    elif record_type == 'NS':
        resource_recs = dnsstuff['ResourceRecords']
        vals = [d['Value'] for d in resource_recs]
        value = ' '.join(vals)
    elif record_type == 'SOA':
        resource_recs = dnsstuff['ResourceRecords']
        for soa_dict in resource_recs:
            value = soa_dict['Value']
    elif record_type == 'MX':
        if 'AliasTarget' in dnsstuff:
            is_alias = 'ALIAS'
            alias_target = dnsstuff['AliasTarget']
            hostedzoneid = alias_target['HostedZoneId']
            value = alias_target['DNSName']
        else:
            resource_recs = dnsstuff['ResourceRecords']
            vals = [d['Value'] for d in resource_recs]
            value = ','.join(vals)
    elif record_type == 'TXT':
        if 'AliasTarget' in dnsstuff:
            is_alias = 'ALIAS'
            alias_target = dnsstuff['AliasTarget']
            hostedzoneid = alias_target['HostedZoneId']
            value = alias_target['DNSName']
        else:
            resource_recs = dnsstuff['ResourceRecords']
            vals = [d['Value'] for d in resource_recs]
            value = ' '.join(vals)
    elif record_type == 'PTR':
        if 'AliasTarget' in dnsstuff:
            is_alias = 'ALIAS'
            alias_target = dnsstuff['AliasTarget']
            hostedzoneid = alias_target['HostedZoneId']
            value = alias_target['DNSName']
        else:
            resource_recs = dnsstuff['ResourceRecords']
            for ptr_record in resource_recs:
                value = ptr_record['Value']
    else:
#        print('This is a DIFFERENT RECORD TYPE')
        value = 'THIS CODE NEEDS HANDLE THIS RECORD TYPE'

    print("{}\t{}\t{}\t{}\t{}".format(record_type,record_name,is_alias,value,hostedzoneid))

print("\nThere are", len(data['ResourceRecordSets']), "records in this hosted zone.")
