# MOZIO Area API

## Documentation
For *OPEN API* documentation visit  
```json
http://35.175.226.92:8080/docs/
```

## Manage Providers
```json
http://35.175.226.92:8080/api/providers/
```


## Search a Point in all Areas example

### 1. Area creation example

```json
http://35.175.226.92:8080/api/areas/
```

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
### 2. Search if a given Point belongs to a service area

For Point Lat=10, Lng=10 
```json
http://35.175.226.92:8080/api/areas/?search_by=10,10
```
## List of all Areas

For a List of all Areas please go to `/api/areas/`

## NOTES
Only `Authenticated` users can create, delete or update areas

For users password setup please go to `/admin/accounts/`

### Admin credentials