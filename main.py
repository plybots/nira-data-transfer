import datetime


def __data__map():
    return {
        "deceased": {
            "surname": "ZYKmQ9GPOaF",
            "givenName": "ZYKmQ9GPOaF",
            "otherNames": None,
            "dateOfBirth": "RbrUuKFSqkZ",
            "age": "q7e7FOXKnOf",
            "identificationNumber": "MOstDqSY0gO",
            "sex": "e96GB4CXyd3",
            "occupation": "dsiwvNQLe5n",
            "nationality": None,
            "nationalityCategory": None,
            "residence": {
                "districtName": None,
                "countyName": None,
                "subcountyName": None,
                "parishName": None,
                "villageName": "zwKo51BEayZ",
            },
        },
        "dateOfDeath": "i8rrl8YWxLF",
        "timeOfDeath": "i8rrl8YWxLF",
        "placeOfDeath": {
            "healthFacilityName": "ouname",
            "districtName": None,
            "countyName": None,
            "subcountyName": None,
            "parishName": None,
            "villageName": None,
        },
        "mannerOfDeath": "FhHPxY16vet|KsGOxFyzIs1|b4yPk98om7e|gNM2Yhypydx|tYH7drlbNya|wX3i3gkTG4m|xDMX2CJ4Xw3|o1hG9vr0peF",
        "caseNumber": "ZKBE8Xm9DJG",
        "medicalPractitionerName": None,
        "causeMedicallyCertified": None,
        "causeOfDeath": {
            "icdCode": "zD0E77W4rFs",
            "icdText": "cSDJ9kSJkFP",
        },
        "externalCauseOfDeath": {
            "dateOfOccurrence": "i8rrl8YWxLF",
            "description": "AZSlwlRAFig&DKlOhZJOCrX",
            "placeOfOccurrence": "kGIDD5xIeLC",
            "otherPlaceOfOccurrence": None,
        },
        "declarantCapacity": None,
        "otherDeclarantCapacity": None
    }


def __nira__dict__():
    return {
        "deceased": {
            "surname": "string",
            "givenName": "string",
            "otherNames": "string",
            "dateOfBirth": "yyyy-MM-dd",
            "age": 0,
            "identificationNumber": "string",
            "sex": "string",
            "occupation": "string",
            "nationality": "string",
            "nationalityCategory": "string",
            "residence": {
                "districtName": "string",
                "countyName": "string",
                "subcountyName": "string",
                "parishName": "string",
                "villageName": "string",
            },
        },
        "dateOfDeath": "yyyy-MM-dd",
        "timeOfDeath": "hh:mm:ss",
        "placeOfDeath": {
            "healthFacilityName": "string",
            "districtName": "string",
            "countyName": "string",
            "subcountyName": "string",
            "parishName": "string",
            "villageName": "string",
        },
        "mannerOfDeath": 0,
        "caseNumber": "string",
        "medicalPractitionerName": "string",
        "causeMedicallyCertified": True,
        "causeOfDeath": {
            "icdCode": "string",
            "icdText": "string",
        },
        "externalCauseOfDeath": {
            "dateOfOccurrence": "yyyy-MM-dd",
            "description": "string",
            "placeOfOccurrence": 0,
            "otherPlaceOfOccurrence": "string",
        },
        "declarantCapacity": 0,
        "otherDeclarantCapacity": "string",
    }


def get_value(field):
    pass


def match_keys(d, data_key):
    for key, value in d.items():
        if isinstance(value, dict):
            return match_keys(value, data_key)
        if key == data_key:
            return value


def get_row_position(header_name, headers):
    count = 0
    for header in headers:
        if header.get('name') == header_name:
            return count
        count += 1


def str_to_bool(s):
    s = s.lower()
    if s == "true":
        return True
    elif s == "false":
        return False
    else:
        return None


def cast_to_get_type(data_key, data_value):
    template = __nira__dict__()
    template_value = str(match_keys(template, data_key))
    if template_value:
        if template_value.isdigit():
            return int(data_value)
        elif type(template_value) == bool:
            return str_to_bool(data_value)
        else:
            return str(data_value)
    return data_value


def format_date(s):
    dt = datetime.datetime.fromisoformat(s)
    return dt.strftime("%Y-%m-%d")


def format_time(s):
    dt = datetime.datetime.fromisoformat(s)
    return dt.strftime("%H:%M:%S")


def get_manner_of_death(s, headers, row):
    for m in s.split('|'):
        position = get_row_position(m, headers)
        if position:
            data_value = str_to_bool(row[position])
            if data_value:
                if m == 'FhHPxY16vet':
                    return 1
                elif m == 'KsGOxFyzIs1':
                    return 2
                elif m == 'b4yPk98om7e':
                    return 7
                elif m == 'gNM2Yhypydx':
                    return 3
                elif m == 'tYH7drlbNya':
                    return 5
                elif m == 'fQWuywOaoN2':
                    return 8
                elif m == 'wX3i3gkTG4m':
                    return 6
                elif m == 'xDMX2CJ4Xw3':
                    return 4
                elif m == 'o1hG9vr0peF':
                    return 10
                elif m == 'AZSlwlRAFig':
                    return 9
    return 10


