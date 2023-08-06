RFC_SKELETON = '''
<!-- BEGIN METADATA
{
  "obsoletes": {{ obsoletes_json }},
  "obsoletedBy": {{ obsoleted_by_json }},
  "lastModified": "{{ last_modified_at_json }}",
  "number": {{ number }}
}
END METADATA -->

# RFC{{ number }} {{ title }}

<!-- DO NOT TOUCH THIS SECTION !! -->

- Request for Comments: {{ number }}
- Category: {{ category }}
- Created By: {{ created_by }}
- Updated By: {{ updated_by }}
- Created: {{ created_at }}
- Last modified: {{ last_modified_at }}

## Status: {{ status }}

<!-- DO NOT TOUCH THIS SECTION !! -->

- Obsoletes: {{ obsoletes }}
- Obsoleted by: {{ obsoleted_by }}

'''