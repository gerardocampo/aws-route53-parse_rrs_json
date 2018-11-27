#!/usr/bin/env python

import json

filename = "hz_vitalschoice.com.json"
fh = open(filename, "r")
data = json.loads(fh.read())

for dnsstuff in data['ResourceRecordSets']:
    record_type = dnsstuff['Type']
    record_name = dnsstuff['Name']
    hostedzoneid = ''

    if record_type == 'CNAME':
        resource_recs = dnsstuff['ResourceRecords']
        for cname_records in resource_recs:
            value = cname_records['Value']
    elif record_type == 'A':
        alias_target = dnsstuff['AliasTarget']
        hostedzoneid = alias_target['HostedZoneId']
        value = alias_target['DNSName']
    elif record_type == 'NS':
        resource_recs = dnsstuff['ResourceRecords']
        vals = [d['Value'] for d in resource_recs]
        value = ' '.join(vals)
    elif record_type == 'SOA':
        resource_recs = dnsstuff['ResourceRecords']
        for soa_dict in resource_recs:
            value = soa_dict['Value']
    elif record_type == 'MX':
        resource_recs = dnsstuff['ResourceRecords']
        vals = [d['Value'] for d in resource_recs]
        value = ','.join(vals)
    elif record_type == 'TXT':
        resource_recs = dnsstuff['ResourceRecords']
        vals = [d['Value'] for d in resource_recs]
        value = ' '.join(vals)
    else:
        print('This is a DIFFERENT RECORD TYPE')
        value = ''

    print("{}\t{}\t{}\t{}\t".format(record_type,record_name,value,hostedzoneid))

print("\nThere are", len(data['ResourceRecordSets']), "records in this hosted zone.")

