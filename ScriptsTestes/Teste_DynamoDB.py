import boto3


def GetDynamoTable():
    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table('agenda')
    return dynamoTable


def InsertInto():
    dynamoTable = GetDynamoTable()
    dynamoTable.put_item(
        Item = {
            'id': 3,
            'Nome': 'Willamy 3333',
            'Telefone': '(84) 9 9669-2906',
            'E-mail': 'willamy.wlp@gmail.com'
        }
    )
def GetItem():
    dynamoTable = GetDynamoTable()
    return dynamoTable.get_item(
        Key = {
            'id': 11
        }
    )

def UpdateItem(ID):
    dynamoTable = GetDynamoTable()
    dynamoTable.update_item(
        Key = {
            'id': 11
        },
        UpdateExpression = 'SET Nome = :Nome, Telefone = :Telefone',
        ExpressionAttributeValues = {
            ':Nome': 'Willamy D O Joventino',
            ':Telefone': '(84)9 9669-2906'
        }
    )

def DeleteItem(ID):
    dynamoTable = GetDynamoTable()
    dynamoTable.delete_item(
        Key = {
            'id': 11
        }
    )



#print('Antes do Update:\t{}'.format(GetItem()['Item']))
DeleteItem(11)
#print('Depois do Update:\t{}'.format(GetItem()['Item']))

