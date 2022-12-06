# Dicitura per Pyinstaller:
import os, sys
#os.chdir(sys._MEIPASS)
import json
import machineid
import page_launcher
import requests


def start_application():
    page_launcher.launch_landing_page()


def verify_license(license_key):
    try:
        machine_fingerprint = machineid.hashed_id('example-app')
        validation = requests.post(
            "https://api.keygen.sh/v1/accounts/{}/licenses/actions/validate-key".format(
                "b1829417-e08f-4dd3-8e35-7da3893c2a3d"),
            headers={
                "Content-Type": "application/vnd.api+json",
                "Accept": "application/vnd.api+json"
            },
            data=json.dumps({
                "meta": {
                    "scope": {"fingerprint": machine_fingerprint},
                    "key": license_key
                }
            })
        ).json()
        print("POST RES:", validation)
        if "errors" in validation:
            errs = validation["errors"]

            return False, "license validation failed: {}".format(
                map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs)
            )

        # license already activated
        if validation["meta"]["valid"]:
            return True, "license has already been activated on this machine"
        if not validation['data']:
            raise ValueError('Licenza inesistente, zinghero')

        # activate license for first time
        activation = requests.post(
            "https://api.keygen.sh/v1/accounts/{}/machines".format("b1829417-e08f-4dd3-8e35-7da3893c2a3d"),
            headers={
                "Authorization": "License {}".format(license_key),
                "Content-Type": "application/vnd.api+json",
                "Accept": "application/vnd.api+json"
            },
            data=json.dumps({
                "data": {
                    "type": "machines",
                    "attributes": {
                        "fingerprint": machine_fingerprint
                    },
                    "relationships": {
                        "license": {
                            "data": {"type": "licenses", "id": validation["data"]["id"]}
                        }
                    }
                }
            })
        ).json()
        #create file to cache data
        with open('cache_data.json', 'w') as cache_file:
            cache_file.write(json.dumps({'expire_date': validation['data']['attributes']['expiry'],
                                         'license_key': validation['data']['attributes']['key']}, indent=4))

    except requests.exceptions.ConnectionError:
        print('dakje')

license_key = "LFML-MN3U-P7UJ-KYNY-3WLJ-UA9X-7RRX-FWTK"
verify_license(license_key)
start_application()











