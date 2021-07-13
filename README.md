# Program Python

Program python untuk menyimpan data word cloud.

## Install Library

```bash
pip install -r requirements.txt
```

## Running Program

```bash
python app.py
```

--- 

## Endpoint

```
/word
```

#### GET

Example Response:

```json
[
    {
        "weight": 20,
        "word": "the"
    },
    {
        "weight": 14,
        "word": "a"
    },
    {
        "weight": 14,
        "word": "ipsum"
    }
]
```

### POST

Example request body:

```json
{
    "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset"
}
```
