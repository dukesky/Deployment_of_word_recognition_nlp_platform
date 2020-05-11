print('container start')

try:
    import unzip_requirements
except ImportError as error:
    pass

import json

from spacy import displacy
import en_core_web_sm

MODEL = en_core_web_sm.load()
print('model loaded')

def create_ner_spans(text):

    doc = MODEL(text)
    spans = []
    for ent in doc.ents:
        span = {
            'start': ent.start_char,
            'end': ent.end_char,
            'type': ent.label_,
        }
        spans.append(span) 
    return spans


def handle_request(event, context):
    text = event['body']
    print('received test from http post: ',text)
    spans = []

    if text is not None:
        spans = create_ner_spans(text)
    print('spans after create: ',spans)

    body = {
       "spans": spans,

    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    return response

def recognize_named_tag(event, context):

    request_body = event['body']
    text = json.loads(request_body)['text']
    print('received test from http post: ',text)
    
    if text is not None:
        doc = MODEL(text)
        parse = displacy.parse_deps(doc) 

    setting = {}
    setting['lang'] = 'en'
    setting['direction'] = 'ltr'

    parse['setting'] = setting

    print('parse after create: ',parse)
    body = parse

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    return response    
