from tera_etl import quality_control as qc
schema = {
    "UserId" : "int",
    "HomePhone" : "string",
    "WorkPhone" : ["string", "null"],
    "Address" : {
        "HouseNo": "string",
        "Streetname": "string",
        "Ward": "string",
        "District": "string",
        "Province": "string",
        "Country": "string"
    },
    "Firstname" : "string",
    "Lastname" : "string",
    "Gender" : "string",
    "RegisterDate" : "datetime",
    "Status" : "string",
    "DataSource" : "string",
    "Source" : "string",
    "EventId" : "string"
}
data = {
    "UserId": 202201439424,
    "HomePhone": "0912919543",
    "WorkPhone": None,""
    "Address": {
        "HouseNo": "",
        "Streetname": "",
        "Ward": "ẤP HÒA CƯỜNG, Xã Minh Hoà",
        "District": "Huyện Dầu Tiếng",
        "Province": "Tỉnh Bình Dương",
        "Country": "Việt Nam"
    },
    "Firstname": "TRẦN VĂN ",
    "Lastname": "TÙNG",
    "Gender": "Male",
    "RegisterDate": "2022-01-01T00:00:00.00Z",
    "Status": "True",
    "DataSource": "VTVHyundai",
    "Source": "VTVHyundai",
    "EventId": "VTVHyundai_IngestProfile_202201439424"
}
qc_type = qc.classify_data(data_chunk=data, schema=schema)
if qc_type == qc.QualityControlResult.ACCEPTED:
    print(qc_type)