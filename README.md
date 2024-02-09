

export CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"
gp env CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"
export PROD_CONNECTION_URL="postgresql://cruddurroot:Dante124#@cruddur-db-instance.cxmcsg4w46fg.us-east-1.rds.amazonaws.com:5432/cruddur"
gp env PROD_CONNECTION_URL="postgresql://cruddurroot:Dante124#@cruddur-db-instance.cxmcsg4w46fg.us-east-1.rds.amazonaws.com:5432/cruddur"

export DB_SG_ID="sg-0088269b917c7f9e0"
gp env DB_SG_ID="sg-0088269b917c7f9e0"

export DB_SG_RULE_ID="sgr-07ccfafda574d316c"
gp env DB_SG_RULE_ID="sgr-07ccfafda574d316c"
aws ec2 modify-security-group-rules \
    --group-id $DB_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={Description=GITPOD,IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"