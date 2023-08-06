import requests


class PaymentAggregation:
    def __init__(self, public_key, sandbox):
        self.public_key = public_key
        self.sandbox = sandbox

    def commission(self, data):
        if self.sandbox:
            url = 'http://slickpay-v2.azimutbscenter.com/aggregations/commission'
        else:
            url = 'http://slickpay-v2.azimutbscenter.com/aggregations/commission'

        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}

        res = requests.post(url, headers=headers, json=data)
        return res.content

    def create(self, data):
        if self.sandbox:
            url = 'http://slickpay-v2.azimutbscenter.com/aggregations'
        else:
            url = 'http://slickpay-v2.azimutbscenter.com/aggregations'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        body = res.json()
        return body

    def aggregationStatus(self, transfer_id):
        if self.sandbox:
            url = 'https://dev.aggregator.slick-pay.com/api/user/transfer/transferPaymentSatimCheck'
        else:
            url = 'https://aggregator.slick-pay.com/api/user/transfer/transferPaymentSatimCheck'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        data = {
            'transfer_id': int(transfer_id)
        }
        res = requests.post(url, headers=headers, data=data)

        return res.content

    def list(self, offset):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations?offset={int(offset)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations?offset={int(offset)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def details(self, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def updateAggregation(self, data, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, json=data)
        body = res.json()
        return body

    def deleteAggregation(self, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/aggregations/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)
        body = res.json()
        return body
