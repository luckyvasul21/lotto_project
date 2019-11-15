# importing the requests library
import requests, json

# api-endpoint
URL = "http://52.17.102.78:43616/xp/practice"

# defining a params dict for the parameters to be sent to the API
pay_load = {
    "billingEntities":{
        "byId":{
            "1":{
                "id":1,
                "ssn":"987-65-4321",
                "zip":"10595-2148",
                "city":"Valhalla",
                "state":"iso-3166-2/US-NY",
                "street":"10 Hillside Ave, Apt 2N",
                "npiType":"NPI-1",
                "tinType":"ssn",
                "taxonomy":"1223E0200X",
                "legalName":"erew",
                "npiNumber":"1730511627",
                "practiceName":"PREETHI C BHASIN MS",
                "practiceTypes":[
                    "group"
                ],
                "originalNpiRecord":{
                    "basic":{
                        "name":"BHASIN PREETHI",
                        "gender":"F",
                        "status":"A",
                        "last_name":"BHASIN",
                        "credential":"M.S.",
                        "first_name":"PREETHI",
                        "middle_name":"CYNTHIA",
                        "name_prefix":"MRS.",
                        "last_updated":"2013-08-02",
                        "sole_proprietor":"YES",
                        "enumeration_date":"2013-08-02"
                    },
                    "number":1730511627,
                    "addresses":[
                        {
                            "city":"VALHALLA",
                            "state":"NY",
                            "address_1":"10 HILLSIDE AVE",
                            "address_2":"APT 2N",
                            "postal_code":"105952148",
                            "address_type":"DOM",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_purpose":"LOCATION",
                            "telephone_number":"973-876-8121"
                        },
                        {
                            "city":"VALHALLA",
                            "state":"NY",
                            "address_1":"10 HILLSIDE AVE",
                            "address_2":"APT 2N",
                            "postal_code":"105952148",
                            "address_type":"DOM",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_purpose":"MAILING",
                            "telephone_number":"973-876-8121"
                        }
                    ],
                    "taxonomies":[
                        {
                            "code":"235Z00000X",
                            "desc":"Speech-Language Pathologist  ",
                            "state":"",
                            "license":"",
                            "primary":True
                        }
                    ],
                    "identifiers":[

                    ],
                    "other_names":[
                        {
                            "code":"1",
                            "type":"Former Name",
                            "prefix":"MS.",
                            "last_name":"KUMAR",
                            "first_name":"PREETHI",
                            "middle_name":"CYNTHIA"
                        }
                    ],
                    "created_epoch":1375401600,
                    "enumeration_type":"NPI-1",
                    "last_updated_epoch":1375401600
                }
            },
            "9":{
                "npiNumber":"1578913232",
                "originalNpiRecord":{
                    "taxonomies":[
                        {
                            "state":"SD",
                            "code":"261QD0000X",
                            "primary":True,
                            "license":"580",
                            "desc":"Clinic/Center Dental"
                        }
                    ],
                    "addresses":[
                        {
                            "city":"RAPID CITY",
                            "address_2":"",
                            "telephone_number":"605-341-6325",
                            "state":"SD",
                            "postal_code":"57701",
                            "address_1":"241 EAST MEADE ST",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"LOCATION"
                        },
                        {
                            "city":"RAPID CITY",
                            "address_2":"",
                            "state":"SD",
                            "postal_code":"577015657",
                            "address_1":"241 E MEADE ST",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"MAILING"
                        }
                    ],
                    "created_epoch":1465862400,
                    "identifiers":[

                    ],
                    "other_names":[

                    ],
                    "number":1578913232,
                    "last_updated_epoch":1465906694,
                    "basic":{
                        "status":"A",
                        "authorized_official_telephone_number":"605-355-2260",
                        "last_updated":"2016-06-14",
                        "name":".INDIAN HEALTH SERVICE",
                        "authorized_official_credential":"DDS",
                        "authorized_official_last_name":"VON HENDRICKS",
                        "organization_name":".INDIAN HEALTH SERVICE",
                        "organizational_subpart":"NO",
                        "authorized_official_title_or_position":"DENTAL CHIEF",
                        "enumeration_date":"2016-06-14",
                        "authorized_official_first_name":"CLAUDIA"
                    },
                    "enumeration_type":"NPI-2"
                },
                "npiType":"NPI-2",
                "practiceName":".INDIAN HEALTH SERVICE",
                "street":"241 E Meade St",
                "city":"Rapid City",
                "state":"iso-3166-2/US-SD",
                "zip":"57701-5657",
                "taxonomy":"1223G0001X",
                "id":9,
                "legalName":"abc",
                "ssn":"987-65-4321",
                "tinType":"ssn",
                "practiceTypes":[
                    "FQHC"
                ]
            },
            "12":{
                "npiNumber":"1578913232",
                "originalNpiRecord":{
                    "taxonomies":[
                        {
                            "state":"SD",
                            "code":"261QD0000X",
                            "primary":True,
                            "license":"580",
                            "desc":"Clinic/Center Dental"
                        }
                    ],
                    "addresses":[
                        {
                            "city":"RAPID CITY",
                            "address_2":"",
                            "telephone_number":"605-341-6325",
                            "state":"SD",
                            "postal_code":"57701",
                            "address_1":"241 EAST MEADE ST",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"LOCATION"
                        },
                        {
                            "city":"RAPID CITY",
                            "address_2":"",
                            "state":"SD",
                            "postal_code":"577015657",
                            "address_1":"241 E MEADE ST",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"MAILING"
                        }
                    ],
                    "created_epoch":1465862400,
                    "identifiers":[

                    ],
                    "other_names":[

                    ],
                    "number":1578913232,
                    "last_updated_epoch":1465906694,
                    "basic":{
                        "status":"A",
                        "authorized_official_telephone_number":"605-355-2260",
                        "last_updated":"2016-06-14",
                        "name":".INDIAN HEALTH SERVICE",
                        "authorized_official_credential":"DDS",
                        "authorized_official_last_name":"VON HENDRICKS",
                        "organization_name":".INDIAN HEALTH SERVICE",
                        "organizational_subpart":"NO",
                        "authorized_official_title_or_position":"DENTAL CHIEF",
                        "enumeration_date":"2016-06-14",
                        "authorized_official_first_name":"CLAUDIA"
                    },
                    "enumeration_type":"NPI-2"
                },
                "npiType":"NPI-2",
                "practiceName":".INDIAN HEALTH SERVICE",
                "street":"241 E Meade St",
                "city":"Rapid City",
                "state":"iso-3166-2/US-SD",
                "zip":"57701-5657",
                "taxonomy":"1223E0200X",
                "id":12,
                "legalName":"3legalname",
                "fein":"66-6666666",
                "tinType":"fein",
                "practiceTypes":[
                    "indian-health-services"
                ]
            }
        },
        "allIds":[
            1,
            9,
            12
        ]
    },
    "practiceLocations":{
        "byId":{
            "2":{
                "id":2,
                "zip":"94404",
                "chip":False,
                "city":"cred_city",
                "email":"aa@aa.com",
                "phone":"(111) 111-1111",
                "state":"iso-3166-2/US-AR",
                "suite":"23213",
                "maxAge":99,
                "minAge":1,
                "street":"dfds",
                "medicaid":True,
                "languages":[
                    "iso-639-1/en"
                ],
                "newPatients":False,
                "locationName":"credlocation",
                "specialNeeds":False,
                "associatedBillingEntityId":1
            },
            "5":{
                "associatedBillingEntityId":9,
                "id":5,
                "locationName":"4354",
                "street":"fg",
                "suite":"23213",
                "city":"fgdg",
                "state":"iso-3166-2/US-AL",
                "zip":"94404",
                "email":"lpalabatla@sagaxtech.com",
                "phone":"(111) 111-1111",
                "languages":[
                    "iso-639-1/en"
                ],
                "chip":True,
                "medicaid":False,
                "newPatients":True,
                "specialNeeds":True,
                "minAge":1,
                "maxAge":99
            },
            "13":{
                "associatedBillingEntityId":12,
                "id":13,
                "locationName":"ghfghgfgfhgfh",
                "street":"uuuuu",
                "suite":"uuu",
                "city":"uuuu",
                "state":"iso-3166-2/US-CA",
                "zip":"94404",
                "email":"uu@uu.com",
                "phone":"(111) 111-1111",
                "languages":[
                    "iso-639-1/en"
                ],
                "chip":True,
                "medicaid":True,
                "newPatients":True,
                "specialNeeds":True,
                "minAge":1,
                "maxAge":101
            },
            "16":{
                "associatedBillingEntityId":12,
                "id":16,
                "locationName":"testpracticelocation",
                "street":"teststreet",
                "suite":"testsuite",
                "city":"testcity",
                "state":"iso-3166-2/US-CA",
                "zip":"94404",
                "email":"test@test.com",
                "phone":"(999) 999-9999",
                "languages":[
                    "iso-639-1/en"
                ],
                "chip":True,
                "medicaid":True,
                "newPatients":True,
                "specialNeeds":True,
                "minAge":1,
                "maxAge":99
            }
        },
        "allIds":[
            2,
            5,
            13,
            16
        ]
    },
    "providers":{
        "byId":{
            "3":{
                "id":3,
                "npiType":"NPI-1",
                "lastName":"AKASHDEEP",
                "taxonomy":"1223G0001X",
                "firstName":"KUMAR",
                "npiNumber":"1720210008",
                "credential":"MD",
                "deaLicenses":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "dentalSchools":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "dentalLicenses":{
                    "byId":{
                        "4":{
                            "id":4,
                            "state":"iso-3166-2/US-AL",
                            "licenseNumber":"321312"
                        }
                    },
                    "allIds":[
                        4
                    ]
                },
                "trainingPrograms":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "originalNpiRecord":{
                    "basic":{
                        "name":"AKASHDEEP KUMAR",
                        "gender":"M",
                        "status":"A",
                        "last_name":"AKASHDEEP",
                        "credential":"M.D.",
                        "first_name":"KUMAR",
                        "name_prefix":"DR.",
                        "last_updated":"2012-10-18",
                        "sole_proprietor":"NO",
                        "enumeration_date":"2009-08-20"
                    },
                    "number":1720210008,
                    "addresses":[
                        {
                            "city":"STURGEON BAY",
                            "state":"WI",
                            "address_1":"1910 ALABAMA ST",
                            "address_2":"",
                            "postal_code":"542353532",
                            "address_type":"DOM",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_purpose":"LOCATION",
                            "telephone_number":"920-746-7200"
                        },
                        {
                            "city":"STURGEON BAY",
                            "state":"WI",
                            "address_1":"1910 ALABAMA ST",
                            "address_2":"",
                            "postal_code":"542353532",
                            "address_type":"DOM",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_purpose":"MAILING",
                            "telephone_number":"920-746-7200"
                        }
                    ],
                    "taxonomies":[
                        {
                            "code":"207R00000X",
                            "desc":"Internal Medicine",
                            "state":"WI",
                            "license":"57468-20",
                            "primary":True
                        }
                    ],
                    "identifiers":[

                    ],
                    "other_names":[

                    ],
                    "created_epoch":1250726400,
                    "enumeration_type":"NPI-1",
                    "last_updated_epoch":1350518400
                },
                "substanceLicenses":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "liabilityInsurance":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "boardCertifications":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "hospitalAffiliations":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "associatedPracticeLocationIds":[
                    2,
                    5
                ]
            },
            "7":{
                "id":7,
                "npiNumber":"1730511627",
                "originalNpiRecord":{
                    "taxonomies":[
                        {
                            "state":"",
                            "code":"235Z00000X",
                            "primary":True,
                            "license":"",
                            "desc":"Speech-Language Pathologist  "
                        }
                    ],
                    "addresses":[
                        {
                            "city":"VALHALLA",
                            "address_2":"APT 2N",
                            "telephone_number":"973-876-8121",
                            "state":"NY",
                            "postal_code":"105952148",
                            "address_1":"10 HILLSIDE AVE",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"LOCATION"
                        },
                        {
                            "city":"VALHALLA",
                            "address_2":"APT 2N",
                            "telephone_number":"973-876-8121",
                            "state":"NY",
                            "postal_code":"105952148",
                            "address_1":"10 HILLSIDE AVE",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"MAILING"
                        }
                    ],
                    "created_epoch":1375401600,
                    "identifiers":[

                    ],
                    "other_names":[
                        {
                            "first_name":"PREETHI",
                            "last_name":"KUMAR",
                            "middle_name":"CYNTHIA",
                            "prefix":"MS.",
                            "code":"1",
                            "type":"Former Name"
                        }
                    ],
                    "number":1730511627,
                    "last_updated_epoch":1375401600,
                    "basic":{
                        "status":"A",
                        "credential":"M.S.",
                        "first_name":"PREETHI",
                        "last_name":"BHASIN",
                        "middle_name":"CYNTHIA",
                        "name":"BHASIN PREETHI",
                        "sole_proprietor":"YES",
                        "gender":"F",
                        "last_updated":"2013-08-02",
                        "name_prefix":"MRS.",
                        "enumeration_date":"2013-08-02"
                    },
                    "enumeration_type":"NPI-1"
                },
                "npiType":"NPI-1",
                "firstName":"PREETHI",
                "middleInitial":"C",
                "lastName":"BHASIN",
                "credential":"MS",
                "taxonomy":"1223E0200X",
                "dentalLicenses":{
                    "byId":{
                        "8":{
                            "licenseNumber":"credscsl",
                            "state":"iso-3166-2/US-AR",
                            "id":8
                        }
                    },
                    "allIds":[
                        8
                    ]
                },
                "dentalSchools":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "trainingPrograms":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "boardCertifications":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "hospitalAffiliations":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "liabilityInsurance":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "deaLicenses":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "substanceLicenses":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "associatedPracticeLocationIds":[
                    5
                ]
            },
            "14":{
                "id":14,
                "npiNumber":"1063581684",
                "originalNpiRecord":{
                    "taxonomies":[
                        {
                            "state":"VA",
                            "code":"207L00000X",
                            "primary":True,
                            "license":"0101027996",
                            "desc":"Anesthesiology"
                        }
                    ],
                    "addresses":[
                        {
                            "city":"CHARLOTTESVILLE",
                            "address_2":"",
                            "telephone_number":"434-924-0000",
                            "state":"VA",
                            "postal_code":"229080001",
                            "address_1":"LEE ST",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"LOCATION"
                        },
                        {
                            "city":"CHARLOTTESVILLE",
                            "address_2":"",
                            "state":"VA",
                            "postal_code":"229032981",
                            "address_1":"500 RAY C HUNT DR",
                            "country_code":"US",
                            "country_name":"United States",
                            "address_type":"DOM",
                            "address_purpose":"MAILING"
                        }
                    ],
                    "created_epoch":1162857600,
                    "identifiers":[

                    ],
                    "other_names":[

                    ],
                    "number":1063581684,
                    "last_updated_epoch":1183852800,
                    "basic":{
                        "status":"A",
                        "first_name":"WILLIAM",
                        "last_name":"'ARNOLD, III'",
                        "middle_name":"P.",
                        "name":"'ARNOLD, III' WILLIAM",
                        "sole_proprietor":"NO",
                        "gender":"M",
                        "last_updated":"2007-07-08",
                        "enumeration_date":"2006-11-07"
                    },
                    "enumeration_type":"NPI-1"
                },
                "npiType":"NPI-1",
                "firstName":"WILLIAM",
                "middleInitial":"P",
                "lastName":"'ARNOLD, III'",
                "taxonomy":"1223E0200X",
                "credential":"dr",
                "dentalLicenses":{
                    "byId":{
                        "15":{
                            "licenseNumber":"3dentallicanse",
                            "state":"iso-3166-2/US-AR",
                            "id":15
                        }
                    },
                    "allIds":[
                        15
                    ]
                },
                "dentalSchools":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "trainingPrograms":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "boardCertifications":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "hospitalAffiliations":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "liabilityInsurance":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "deaLicenses":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "substanceLicenses":{
                    "byId":{

                    },
                    "allIds":[

                    ]
                },
                "associatedPracticeLocationIds":[
                    2,
                    5,
                    13
                ]
            }
        },
        "allIds":[
            3,
            7,
            14
        ]
    },
    "ids":{
        "lastId":16
    },
    "currentLocation":"loi/practiceLocations/16/services"
}