def get_sex(s, headers, row):
    position = get_row_position(s, headers)
    if position:
        value = row[position]
        if value:
            value = str(value).lower()
            if value == 'male' or value == 'm':
                return 'M'
            elif value == 'female' or value == 'f':
                return 'F'
            elif value == 'alien':
                return 'A'
            else:
                return 'X'
    return 'X'


def get_national_category(s, headers, row):
    position = get_row_position(s, headers)
    if position:
        value = row[position]
        if value:
            value = str(value).lower()
            if value == 'national':
                return 'N'
            elif value == 'foreigner':
                return 'F'
            elif value == 'alien':
                return 'A'
            elif value == 'refugee':
                return 'R'
            else:
                return 'N'
    return 'N'

def get_declarant_capacity(s, headers, row):
    position = get_row_position(s, headers)
    if position:
        value = row[position]
        if value:
            value = str(value).lower()
            if 'attended to deceased before death' in value:
                return 1
            elif 'examined body after death' in value:
                return 2
            elif 'conducted postmortem of the body' in value:
                return 3
            elif value == 'other':
                return 4
            else:
                return 4
    return 4

def iterate_dict(d, headers, row):
    output = {}
    for key, value in d.items():
        if not isinstance(value, dict):
            try:
                if key == 'mannerOfDeath':
                    output[key] = get_manner_of_death(value, headers, row)
                elif key == 'sex':
                    output[key] = get_sex(value, headers, row)
                elif key == 'nationalityCategory':
                    output[key] = get_national_category(value, headers, row)
                elif key == 'declarantCapacity':
                    output[key] = get_declarant_capacity(value, headers, row)
                else:
                    position = get_row_position(value, headers)
                    if position is not None:
                        data_value = row[position]
                        if str(data_value):
                            # Use a dictionary to map keys to functions
                            key_funcs = {
                                'surname': lambda x: x.split(" ")[0],
                                'givenName': lambda x: " ".join(x.split(" ")[1:]),
                                'dateOfDeath': format_date,
                                'dateOfOccurrence': format_date,
                                'timeOfDeath': format_time
                            }
                            # Use the get method to apply the function or return the default value
                            output[key] = cast_to_get_type(key, key_funcs.get(key, lambda x: x)(data_value))
            except Exception as e:
                pass

    return output


