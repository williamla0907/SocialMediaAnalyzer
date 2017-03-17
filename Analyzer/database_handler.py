import boto3
from boto3.dynamodb.conditions import Key, Attr

class DatabaseHandler:

    def __init__(self):
        #self.dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
        self.session = boto3.session.Session(aws_access_key_id='AKIAJZ5AB4UMBOILNJBQ', aws_secret_access_key='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', region_name='us-east-1')
        self.dynamodb = self.session.resource('dynamodb')
        self.table = self.dynamodb.Table('TweetsDB')



    def getItem(self, keyword):
        response = self.table.scan(
            FilterExpression=Attr('text').contains(keyword.lower()) | Attr('text').contains(keyword.upper()) | Attr('text').contains(keyword.title())
        )
        items = response['Items']
        '''
        while (response.get('LastEvaluatedKey')):
            response = self.table.scan(
                FilterExpression=Attr('text').contains(keyword.lower()) | Attr('text').contains(keyword.upper()) | Attr(
                    'text').contains(keyword.title()),
                ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])
        '''
        return items


    def getAllItem(self):
        response = self.table.scan()
        items = response['Items']
        while (response.get('LastEvaluatedKey')):
            response = self.table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])

        return len(items)



