# MOZIO Area API

## Documentation
For documentation visit  `/docs/`

## Examples
### Search if a given Point belongs to a service area

For Point Lat=10, Lng=10 
`/api/areas/?search_by=10,10`

### Area creation example

```json
{
    "name": "Nokia Store Delivery Area",
            "region": {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [
                            0.0,
                            0.0
                        ],
                        [
                            0.0,
                            50.0
                        ],
                        [
                            50.0,
                            50.0
                        ],
                        [
                            50.0,
                            0.0
                        ],
                        [
                            0.0,
                            0.0
                        ]
                    ]
                ]
            ]
        },
    "owner": 1
}
```

## List of all Areas

For a List of all Areas please go to `/api/areas/`

## NOTES
Only `Authenticated` users can create, delete or update areas

For users password setup please go to `/admin/accounts/`

### Admin credentials