def get_dhis_data():
    import requests
    url = "https://hmis.health.go.ug/api/29/analytics/events/query/vf8dN49jprI.json?dimension=pe:2022;2023;2021&dimension=ou:akV6429SUqu&dimension=aKclf7Yl1PE.ZKBE8Xm9DJG&dimension=aKclf7Yl1PE.MOstDqSY0gO&dimension=aKclf7Yl1PE.ZYKmQ9GPOaF&dimension=aKclf7Yl1PE.zwKo51BEayZ&dimension=aKclf7Yl1PE.Z41di0TRjIu&dimension=aKclf7Yl1PE.dsiwvNQLe5n&dimension=aKclf7Yl1PE.RbrUuKFSqkZ&dimension=aKclf7Yl1PE.q7e7FOXKnOf&dimension=aKclf7Yl1PE.e96GB4CXyd3&dimension=aKclf7Yl1PE.i8rrl8YWxLF&dimension=aKclf7Yl1PE.sfpqAeqKeyQ&dimension=aKclf7Yl1PE.zD0E77W4rFs&dimension=aKclf7Yl1PE.cSDJ9kSJkFP&dimension=aKclf7Yl1PE.WkXxkKEJLsg&dimension=aKclf7Yl1PE.Ylht9kCLSRW&dimension=aKclf7Yl1PE.zb7uTuBCPrN&dimension=aKclf7Yl1PE.tuMMQsGtE69&dimension=aKclf7Yl1PE.uckvenVFnwf&dimension=aKclf7Yl1PE.fleGy9CvHYh&dimension=aKclf7Yl1PE.myydnkmLfhp&dimension=aKclf7Yl1PE.QGFYJK00ES7&dimension=aKclf7Yl1PE.C8n6hBilwsX&dimension=aKclf7Yl1PE.ZFdJRT3PaUd&dimension=aKclf7Yl1PE.hO8No9fHVd2&dimension=aKclf7Yl1PE.aC64sB86ThG&dimension=aKclf7Yl1PE.CnPGhOcERFF&dimension=aKclf7Yl1PE.IeS8V8Yf40N&dimension=aKclf7Yl1PE.Op5pSvgHo1M&dimension=aKclf7Yl1PE.eCVDO6lt4go&dimension=aKclf7Yl1PE.cmZrrHfTxW3&dimension=aKclf7Yl1PE.QTKk2Xt8KDu&dimension=aKclf7Yl1PE.dTd7txVzhgY&dimension=aKclf7Yl1PE.xeE5TQLvucB&dimension=aKclf7Yl1PE.ctbKSNV2cg7&dimension=aKclf7Yl1PE.mI0UjQioE7E&dimension=aKclf7Yl1PE.krhrEBwJeNC&dimension=aKclf7Yl1PE.u5ebhwtAmpU&dimension=aKclf7Yl1PE.ZKtS7L49Poo&dimension=aKclf7Yl1PE.OxJgcwH15L7&dimension=aKclf7Yl1PE.fJDDc9mlubU&dimension=aKclf7Yl1PE.Zrn8LD3LoKY&dimension=aKclf7Yl1PE.z89Wr84V2G6&dimension=aKclf7Yl1PE.Kk0hmrJPR90&dimension=aKclf7Yl1PE.j5TIQx3gHyF&dimension=aKclf7Yl1PE.JhHwdQ337nn&dimension=aKclf7Yl1PE.jY3K6Bv4o9Q&dimension=aKclf7Yl1PE.UfG52s4YcUt&dimension=aKclf7Yl1PE.FhHPxY16vet&dimension=aKclf7Yl1PE.KsGOxFyzIs1&dimension=aKclf7Yl1PE.b4yPk98om7e&dimension=aKclf7Yl1PE.gNM2Yhypydx&dimension=aKclf7Yl1PE.tYH7drlbNya&dimension=aKclf7Yl1PE.fQWuywOaoN2&dimension=aKclf7Yl1PE.wX3i3gkTG4m&dimension=aKclf7Yl1PE.xDMX2CJ4Xw3&dimension=aKclf7Yl1PE.o1hG9vr0peF&dimension=aKclf7Yl1PE.AZSlwlRAFig&dimension=aKclf7Yl1PE.U18Tnfz9EKd&dimension=aKclf7Yl1PE.DKlOhZJOCrX&dimension=aKclf7Yl1PE.kGIDD5xIeLC&dimension=aKclf7Yl1PE.V4rE1tsj5Rb&dimension=aKclf7Yl1PE.ivnHp4M4hFF&dimension=aKclf7Yl1PE.jf9TogeSZpk&dimension=aKclf7Yl1PE.xAWYJtQsg8M&dimension=aKclf7Yl1PE.lQ1Byr04JTx&dimension=aKclf7Yl1PE.DdfDMFW4EJ9&dimension=aKclf7Yl1PE.GFVhltTCG8b&dimension=aKclf7Yl1PE.KpfvNQSsWIw&dimension=aKclf7Yl1PE.AJAraEcfH63&dimension=aKclf7Yl1PE.ymyLrfEcYkD&dimension=aKclf7Yl1PE.K5BDPJQk1BP&dimension=aKclf7Yl1PE.uaxjt0inPNF&dimension=aKclf7Yl1PE.Kz29xNOBjsJ&dimension=aKclf7Yl1PE.ZXZZfzBpu8a&dimension=aKclf7Yl1PE.cp5xzqVU2Vw&dimension=aKclf7Yl1PE.lu9BiHPxNqH&dimension=aKclf7Yl1PE.PaoRZbokFWJ&dimension=aKclf7Yl1PE.twVlVWM3ffz&stage=aKclf7Yl1PE&displayProperty=NAME&outputType=EVENT&desc=eventdate&paging=false"
    basic_auth_credentials = ("moh-rch.dmurokora", "Dhis@2022")
    # send a get request with the auth header
    response = requests.get(url, auth=basic_auth_credentials)
    # print the response text
    return response.json()


def get_nira_data(row):
    keys = ['deceased', 'causeOfDeath', 'externalCauseOfDeath', 'placeOfDeath']
    # Initialize the nira_post_data with the top level dict
    post_data = iterate_dict(nira_dict, dhis_data['headers'], row)
    # Loop over the keys and update the nira_post_data accordingly
    for key in keys:
        sub_dict = iterate_dict(nira_dict[key], dhis_data['headers'], row)
        if sub_dict:
            post_data[key] = sub_dict
            # Handle the nested residence key separately
            if key == 'deceased':
                residence = iterate_dict(nira_dict[key]['residence'], dhis_data['headers'], row)
                if residence:
                    post_data[key]['residence'] = residence
        if key == 'externalCauseOfDeath':
            if len(sub_dict) <= 1:
                post_data.pop('externalCauseOfDeath')
    return post_data


def submit_to_nira(data):
    import requests
    from requests.auth import HTTPDigestAuth
    url = "http://mobilevrs.nira.go.ug:8080/test/ThirdPartyApi/deaths.php"
    username = "dhsi2.api"
    password = "7162165ccebfa49657126bd8"
    realm = "mVRS API:deaths"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, auth=HTTPDigestAuth(username, password), json=data, headers=headers)
    try:
        data = response.json()
        return True if response.status_code == 200 else False
    except Exception:
        return False


if __name__ == '__main__':
    nira_dict = __data__map().copy()
    dhis_data = get_dhis_data()
    count = 0
    failed = 0
    for row in dhis_data['rows']:
        nira_post_data = get_nira_data(row)
        if submit_to_nira(nira_post_data):
            count += 1
        else:
            failed += 1
    print(f"Success: {count}, Failed: {failed}")