headers = {"Content-Type": "application/json", "Cookie": "access_token=eyJraWQiOiJrMSIsImFsZyI6IlJTNTEyIn0.eyJpc3MiOiJ3d3cubWNuYS5uZXQiLCJleHAiOjE1MjU0NTA1MzYsImp0aSI6Ikd5S1NFMjNiV1FneVNVRm9lazBmRVEiLCJpYXQiOjE1MjU0NDUxMzYsIm5iZiI6MTUyNTQ0NTAxNiwic3ViIjoic2FnYXh0ZXN0QGdtYWlsLmNvbSIsImdyb3VwcyI6W10sInhzcmZUb2tlbiI6IjIxMThkZTlhLWQ2YzAtNGM1Zi05Y2UxLThmN2U1YzQ1OTA5YyIsInVzZXJfdXVpZCI6Ijc2NGMyMjgwLTJiZmYtNDhhMC04OGZiLTNkZTVjZjdhODU4YiJ9.RjSdJkbBWGUoxUt75fi7ybc0fIaPK3nqki9k6B0rnbEZ0ldLQSbPTZHlzo0htZXN1nDTbhotGeBbtNDKgNcXFZnQXi_T4YDO5QtvqIxMbaSIp_RDx-ImNuX87I2XTz18zpSmiYdiyLXtR6ojhalRmHw6E2n7lw4l1aHHwtd7kaDknfGZgOjjlzv7Z2LamAVtIoBrqjd7AWSYMhBNflXHsV6G5wK5v94UDJCw3NEA5Qe6JrihNCELrUx1deQ7OKuwIjZ_cQ9DdkcZbkNEScYRpOCXmme-oMg1wUNtV5myI42_D9Yadufn7xFGkTAE0pGpY2RPy4m1cPlUZEeGCb_Ldw; path=/; domain=52.17.102.78; HttpOnly; Expires=Fri, 03 Jan 2020 13:58:32 GMT;"}
# sending get request and saving the response as response object

r = requests.post(url = URL, data=json.dumps(pay_load), headers=headers)

assert 204 == r.status_code
# print(r.status_code)

# extracting data in json format
# data = r.json()
# print(data.text)