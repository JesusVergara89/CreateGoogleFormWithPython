import os
from apiclient import discovery
from httplib2 import Http
from oauth2client.service_account import (ServiceAccountCredentials)
import json
from dotenv import load_dotenv

load_dotenv()

credentials_info = {
  "type": os.getenv("type_"),
  "project_id": os.getenv("project_id_"),
  "private_key_id": os.getenv("private_key_id_"),
  "private_key": os.getenv("private_key_"),
  "client_email": os.getenv("client_email_"),
  "client_id": os.getenv("client_id_"),
  "auth_uri": os.getenv("auth_uri_"),
  "token_uri": os.getenv("token_uri_"),
  "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url_"),
  "client_x509_cert_url": os.getenv("client_x509_cert_url_"),
  "universe_domain": os.getenv("universe_domain_")
}
for key, value in credentials_info.items():
    print(f"{key}: {value}")

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    credentials_info,
    SCOPES
)

http = creds.authorize(Http())

form_service = discovery.build(
    'forms',
    'v1',
    http=http,
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False
)

NEW_FORM ={
    "info": {
        "title": "Mi formilario"
    }
}

NEW_QUESTIONS = {
    "requests": [
        {
            "createItem": {
                "item": {
                    "title": "¿Qué es una clase en programación orientada a objetos?",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "Una función que realiza una tarea específica"},
                                    {"value": "Un tipo de variable que almacena datos"},
                                    {"value": "Un molde o plantilla para crear objetos"},
                                    {"value": "Una estructura para almacenar datos de manera temporal"},
                                ],
                                "shuffle": True
                            }
                        }
                    },
                },
                "location": {
                    "index": 0
                }
            }
        },
        {
            "createItem": {
                "item": {
                    "title": "¿Qué es la herencia en programación orientada a objetos?",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "Un concepto que permite a una clase heredar características de otra clase"},
                                    {"value": "El proceso de crear una nueva instancia de una clase"},
                                    {"value": "Un método para definir múltiples funciones con el mismo nombre"},
                                    {"value": "Un tipo de variable que almacena valores constantes"},
                                ],
                                "shuffle": True
                            }
                        }
                    },
                },
                "location": {
                    "index": 1
                }
            }
        },
        {
            "createItem": {
                "item": {
                    "title": "¿Qué es el polimorfismo en programación orientada a objetos?",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "La capacidad de una función para procesar datos de diferentes tipos"},
                                    {"value": "El proceso de encapsular datos dentro de una clase"},
                                    {"value": "Un tipo de variable que almacena datos de manera secuencial"},
                                    {"value": "Un método para definir estructuras de control de flujo"},
                                ],
                                "shuffle": True
                            }
                        }
                    },
                },
                "location": {
                    "index": 2
                }
            }
        },
        {
            "createItem": {
                "item": {
                    "title": "¿Qué es la encapsulación en programación orientada a objetos?",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "El proceso de esconder los detalles de implementación y exponer solo lo necesario"},
                                    {"value": "El proceso de heredar características de una clase base"},
                                    {"value": "Una técnica para dividir un programa en módulos"},
                                    {"value": "Una forma de evitar errores de compilación"},
                                ],
                                "shuffle": True
                            }
                        }
                    },
                },
                "location": {
                    "index": 3
                }
            }
        }
    ]
}


result = form_service.forms().create(
    body=NEW_FORM
).execute()

question_setting = form_service.forms().batchUpdate(
    formId = result["formId"],
    body=NEW_QUESTIONS
).execute()

get_result = form_service.forms().get(
    formId=result["formId"]
).execute()

print(json.dumps(get_result, indent = 4))





