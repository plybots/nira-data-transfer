import datetime
import json
import os

import requests


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
            "occupation": "b70okb06FWa",
            "nationality": None,
            "nationalityCategory": None,
            "residence": {
                "districtName": 'u44XP9fZweA',
                "countyName": 'dsiwvNQLe5n',
                "subcountyName": 't5nTEmlScSt',
                "parishName": 'bNpMzyShDCX',
                "villageName": 'dsiwvNQLe5n',
            },
        },
        "dateOfDeath": "i8rrl8YWxLF",
        "timeOfDeath": "i8rrl8YWxLF",
        "placeOfDeath": {
            "healthFacilityName": "ou",
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


def get_dict_value_at_level(d, level):
    try:
        if d.get('level') == level:
            return d.get('name')
        elif d.get('parent').get('level') == level:
            return d.get('parent').get('name')
        elif d.get('parent').get('parent').get('level') == level:
            return d.get('parent').get('parent').get('name')
    except Exception:
        return None


def get_place_of_death(ouid):
    url = f"{os.environ.get('DHIS_BASE_URL', 'https://hmis.health.go.ug')}/api/organisationUnits/{ouid}?fields=name,level,parent[name,level,parent[name,level,parent[name,level,parent[name,level]]"
    basic_auth_credentials = (f"{os.environ.get('DHIS_USERNAME', 'moh-rch.dmurokora')}", f"{os.environ.get('DHIS_PASSWORD', 'Dhis@2022')}")
    # send a get request with the auth header
    response = requests.get(url, auth=basic_auth_credentials)
    data = response.json()
    healthFacilityName = get_dict_value_at_level(data, 5)
    districtName = get_dict_value_at_level(data, 3)
    subcountyName = get_dict_value_at_level(data, 4)
    placeOfDeath = {}
    if healthFacilityName:
        placeOfDeath['healthFacilityName'] = healthFacilityName
    if districtName:
        placeOfDeath['districtName'] = districtName.replace("District", "").strip()
    if subcountyName:
        placeOfDeath['subcountyName'] = subcountyName
        placeOfDeath['countyName'] = subcountyName

    return placeOfDeath if placeOfDeath else None


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
    url = f"{os.environ.get('DHIS_BASE_URL', 'https://hmis.health.go.ug')}{os.environ.get('DHIS_DATA_URL', '/api/29/analytics/events/query/vf8dN49jprI.json')}?dimension=pe:2022;2023;2021&" \
          "dimension=ou:akV6429SUqu&dimension=aKclf7Yl1PE.ZKBE8Xm9DJG&dimension=aKclf7Yl1PE.MOstDqSY0gO&dimension=" \
          "aKclf7Yl1PE.ZYKmQ9GPOaF&dimension=aKclf7Yl1PE.Z41di0TRjIu&dimension=aKclf7Yl1PE.dsiwvNQLe5n&dimension=" \
          "aKclf7Yl1PE.RbrUuKFSqkZ&dimension=aKclf7Yl1PE.q7e7FOXKnOf&dimension=aKclf7Yl1PE.e96GB4CXyd3&dimension=" \
          "aKclf7Yl1PE.i8rrl8YWxLF&dimension=aKclf7Yl1PE.FhHPxY16vet&dimension=aKclf7Yl1PE.gNM2Yhypydx&dimension=" \
          "aKclf7Yl1PE.KsGOxFyzIs1&dimension=aKclf7Yl1PE.b4yPk98om7e&dimension=aKclf7Yl1PE.wX3i3gkTG4m&dimension=" \
          "aKclf7Yl1PE.tYH7drlbNya&dimension=aKclf7Yl1PE.fQWuywOaoN2&dimension=aKclf7Yl1PE.o1hG9vr0peF&dimension=" \
          "aKclf7Yl1PE.xDMX2CJ4Xw3&dimension=aKclf7Yl1PE.AZSlwlRAFig&dimension=aKclf7Yl1PE.t5nTEmlScSt&dimension=" \
          "aKclf7Yl1PE.u44XP9fZweA&dimension=aKclf7Yl1PE.zwKo51BEayZ&dimension=aKclf7Yl1PE.b70okb06FWa&dimension=" \
          "aKclf7Yl1PE.bNpMzyShDCX&stage=aKclf7Yl1PE&displayProperty=NAME&outputType=EVENT&desc=eventdate&paging=false"
    basic_auth_credentials = (f"{os.environ.get('DHIS_USERNAME', 'moh-rch.dmurokora')}", f"{os.environ.get('DHIS_PASSWORD', 'Dhis@2022')}")
    # send a get request with the auth header
    response = requests.get(url, auth=basic_auth_credentials)
    # print the response text
    try:
        return response.json()
    except Exception as e:
        print(str(e))
        print(response.text)
        return None


def get_age(s, headers, row):
    return 0


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
                    if residence.get('districtName'):
                        residence['districtName'] = residence.get('districtName').replace("District", "").strip()

                    if residence.get('subcountyName'):
                        residence['subcountyName'] = residence.get('subcountyName').replace("Subcounty", "").strip()

                    post_data[key]['residence'] = residence
        if key == 'externalCauseOfDeath':
            if len(sub_dict) <= 1:
                post_data.pop('externalCauseOfDeath', None)
        if key == 'placeOfDeath':
            post_data[key] = get_place_of_death(sub_dict.get('healthFacilityName'))

    date_of_death = post_data.get('dateOfDeath')
    date_of_birth = post_data.get("deceased").get('dateOfBirth')
    if date_of_birth and date_of_death:
        age = post_data.get("deceased").get('age')
        print(age)
        if not age:
            try:
                date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
                date_of_death = datetime.datetime.strptime(date_of_death, "%Y-%m-%d")
                age = int((date_of_death - date_of_birth).days // 365)
                post_data.get("deceased")['age'] = age
            except Exception as e:
                print(str(e))
    print(json.dumps(post_data))
    return post_data


def submit_to_nira(data, debug=False):
    import requests
    from requests.auth import HTTPDigestAuth
    url = f"{os.environ.get('NIRA_URL', 'http://mobilevrs.nira.go.ug:8080/test/ThirdPartyApi/deaths.php')}"
    username = f"{os.environ.get('NIRA_USERNAME', 'dhsi2.api')}"
    password = f"{os.environ.get('NIRA_PASSWORD', '7162165ccebfa49657126bd8')}"
    realm = f"{os.environ.get('NIRA_REALM', 'mVRS API:deaths')}"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, auth=HTTPDigestAuth(username, password), json=data, headers=headers)
    try:
        _data = response.json()
        if debug:
            print(url)
            print(_data)
            print("#### BEGIN SUBMITTED RECORD ####")
            print(json.dumps(data))
            print("#### END SUBMITTED RECORD ####")
        return True if response.status_code == 200 else False
    except Exception as e:
        if debug:
            print(str(e))
        return False


def transfer(debug=False):
    count = 0
    failed = 0
    start = os.environ.get('START_COUNT', 'X')
    end = os.environ.get('END_COUNT', 'X')
    dhis_data_rows = dhis_data['rows']
    if start != 'X' and end != 'X':
        try:
            dhis_data_rows = dhis_data_rows[int(start):int(end)]
        except Exception:
            pass

    for row in dhis_data_rows:
        nira_post_data = get_nira_data(row)
        if submit_to_nira(nira_post_data, debug=debug):
            count += 1
        else:
            failed += 1
    print(f"Success: {count}, Failed: {failed}")


if __name__ == '__main__':
    nira_dict = __data__map().copy()
    dhis_data = get_dhis_data()
    transfer(debug=bool(os.environ.get('DEBUG', 0)))

