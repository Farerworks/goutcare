# Models

## User
- **id**: int
- **email**: str
- **password_hash**: str
- **created_at**: datetime

## FlareEvent
- **id**: int
- **user_id**: int
- **symptoms_jsonb**: JSONB
- **severity_score**: int
- **trigger_text**: str
- **reported_at**: datetime

## MediaAttachment
- **id**: int
- **event_id**: int
- **file_path**: str
- **mime_type**: str
- **checksum**: str

## Symptom
- **id**: int
- **name**: str
- **type**: str (e.g., pain, swelling)

## Trigger
- **id**: int
- **user_id**: int
- **food_item**: str
- **occurrence_count**: int