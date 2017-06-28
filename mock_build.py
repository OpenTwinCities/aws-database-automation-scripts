import boto3

# Not at all operational
# A general baseline structure


class TableInterface(object):
    def __init__(self):
        self.ddb = boto3.client('dynamodb')

    def create(self):
        resp = self.ddb.create_table(
            AttributeDefintions=[],
            TableName="",
            KeySchema=[],
            ProvisionedThroughput={}
        )

    def load_line(self, csv_line):
        resp = self.ddb.put_item(
            TableName="",
            Item={} # Convert items to syntax
        )

    def load(self, csv):
        for line in csv:
            self.load_line(line)
        # First line will be all strings as the categories
