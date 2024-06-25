class Config:
    SECRET_KEY = "5791628bb0b13ce0c676dfde280ba245"

    JWT_SECRET_KEY = "134165867gn13ce0c676dfde280ba245"
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_TYPE = "Bearer"
    JWT_HEADER_NAME = "Authorization"

    AWS_ACCESS_KEY_ID = ""
    AWS_SECRET_ACCESS_KEY = ""
    AWS_S3_BUCKET = ""
    AWS_S3_REGION = ""
    AWS_UPLOAD_FOLDER = ""
    
    # OpenAI
    OPENAI_KEY = ""
