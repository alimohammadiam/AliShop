from kavenegar import *
from urllib.error import HTTPError


def send_sms_with_template(receptor, tokens: dict, template):
    """
        sending sms that needs template
    """
    try:
        api = KavenegarAPI(
            '6D4874766C44655279436D4835727367456750522F386A56636B54445745323876495857544355314A74453D'
        )
        params = {
            'receptor': receptor,
            'template': template,
        }
        for key, value in tokens.items():
            params[key] = value

        response = api.verify_lookup(params)
        print(response)
        return True
    except APIException as e:
        print(e)
        return False
    except HTTPError as e:
        print(e)
        return False


def send_sms_normal(receptor, message):

    try:
        api = KavenegarAPI(
            '6D4874766C44655279436D4835727367456750522F386A56636B54445745323876495857544355314A74453D'
        )
        params_buyer = {
            'receptor': receptor,
            'message': message,
            'sender': '2000660110'
        }
        response = api.sms_send(params_buyer)
        print(response)
    except APIException as e:
        print(e)
    except HTTPError as e:
        print(e)
