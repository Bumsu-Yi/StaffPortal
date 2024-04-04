## API 명세서

### 직원 정보 조회 API

#### Endpoint:
GET /api/employee/<employee_id>/

#### Request:
```json
{
    "employee_id": 123
}
```
#### Response:
```json
{
    "employee_id": 123,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone_number": "123-456-7890",
    "hire_date": "2022-01-01",
    "job": "Manager",
    "salary": 50000.00,
    "commission_pct": 0.1,
    "manager": null,
    "department": "Engineering"
}
```
### 직원의 업무 이력 조회 API
#### Endpoint:
GET /api/jobhistory/<employee_id>/

#### Request:
```json
{
    "employee_id": 123
}
```
#### Response:
```json
[
    {
        "employee_id": 123,
        "start_date": "2022-01-01",
        "end_date": "2023-01-01",
        "job_id": 1,
        "department_id": 1
    },
    {
        "employee_id": 123,
        "start_date": "2023-01-01",
        "end_date": null,
        "job_id": 2,
        "department_id": 2
    }
]
```
### 부서와 위치 정보 조회 API
#### Endpoint:
GET /api/departments/

#### Response:
```json
[
    {
        "department_id": 1,
        "department_name": "Engineering",
        "location": "Seoul"
    },
    {
        "department_id": 2,
        "department_name": "Sales",
        "location": "New York"
    }
]
```
### 급여 인상 API
#### Endpoint:
PUT /departments/<department_id>/increase-salary/

#### Request body:
```json
{
    "salary_increase_rate": 0.1
}
```
#### Response:
```json
{
    "message": "Salaries increased successfully."
}
```
### 자외선 지수 조회 API
#### Endpoint:
GET /uv-index/<area_no>/

#### Request:
```json
{
    "area_no": "1100000000"
}
```
#### Response:
```json
{
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "NORMAL_SERVICE"
        },
        "body": {
            "dataType": "JSON",
            "items": {
                "item": {
                    "code": "A07_2",
                    "areaNo": "1100000000",
                    "date": "2024040415",
                    "h0": "4",
                    "h3": "0",
                    "h6": "0",
                    "h9": "0",
                    "h12": "0",
                    "h15": "0",
                    "h18": "3",
                    "h21": "4",
                    "h24": "2",
                    "h27": "0",
                    "h30": "0",
                    "h33": "0",
                    "h36": "0",
                    "h39": "1",
                    "h42": "5",
                    "h45": "6",
                    "h48": "4",
                    "h51": "0",
                    "h54": "0",
                    "h57": "",
                    "h60": "",
                    "h63": "",
                    "h66": "",
                    "h69": "",
                    "h72": "",
                    "h75": ""
                }
            }
        },
        "pageNo": 1,
        "numOfRows": 10,
        "totalCount": 1
    }
```
}
